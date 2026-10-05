# Requirements and decisions

## User requirements

These are excerpts from the user's initial request, preserving their wording:

> I want to start a brand-new software project with the working title AICQ.

> It should work as a ChatGPT plugin: an in-ChatGPT app modeled on the glory days of ICQ instant messaging.

> The chat is for communicating with other agents, not other users.

> Agent-to-agent communication should be monitorable by the human users who own the agents involved.

> It should provide universal agent chat so that, while working on something with ChatGPT, a user can say, “Hey, share this with Alice’s agent,” and that just works. Alice can likewise share with Bob’s agent.

## Backend decision

Build AICQ strictly on Fulcra for identity, messages, artifacts and shared work.
This 2026-10-05 decision supersedes the original backend exploration. The original
quotations remain in [decision history](../workspace/aicq/decisions.md).
The concrete Fulcra resource layout remains to be evaluated.

## Follow-up direction

> I’m excited! The Fulcra MCP server is open source, so we can make a fork implementing MCP Events and if it’s great we can push it to main

Proceed with the Fulcra MCP Events contribution as the delivery foundation for
AICQ. Keep the contribution reusable by other Fulcra clients. Upstream inclusion
is conditional on quality and review; this does not authorize a direct main-branch
push now. Reuse the existing `kubla/fulcra-context-mcp` fork and prepare a separate
development branch.

## UX direction

> but I want to reason backward from a great user experience

When asked which experience AICQ should optimize first, the user answered:

> Both! It’s easy to put two agents in a chat room, so we gotta help agents exchange more than chat or it doesn’t offer a unique enough value prop

Support ongoing agent conversations and useful exchanges of work. Define the
owner experience before choosing between Fulcra messaging patterns. The proposed
[review walkthrough](first-experience.md) makes this direction concrete; its
specific screens, objects, and behavior remain design hypotheses.

## Post-signup setup direction

> A freshly signed up user would need to issue the fulcra commands necessary to make new data rows or whatever; thIs can be done via MCP or CLI, either with instructions or an installable skill or plugin

Use authenticated Fulcra MCP or CLI operations to create the necessary AICQ
application resources after signup. A packaged setup skill is the proposed
ChatGPT experience; existing accounts should reuse verified resources. See the
[onboarding design](onboarding.md). The messaging schema remains open.

## Supported harnesses

> Good. For ChatGPT we’ll prefer the plugin, but we should support Codex and other agent harnesses as well

ChatGPT's plugin is the preferred experience. Codex and other compatible harnesses
must be able to participate in the same contacts, conversations, handoffs, and
artifact exchanges. Keep the core contract independent of ChatGPT UI and thread
identifiers. Verify individual integrations before claiming support.

## Proposed first-release interpretation

- Each authenticated owner has a stable AICQ identity and one default agent
  address. Sessions attach to that address rather than becoming new contacts.
  Keep the identity model extensible to multiple named agents per owner.
- Contacts use explicit invitations or existing authorized connections. Resolve
  “Alice” within the owner's contacts; ask for disambiguation if there is more
  than one match. There is no assumed global directory of ChatGPT users.
- Both owners can inspect the complete exchanged message history and delivery
  state for their conversation. This does not grant access to private ChatGPT
  sessions, unrelated Fulcra records, or private agent reasoning.
- Sending shares the selected message, handoff, or artifact. The agent derives
  “this” from the user's instruction and current permitted context. Ambiguous
  content requires clarification; the plugin cannot independently read arbitrary
  ChatGPT transcripts.
- An offline agent has a durable inbox. Receiving a message and executing work
  are distinct. An authorized subscription can trigger a supported ChatGPT Work
  chat; otherwise the next session retrieves pending messages.
- Human UI controls connect contacts, inspect messages, set policies and pause
  agents. Replies are authored through an agent workflow. A human instruction
  relayed verbatim is labeled with that provenance rather than presented as an
  independently generated agent response.
- “Universal” means an address and message contract available to compatible
  agent runtimes. ChatGPT, Codex, and other harnesses use the same stable identity
  and shared exchange state. MCP tools are the proposed common interface;
  background activation needs a supported integration for each runtime. No live
  AICQ integration has been verified yet.

## Proposed owner controls

Contact acceptance, selected-content sharing, permitted agent reply behavior,
pause/resume, block/revoke, unread status, and a clear exchange timeline. A remote
message supplies context or a request; it does not expand the recipient's authority
to use tools. Automatic agent conversations have a bounded turn budget and a
correlation ID so receipt notifications cannot create endless reply loops.

These interpretations and controls are draft design choices awaiting review.
