# UX-P09 — Agents own their tools

Source: `mcp/ui/prototypes/alice-v3.html`, SHA256 `44dd98df1dbd116e397c98f731f8fa4202812c48023996c21ee5806b5830b423`.

Michael’s confirmed boundary is communication among agents/products. Their private
context, tool access and preferences stay with them. AICQ settings now contain the
three autonomy modes and sharing explanation; calendar connection and meeting
preferences were removed. Work while I’m away was an inert Enabled badge, not an
execution control, and was removed. A cloud responder setup is recorded as a
proposal only; no worker or Codex integration was provisioned.

The model review remains interactive. AICQ shows an agent-reported scheduling
outcome, with the chosen time/location/artifact and “Sent · Reported by your agent.”
No calendar connection flag, calendar event store or calendar API trace remains.
The demo control stands in for an agent reporting its result, rather than a calendar
service callback. These results and all tools/agents are fictional simulations.

Alice’s invitation asks for a person and message. New link payloads contain only
name, introduction and id. Old platform hints are ignored. The recipient starts
without an app selected and chooses their own app. Only accepted recipient setup
resolves the platform displayed in Alice’s contact roster.

## Actual evaluation

Initial review passed settings and recipient setup, then found a completed-card
reference to deleted calendar state. The failed REVIEW and retry branch were
recorded/read back; the broken source was not published. One UX-only retry repaired
meetingCard to use agent-reported outcomes. Separate browser review exercised:

- Settings with all three autonomy modes and no calendar/away controls.
- Person-only sender form, platform-free generated URL, independent Hermes choice,
  interrupted/resumed setup and accepted contact; old Grok-hint link opens unselected.
- Autonomous share/retrieve/agreement/report with completed card; approval-only
  waits before handoff and before commitment; judgment mode waits before Monday.
- Unavailable agent, pause and block prevent retrieval; sender revocation works.
- 390px sender, recipient acceptance and completed result; page width equals 390px.

Evidence: `agent-boundary-observations.json`, failed-candidate observations and
adjacent screenshots. The repaired candidate generated no new console errors;
the original recorded calendar-reference error remains in the session log.
Node script syntax and git diff checks passed. Official pinned OpenAI settings
reference was inspected; no new installed-client capture or live integration.
Browser viewport override reset. Existing historical study routes remain unchanged.
M1 complete; M2 incomplete with one retry; M3–M6 pending.

Exact reviewed HTML published as public Site version 6; native deployment succeeded.
Receipt: `agent-boundary-sites-deployment.json`.
