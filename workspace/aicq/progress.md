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
The current run is DOC-P01 retry 1 `doc-p01-90502b16-82af-4065-a66d-997d5ad62a39`. Documentation REVIEW passed;
canonical delivery and repository publication are in progress. No product milestone
is promoted. One documentation retry repaired diagram legibility. Latest prototype
remains UX-P09 public Site version 6. M2 has one retry unchanged. See
history/20261005_spec-readability.md and history/20261005_agent-boundary.md.

- UX-P03 retry `ux-p03-f8c30fc1-0cbf-4de2-bc18-c876c3165901`: passing
  REVIEW, MARK_COMPLETE and RUN_COMPLETE read back; terminal record
  `039f07af-c39f-5639-bfe1-45220f74ae96`. One UX retry after a browser
  inspection timeout; M2 retry count unchanged. See history/20261003_fulcra-prototype.md.

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

## Interaction prototype

UX-P08 (2026-10-03): published the host realism pass at the existing public Alice
route. @AICQ uses native blue inline highlighting in drafts/sent messages; picker,
keyboard, context/history controls, bubbles, status copy and spreadsheet preview
were corrected. Actual desktop and 390px journeys passed, alongside invitations,
coordination and retained review/version conflict. Two UX-only retries closed;
M2 remains incomplete with one retry. See
`history/20261003_host-realism.md` and `prototypes/host-realism-notes.md`.


UX-P07 (2026-10-03): canonical spec and decisions were saved and read back before
prototype edits. Alice’s example now leads with agents’ current work and completed
outcomes. It includes autonomy controls, typical responsiveness, a completed model
shared through one instruction, routine meeting coordination, judgment/approval/
waiting states, and fresh-chat continuation. Browser evaluation and public Sites
version 4 publication passed. Two UX-only retries were used and closed; M2's
remaining retry is unchanged. No live host, calendar or agent execution is claimed.
See `history/20261003_autonomous-collaboration.md` and `prototypes/autonomy-notes.md`.


UX-P03 (2026-10-03): both HTML studies now use the sourced Fulcra logo, Rubik,
mint actions, violet selection and charcoal app surfaces inside a native-style
OpenAI host. Browser review exercised existing simulated flows and desktop/narrow
layouts. See `history/20261003_fulcra-prototype.md` and `fulcra-design-reference.md`.
Owner design review and live integration remain open. One UX-only retry followed
a browser-inspection timeout; M2's remaining retry is unchanged.

2026-10-03: saved a desktop host visual reference with nine pinned OpenAI Bits &
Bolts screenshots, gallery, provenance/hashes, sampled colors and layout rules.
Computer Use refused access to the installed ChatGPT/Codex app, so no live plugin
capture was obtained. AGENTS.md directs future mockups to consult this reference.
UX-P03 subsequently applied a host fidelity and Fulcra styling pass. See `host-ui-reference.md`
and `history/20261003_host-ui-reference.md`. No product run or M2 retry occurred.

UX-P02 now provides seven Extensions-specific examples in
`mcp/ui/prototypes/extensions-v2.html`, on local throwaway branch
`kublascratchpad/ux-extensions-v2`. Pinned official spec: ca16cb3. Global/sidebar
navigation, thread tabs, inline/fullscreen, context/message actions, mentions,
forms, file conflicts and settings/onboarding are modeled with exact illustrative
payloads and capability fallbacks. Sixteen browser cases and responsive layouts
were exercised; live host integration and owner design validation remain open.
Initial render failed; a recorded UX-only retry repaired and passed the prototype.
One prototype retry was used; M2's remaining retry is unchanged. See
`history/20261002_extensions-prototype.md` and `extensions-interaction-map.md`.

UX-P01 delivered a local, self-contained HTML prototype on throwaway branch
`kublascratchpad/ux-prototype-v1`. Browser evaluation verified sharing, retrieval,
clarification, revision use, changed-source reconciliation, pause/resume, simulated
new sessions, ordinary chat, mock invitation and desktop/mobile rendering.
Design validation by Michael and live host integration remain open. No milestone
was promoted or M2 retry consumed. See `history/20261002_interaction-prototype.md`.

## Next actions

Prioritize iteration on the prototype before further heavyweight engineering,
as directed by the user. Try the model-sharing/scheduling, judgment, approval-only and waiting
scenarios, alongside the existing review and invitation flows. Use feedback to
choose the interaction; keep production
requirements distinct from mechanically verified simulated controls.


The user explicitly retained the embedded UI. Keep AICQ's UI/tool adapter while
using polling rather than requiring new Fulcra MCP Events support for the
prototype. Current code can serve bundled HTML, four account/setup/entrypoint
tools and OAuth routes in one Python service; contacts/messages remain to build.
Recommendation: a dedicated single-process host with stable HTTPS and private
persistent credential state, plus the exact upstream callback registration.
VM access, hostname and live account-linking remain unverified. See
history/20261002_embedded-ui-hosting.md. No new M2 attempt or hosting action began.

The user accepts polling for now and asked for a design without MCP server
changes. Reviewed the canonical architecture, local adapter and Fulcra Mesh
workflow. Client-side polling can replace the Events contribution; retaining the
custom ChatGPT UI still requires AICQ's own adapter and its hosting/authentication.
An existing-connector-plus-skill route can avoid that new gateway if the embedded
UI is deferred. That deferral and revised milestone gates remain proposals. See
history/20261002_polling-design.md. No retry, server change, schedule or sharing
grant was created.

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

The user then chose "Make Fulcra changes easy to run, test and review" as the
Platform project for this set of development helpers. Created and read back
P-PLAT-26; verified membership of PLAT-338, PLAT-259, PLAT-396, PLAT-513 and
PLAT-546. Earlier issue statuses and ownership were preserved; the MCP helper
remains Backlog/unassigned. See history/20261002_toolkit-project-created.md and
https://linear.app/fulcradynamics/project/make-fulcra-changes-easy-to-run-test-and-review-59c14f60422b.

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

UX-P04 sharing edition published privately at
https://aicq-interaction-studies.mtiffany.chatgpt.site with both interactive studies.
Use native Site sharing controls to grant viewers access. Deployment succeeded;
no actual agent messaging or live integration is hosted. Zero retries; M2 unchanged.
See `history/20261003_prototype-site.md`.

UX-P05 (2026-10-03): Alice’s worked ChatGPT example published at
https://aicq-interaction-studies.mtiffany.chatgpt.site/alice.html on the existing Site.
My Agents/Friends Agents, six populated exchanges, invitation recipient walkthrough,
review/clarification/revision conflict, file editing, owner controls and later-session
continuation are interactive simulations. Desktop and narrow browser review passed.
One UX-only retry repaired receipt routing; passing REVIEW, MARK_COMPLETE and
RUN_COMPLETE read back. M2 remains incomplete with one retry; no live integration
claimed. Existing studies and owner-private audience preserved. See
`history/20261003_alice-worked-example.md` and `prototypes/alice-v3-notes.md`.

UX-P06 (2026-10-03): corrected product copy/viewpoints across Alice’s worked
example and republished /alice.html. Demo narration is outside the product;
recipient app choice and account controls belong to the recipient. Account and
contact settings are separate. One prototype retry repaired a clipped narrow
recipient card; browser review and native deployment passed. Passing REVIEW,
MARK_COMPLETE and RUN_COMPLETE read back; terminal 60b192ca-2455-5702-97d0-0f80d96886db.
No active run; M2 remains incomplete with one retry. See
`history/20261003_alice-realism.md` and `prototypes/alice-realism-notes.md`.
