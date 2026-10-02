#!/usr/bin/env python3
"""Record and read back AICQ harness events using the client's Fulcra CLI."""

import argparse
import datetime as dt
import json
import pathlib
import subprocess
import time
import uuid

ANNOTATION = "MomentAnnotation/51f5fa9c-a6c7-4ee5-a0e3-f602496e3bed"
STATE = pathlib.Path(__file__).resolve().parents[1] / ".local/harness-run.json"
parser = argparse.ArgumentParser()
parser.add_argument(
    "--milestone",
    choices=["M1", "M2", "M3", "M4", "M5", "M6"],
    help="Required when starting a new run",
)
parser.add_argument("step")
parser.add_argument("status", choices=["started", "completed", "failed"])
parser.add_argument("detail")
parser.add_argument("evidence")
parser.add_argument(
    "--timeout-minutes",
    type=int,
    default=15,
    help="Must match the recorded plan configuration",
)
args = parser.parse_args()
if not args.evidence.strip():
    parser.error("Evidence is required")
now = dt.datetime.now(dt.timezone.utc)
if args.step == "RUN_START":
    if not args.milestone:
        parser.error("RUN_START requires --milestone")
    state = {
        "milestone": args.milestone,
        "run_id": args.milestone.lower() + "-" + str(uuid.uuid4()),
        "started_at": now.isoformat(),
        "timeout_minutes": args.timeout_minutes,
    }
    STATE.parent.mkdir(exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2) + "\n")
else:
    state = json.loads(STATE.read_text())
    state.setdefault("milestone", "M1")
    if args.milestone and args.milestone != state["milestone"]:
        parser.error("Milestone does not match the active run")
    elapsed = now - dt.datetime.fromisoformat(state["started_at"])
    if elapsed.total_seconds() > state["timeout_minutes"] * 60 and args.step not in {
        "REVIEW",
        "ESCALATE",
        "RUN_COMPLETE",
        "RUN_INCOMPLETE",
    }:
        parser.error("Run timeout reached; record failure and close the run")
event = {
    "event_id": str(uuid.uuid4()),
    "run_id": state["run_id"],
    "milestone": state["milestone"],
    "step": args.step,
    "status": args.status,
    "detail": args.detail,
    "evidence": args.evidence,
}
record = json.dumps({"note": json.dumps(event), "recorded_at": now.isoformat()})
subprocess.run(
    ["fulcra", "record", ANNOTATION],
    input=record,
    text=True,
    check=True,
    capture_output=True,
)
deadline = time.monotonic() + 60
while True:
    result = subprocess.run(
        ["fulcra", "get-records", ANNOTATION, "2h"],
        text=True,
        check=True,
        capture_output=True,
    )
    for line in result.stdout.splitlines():
        item = json.loads(line)
        note = json.loads(item.get("note") or "{}")
        if note.get("event_id") == event["event_id"]:
            if note != event:
                raise RuntimeError("Read-back event differs from submitted event")
            print(
                json.dumps(
                    {
                        "record_id": item["id"],
                        "recorded_at": item["recorded_at"],
                        **note,
                    },
                    indent=2,
                )
            )
            with (STATE.parent / "harness-events.jsonl").open("a") as log:
                log.write(
                    json.dumps(
                        {
                            "record_id": item["id"],
                            "recorded_at": item["recorded_at"],
                            **note,
                        }
                    )
                    + "\n"
                )
            raise SystemExit(0)
    if time.monotonic() >= deadline:
        raise RuntimeError("Event accepted but not read back; do not resubmit blindly")
    time.sleep(3)
