# Polling design without a Fulcra MCP server change

Date: October 2, 2026. Design assessment only. Canonical plan, spec, decisions, progress, workboard, onboarding and M2 history were refreshed through normal Fulcra credentials and matched repository mirrors.

## Accepted direction

> How can we change our design to not require an MCP server change? It's OK if participating agents/products use polling for now

Polling is acceptable. A specific replacement architecture and embedded UI deferral have not yet been selected.

## Existing path

The recorded onboarding design identifies ordinary Fulcra operations for identity, dedicated annotation types, own-account writes, narrow shares, shared reads and private files. The installed Fulcra Mesh skill describes reciprocal per-peer outboxes, explicit peer authorization, envelopes serialized in the annotation note field, read-back checks, durable cursors and scheduled sweeps. Its MCP reference is descriptive; actual available tool names and behavior must be checked in each connected client. AICQ has not verified a two-owner exchange with these primitives.

The current local AICQ adapter adds four tools, UI resources and its own resource-bound OAuth gateway. Removing Events does not remove this adapter's hosting or callback requirements.

## Proposed transport and runtime boundary

Each owner writes to a dedicated outbox for one peer relationship and narrowly shares it to that peer. The recipient queries the outbox under their own authenticated access. Replies and acknowledgments go to the recipient's own reciprocal outbox. Keep contacts, thread/message identifiers, response policies and processing state in owner-scoped AICQ records/files.

Use stable logical message identifiers, reply references and explicit artifact versions. Verify persistence through read-back, distinguish persistence from recipient consumption, and deduplicate overlapping reads/retries. Pollers must catch up after downtime, address delayed visibility and ordering, and advance only safely committed processing state. Time windows alone are not an exactly-once queue. Prevent concurrent runtimes from answering the same request twice through an explicit single active consumer initially; stronger coordination needs separate validation.

Client polling runs when the user asks, when a session starts, or through an explicitly configured scheduler in a capable runtime. A persistent shell client can poll cheaply and invoke model work only for new actionable messages. An inactive chat does not become an autonomous poller because it has a skill. User-facing availability should report monitoring state and last check, not imply continuous presence.

## Two scope options

1. Retain AICQ's UI/tool adapter; remove all required Fulcra MCP Events, subscription and webhook relay work. AICQ code supplies polling. Fulcra's MCP server remains unchanged, but AICQ still needs a reachable, authenticated endpoint for the embedded ChatGPT UI.
2. Use the existing Fulcra connector/CLI plus an AICQ skill and a standalone owner dashboard. This avoids a new MCP gateway for core messaging. The native ChatGPT buddy-list/sidebar remains deferred until an AICQ adapter or another supported UI mechanism exists. That deferral requires a user decision before revising M2 acceptance.

Recommended sequencing: remove Events from the first-release critical path, validate the two-owner exchange and offline catch-up using existing tools, and decide the embedded UI boundary explicitly. Replace the proposed M5 subscription gate with opt-in polling/restart/revocation/bounded-response evaluation after that decision. Preserve M2's failed history and incomplete status; do not spend its remaining retry merely because a proposal exists.

## Official client evidence

[OpenAI MCP Events](https://developers.openai.com/plugins/build/mcp-events), fetched October 2, documents webhook delivery and explicitly excludes polling from that integration. Ordinary scheduled tool calls are a different path and need a real client acceptance check.

[OpenAI MCP server and UI quickstart](https://developers.openai.com/plugins/build/app-quickstart), fetched October 2, shows UI resources and associated MCP tools served by an MCP server. The current AICQ UI uses this model. Existing Fulcra storage tools alone do not expose the AICQ UI resource.

No code, test accounts, channels, shares, schedules, deployments, Linear ticket closures or milestone events were created in this assessment. PLAT-546 remains useful independent development tooling even if AICQ adopts the existing-connector route. The separate Events fork remains available for later work.
