# AICQ agent instructions

Canonical workspace: `workspace/aicq/` in the owner's Fulcra File Store.
Before creating or revising ChatGPT/Codex mockups, read
`docs/design-references/openai-host/README.md` and inspect the matching screenshots.
Use their host layout and controls; distinguish official reference images from
installed-client observations and simulated AICQ behavior.
For AICQ app styling, also read `docs/design-references/fulcra/README.md`.
Use its sourced Fulcra logo and app tokens; preserve the native host styling.
Skill: [Fulcra App Starter](https://github.com/fulcradynamics/community-skills/blob/main/skills/fulcra-app-starter/SKILL.md).
Local reference snapshots: `docs/references/fulcra-app-starter-SKILL.md` and
`docs/references/fulcra-harness-control-flow.md`.

Before continuing, read the canonical plan, spec, decisions, progress, workboard,
and relevant history using authenticated Fulcra file tools or the CLI. Reconcile
them with repository mirrors and actual source state. Honor the user's instructions
over skill defaults. Preserve exact user decisions; distinguish them from proposals.

The user chose local-first development when feasible, with substantial infrastructure
problems deferred to Josh/GCP. M1 therefore evaluates a real local authenticated
baseline and populated owner dashboard; public deployment is deferred. Keep all
other harness recording, evaluation, and access-isolation requirements.

Implementation must follow recorded milestone runs. Use the existing harness type
`MomentAnnotation/51f5fa9c-a6c7-4ee5-a0e3-f602496e3bed` in the project owner's account;
do not create another or assume a different owner can write it. Nurse manages harness
machinery, Coordinator manages state, Generator implements, and Evaluator performs
separate verification. A single agent may perform those roles sequentially.
Record real evidence, read back events, and keep blocked checks incomplete.
The defaults are two retries and a 15-minute run timeout; record overrides first.

ChatGPT is the preferred plugin experience. Core contacts, exchanges, and artifacts
must support Codex and other compatible harnesses. Client-specific UI and background
activation must not be required for basic messaging. No live AICQ integration has
yet been verified. Keep the reusable Events contribution separate in the Fulcra MCP
fork, branch `aicq/mcp-events`; published prerequisite commit `429da58` is protocol
readiness, not an Events implementation.

Keep credentials in the executing client's normal credential management. Never
commit tokens, browser cookies, device authorization codes, or secret configuration.
Connecting to another executor or agent does not transfer authentication or private
conversation history. Use explicit handoff state and authenticate separately.
