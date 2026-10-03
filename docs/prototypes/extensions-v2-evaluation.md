# UX-P02: Extensions-grounded interaction prototypes

User request: use the actual OpenAI MCP Extensions affordances to make the
interaction prototypes specific, with sidebar navigation preferred and multiple
examples where useful. Hook choices remain proposals awaiting Michael's review.

## Sources and deliverables

Source: openai/mcp-extensions revision
`ca16cb3bc015baaa1b849082d8755bbef18770cb`, docs/spec.md, SHA256
`a17f3a0ad36fe2175791ff9f5b9572bd368313a4a4651a8eb80dd2ac49a10b10`.
The standard MCP Apps specification supplied request-display-mode syntax.
Official global/library and thread/tray screenshots were inspected. Current
canonical plan, spec, decisions, progress, workboard, overview, first experience,
previous prototype/M2 histories and outstanding issues were refreshed and matched.

Local branch: `kublascratchpad/ux-extensions-v2`.
Local prototype: `mcp/ui/prototypes/extensions-v2.html`.
Canonical prototype: `prototypes/extensions-v2.html`.
Final HTML SHA256: `733e2ff0e344e64a14bfbfa03bf46c80f6debff6b9900ee5b7c9b71ed0f77ef1`.
Canonical recommendation: `extensions-interaction-map.md`.
Local illustrative metadata: `docs/prototypes/extensions-v2-contracts.json`.
Browser URL: http://127.0.0.1:6188/extensions-v2.html.

## Design outcome

Recommend global AICQ navigation, an Agent exchanges thread tab and compact
inline receipts. The spec has no sidebar display mode: global entrypoints open
fullscreen, while a thread entrypoint supplies a content tab. Host controls remain
host-owned. The desktop permanent app tab's active conversation differs from the
previous launch chat. A global action cannot silently inject a proposal into that
older conversation; it asks for the current document or directs the owner to use
its thread tab instead.

Add to this chat uses visible context replacement without a turn. Continue/Use
sends an explicit user instruction to the active host chat; new-thread target is
optional on desktop/web. No send:false is invented. Optional mentions, resource
clarification and file view each have appropriate platform fallbacks. Resource
writes use the opened writable URI and ETag. Background permission does not start
a runtime; polling updates the app without generating an agent turn.

Seven example tabs cover global, thread, inline, mentions, clarification, file
viewer and setup/settings. The selector simulates expected support from the
pinned spec, not negotiated capabilities or installed-client verification. The
form example is legacy direct-MCP; registered-server MRTR remains to implement.
The file type is a proposed .aicq snapshot, not a handler for arbitrary documents.

## Harness and evaluation

Existing owner annotation reused. Independent UX-P02 state and 45-minute timeout
override were uploaded/read back before RUN_START. Two prototype retries allowed;
one used, no M2 retry consumed. One agent performed sequential Nurse, Coordinator,
Generator and separate browser Evaluator passes. No product MARK_COMPLETE.

Attempt 1 `ux-p02-db441f1f-43b3-42f2-96d2-15532505d98a` failed its first browser
render with a resource-form syntax error. Generator repaired it; the failed
initial review and closed run remain recorded. Retry 1
`ux-p02-15577fad-88f8-4db3-a162-0191fd145eb3` passed mechanical evaluation.
Events were written/read back; exact sanitized receipts are in
`20261002_extensions-prototype-events.json`. An incomplete GENERATE hash hint is
not a revision identifier; the final REVIEW corrects it with the exact hash above.

Actual browser interactions captured sixteen cases in
`prototypes/extensions-v2-browser-evidence.json`:

- Global navigation, initial result, service arrival without a turn, foreground
  polling, visible attachment and host chip removal.
- Context replacement rather than accumulation; per-thread attachment isolation;
  explicit active and new-thread messages.
- Host refusal of fullscreen and desktop deep-link routing.
- Authorized desktop mention typeahead; mobile/web mention fallback.
- Direct form resource preview and selection, with its response matching the
  original form request ID after an intervening preview request.
- iOS active-only messages with text instead of resource-link content;
  conversational mobile clarification; Android deep-link fallback.
- Portable tool-only selected-artifact receipt, with no OpenAI UI dependency.
- File conflict preserves draft; reload/reconciliation saves with current ETag;
  web file handler disabled.
- Native settings schema/effective values, changed-property-only updates,
  setup skill and custom MCP App settings modal; no background runtime assumed.

Desktop 1440x1060 and mobile 390x844 screenshots inspected; temporary viewport
reset. No console errors occurred since final reload. Thread example left open
with a removable Alice attachment and zero host turns, ready for owner review.
Local screenshots: `docs/prototypes/extensions-v2-desktop.png` and
`docs/prototypes/extensions-v2-mobile.png`.

## Status boundaries and next step

All host/tool behavior is simulated. No bridge, real agent exchange, resource
write, permission grant, deployment or production endpoint was changed. Tool
names beyond the current M2 entrypoints are proposals, not implemented services.
M1 remains complete; M2 incomplete with one retry; M3–M6 pending. Design validation
by Michael and live Extensions/account acceptance remain open.

Have Michael compare the global home with the existing-thread tab and distinguish
adding context from starting work. Adopt validated interaction decisions later;
keep this HTML and metadata on the throwaway branch as primary design evidence.
