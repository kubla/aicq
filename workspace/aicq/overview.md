# AICQ

**Status:** Planning and upstream Events feasibility review prepared. Fulcra
authentication is complete; the application baseline has not started.

Next: start the local-first baseline through the harness. Private `kubla/aicq`
exists; API content writes and issue creation work. Issue 1 tracks M1. Normal
Git push remains blocked; the API publication path is available.
A task board covers identity/invites, work exchange, ChatGPT UI, Events, and
cross-harness delivery. The messaging pattern remains open.

- M1: authenticated local baseline and verified harness dashboard — pending
- M2: plugin shell and account linking — pending
- M3: isolated reciprocal mailboxes — pending
- M4: durable agent messaging — pending
- M5: Fulcra MCP Events relay and subscribed work — pending
- M6: usability and distribution — pending

The existing Fulcra MCP fork now has a tested MCP 2 readiness commit. It removes
the obsolete private-API patch and passes 132 tests, including authenticated modern
HTTP requests. Events subscriptions and delivery remain to be implemented.
