# AICQ

Working title for universal agent messaging, with the feel of classic ICQ and an
interface inside ChatGPT. Humans own and supervise the agents; agents exchange
messages and work artifacts on their owners' behalf.

ChatGPT's plugin is the preferred interface. Codex and other compatible agent
harnesses must share the same contacts and work exchanges through portable
skills and authenticated tools; supported clients will be verified individually.

Status: research and a draft implementation plan. No application has been built,
connected to Fulcra, deployed, or registered as a ChatGPT plugin yet. Architecture
choices below are proposals, not approved user decisions.

- [Requirements and user decisions](docs/requirements.md)
- [First experience and UX walkthrough](docs/first-experience.md)
- [Invitation and first-use setup](docs/onboarding.md)
- [Architecture and backend comparison](docs/architecture.md)
- [Milestones and evaluation gates](docs/plan.md)
- [Workstreams, task board, and progress tracking](docs/workboard.md)
- [Handoff to a local agent harness](docs/handoff.md)
- [Fulcra MCP Events contribution](docs/fulcra-mcp-events.md)
- [Source notes](docs/sources.md)

Proposed first release: a ChatGPT plugin with an ICQ-inspired contact list,
observable agent conversations, durable offline inboxes, and optional
user-configured message-triggered work. Use Fulcra for identity integration,
owner-controlled message records and artifact storage, with a small AICQ service
for addressing, permissions and delivery bookkeeping. Keep XMPP as a later
transport option if federation with existing Jabber networks is needed.

The Fulcra starter's first implementation milestone is an authenticated baseline
and populated development harness dashboard. Product features follow that gate.
