# AICQ progress

## Current status

M1 passed local acceptance on 2026-10-01 (America/New_York). The authenticated
baseline and populated owner dashboard run at http://127.0.0.1:6173/harness.
Real owner and authenticated non-owner browser/API journeys passed. Public
deployment remains deferred.

M2 is incomplete. Local source candidate `9d766b9` on
`kublascratchpad/m2-plugin-shell` passed its repaired local evaluation. The portable
plugin exposes identity, resumable private profile/settings setup, global/thread
entrypoint tools, and a bundled MCP App UI. Real owner setup/read-back/reuse and
identity across fresh server processes passed. Required ChatGPT installation,
host rendering, browser OAuth linking/refresh, and separate fresh test-owner setup
remain blocked. No M2 MARK_COMPLETE was recorded; M3–M6 remain pending.

## Harness state

Reuse owner annotation `MomentAnnotation/51f5fa9c-a6c7-4ee5-a0e3-f602496e3bed`.
The latest run is closed; no run is active.

- M1 run `m1-7abb2258-7b2d-44d0-bb90-7e630b431618`: passing REVIEW, MARK_COMPLETE,
  and RUN_COMPLETE read back. Terminal record `c363bd6f-cab2-5e82-9170-7d380e4ba4a5`.
  Zero retries used.
- M2 attempt 1 `m2-2ad50a7c-89bc-444a-b7ab-4548aa1e15d1`: failed REVIEW on
  `9161037`; local authorization error needed repair and required integration
  checks were blocked. RUN_COMPLETE `884667bd-6042-5ae2-83be-7a983949113a` read back.
- M2 retry 1 (attempt 2 of 3) `m2-fac0fd7f-faf4-44d2-938a-6490e8795e91`:
  repaired candidate `9d766b9`; local checks passed, required integration checks
  remained blocked. Failed REVIEW `d2f7ed1b-1cc5-55cc-8cd6-5a991825dd0a` and
  RUN_COMPLETE `078eb55c-81b1-5cac-9a58-96e70cd7a175` read back at
  2026-10-02 03:48 UTC. One milestone retry remains; no timeout or harness repair
  retry was consumed. Wait for changed prerequisites before another attempt.

Default configuration remains two milestone retries, two harness repair retries,
and a 15-minute run timeout. Initial M1 and M2 60-minute overrides were recorded
before those runs. M2 retry 1 used the default 15 minutes.

## Verified evidence

M1 candidate `fdcec134f149bb6f95b36c084e58b90ec9d5fd34`: fresh Google/Fulcra owner
sign-in/logout/re-sign-in, navigation, live event display, canonical panels, and
real test-account page/API 403 passed. Type check, lint, 6 security tests, and
Node build passed. History and sanitized receipts were uploaded/read back.

M2 candidate `9d766b9`: 10 focused tests passed. The extracted archive ran its
exact portable manifest command with the executing client's normal owner
credentials. Both entrypoint tools and the compiled UI resource worked; owner
profile/settings were reused and identity survived process restart. Live HTTP
wrong-resource authorization now returns `invalid_target` without upstream login;
discovery and missing/invalid bearer denial passed. UI type check/build, official
metadata/schema checks, and M1 regression checks passed during evaluation.

See `history/20261001_m1-local-baseline.md`,
`history/20261001_m2-local-plugin.md`, and their sanitized evidence files.

## Next actions

October2 research checked GitHub source/discussions, Nuclino, Linear, and #eng.
Existing MCP client IaC allows the rejected loopback callback; the earlier attempt
selected the SDK client. Verify correct local client configuration and real linking
before requesting new local callback registration. Portal has operational Cloud Run
previews. The follow-up recommends a reusable Fulcra MCP test service at a stable
hostname, with MCP-specific federation, OAuth and isolated state, rather than
centering the contribution on an AICQ gateway. This remains a proposal for
Josh/Fulcra/GCP. Fulcra-managed Vercel provisioning is still pending. No deployment
or milestone retry was started. See history/20261002_mcp-preview-design.md.
See history/20261002_fulcra-dev-deployments.md and outstanding-issues.md.

Follow-up VM research found Leif's established Agent Playground GCE creation/SSH
recipe and the newer Shell Beach command generator. This supplies an existing
Fulcra-infrastructure candidate for a manual single-process development server;
CI/CD upgrades need not gate AICQ. Fulcra owns the devfulcra.com DNS zone, but
playground access, an available image, stable addressing, ingress and TLS still
need verification/configuration before a callback can be registered. No VM or
hostname was created. See history/20261002_fulcra-vm-hosting.md.

The toolkit's `portal-dev-tool` supplies an even smaller manual Cloud Run route:
normal operator gcloud authentication deploys an existing image directly, without
GitHub federation or new CI/CD. An MCP adaptation can use one stable service name
and Cloud Run's supplied HTTPS URL, with callback/base URL and isolated persistent
OAuth storage still configured and evaluated. The current tool instead creates a
Portal service per image tag. No helper adaptation or deployment was performed;
this remains an option. See history/20261002_portal-dev-tool-mcp.md.

Live Linear/GitHub tracing confirmed that Toolkit helpers are tracked through
Platform tickets PLAT-338 and PLAT-513, neither attached to a Linear project.
Created and read back PLAT-546, "Toolkit: add a manual MCP development deployment
helper", in Platform Backlog, unassigned and without a project, related to both
existing tickets. No deployment or milestone retry was started. See
history/20261002_toolkit-project-tracking.md and
https://linear.app/fulcradynamics/issue/PLAT-546/toolkit-add-a-manual-mcp-development-deployment-helper.

Resolve actual host reachability/authentication prerequisites, then resume M2's
required live host/account tests in a new recorded run. Hosting could replace the
Platform tunnel route; ChatGPT authentication/install/render/link gates remain. Do not
advance to M3 or count local tools as completed ChatGPT integration.

The user authorized Computer Use, Google test-account sign-in, and milestone work
while sleeping for eight hours. The overnight window ended at
2026-10-02 10:55 UTC (06:55 America/New_York). Heartbeat
`aicq-overnight-milestones` was paused at the first wake after that deadline.
Canonical prerequisites remained unchanged throughout the overnight checks; no
additional milestone attempt or implementation was started. See
`history/20261002_overnight-handoff.md`. Automatic approval review previously rejected reading the private OpenAI MFA
email and clearing Fulcra SSO. The user subsequently gave standing permission
to log out of Fulcra. Logout and a new Google test-client device login now
succeeded; read-only Fulcra identity checks confirmed a distinct non-owner
with no AICQ setup yet. OpenAI verification-email access remains unapproved.
See `history/20261002_test-account-authentication.md`. Credentials remain in normal
client management; no external messages or public publication were performed.

## Earlier prerequisites

Private kubla/aicq planning publication: `00a0f04bb7ea10659c6667d62eaa8cd560ae18fb`.
Earlier cloud Git push failed with HTTP 401; API publication succeeded. Current
local push capability has not been retested; local application commits are unpublished.
Separate Fulcra MCP branch `aicq/mcp-events`, prerequisite `429da58`, provides
protocol readiness and the reused OAuth gateway. It does not implement Events.
