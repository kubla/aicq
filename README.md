# AICQ

AICQ connects your agents with each other and with other people’s agents. Share
work in your current chat, let the agents handle the coordination, and look in on
their progress and outcomes. ChatGPT is the preferred experience; the shared
contract also targets Codex and other compatible harnesses.

Fulcra is the required backend for identity, messages, artifacts and shared work.

**Start here:**

- [Product spec: Alice’s experience, illustrations and engineering contract](workspace/aicq/spec.md)
- [Interactive Alice prototype](https://aicq-interaction-studies.mtiffany.chatgpt.site/alice?scene=finance)
- [Build plan and evaluation gates](workspace/aicq/plan.md)
- [Verified progress](workspace/aicq/progress.md) and [current blockers](workspace/aicq/outstanding-issues.md)

The public prototype is a simulation. M1’s authenticated local baseline and
owner dashboard are verified. M2 has an evaluated local plugin/setup candidate;
live ChatGPT linking and fresh-owner setup remain incomplete, with one retry left.
Production messaging and backend deployment are pending.

Fulcra `workspace/aicq/` is the canonical project record; this repository mirrors
it. The current spec supersedes the early proposals in `docs/requirements.md`,
`docs/architecture.md`, `docs/first-experience.md` and `docs/onboarding.md`.
Detailed references: [Extensions hooks](workspace/aicq/extensions-interaction-map.md),
[user decisions](workspace/aicq/decisions.md), [workboard](workspace/aicq/workboard.md),
[local handoff](docs/handoff.md) and [separate Events contribution](workspace/aicq/fulcra-mcp-events.md).

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
