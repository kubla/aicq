# Host UI reference gathering

Date: 2026-10-03. Local branch: `kublascratchpad/host-ui-reference`.

## User request and scope

Michael requested more realistic mockups by inspecting installed Bits & Bolts and
the surrounding ChatGPT/Codex window through Computer Use. He explicitly allowed
realistic web screenshots if the inspection failed, and asked for durable project
artifacts to guide future mockups. This task gathered references and documented
them; it did not implement a product milestone or redesign existing prototypes.

## Reconciliation

Authenticated via the executing client's normal Fulcra CLI storage. Downloaded
canonical plan, spec, decisions, progress, workboard, overview, interaction map
and UX-P02 history; all matched repository mirrors before changes. M1 complete;
M2 incomplete with one retry; M3–M6 pending. These statuses are unchanged.

## Computer Use evidence

`cua.getState()` found the running ChatGPT app, bundle `com.openai.codex`. The
Codex MCP Apps browser had no tabs. `cua.getApp("com.openai.codex")` returned:
“Computer Use is not allowed to use the app 'com.openai.codex' for safety reasons.”
No native interaction or live capture followed. No callable CAD/library/tray
tools were exposed to this executor. The installed Bits & Bolts Remote 1.0.23
skill was read; it describes library and tray tools but does not grant app access.
Unrelated inventory titles were excluded from durable artifacts.

## Authorized fallback and deliverables

Saved nine unchanged PNG screenshots from OpenAI's public `mcp-extensions` repo,
pinned to `ca16cb3bc015baaa1b849082d8755bbef18770cb`. Reopened the current public
spec during this task; source image paths match the pinned specification. Images
show Bits & Bolts Local and carry documentation annotations. They do not verify
the installed Remote plugin or current client behavior.

Repository: `docs/design-references/openai-host/`. Canonical folder:
`workspace/aicq/design-references/openai-host/`. Files: nine original PNGs,
README.md, index.html gallery, manifest.json, host-tokens.css. The manifest records
source URLs, dimensions, byte counts, SHA256 hashes, palette sample coordinates,
approximate layout bounds and the Computer Use failure. `host-ui-reference.md`
is the canonical summary. AGENTS.md and docs/prototypes/README.md point future
mockup work to the guide. Plan, decisions, progress and workboard record the scope.

## Verification

All nine PNGs were opened and visually inspected. PNG decoding/dimensions and
SHA256 hashes were checked. Exact palette values were sampled from named image
coordinates; layout measurements are approximate and normalized by a declared
half-size convention, not a claimed device pixel ratio. Font, padding and radius
tokens are explicitly estimates. The gallery opened in the in-app browser at
http://127.0.0.1:6190/; its source/status notice, navigation, global image and
chat-side tray anchor were inspected. This browser observation verifies the
reference gallery, not a live Bits & Bolts interface.

## Resume state

Use the guide for the next prototype fidelity pass. Existing interaction-v1 and
extensions-v2 were not changed. Native installed-client captures, light theme and
mobile host appearance remain unverified. No deployment, product run, milestone
promotion, M2 retry, security access expansion or message to another person.
Canonical upload/read-back receipts are in host-ui-reference-sync.json.
