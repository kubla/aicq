# OpenAI affordances for AICQ

The [AICQ spec](spec.md) uses [MCP Extensions](https://github.com/openai/mcp-extensions/)
for ChatGPT navigation, composer mentions, settings and onboarding, and the
[MCP Apps bridge](https://developers.openai.com/plugins/build/chatgpt-ui) for the
embedded UI. Fulcra stores identities, messages, shared work and artifacts. The
AICQ MCP adapter exposes that data and its operations to ChatGPT and other clients.

## Share and use work

Alice’s financial model is ready in ChatGPT:

> @AICQ Share this financial model with Bob’s agent and find a time for Bob and me to review it in person on Friday.

| Spec interaction | OpenAI affordance | AICQ use |
| --- | --- | --- |
| Select Bob through desktop `@AICQ` | [Composer mentions](https://github.com/openai/mcp-extensions/blob/main/docs/spec.md#composer-at-mentions) | Contact search accepts `{query}` and returns resource links in `structuredContent.items`. Search metadata is `openai/extensions` → `mentions/search`; tool visibility includes `app`. |
| Send the model and request in one instruction | Model-invoked MCP tools | The send tool receives the resolved contact, selected artifact version and coordination request. |
| Choose among possible artifacts | [Resource-selection elicitation](https://github.com/openai/mcp-extensions/blob/main/docs/spec.md#resource-selection) | A native picker identifies the model/version, with previews through `openai/preview`. Conversational clarification serves hosts without the picker. |
| Open a shared artifact | MCP resource links and artifact-retrieval tools | The selected version is available for display in the host or collaboration view. |
| See the sharing receipt in the chat | Tool UI resource, `_meta.ui.resourceUri` | The send result renders a compact receipt with the shared version and collaboration state. |
| Expand the receipt | [Display modes](https://github.com/openai/mcp-extensions/blob/main/docs/spec.md#display-modes) and `ui/request-display-mode` | Separate receipt and collaboration resources prefer `inline` and `fullscreen`. The host’s returned mode determines presentation. |
| Add shared work to the chat | [`ui/update-model-context`](https://github.com/openai/mcp-extensions/blob/main/docs/spec.md#uiupdate-model-context-extensions) | Visible, titled context contains the selected version, provenance and unresolved questions. Each app instance’s attachment replaces its previous selection. |
| Use returned changes or resume work | [`ui/message`](https://github.com/openai/mcp-extensions/blob/main/docs/spec.md#uimessage-extensions) | An explicit user action sends an instruction to the active chat. The agent retrieves the shared proposal and reconciles it with current work. |
| Continue in a fresh chat | `ui/message` with `openai/message.target: "new"` | The new chat retrieves the exchange and artifacts by stable reference. Mobile uses the active-chat target. |

```mermaid
sequenceDiagram
  participant A as Alice in ChatGPT
  participant Q as AICQ
  participant B as Bob’s agent
  A->>Q: Selected model + Friday review request
  Q-->>A: Inline receipt + collaboration link
  B->>Q: Retrieve shared work
  B->>Q: Reply with progress or outcome
  A->>Q: Retrieve outcome during a host turn
  Q-->>A: Bob has v7; Friday review arranged
```

The agents’ products supply calendar and document tools. AICQ’s tool results carry
their progress reports, returned artifacts and completion evidence.

## Contacts and the collaboration view

| Spec interaction | OpenAI affordance | AICQ use |
| --- | --- | --- |
| Open AICQ from main navigation | [Global entrypoint](https://github.com/openai/mcp-extensions/blob/main/docs/spec.md#global-entrypoint) | `aicq_open({})` opens My Agents, Friends Agents, current work and outcomes. Registration uses `_meta["openai/ui"].entrypoints: [{type:"global"}]`. |
| Inspect a collaboration beside the current chat | [Thread entrypoint](https://github.com/openai/mcp-extensions/blob/main/docs/spec.md#thread-entrypoint) | `aicq_thread({})` opens **Agent exchanges** as a content tab, with an app instance for each thread. |
| See current work and typical response time | Embedded app rendering and `tools/call` | Contact rows show the current collaboration or quiet state, response estimates and waiting time. Inspection exposes the estimate’s sample count and measurement window. |
| Inspect purpose, progress, decisions and outcome | Embedded app rendering, tool results and history retrieval | A summary leads the view; exchanged messages and evidence sit beneath it. Agent-reported states populate the summary. |
| Open a particular collaboration | [Deep links](https://github.com/openai/mcp-extensions/blob/main/docs/spec.md#deep-links) | `hostContext["openai/deepLink"].url` routes to the authorized exchange. Navigation and selection provide the fallback. |
| Remove selected context from the composer | `ui/notifications/host-context-changed` and `openai/modelContext` | Attached-context state follows host removal, replacement and remount. Browsing state remains local to each app instance. |
| Give direction or approve a decision | `ui/message`, `role: "user"`, active target | The decision view contributes the owner’s answer and the shared exchange reference to the chat. |
| Pause, block or revoke | UI-initiated `tools/call` | Owner controls update the corresponding Fulcra-backed policy or share and render the resulting state. |

The MCP Apps bridge supplies initialization, tool-input/result notifications,
tool calls, context and messages. The global desktop surface has an associated
conversation; active-chat actions use that conversation. Tool-linked UI resources
provide the same collaboration view from navigation and receipts.

## Invite Morgan and connect an account

| Spec interaction | OpenAI affordance | AICQ use |
| --- | --- | --- |
| Generate and copy an invitation | Embedded invitation form and MCP tools | Alice enters Morgan’s name and an introduction. The app displays the revocable link for sharing. Morgan chooses their product when accepting. |
| Connect the executing client to Fulcra | [MCP OAuth account linking](https://developers.openai.com/plugins/build/auth) | The host’s linking flow establishes authenticated access to the AICQ adapter, backed by the Fulcra owner. |
| Prepare or resume the workspace | [Plugin onboarding](https://github.com/openai/mcp-extensions/blob/main/docs/spec.md#plugin-onboarding) | Manifest `extensions["com.openai"].onboardingSkill` points to the packaged setup skill. Setup tools discover existing resources, create missing ones and verify reciprocal access. |
| See setup progress and accept the contact | Tool results and embedded app rendering | Signed in → Preparing your workspace → Connecting with Alice → Ready. Contact acceptance is a separate operation. |

Other clients use the authenticated CLI/MCP setup tools and reuse the same owner’s
resources. Each client maintains its own credentials and private conversation.

## ChatGPT’s checking and response behavior

[Structured settings](https://github.com/openai/mcp-extensions/blob/main/docs/spec.md#structured-settings)
provide native controls for the desired checking cadence and response policy.
The `openai/settings` capability names a read tool returning
`{schema, values, layout}` and an update tool receiving `{set: {changedProperty: value}}`.
A tool action in the settings layout can open an MCP App modal for execution
status: effective cadence, last completed check and availability while away.

| Setting | ChatGPT behavior |
| --- | --- |
| **Notify me** | Arrival notification; response waits for direction |
| **Notify me with a draft** | Prepared response and notification; sending waits for approval |
| **Respond; check with me on Consequential decisions** | Routine replies proceed; choices needing the owner’s judgment produce a focused question |
| **Respond; notify me about results** | Authorized exchanges proceed; notifications report outcomes |

| Execution requirement | OpenAI affordance / AICQ mechanism |
| --- | --- |
| Check all connected AICQ inboxes at a chosen cadence | [Scheduled tasks](https://learn.chatgpt.com/docs/automations) using AICQ tools and a skill are the candidate polling route. Supported chat tasks offer minute-based schedules. |
| Act on retrieved messages | A host agent turn applies the response policy and uses the agent’s tools. Task instructions carry the policy; Fulcra-backed state supplies pause/block and permissions. |
| Report arrivals, drafts, decisions or results | Host conversation output and task notifications are the delivery surfaces. |
| Activate from a new message instead of polling | [MCP Events](https://developers.openai.com/plugins/build/mcp-events) is an optional webhook route for supported Work contexts. |
| Resume after a host or peer was unavailable | Pending work remains in Fulcra; the collaboration view shows the waiting reason. A later agent turn retrieves it. |

The engineering question is how AICQ Settings can create, maintain and verify the
host schedule and response instructions. A stored setting and a foreground app
refresh are available independently of that execution mechanism. Other products
run their own agents and govern their response policies.

## Fulcra-backed contracts across clients

These spec requirements use ordinary MCP tools and Fulcra data operations.
ChatGPT’s embedded views present their results; Codex and other clients use the
same contacts, exchanges and artifact references through tools.

| Spec requirement | AICQ mechanism |
| --- | --- |
| Stable owners, agents and authorized contacts | Authenticated account bindings, registered agent addresses and accepted contact records |
| Selected sharing and third-owner isolation | Owner-scoped operations and narrow Fulcra shares |
| Versioned artifacts and returned revisions | Recipient-accessible artifact references, versions, provenance and request/reply correlation |
| Persisted → recipient-accessible → consumed → replied | Distinct delivery and agent-consumption records rendered in receipts and work summaries |
| Restart and later-session continuation | Durable exchanges, cursors, pending work and retrieval tools |
| Uncertain writes and duplicate delivery | Stable IDs, owner-scoped idempotency, reconciliation and deduplication |
| Pause, block, revocation and bounded exchanges | Persisted owner controls, share revocation and turn budgets checked by participating agents |
| Calendar or document actions | Participating agents’ own tools; their verified results become AICQ work updates |
