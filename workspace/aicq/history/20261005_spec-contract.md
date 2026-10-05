# DOC-P03 — Product contract and writing pass

Michael requested removal of development status from the spec, including build
status and its link, and supplied the Fulcra accessibility framing. Re-read his
complete writing rules. The spec now states behavior directly, keeps illustrations
and product work states, and separates shared-context attachment from explicit
host actions. No development ledger, implementation history or pinned Extensions
reference remains in the spec.

The new section introduction uses Michael’s requested wording and unpinned link:
https://github.com/openai/mcp-extensions/. README reflects the same positioning.
Current official OpenAI documentation was searched and fetched:
https://developers.openai.com/plugins/build/extensions and the user-requested
Extensions repository. Removed the older categorical no-picture-in-picture claim;
the product selects inline receipts/fullscreen detail and negotiates capabilities.

Development status and blockers remain in progress/workboard/outstanding issues.
Implementation questions remain in plan/decisions and previous spec snapshots.
No status was hidden from the project ledger and no product milestone advanced.

## Design choices retained outside the product contract

The previous prototype interpretations remain proposals with their existing
provenance: default Handle it for me; exact state labels; median response-time
calculation over at most 20 completed samples in 30 days with five required;
notification timing/channels; future cloud responder setup; concrete Fulcra
resource layouts and execution coordination. Removing prototype/status wording
from the spec does not approve these choices or claim they are implemented.
The existing task/contact/account policy precedence remains in the spec.

Stack, hosting and optional reusable Events delivery mechanics remain engineering
planning, not the product’s positioning. Fulcra remains the fixed backend;
polling and portable clients are retained. Three images and two diagrams use the
same assets/diagram source as the earlier reviewed spec.

## Evaluation scope

Sequential roles use the existing owner annotation, independent DOC-P03 state,
default 15-minute timeout and two retries. Evaluate the full prose, invariant
coverage, absence of development status/pins/ledger links, relative assets and
Markdown structure. This is documentation evaluation, not live integration.


Review compared the full prior spec with the revised document. Selected content
and artifact versions, agent-owned tools, independent authority, policy precedence,
resumable setup, access isolation, client portability, durable IDs, write recovery,
receipts/outcomes and host interaction distinctions remain. Removed planning and
status material stays in its existing project records; provisional estimator/default
choices are recorded above. The same three images and byte-identical diagram code
remain. Markdown checks find no missing relative assets, ledger/history links,
development-status language or pinned source. Read aloud for defensive framing,
repetition and prose that announces rather than explains. No app tests are needed
for a documentation-only edit with unchanged diagrams/assets.


Final spec: 2,233 words. Run `doc-p03-2f774ab5-043a-4f06-95f1-fe7c9178e50b` closed at
2026-10-05T21:37:24.738355+00:00; terminal `cb846d36-be7f-59af-a63a-3c38f074cc8c`. No retries.
REVIEW, MARK_COMPLETE and RUN_COMPLETE were read back; adjacent events JSON
contains actual receipts. Spec, plan, decisions, review and checks byte-matched
canonical Fulcra before completion. Final closed-state records are synced separately.
