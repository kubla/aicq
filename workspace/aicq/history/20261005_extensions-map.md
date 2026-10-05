# DOC-P05 — Current Extensions interaction map

Michael requested an update to `extensions-interaction-map.md` for the team’s
engineering reading pack. The current spec controls the design; it was not edited.

The map now follows Alice’s model handoff, contacts/work/outcomes, Morgan’s
person-first invitation and four ChatGPT response policies. It documents native
entrypoints, authorized contact mentions, per-instance context, explicit host
turns, receipts, settings, setup and capability fallbacks. Calendars remain with
agents. Polling is acceptable; MCP Events is an optional host activation path.

Current unpinned OpenAI sources were fetched. Extensions-specific display modes
are distinguished from the broader UI guide’s picture-in-picture examples;
capabilities and host responses control rendering. Settings persistence, checking
cadence and host execution are separate. Scheduled tasks are a candidate to test,
not a configured AICQ worker. The historical hook lab is linked as historical.

## Evaluation

Sequential Nurse, Coordinator, Generator and separate Evaluator roles used the
existing owner annotation, independent DOC-P05 state, 15-minute default timeout
and two retries. All nine preflight canonical documents matched their mirrors.
Attempt 1 `doc-p05-ce26fa21-a223-42a9-a025-e5c6b65c1b86` closed with failed REVIEW after a
local-link check found the absent workspace prototype mirror. Retry 1
`doc-p05-7c74097d-1c8a-4fe6-9b26-649ae12495dd` corrected the link to the existing repository HTML.

The Evaluator parsed Markdown with `marked`: four tables, three valid JSON
examples and five existing local links. Checked empty entrypoints, context
replacement/removal/remount, message options, mention visibility/search, settings
read/update semantics, onboarding and deferred file-write contracts against the
current fetched source. Reviewed the current spec’s authority, four policies,
all-inbox cadence, agent tool boundary and capability fallbacks. The diagram keeps
foreground refresh separate from the host-turn path. `git diff --check` passed.
Source receipts and the document hash are in the adjacent checks JSON.

No code, prototype, Site or application runtime was changed. Required live M2
checks were not run; M2 remains incomplete with one retry, M3–M6 pending. Canonical
publication and terminal event read-back are recorded below when completed.

Run `doc-p05-7c74097d-1c8a-4fe6-9b26-649ae12495dd` closed at 2026-10-05T22:25:05.148479+00:00.
REVIEW, MARK_COMPLETE and RUN_COMPLETE were read back; terminal
`1639bf8a-3c64-5cf8-b011-98ffb20d129e`. Five canonical documents byte-matched before completion;
closed-state progress/workboard/plan/history/event mirrors are synced afterward.
