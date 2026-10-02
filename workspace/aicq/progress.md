# AICQ progress

## Current status

Fulcra sign-in completed. Project planning and the MCP server source review are
prepared. The existing GitHub fork is `kubla/fulcra-context-mcp`; its separate
development branch is `aicq/mcp-events`.

The product direction now includes useful work exchange alongside conversations,
post-signup MCP/CLI resource setup, and ChatGPT-preferred delivery with Codex and
other harness support. The workboard defines workstreams, dependencies, evidence,
and client experiment candidates. No application implementation has started.

## Active milestone

M1 — Working local baseline and harness dashboard — pending. No application milestone
has passed review, and no Events implementation or ChatGPT subscription has passed.

## Harness state

Annotation ID: `MomentAnnotation/51f5fa9c-a6c7-4ee5-a0e3-f602496e3bed`.
This type was created in the owner's authenticated account and must be reused.
No milestone run has started. Source-review evidence is a preflight record, not
an app milestone completion.

Configuration: two milestone retries, two repair retries, 15-minute timeout per
milestone run. Retry count: zero. Generation and evaluation are separate roles.

## Verified preflight results

- Source commit `9efe894e15ebb612298e41341a232e713c459505`.
- Frozen upstream dependency environment: FastMCP 3.4.7 / MCP 1.28.0.
- Unmodified baseline: `uv run --frozen pytest -q`: 127 passed in 5.66s.
- PyPI exposes FastMCP 4.0.10 and MCP 2.2.0, providing a supported upgrade path
  to investigate rather than writing a protocol-version shim.
- Isolated upgrade probe, without changing the checkout: test collection fails
  because the existing `ServerSession._received_request` monkeypatch targets a
  private API removed by MCP 2. This was subsequently resolved in the migration.
- The upstream OAuth gateway and documented reciprocal shared-folder mailboxes
  can be reused. Browser linking and two-owner isolation remain unverified.

## Next actions

Define the owner experience using the proposed first-experience walkthrough,
including a review request, a returned artifact revision and later-session
continuation. The user created private `kubla/aicq`; private visibility and API
read/write access are verified. Agent-side creation still failed with HTTP 403;
normal Git push failed with HTTP 401. Use the verified GitHub API publication
path. Issue 1 tracks M1: https://github.com/kubla/aicq/issues/1.
The user chose local-first hosting, with substantial infrastructure blockers
deferred to Josh/GCP. Local git is initialized at planning commit `c84c83f`.
Arrange separate test principals before multi-owner acceptance. Then start M1 through
the harness and evaluate the app baseline.
Root AGENTS.md and a handoff document prepare continuation in a local harness;
no laptop connection or local agent has been configured.
The separate upstream prerequisite now exists as commit `429da58` on
`aicq/mcp-events`: FastMCP 4.0.10 / MCP 2.2.0, obsolete private patch removed,
modern routing headers enabled. Its complete regression suite passed with
132 tests in 6.36s, including modern authenticated HTTP discovery, listing and
tool execution. No Events capability is advertised yet.

Add generic Fulcra change Events and the durable relay after choosing and
validating the messaging model and subscription/worker persistence seam. Validate the real ChatGPT
subscription lifecycle before proposing upstream inclusion.

## Recent completions

No application milestones completed.

Setup: published 36 planning/instruction files to private kubla/aicq via the
Git Data API at commit 00a0f04bb7ea10659c6667d62eaa8cd560ae18fb, verified the
remote tree exactly matches local source, and created issue 1 for M1. Local
main tracks origin/main; planning history is preserved locally. Normal Git
push remains blocked by HTTP 401.
