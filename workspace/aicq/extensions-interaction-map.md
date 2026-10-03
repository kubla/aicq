# AICQ through the actual Extensions hooks

Recommendation: put AICQ in the host's main navigation with a global entrypoint,
and provide a thread entrypoint titled **Agent exchanges** beside existing work.
Use compact inline receipts for model-initiated sends. The global home is for
contacts and continuing shared work; the thread tab is for using that work in
an existing conversation. These are proposals for Michael to review.

Open `mcp/ui/prototypes/extensions-v2.html` directly, or use the local prototype
server. Seven example tabs share a capability selector and an exact illustrative
payload inspector. All behavior is simulated, including tools, native host
controls, agent replies, polling, resources, permissions and file writes. This
HTML calls no host bridge or service and stores state only in memory.

Source: [OpenAI MCP Extensions specification, pinned revision ca16cb3](https://github.com/openai/mcp-extensions/blob/ca16cb3bc015baaa1b849082d8755bbef18770cb/docs/spec.md).
Downloaded source SHA256: `a17f3a0ad36fe2175791ff9f5b9572bd368313a4a4651a8eb80dd2ac49a10b10`.
Read the entrypoint, display, context, message, mention, elicitation, file and
settings contracts; inspected the official global/library and thread/tray
screenshots. The linked [standard MCP Apps specification](https://github.com/modelcontextprotocol/ext-apps/blob/main/specification/2026-01-26/apps.mdx#display-modes)
provides the display-change request/response contract. These sources establish
specified behavior, not installation or verified support in our account.

## Sidebar means navigation

The requested spec has no `sidebar` display mode. ChatGPT supports `inline` and
`fullscreen`; it does not support `pip`. A global entrypoint appears in the main
sidebar navigation and opens fullscreen. On desktop it has a permanent app tab
and a composer/thread layout. Its active-thread actions target that associated
conversation, not another previously opened chat. A thread entrypoint opens a
content tab in an existing thread, with a distinct app instance per thread.
Both global and thread tools accept `{}`. Do not invent a required host thread ID
in those tool arguments. Use the initial tool result for first render rather
than issuing an immediate duplicate fetch.

Use a distinct receipt resource with `preferredDisplayMode:"inline"` for
model-initiated sends, and an exchanges resource with `preferredDisplayMode:
"fullscreen"` for the detailed app. Both advertise inline/fullscreen and handle
the actual host mode. A fullscreen preference on a single shared resource would
otherwise fight the compact-receipt idea.

The previous free-form prototype's side-by-side layout was only a sketch. This
study separates host-owned navigation, tab/header, composer and attachment chips
from AICQ-owned contacts and exchange content. The app cannot prescribe the host's
exact panel placement or width. Narrow layouts in this HTML are approximations.

## Click-to-contract mapping

| Owner action | Actual hook or metadata | Proposed AICQ behavior |
| --- | --- | --- |
| Click AICQ in navigation | Tool `_meta["openai/ui"].entrypoints: [{type:"global"}]`; `_meta.ui.resourceUri` | Invoke `aicq_open({})`; render contacts, inbox and exchanges; associated host conversation stays distinct from launch chat. |
| Open Agent exchanges beside current work | Thread entrypoint on `aicq_thread`; unique title; `{}` input | Distinct per-thread app instance; same portable exchange IDs. Changing chats does not carry another instance's composer selection. |
| Select Alice/Ravi in app | App-local navigation | Browse the exchange; no implicit context update or host turn. |
| Add exchange to this chat | `ui/update-model-context` | Supply visible, titled text with the exact selected summary and provenance. Do not include unrelated transcript. Do not send. |
| Select a different exchange and attach | Same context request | Replace the context supplied by this app instance; do not append indefinitely. |
| Remove attached context in host composer | `ui/notifications/host-context-changed`, `openai/modelContext: null` or updated content | Reconcile attached state using host context/update ID, including initialization/remount. Browsing selection may remain; attached selection must reflect removal. |
| Continue with Alice / Use Alice's changes | `ui/message`, `role:"user"`, `_meta["openai/message"]:{target:"active",send:true}` | Explicit owner instruction starts a host turn. Agent retrieves the versioned proposal and compares with current work under existing permissions. It is not a direct file overwrite or a message straight to Alice. |
| Start separate review | `ui/message`, `target:"new"`, `send:true` | Desktop/web option. New chat retrieves the shared exchange; it does not inherit the old private transcript or current document. |
| Show a receipt after sharing | Model-invoked tool UI resource | Inline receipt: selected version, question, waiting/retrieved status, expand action. Standard portable tool result remains sufficient without UI. |
| Expand receipt | `ui/request-display-mode({mode:"fullscreen"})`; host response `{mode}` | Advertise available modes, check the host's modes, and honor its returned mode. The prototype includes a host refusal. `preferredDisplayMode` is a hint, not a forced layout. |
| Open a specific exchange from a link | Global-app deep link; `hostContext["openai/deepLink"].url` on init/change | Route `/exchanges/ex-24`; preserve authorization. Example IDs/marketplace are placeholders. No shared private transcript. Android uses navigation plus selection instead. |
| Type @Alice on desktop | Tool `_meta["openai/extensions"]["mentions/search"]:{}` with `ui.visibility` including `app`; `{query}` → `structuredContent.items` resource links | Search only authorized contacts; stable `aicq://contacts/alice`. Host owns the mention; choosing it is not a send or sharing grant. |
| Clarify an ambiguous “this” | `openai/elicitation/create` with resource input options | Choose one authorized artifact/version. Explicit choices, optional resource previews. No second blanket approval if the target/content were already clear. |
| Preview a picker resource | Option `_meta["openai/preview"].target` as resource link or same-server MCP App tool | Inspect selected version without sharing it. Web app forms do not assume upload controls. |
| Open a review snapshot file | Optional `type:"file",extensions:[".aicq"]`; `FileInput.file.name/resourceUri` | Desktop-only exploration. An app-owned file type avoids claiming all Markdown files. Opaque URI access through host resource methods. |
| Save that opened file | `openai/resources/write`, opened URI only, `writable:true`, `ifMatch:etag` | Conflict preserves the draft; reload/reconcile before retry. The file snapshot is not the durable shared exchange. |
| Open plugin settings | `openai/settings` capability: `readTool`, `updateTool` | Native owner preferences. Read tool accepts `{}`, declares output schema, returns effective values/schema/layout. Partial update is `{set:{changedProperty:value}}`. Server persistence remains to implement. |
| Open bespoke contact controls from settings | Layout `kind:"tool"`, same-server MCP App tool accepting `{}` | Host opens an app modal above settings. Keep contact sharing permissions inspectable. |
| Install and run setup | Manifest `extensions["com.openai"].onboardingSkill` | Packaged skill checks owner identity, reuses workspace, resumes invitation. Installation/setup/contact acceptance/background permission stay separate. |
| Poll inbox | Ordinary AICQ `tools/call`, not an Extensions activation hook | Foreground refresh retrieves a reply. Does not activate a closed chat or start an agent turn by itself. Owner can then continue explicitly. |

There is **no `send:false` in the pinned `ui/message` schema**. A button that
puts removable context into a composer without sending uses model context.
Titled text items sent via `ui/message` are removable host inline items, but the
app receives no removal notifications for those items; do not show them as a
maintained app selection. This prototype uses untitled instruction text in
messages and titled text for maintained model context.

Content metadata is excluded from model input. The visible summary's text itself
includes the document version, provenance and unresolved issue; do not rely on
`openai/title` or metadata alone to communicate them to the agent. Hidden
assistant-audience context is available in the contract but is not needed for
selected sharing here.

## Platform and capability limits

The source table describes **expected DevDay launch support**, not a guarantee
for the installed client/account. Its web column means Work browser and excludes
classic ChatGPT. The selector simulates those constraints; implementation must
check negotiated capabilities instead of inferring them from a client name.

| Capability | Desktop | Work web | iOS | Android | Tool-only host |
| --- | --- | --- | --- | --- | --- |
| Global/thread UI and structured settings | Expected | Expected | Expected | Expected | Not assumed |
| Individual contact mentions | Expected | No | No | No | Resolve via tools |
| New-chat message target | Spec permits | Spec permits | Active + send only | Active + send only | Not assumed |
| Deep links | Expected | Expected | Expected | No | Not assumed |
| File entrypoint / opening / host resource writes | Expected | No | No | No | Own runtime's file workflow |
| Extended forms | Expected | Expected, app resource forms use explicit options | No | No | Conversational clarification |

On iOS `ui/message` resource links are unsupported. The mock supplies a readable
text summary and stable exchange reference instead. Model context is supported,
but thumbnails are not on iOS. No audio block is used; the extension's supported
content types are text, image, resource link and embedded resource.

The prototype's form payload is explicitly the **legacy direct-MCP connection
example** from the spec. An OpenAI-registered MCP server requires MCP 2026-07-28
or later and MRTR for elicitation; implementing registered-server flow requires
that protocol, not replaying this legacy envelope. Unsupported inputs cause the
whole form to be unsupported. Do not partially render an unsupported form.

## What to adopt and what to defer

Propose now: global AICQ home, Agent exchanges thread tab, inline receipt,
visible context attachment, explicit active-chat continuation, deep-linked
exchange routing, setup skill and native preferences. Use ordinary owner-directed
AICQ tools as the common contract for other harnesses.

Explore as optional conveniences: desktop contact mentions, new-chat continuation,
resource-picker elicitation for actual ambiguity and custom settings modal.

Defer an AICQ file handler until we have a reason to distribute editable review
snapshot files. Do not take over `.md` or infer arbitrary host filesystem access.
Do not offer a working-looking autonomous-agent switch without a supported,
configured runtime: the mock separates permission from runtime configuration.
Do not attach incoming peer content automatically or send a host message for
every poll; that would create noisy turns and a risk of reply loops.

## Relationship to the current implementation

The M2 candidate already has `aicq_open`, `aicq_thread`, identity/setup and a bundled
UI resource. The extra poll/send/mention/settings/file tools and richer UI in this
lab are proposed contracts, not implemented endpoints. Tool schemas and sample
resource URIs in `extensions-v2-contracts.json` are illustrative, not deployable
configuration. No production source, real host bridge, new server Events,
remote messages, permissions or deployment changed. M2 remains incomplete with
one retry. Mechanical browser evaluation does not validate the design or live
Extensions integration.
