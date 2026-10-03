# UX-P03 — Fulcra identity and host fidelity

Date: 2026-10-03. Branch: `kublascratchpad/ux-fulcra-host-fidelity`.
Base: `a034617`. Latest user direction: “Cool. Pull relevant design cues from
https://github.com/kubla/fulcra-design-reference/blob/main/context-web/DESIGN.md
and use the Fulcra logo”. Authenticated canonical plan, spec, decisions,
progress, workboard, overview and relevant histories matched repository mirrors
before source changes. The guide and logo were read from authenticated GitHub.

## Scope and evidence

Revised `mcp/ui/prototypes/interaction-v1.html` and `extensions-v2.html`.
Original logo geometry, bundled Rubik, mint actions, violet selection and charcoal
app panels now sit inside screenshot-derived neutral host chrome. Native rail,
content tabs, chat/app division, context chips and composers were revised.
Simulation controls are outside the depicted window. Source reducers and the
existing simulated exchanges remain; no real service or host bridge is called.

Source SHA256:
- interaction-v1.html: 448546d4a0359f278228e376ceaad4b823d2ae8bc6fa042c7abec3eef82b09cd
- extensions-v2.html: fc6d1908f6027fe58172760323d0ff2cb1fb6a2113271033712d988c85b31df1

Local reusable guide: `docs/design-references/fulcra/README.md`.
Canonical guide: `fulcra-design-reference.md` and `design-references/fulcra/`.
Browser observations: `prototypes/fulcra-browser-observations.json` (22 observations).
Report: `prototypes/fulcra-evaluation.md` and `.json`; six screenshot files.
Existing flows cover polling, context versus send, mentions, inline expansion,
resource selection, file conflicts/reconciliation, setup, review/clarification,
revision use, later-session continuation and mock invitations. Console error
lists were empty. Both 390px layouts had no horizontal overflow. Logo path/viewBox
checks and embedded font byte equality passed. Browser font readiness reported
loaded; platform-font identity inspection was abandoned after a stall.

## Harness

Nurse reused owner annotation
`MomentAnnotation/51f5fa9c-a6c7-4ee5-a0e3-f602496e3bed`. Coordinator selected
independent UX-P03; Generator implemented; Evaluator performed separate browser
and integrity checks. The fixed-brand scope and 45-minute timeout override were
recorded in canonical plan before RUN_START; normal two retries remained.

Attempt 1: `ux-p03-d3e2cf79-5c86-4baa-bb76-0154abac085a`, started 13:02:32 UTC.
A CUA call took 1983.4688 seconds and exceeded the timeout. Failed REVIEW
`ad03d22e-5c92-5157-951a-4ed6be61ee0c` and RUN_INCOMPLETE
`5bfd1b54-f4a8-5473-8664-7843415800e1` were written/read back. No retroactive
extension or product promotion occurred.

Attempt 2: `ux-p03-f8c30fc1-0cbf-4de2-bc18-c876c3165901`, started 14:03:07 UTC.
Retry 1 of 2 reused the candidate, bounded subsequent browser calls and finished
narrow review, final global capture and provenance/integrity documentation.
All event receipts are in `20261003_fulcra-prototype-events.json`.

## Limits

Awaiting Michael's interaction/design judgment. These are mock captures,
not installed-client captures. Desktop appearance uses pinned official reference
images; narrow layout is extrapolated. Live linking, persistence, delivery and
permissions remain unverified. M1 complete; M2 incomplete with one retry;
M3–M6 pending. No M2 attempt, deployment, publication or security-access expansion.

Final REVIEW `a4d5c018-310a-5a42-95df-b8827749b77d`, MARK_COMPLETE
`111939af-4e27-553b-9767-4cea6720e9f0`, and RUN_COMPLETE
`039f07af-c39f-5639-bfe1-45220f74ae96` were written and read back.
Attempt 2 closed at 14:09:30 UTC, within its 45-minute limit. No active run remains.

Canonical delivery: 29 workspace, source, reference and evidence files were
uploaded and downloaded with exact byte equality. Readback receipt:
`prototypes/fulcra-canonical-readback.json`. The receipt and this final history
were then also uploaded/downloaded and compared exactly.
