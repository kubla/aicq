# AICQ local continuation

Workspace: /Users/mjjt/Documents/Code/aicq. Canonical owner Fulcra files:
workspace/aicq/. Read AGENTS.md and authenticated canonical requirements/state/history.

M1 is complete; evidence: history/20261001_m1-local-baseline.md.
M2 remains incomplete; source branch `kublascratchpad/m2-plugin-shell`, verified
local candidate `9d766b9`. Evidence: history/20261001_m2-local-plugin.md and
20261001_m2-local-evidence.json. Local dashboard: http://127.0.0.1:6173/harness;
HTTP MCP gateway: http://127.0.0.1:4499/mcp. Both are loopback-only.

M2 attempt 1 and retry 1 are closed. Latest run
`m2-fac0fd7f-faf4-44d2-938a-6490e8795e91` has failed REVIEW plus RUN_COMPLETE
`078eb55c-81b1-5cac-9a58-96e70cd7a175`, read back. Ten focused tests and extracted
plugin/real owner/process restart checks passed. No M2 MARK_COMPLETE exists.
One milestone retry remains; no timeout/harness repair retry consumed. Start the
next run only when integration prerequisites change; default timeout is 15 minutes.

Read history/20261002_fulcra-dev-deployments.md and outstanding-issues.md. Source
research found the existing MCP client already allows the loopback callback; the
failed attempt selected the SDK client. Correct configuration and live exchange
remain unverified. Follow-up research recommends a reusable Fulcra MCP test
service at a stable hostname first; read history/20261002_mcp-preview-design.md
for the Portal controller, public-repo federation, ingress, OAuth and state
differences. Josh/Fulcra/GCP bootstrap is still needed. Fulcra-managed Vercel
provisioning remains pending. No provider/deployment was chosen.
Platform is awaiting email MFA; no tunnel,
runtime key, workspace association, or ChatGPT plugin is verified. OpenAI MFA email access remains unapproved. The user granted standing Fulcra
logout permission; logout/new Google device login succeeded. The isolated test
client now verifies as non-owner 81359eb8-9c06-47e3-92d2-ac80b053c40c with
AICQ setup incomplete. No bootstrap resources were written. Read
history/20261002_test-account-authentication.md before fresh-account evaluation.

Build/install instructions: docs/mcp-development.md. Portable archive:
.local/aicq-development-plugin.zip. Its configured stdio command uses uv with
--frozen --no-editable in mcp/. Preserve normal executing-client credential storage;
never transfer cookies/tokens between browser, CLI, executor, or another agent.

Reuse `MomentAnnotation/51f5fa9c-a6c7-4ee5-a0e3-f602496e3bed` in the real owner's
account. Separate read-only fork checkout:
/Users/mjjt/Documents/Code/aicq-fulcra-mcp-reference, branch aicq/mcp-events at
429da58508a179cc425d10728434739ca6620e1a. AICQ pins its existing OAuth gateway;
no reusable Events changes were made. No live ChatGPT AICQ integration is claimed.

The overnight window ended at 2026-10-02 10:55 UTC (06:55 America/New_York).
Heartbeat `aicq-overnight-milestones` is paused. No prerequisites changed during
the overnight checks; no additional attempt was consumed. See
history/20261002_overnight-handoff.md. Resume the earliest incomplete milestone
when prerequisites change and further continuation is authorized. Keep development
local-first; substantial infrastructure goes to Josh/GCP. Do not send external
messages or publish publicly. Authentication on another executor is separate.
