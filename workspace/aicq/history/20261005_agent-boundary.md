# UX-P09 — Agent boundary and person-first invitations

Canonical plan/spec/decisions/progress/workboard/overview/outstanding issues and
UX-P07/P08 history matched authenticated Fulcra before work. Revised spec, decisions
and 45-minute override were uploaded/read back before prototype edits. Existing
owner annotation reused; sequential Nurse, Coordinator, Generator and separate
Evaluator roles. The two-retry default stayed unchanged.

Michael requires AICQ to help agents communicate without owning their private
context or tools. Calendar connection and meeting preferences were removed.
Work while I’m away was an inert badge and was removed. A Codex cloud responder
setup remains a proposal; no cloud runner was created. Sender invitation is
person/name/message only; recipient chooses their own app, and old hints are ignored.

First run ux-p09-b164babb-9930-4b52-8449-1d5a4bf63142 failed browser REVIEW because
meetingCard still read removed calendarEvents/calendarId. The failed review and
retry branch closed and read back; broken source was never published. Retry
ux-p09-5899317d-ae38-4877-beba-6b18221aa570 repaired the card to show an agent-reported
result. Actual settings, platform-neutral URL, recipient Hermes choice and resumed
acceptance, old hinted link, autonomous scheduling, both approval gates, Monday
judgment, unavailable/pause/block controls and sender revocation passed. 390px
sender/recipient/result page width matched viewport. No new console errors after
repair. Syntax/diff checks passed. See prototypes/agent-boundary-notes.md,
observations JSON and PNGs. No live product or calendar access was exercised.

Reviewed HTML SHA256 44dd98df1dbd116e397c98f731f8fa4202812c48023996c21ee5806b5830b423
byte-matches deployment archive dist/alice.html. Native Sites source
 da3d5eef165f819fc36b38e4d3193012baefb2d6 produced archive-backed version 6.
Public deployment appgdep_6ac3ca5e3e3c819183b5239c8559d701 succeeded at
2026-10-05T16:03:50.812496+00:00. Public audience and historical study routes preserved.
No credentials/private backend content published. An expired source credential was
renewed normally; no alternate hosting or security changes used.

Passing REVIEW f9f6d90f-1871-5ef2-a1f5-bac399383a44 and terminal events read back.
Final run closed 2026-10-05T16:04:25.502473+00:00; terminal record 8a3c4c09-2ff4-5616-afd7-961a6bcf7b4b.
One UX-only retry used. M1 complete; M2 incomplete with one retry; M3–M6 pending.
Full event readbacks are in the adjacent JSON. Browser viewport override reset.
