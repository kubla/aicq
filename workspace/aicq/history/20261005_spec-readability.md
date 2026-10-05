# DOC-P01 — Engineer-readable specification

Michael requested a concise, illustrated spec for fellow Fulcra engineers after
the prototype demo. The authenticated canonical plan/spec/decisions/progress/
workboard/overview/blockers and latest UX history matched the repository before work.
The audience index and Michael’s writing rules were consulted. No suitable linked
writing sample was returned by the narrow connected-document lookup; the explicit
writing rules and user’s product direction controlled the prose.

The spec now leads with Alice sharing model v7 and arranging Friday’s review,
followed by the agent boundary, work view, autonomy, Morgan’s invitation, shared
contract, host integration, open choices and acceptance journeys. It uses three
unchanged UX-P09 screenshots and two Mermaid diagrams. README points to this
current spec and the public prototype, replacing early proposals as the entry path.
The [previous spec](20261005_spec-before-readability.md) preserves its wording;
archival notice and adjusted relative links are the only archival changes.

## Requirement coverage review

Evaluator compared the full previous spec and recorded decisions with the rewrite.
The following are coverage results, not evidence that product features work.

| Prior contract / latest decision | Location in current spec |
| --- | --- |
| Agent conversations and useful work beyond chat | One instruction, two outcomes; review/revision example and ordinary FYI |
| Selected artifact, exact version, permitted context, ambiguous “this” | Primary journey; shared contract; acceptance journeys |
| Both owners inspect exchanged work, not private chats/reasoning | Agent boundary; shared contract |
| Tools, calendars, preferences and verification stay with agents | Agent boundary; durability and access |
| Work/outcomes lead, no human inbox chores | A window on the work |
| My Agents / Friends Agents; idle, waiting, working, decision, approval, completed and stopped states | A window on the work |
| Measured responsiveness proposal, sample/window disclosure, fictional telemetry | A window on the work |
| Three autonomy modes, default and task/contact/account precedence | How much should your agents handle? |
| Routine authorized meeting needs no reapproval; explicit Friday constraint | Primary journey; autonomy; acceptance journeys |
| Policy checked at next action; pause/block wins; independent owners | Autonomy; durability and access |
| Availability separate from authority; no inert away switch | Autonomy; portable participation |
| Cloud responder is a proposal requiring real setup | Autonomy |
| Person-first invitation, no platform hint; recipient chooses | Invite Morgan |
| Signup versus resource setup; portable skill/CLI/MCP; actual manifest/read-back | Invite Morgan |
| Fresh/existing/interrupted/repeated/concurrent setup; uncertain creates | Invite Morgan; acceptance journeys |
| Contact acceptance versus content and background permissions | Invite Morgan |
| Stable owner/agent identity, sessions, authenticated sender and declared runtime provenance | Shared contract; portable participation |
| Durable IDs, idempotency, uncertain writes, deduplication and cursor advancement | Durability and access |
| Queryable/shared receipts, explicit consumption, callbacks versus execution | Durability and access |
| Scoped outboxes, reciprocal contributions, third-owner isolation and revocation | Open choices; durability; acceptance journeys |
| Artifact access/provenance, changed-source reconciliation and later sessions | Primary and review journeys; shared contract |
| Loop budget, correlation and remote-data authority boundary | Durability and access |
| Embedded ChatGPT UI, global/thread entrypoints, inline receipts and mentions | ChatGPT surfaces and portable participation |
| Visible context versus explicit host turn; removal and capability handling | Host integration table and linked hook study |
| Core tool-only use, other harnesses, separate client credentials | Portable participation; acceptance journeys |
| Polling accepted; no Fulcra MCP server change prerequisite | Portable participation; build status |
| Reusable optional Events, signed callbacks and lifecycle/delivery requirements | Implementation direction and linked contribution plan |
| Authentication flow/resource/audience checks; reuse existing gateway | Open choices |
| Mailbox/schema/database/hosting/XMPP/license choices remain open | Open choices; archived comparison and envelope/tool proposals |
| Local-first; substantial infrastructure to Josh/GCP | Implementation direction |
| M1 verified; M2 incomplete, one retry; M3–M6 pending | Build status |

The illustrative JSON envelope, backend comparison, original quotations, available
Fulcra primitive list and proposed tool names remain accessible in linked history.
Exact optional Extensions payloads and platform restrictions remain in the linked
hook study. No new transport, provider, schema, notification channel, executor or
production capability was selected by the rewrite.

## Evaluation evidence

Sequential Nurse, Coordinator, Generator and separate Evaluator roles used the
existing owner annotation, independent DOC-P01 state, two retries and a 45-minute
timeout override uploaded/read back before RUN_START.

First attempt `doc-p01-f593d538-25dc-41e8-893c-9b4b2abcbcf4` failed REVIEW: Mermaid
parsed, but horizontal diagrams shrank labels. It closed without publication.
Retry 1 `doc-p01-90502b16-82af-4065-a66d-997d5ad62a39` changed the boundary to a
vertical flow and invitations to a sequence diagram. Browser-rendered Markdown
at 1280px showed legible boundary (586 × 454) and invitation (792 × 507) diagrams,
three loaded screenshot assets and no console errors/warnings. This temporary
local preview used Marked and Mermaid 11.12.0; no app source dependency changed.

The rewrite is 3,255 words versus 6,028 (46% shorter), with one main reading path.
Link checking caught an older reference to a missing canonical Events contribution
file. Mirrored the existing contribution plan into that path and corrected its
stale M1 status/polling prerequisite sentence in both copies. Relative files,
image paths and linked heading anchors are checked separately.
This review does not run or promote any live ChatGPT, sharing, messaging, calendar
or responder acceptance gate. M2’s retry remains unchanged.
