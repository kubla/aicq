# DOC-P04 — ChatGPT-specific agency settings

Michael reframes the control as “How far can our plugin push ChatGPT to act
agentically?” Participation by other products assumes they run their own agents
and write back autonomously. AICQ Settings aspires to change ChatGPT’s participation;
it is not a policy that remotely controls every connected agent/product.

The spec now separates checking cadence across all connected AICQ inboxes from
four response/notification policies: arrival only; arrival with a draft;
autonomous routine response with Consequential decisions brought to the owner;
autonomous response with results-only notification. The primary Alice example
states its autonomous/results-only setting instead of treating that as ChatGPT’s
default. Missing authority or explicit constraints remain binding in every mode.

Actual/effective cadence, last completed check, ability to run while away and
the distinction between fetching a message and starting a host turn are explicit.
No interval or default mode was chosen, and no host-control ability was asserted.
The outdated three-mode settings screenshot was removed from the spec; its file
and public prototype remain unchanged. Other illustrations/diagrams are retained.

## Official host research

Read current official documentation, without pinned links:

- [MCP Events](https://developers.openai.com/plugins/build/mcp-events): webhook
  subscriptions activate supported Work contexts according to user instruction.
  This integration does not support its draft protocol’s polling or streaming
  modes. It is not evidence for an AICQ-configured client polling cadence.
- [Scheduled tasks](https://learn.chatgpt.com/docs/automations): scheduled web tasks
  can use plugins/skills available to their chat; chat follow-ups can have
  minute-based intervals. Skills can create/update scheduled tasks. This suggests
  a candidate polling route without a Fulcra MCP change, not proof of AICQ setup
  or of a plugin settings control enforcing it. No schedule was configured.

Engineering inference: desired check frequency, host activation and response policy
need separate evaluation. Do not substitute UI refresh for agent execution, claim
all ChatGPT surfaces can run in the background, or silently add an Events server
change as a prerequisite. Polling remains acceptable for other participating
products and any supported ChatGPT executor we establish. Fulcra-only backend
and local-first hosting directions are unchanged.

## Review scope

Sequential Nurse, Coordinator, Generator and separate Evaluator roles use the
existing owner annotation, independent DOC-P04 state, default 15-minute timeout
and two retries. Evaluate four policies, checking scope/cadence, remote-product
authority, truthful unsupported execution, constraints, notification semantics,
product-only prose and Markdown/assets. No code/prototype/hosting was changed;
no required M2 live gate was exercised and its retry remains unchanged.


Separate review passed: all four behaviors and all-inbox cadence are explicit;
the desired policy is scoped to ChatGPT, rather than peers; requested interval
is not reported as an available scheduler; read/refresh is distinct from an
agent turn. Mode four remains within permissions and host confirmations, and
mode three escalates Consequential decisions. No default or interval invented.
Two existing images and both unchanged diagrams remain; Markdown/assets/diff
checks pass. Existing versioning, isolation, recovery and Fulcra-only contracts
remain. No prototype or application source changed.


Run `doc-p04-02a7480c-0c2c-42fa-8cb4-f98df5ebbe4e` closed at 2026-10-05T21:54:46.693909+00:00; terminal
`f50e6122-118c-5bf6-9341-6b4be759445d`. No retries. REVIEW, MARK_COMPLETE and RUN_COMPLETE were
read back; actual event receipts are in the adjacent JSON. Five canonical documents
byte-matched before completion; final closed-state records are synced separately.
