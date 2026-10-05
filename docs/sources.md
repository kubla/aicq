# Documentation reviewed

Retrieved over HTTPS on 2026-10-01. These are documentation observations, not
results of running a Fulcra or ChatGPT integration. References can change; consult
live contracts again at implementation time.

## Requested sources

1. [Fulcra App Starter skill](https://github.com/fulcradynamics/community-skills/blob/main/skills/fulcra-app-starter/SKILL.md).
   Requires approval of the enhanced vision before proceeding, then a recorded
   development harness, with an authenticated baseline and evaluated owner
   dashboard as M1. Snapshot: `references/fulcra-app-starter-SKILL.md`.
2. [The exact OpenAI Plugin Extensions page](https://developers.openai.com/plugins/build/extensions).
   Read the live HTML page and its Markdown representation. Documents sidebar and
   thread entrypoints, settings, deep links, Model-App Context, composer mentions,
   rich forms and onboarding. Snapshot: `references/openai-extensions.md`.

## Supporting sources

- [Fulcra harness control flow](https://github.com/fulcradynamics/community-skills/blob/main/skills/fulcra-app-starter/references/harness-control-flow.md): role separation, evidence requirements, retry counts and timeout.
- [Fulcra for agents](https://github.com/kubla/fulcra-for-agents/blob/main/fulcra-for-agents.md): owner-scoped records, direct sharing, resumable discovery, and limits of queue/group semantics.
- [Fulcra platform concepts](https://docs.fulcradynamics.com/fulcra-platform/): records, types, sources, tags and versioned files.
- [Fulcra Groups](https://docs.fulcradynamics.com/groups/): read-only participant-to-owner access, immutable group scope and consent; not a shared writable chat store.
- [Fulcra agent onboarding](https://docs.fulcradynamics.com/agent-get-started.txt): device authorization, shared-data reads and update discovery.
- [Official Fulcra Svelte template README](https://github.com/fulcradynamics/app-template-svelte/blob/main/README.md): Auth0 device flow, cookie-based server proxy, actual configuration names and framework.
- [OpenAI MCP Events](https://developers.openai.com/plugins/build/mcp-events): supported ChatGPT surfaces, protocol requirements, verified signed webhooks, persistence, replay and subscription lifecycle.
- [OpenAI plugin authentication](https://developers.openai.com/plugins/build/auth): protected resource discovery, OAuth code/PKCE, issuer/audience checks and stable identity requirements.
- [OpenAI MCP Extensions protocol](https://github.com/openai/mcp-extensions/blob/main/docs/spec.md): entrypoints, host context, deep links and extension capabilities.
- [OpenAI MCP Extensions TypeScript SDK](https://github.com/openai/mcp-extensions/blob/main/typescript/README.md): resource/tool registration and app-host bridge integration.

Local snapshots of the requested sources and principal supporting references are
included under `references/` for review. Fulcra is the required backend;
implementation research evaluates Fulcra resource layouts and API contracts.
