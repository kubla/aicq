# AICQ

Working title for universal agent messaging, with the feel of classic ICQ and an
interface inside ChatGPT. Humans own and supervise the agents; agents exchange
messages and work artifacts on their owners' behalf.

ChatGPT's plugin is the preferred interface. Codex and other compatible agent
harnesses must share the same contacts and work exchanges through portable
skills and authenticated tools; supported clients will be verified individually.

Status: M1 passed local acceptance. The official Fulcra Svelte baseline and owner
dashboard run locally. M2 has a verified local plugin/account setup implementation;
required ChatGPT installation and account linking remain blocked. See
[the M2 evaluation](workspace/aicq/history/20261001_m2-local-plugin.md) and
[configuration/access blockers](workspace/aicq/outstanding-issues.md). Product
messaging and public deployment remain pending. Architecture choices below remain proposals.

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

## Local development

Requires Node.js 22 and npm. Run `npm ci`, copy `.env.example` to `.env`, and set
`OWNER_USER_ID` from the intended owner's `fulcra user-info` result. The example
uses Fulcra's public device-flow client and API endpoint. Never add credentials
to these files; the Fulcra CLI and browser authenticate separately.

Run `npm run dev`, then open http://127.0.0.1:6173/. Sign in through the browser.
The server binds to loopback only. The configured owner sees global navigation
to `/harness`; other accounts cannot read the dashboard or its data endpoints.
Run `npm run check`, `npm run lint`, `npm test`, and `npm run build` to verify
the source. The build uses the Node adapter; no public deployment is configured.

The dashboard reads actual events from the existing harness annotation and
canonical `workspace/aicq/overview.md` and `outstanding-issues.md` files in Fulcra.
It refreshes every five seconds and shows failures explicitly. Ownership is
verified through Fulcra on the server; the configured owner ID stays server-only.

`scripts/harness.py` records an event, polls for that exact event's read-back,
and retains a local receipt under ignored `.local/`. Every event needs truthful
detail and evidence. Load the canonical workspace before starting another run;
use the configuration recorded in `workspace/aicq/plan.md`. The initial M1 setup
run has a recorded 60-minute override; later runs default to 15 minutes.

Template source: `fulcradynamics/app-template-svelte` at
`613a3d817df7933e73b6fb9cbda86fd7377b8e6b`.
