# UX-P08 — host realism pass

Michael requested realistic @AICQ highlighting and a wider detail audit. Canonical
plan/spec/decisions/progress/workboard/overview and UX-P07 history were authenticated
and byte-reconciled before work. The existing public Site revision 2, version 4 and
source 8746394ffaa29b732d787d6acbbc20da180ec3da were reconciled through native Sites.
The scope and 45-minute per-run override were saved/read back before RUN_START;
two retries remained the default. Nurse, Coordinator, Generator and Evaluator
operated sequentially under the existing MomentAnnotation owner type.

Official pinned composer-mention, thread-tray and context screenshots were visually
inspected. Blue inline plugin-text treatment replaces raw @AICQ text and a detached
contact chip. The audit also corrected keyboard/draft behavior, picker dismissal,
context/history controls, user-bubble measure, status labels and the plain-text
.xlsx editor. A spreadsheet preview provides three sheets with consistent values.
See `prototypes/host-realism-notes.md` for every correction and evidence boundary.
No installed-client screenshot or new live host integration was obtained.

Initial run `ux-p08-95e7a983-ef0b-4428-915e-67f8158d200d` began 21:28:18 UTC.
Actual evaluation passed highlighting, keyboard sending, scheduling, spreadsheet
and context/history checks, but Escape left the picker open, the inspector called
a completed exchange Not started, and solo bubbles stretched beyond the transcript
measure. REVIEW `1788e838-ad38-5a1a-a44c-ca26f222d135` failed; RUN_COMPLETE
`006d9e55-657a-5c16-ad85-6712d3332e25` closed on the retry branch. Evidence:
`prototypes/host-realism-initial-observations.json`.

Retry 1 `ux-p08-5fefa822-920d-45fc-9e05-e4afe5d97f14` repaired those defects. Actual
mention deletion, repeated selection, Enter/Shift+Enter, draft/context/history,
spreadsheet and approval-only checks passed. The retained ordinary plan review
exposed an older contradiction: its summary said October 20 while the actual v3
launch stayed October 15. REVIEW `a0bd31e4-3c4d-54c1-8c2b-4c37c8e1f1ce` failed;
RUN_COMPLETE `0747f0f3-67c0-5e7f-b525-8fb6fbc5629e` closed. Evidence:
`prototypes/host-realism-retry1-observations.json`. Neither failed source was published.

Final retry `ux-p08-1b4465a4-f85f-4c8f-921b-91010fc1859b` began 21:43:25 UTC. The summary now derives its value
from the current document. Evaluator observed October 15 in ordinary review,
October 20 in the newer-document case, and v5 preserving October 20/October 19 after
reconciliation. A complete invite journey let Morgan independently choose Hermes
and accept the connection. The final @AICQ draft/sent message, continued chat,
calendar result, actual Completed inspector state and one invitation were observed.
The 390px journey displayed the latest result at bottom, with page width 390 and
no footer overflow. Resize preserves pixel scroll position and may require scrolling
to the latest result; narrow host chrome is extrapolated. No console errors; Node
syntax and diff checks passed. Actual retained and final observations/screenshots
are in `prototypes/host-realism-observations.json` and its adjacent PNGs.

Exact reviewed HTML SHA256:
`fb3733278a122ccf8273a691bebf4d14830e17aaf255ee236233d075a0af9b53`.
Native push/package produced Site source `e6b3ab97780011847674797a4e630d63ee4badba`.
Archive-backed version 5 publication `appgdep_6ac1788900e881918e7eeb9dcc959d5a`
succeeded at 21:50:09 UTC. Public audience and prior routes were preserved; the
archive's Alice HTML was byte-compared to reviewed source. Sanitized receipt:
`prototypes/host-realism-sites-deployment.json`.

Passing REVIEW `5ece3271-e14a-5cd4-80e4-02efe3f7f62d`, MARK_COMPLETE `c2905480-3efa-5c6d-ad07-8a72e9286eb4` and
RUN_COMPLETE `29ba9b49-99cd-5663-ac35-b7abb456a9fd` read back. Final run closed 2026-10-03T21:51:46.908983+00:00.
Two UX-only retries used. Temporary tab/server closed, viewport reset and unused
Sites stdin waiter terminated; earlier processes preserved. Full event readbacks
accompany this history. The canonical host-reference README still had pre-UX-P03
styling status; it was reconciled to the existing documented local fidelity pass
and augmented with this applied mention treatment. Screenshot source files unchanged.

The prototype remains a fictional HTML simulation: no real contacts, messages,
calendars, background worker or live client integration. M1 complete; M2 incomplete
with one retry; M3–M6 pending. No credentials or private backend data were published.
