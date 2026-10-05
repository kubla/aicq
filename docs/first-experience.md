# First experience: a review that becomes useful work

Status: proposed UX walkthrough, informed by the user's requirement to support
both conversations and exchanges beyond chat. The details below are design
hypotheses, not additional approved user decisions. UX-P01 now provides a
self-contained HTML prototype at `prototypes/interaction-v1.html`; browser controls
were exercised, but the design and live integration remain unvalidated. See
`history/20261002_interaction-prototype.md`. UX-P02 adds actual Extensions hook
examples at `prototypes/extensions-v2.html`, with a source-grounded mapping in
`extensions-interaction-map.md`; specific interaction choices still await review.

## Product promise

Share selected work with another person's agent, get a useful result back, and
continue the collaboration across sessions. Both owners can follow the exchange.

## First walkthrough

Bob is working on a launch plan in ChatGPT and already has Alice as a connected
AICQ contact. He says:

> Ask Alice's agent to review this launch plan for scheduling conflicts and
> suggest a revision.

1. Bob's agent prepares a handoff containing the selected plan, the review
   question, relevant constraints, and the desired output: a proposed revision
   with an explanation of changes. It uses permitted context to make the request
   intelligible without sharing unrelated conversation history. If “this” is
   ambiguous, it asks which artifact to send.
2. AICQ records the request and the exact artifact version. Bob sees the review
   in Alice's contact view, with its purpose and current state. Sending follows
   the host's tool confirmation behavior and Bob's configured sharing policy;
   the design adds no separate approval step by default.
3. If Alice has no authorized active workflow, the request waits in her inbox.
   The UI says “Waiting for Alice's agent,” without implying that a webhook or
   storage receipt means work has begun.
4. Alice's next authorized session, or an explicitly configured supported
   subscription, retrieves the handoff. Her agent may use context available
   under Alice's permissions, and shares only the information needed and
   permitted for this exchange. Missing information produces a focused question.
5. The agents can exchange clarification in the same review. Both owners see
   what was exchanged and can provide direction or pause the collaboration.
6. Alice's agent returns a proposed plan revision, the reasons for its changes,
   and any unresolved questions. AICQ presents the result beside the discussion,
   linked to the version Alice reviewed.
7. Bob says “Use Alice's changes.” His agent inspects the proposal against the
   current plan and incorporates the applicable changes within its existing
   permissions. If the plan changed in the meantime, it reconciles differences
   rather than silently replacing newer work.
8. In a later session, Bob says “Pick this back up with Alice.” His agent
   retrieves the exchange's latest result and unresolved questions. AICQ supplies
   shared continuity; it does not need access to an earlier private transcript.

## Three surfaces to sketch first

| Surface | What the owner should understand immediately |
| --- | --- |
| Contact roster | Who is connected, what arrived, and which collaborations need attention |
| Collaboration view | Purpose, participating agents, exchanged messages, current progress, and questions for the owner |
| Result view | Returned artifact, version reviewed, proposed changes, rationale, and actions to use the result in the current chat |

The contact view holds both ordinary conversation and purposeful collaborations.
A simple FYI message must remain easy to send; it should not require a task form.
Conversational follow-ups can refer to a request or artifact without losing their
relationship to the work.

## Smallest useful product model

- **Contact:** a stable authorized relationship between owners' agent addresses.
- **Exchange:** a continuing conversation with an optional purpose and outcome.
- **Handoff:** selected context, a request or FYI, and artifact references.
- **Artifact:** a recipient-accessible version with provenance and a relationship
  to the request or result that produced it.
- **Work update:** a stated acknowledgment, progress report, question, or result.
  Persisted messages and callback receipts alone cannot imply this progress.

The first design should demonstrate waiting, working, input needed, result ready,
and paused. These are proposed owner-facing states; the delivery implementation
will also need separate persistence and retrieval receipts.

## Design walkthrough checks

Before choosing the transport, walk through the scenario and ask whether each
owner can tell what was shared, what the other agent is doing, what came back,
and how to continue. Include an offline recipient, a clarification question, a
changed source document, a paused exchange, and a later session.

The decisive outcome is a usable revision with preserved context and provenance.
Two agents exchanging text alone does not satisfy this walkthrough. Ordinary
agent chat remains part of the required product.

## Implementation sequence

1. Sketch these three surfaces and the exchange transitions against this story.
2. Start the Fulcra starter's required M1: authenticated local baseline and populated,
   evaluated owner harness dashboard. Keep product implementation within the
   subsequent milestone runs.
3. Validate ChatGPT linking and two-owner sharing. Compare per-peer annotation
   outboxes from Fulcra Mesh with reciprocal shared-folder mailboxes against the
   same handoff, artifact, discovery, and access-revocation requirements.
4. Implement and evaluate one complete two-owner review exchange, including
   ordinary replies, a returned revision, and later-session retrieval.
5. Add and validate optional Events activation for that already durable exchange.

Fulcra is the fixed backend. Its resource layout, adapter hosting and exact
structured request/result schema remain open. The existing MCP 2 readiness commit is a prerequisite; it does not yet
implement Events or the AICQ app.
