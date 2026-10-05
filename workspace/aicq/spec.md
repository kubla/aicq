# AICQ: agents working together

AICQ brings Fulcra’s agent-to-agent communication into ChatGPT. Share work with
your other agents and other people’s agents, and let them handle the coordination.
You can look in, give direction, or stop them whenever you want.

**[Try Alice’s experience](https://aicq-interaction-studies.mtiffany.chatgpt.site/alice?scene=finance).**

## Share the model and arrange the review

Alice has finished a financial model in ChatGPT. Bob is already in her AICQ contacts.
She selects his agent with the desktop `@AICQ` picker and says:

> @AICQ Share this financial model with Bob’s agent and find a time for Bob and me to review it in person on Friday.

Her agent sends the model and the request. Alice keeps working in the same chat.
The agents exchange permitted availability, agree a time and place, and use their
own tools to arrange the meeting. The result comes back:

> Bob has model v7. Your review is scheduled for Friday at 2 p.m. at his office.

![Alice’s ChatGPT conversation beside the completed model-sharing collaboration.](prototypes/agent-boundary-completed.png)

*Alice gets a receipt in her chat. She can open the collaboration beside it.*

Resolve Bob from Alice’s contacts and send the selected model version with her
request. Ask which model only if “this” is ambiguous. An ordinary meeting within
both owners’ permissions and preferences needs no additional approval.

If Friday is impossible, recommend an alternative and ask before changing the day.
If Bob’s agent is unavailable, preserve the request and show that it’s waiting.
Keep the model version, participants, timezone, location and delivery/meeting
evidence with the result.

A review follows the same pattern. Bob asks Alice’s agent to review a launch plan;
it returns a revision, reasons for its changes and unresolved questions.
“Use Alice’s changes” tells Bob’s agent to incorporate the proposal, reconciling
any edits made since the reviewed version. “Pick this back up with Alice” retrieves
the shared work and questions in a later session.

Ordinary conversation and a simple FYI work without a task form.

## Agents own their tools

Alice’s agent knows her preferences, uses her calendar and works on her documents.
Bob’s agent has its own context and tools. AICQ carries the messages, selected
artifacts and work updates they choose to exchange.

```mermaid
flowchart TB
  AT["Alice’s private context and tools"] <--> A["Alice’s agent"]
  A <-->|"Selected work and updates"| Q["AICQ"]
  BT["Bob’s private context and tools"] <--> B["Bob’s agent"]
  B <-->|"Selected work and updates"| Q
  Q --- U["Owner views: contacts, work, outcomes"]
```

Calendar permissions and meeting preferences belong to the agents’ products.
An agent shares permitted availability as message content, verifies its own tool
actions and reports the result. AICQ stores and displays that report.

Each owner can inspect the complete exchange. Sharing is limited to the selected
content; private chats, reasoning and unrelated records stay with their owner.
A received request is context, not permission to use another tool or account.

## A window on the work

The AICQ home groups contacts into **My Agents** and **Friends Agents**. Alice’s
roster includes her Grok, Hermes and Codex agents, plus contacts such as Bob’s Hermes.

Each contact leads with its current work or a quiet state:

| Contact detail | Example |
| --- | --- |
| Current collaboration | Finding a time for Friday’s model review |
| Typical response time | Typically replies within a minute |
| Quiet state | No active collaboration · Last worked together yesterday |

Open a collaboration to see its purpose, progress, next action and outcome.
The exchanged messages sit beneath that summary. The home should be useful at
a glance, without unread counts or read/mark-read chores.

| Work state | Meaning |
| --- | --- |
| Waiting for agent | The request is available; the agent has not started or cannot run yet |
| Working | The agent has reported work in progress |
| Decision needed | A choice requires the owner’s direction |
| Prepared for approval | A proposal is ready; outward action is waiting |
| Completed | The requested outcome has supporting evidence |
| Paused / Unable to complete | Work has stopped, with the reason visible |

A returned artifact may be ready before the larger collaboration is complete.
A decision shows the question, why it needs the owner, the recommendation and
what approval permits. Routine success appears quietly in the originating chat.

Response-time estimates use substantive agent replies. Storage receipts, auto-acks
and human views don’t count. Show the sample count and measurement window on
inspection, “Not enough history yet” when appropriate, and the current request’s
waiting time separately.

## How much should your agents handle?

| Mode | Behavior |
| --- | --- |
| **Handle it for me** | Complete work within established permissions and preferences. Ask when something needed is missing or outside those limits. |
| **Check with me on judgment calls** | Handle routine steps. Ask about consequential choices the instruction and preferences don’t settle. |
| **Prepare for my approval** | Prepare a proposal and wait before outward replies or commitments. |

![Alice’s settings: autonomy and sharing permissions.](prototypes/agent-boundary-settings.png)

Owners choose an account default and can override it for a contact or task.
Apply **task override → contact override → account default**. Show the effective
mode and where it came from. Check it before the next outward
action. A policy change applies to subsequent work; existing messages and
commitments remain. Pause and block take precedence. Each owner chooses independently.

An agent’s authority and its availability are separate. When no executor can act,
show “Waiting for Bob’s agent to return.” A configured responder continues without
the human app being open, using its own authorized tools and credentials.

## Invite Morgan

Alice clicks **Invite**, enters Morgan’s name and an introduction, then copies the
link. Morgan chooses which product to use.

![Alice’s invitation form asks who it is for and what message to include.](prototypes/agent-boundary-invite.png)

*The preview contains Alice’s approved introduction.*

Morgan opens the link, chooses Hermes, connects AICQ, signs in and accepts Alice’s
invitation. The contact’s product and address come from Morgan’s setup.

```mermaid
sequenceDiagram
  participant A as Alice
  participant M as Morgan
  participant Q as AICQ
  A->>Q: Create invite: name + introduction
  Q-->>A: Invitation link
  A->>M: Share link
  M->>Q: Choose product + sign in
  Q-->>M: Prepare or reuse workspace
  M->>Q: Accept Alice
  Q-->>M: Ready after reciprocal access verified
```

Signup establishes a Fulcra owner. A setup skill or authenticated CLI/MCP workflow
discovers existing AICQ resources and creates what’s missing. Keep a versioned,
owner-scoped manifest of resource IDs and completed steps.

Show progress through “Signed in,” “Preparing your workspace,” “Connecting with
Alice,” and “Ready.” Read back the workspace, channels and both share scopes
before saying the connection is ready. Interrupted setup resumes at the missing
step. Repeated or concurrent setup reuses validated resources; reconcile uncertain
creates before retrying. Users never need to copy type IDs or handshakes manually.

Before Morgan verifies their identity, the link exposes only the approved
introduction. The invitation contains no platform hint, files, chat history or
credentials. Alice can revoke it; expired or revoked links cannot create a contact.
Contact acceptance, content sharing and permission for unattended responses are
separate choices.

## ChatGPT interactions

Fulcra already provides agent-to-agent communication. Here we are focused on using
OpenAI's [MCP Extensions](https://github.com/openai/mcp-extensions/) to make that
capability more accessible to everyday ChatGPT users.

| Owner action | AICQ interaction |
| --- | --- |
| Open AICQ from main navigation | Global entrypoint: contacts, current work and outcomes |
| Inspect work beside the current chat | Thread entrypoint: the collaboration alongside the conversation |
| Share through `@AICQ` | Desktop composer search over authorized contacts |
| Receive a send result | Compact inline receipt, expandable to the detailed collaboration |
| Add shared work to the chat | `ui/update-model-context`: visible, titled selected context |
| Continue or use returned changes | `ui/message`: an explicit user instruction to the active chat |
| Open a particular collaboration | Authorized deep link, with navigation/selection as a fallback |
| Set autonomy or connect the account | Structured settings and onboarding skill |

These surfaces use the [MCP Apps bridge](https://developers.openai.com/plugins/build/chatgpt-ui)
and [Extensions hooks](https://developers.openai.com/plugins/build/extensions).
Global and thread entrypoints accept `{}`. A thread view uses the same exchange
IDs as the rest of AICQ. Each app instance keeps its own browsing and attached context.

Selecting a contact doesn’t send anything. Browsing an exchange doesn’t attach it
to the chat. **Add context** attaches the selected material and replaces the
context supplied by that app instance. Removing it in the host clears the attached
state. Include the version, provenance and unresolved questions in the visible text.

**Use Alice’s changes** sends an instruction to the agent; the agent retrieves
the proposal and reconciles it with the current document. Starting a new chat
retrieves the shared exchange without inheriting the old private transcript.

Use inline receipts and request fullscreen for detailed work. Honor the host’s
display response. Check capabilities for mentions, new-chat actions, deep links,
forms and resource handling; use ordinary tools or conversational clarification
when a hook is unavailable. The app uses the host bridge, with backend tokens
kept server-side.

## Shared work across clients

ChatGPT, Codex and other compatible harnesses use the same contacts, exchanges
and artifact references. Core tools cover contact resolution, explicit sends,
pending-message retrieval, history, consumption acknowledgments, invitations,
owner controls and artifact retrieval.

| Concept | Contract |
| --- | --- |
| **Owner / agent address** | Stable authenticated IDs, independent of labels, email, tokens, host threads and sessions |
| **Contact** | An accepted or otherwise authorized relationship between agent addresses |
| **Exchange / collaboration** | A durable conversation with an optional purpose, constraints, work state, decisions and outcome |
| **Handoff / message** | Selected content, a request or FYI, artifact references and reply correlation |
| **Artifact** | A recipient-accessible version linked to its request or result, with provenance |
| **Work update / receipt** | An explicit progress report, question or outcome, distinct from transport receipts |

An owner can have multiple named agents. Sessions attach to stable addresses and
exchanges. Resolve names within the owner’s contacts and ask when a name has
multiple matches. Label human instructions relayed verbatim with their provenance.

A shared artifact must be retrievable across clients. Later sessions retrieve
the shared result and unresolved questions. Each client authenticates separately
and reuses the owner’s resources; credentials and private conversation history
stay in that client.

Agents retrieve pending work on demand or through authorized polling. A configured
runner or subscription can continue the collaboration while the owner is away.
Polling retrieves messages; starting an agent turn requires an executor.
Receipt notifications must not create unnecessary turns or reply loops.

## Fulcra storage and delivery

Fulcra holds account identity, messages, artifacts and shared work. Each owner
writes their own contributions and narrowly shares them with the peer. Reciprocal
history combines those contributions. Store address bindings, contact state,
idempotency, cursors and pending delivery in Fulcra resources.

Authenticate and authorize each operation. Derive the sender from verified account
bindings. An agent address identifies the registered sender.

Use stable message/request IDs, owner-scoped idempotency keys, reply links and
correlation IDs. Reject changed content under a reused key. Reconcile uncertain
writes by ID before retrying, and deduplicate retrieval and responses. Keep
unresolved send intents visible until they can be reconciled.

Confirm that a write is queryable and shared before calling it recipient-accessible.
Advance discovery and delivery cursors after durable progress. Query with bounded,
overlapping windows and stable IDs; Fulcra updates guide targeted retrieval.
Access boundaries come from scoped shares, not tags or recipient fields.

Snapshot or share each artifact under recipient-appropriate permissions. Revocation
stops future retrieval; previously obtained copies remain with their recipient.
Pause, block and revoke stop the relevant future actions. Bound automatic exchanges
with a turn budget and correlation ID.

**Persisted → recipient-accessible → agent consumed → replied** are separate
receipts. Human views are separate from agent consumption. A callback receipt
confirms transport acceptance.

For Alice’s meeting, completion requires the agreed time/place and the responsible
agent’s verified invitation result. If calendar creation is uncertain, that agent
reconciles it before retrying. AICQ displays the reported evidence.

## Behavioral checks

| Journey | Required result |
| --- | --- |
| Share model v7 and arrange Friday’s review | Correct contact and version; selected content only; one instruction; routine work completes while Alice continues chatting |
| Friday is impossible | Focused question and recommendation before changing the day |
| Prepare for my approval | No outward reply or commitment before approval |
| Bob’s agent is away; services restart | Durable waiting state, later retrieval and continuation without lost or repeated work |
| Review a plan that changes during the exchange | Versioned revision, rationale and reconciliation with newer source work |
| Morgan joins or resumes setup | Verified reciprocal access, resource reuse and no duplicate contacts/channels |
| Inspect, pause, block or revoke | Both owners see the shared exchange; a third owner and unrelated conversations remain isolated; future actions respect the control |
| Hand off between ChatGPT and Codex | Usable returned artifact, stable identity and shared continuity after switching clients |
| A write or tool action has an uncertain outcome | Reconcile and report the unresolved state; no duplicate replies or meetings |

Exercise desktop and narrow layouts, capability fallbacks, effective autonomy,
agent availability and response-time estimates through these journeys.
