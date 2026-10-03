# AICQ interaction studies

For host appearance, consult [the OpenAI host reference](../design-references/openai-host/README.md)
and [its screenshot gallery](../design-references/openai-host/index.html) before
revising either prototype. Both studies received a host appearance and Fulcra
styling pass in UX-P03. Read [the Fulcra reference](../design-references/fulcra/README.md)
for app tokens and sourced logo assets. [Current evaluation](fulcra-evaluation.md)
records screenshots, source hashes, simulated-flow checks and remaining limits.

Open `../../mcp/ui/prototypes/interaction-v1.html` directly in a browser. It is
one HTML file with inline CSS and JavaScript; no install, build, authentication
or service is needed. State lives in memory and resets on reload.

Question: can an owner share selected work, follow the exchange and use the
returned work without managing a task system?

Try Review a plan, A question comes back, Your document changed, and Return
tomorrow. Free play supports contact switching, notes, pause/resume and a mock
invitation. The bottom prototype controls stand in for another agent; they
perform no network calls. New session simulates continuation within this page,
not persistence across reloads. Inspect the exchange state shows current/shared
versions and observed retrieval.

Hypotheses to review:

- Asking the host agent to share sends directly, with an inspectable receipt.
- People remain the navigation; documents and returned changes anchor the exchange.
- A newer source document requires reconciliation before using a revision.
- Waiting reports lack of retrieval; it does not suggest an inactive agent is working.

These are prototype choices awaiting Michael's review. Browser control checks
passed; no real agent delivery, ChatGPT rendering, contact permissions or Fulcra
persistence is implemented. M2 remains incomplete. Keep this throwaway prototype
separate from application source until an interaction is validated.

Canonical record: workspace/aicq/history/20261002_interaction-prototype.md.

## Extensions study 02

Open `../../mcp/ui/prototypes/extensions-v2.html` directly. Seven examples map
AICQ to the actual Extensions hooks; use the host capability selector and the
payload inspector. Notes: `extensions-v2-notes.md`. Proposed metadata:
`extensions-v2-contracts.json`. Browser observations:
`extensions-v2-browser-evidence.json`. This HTML calls no host bridge or service.

Recommend global navigation + Agent exchanges thread tab + inline receipts.
These hook choices await owner review; real installed-host support remains open.
