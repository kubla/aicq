# AICQ workboard

Status: M1 passed local acceptance on 2026-10-01. M2 is incomplete after local verification; later product
and integration milestones remain pending. The recorded architecture proposals
remain proposals.

## Design experiment

UX-P09 (2026-10-05): removed AICQ calendar/meeting preferences and the inert away
badge. The three autonomy modes remain; scheduling is an agent-reported outcome.
Person-only sender invitations contain no platform hint; recipient chooses own app.
Actual desktop and 390px invitation/result journeys, authority/waiting controls
passed after one repaired stale-view reference. Public Site version 6 published.
Cloud responder setup remains a proposal. M2 still incomplete with one retry.
See history/20261005_agent-boundary.md and prototypes/agent-boundary-notes.md.

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

Host appearance reference (2026-10-03): nine OpenAI source screenshots and durable
layout guidance saved. Installed-client Computer Use was blocked; fallback images
are labeled. Future mockups consult `host-ui-reference.md`. UX-P03 subsequently applied those cues to both HTML studies; no product
implementation attempt was started.

UX-P02: seven hook-specific HTML examples and source-grounded contract mapping
built; mechanical browser evaluation passed after one prototype retry. Owner
review and live Extensions support remain open. Source:
`prototypes/extensions-v2.html`; recommendation: `extensions-interaction-map.md`;
evidence: `history/20261002_extensions-prototype.md`. No M2 retry consumed.

UX-P01: self-contained HTML review exchange built and mechanically verified in
browser. Awaiting Michael's interaction review. This is separate from M1–M6;
M2 remains incomplete with one retry. Source: `prototypes/interaction-v1.html`;
local source: `mcp/ui/prototypes/interaction-v1.html`. Evidence and iteration
questions: `history/20261002_interaction-prototype.md`.

## Starting information

The product direction is sufficient to start: agent collaboration with useful
work exchanges, owner visibility, durable continuity, easy invitations, and
ChatGPT-preferred delivery with Codex and other harness support.

The user created private `kubla/aicq` after agent-side creation was rejected.
Verified the repository is private and accessible. Reading repository metadata,
creating/deleting a temporary branch in the Fulcra MCP fork, writing initial
content to AICQ, and creating an AICQ issue all succeeded. Ordinary Git push
returned HTTP 401; use GitHub's content/Git Data API for publication while that
transport remains blocked. Local git was initialized at planning commit `c84c83f`.

The user chose local-first development if feasible, with GCP deferred to Josh
when a substantial infrastructure problem arises. Local implementation can proceed
once the first harness run is recorded. Reuse existing Fulcra authentication and
the harness annotation instead of creating another.

Before two-owner acceptance, arrange a second Fulcra owner with separately
authorized credentials. Sharing isolation also needs a third authenticated test
principal. Do not borrow credentials from the invitation or from another owner.
Test clients installed on the user's computer require a local test handoff or
explicitly configured access; this workspace does not imply access to that computer.

Use the official Svelte template by default and make the stack reproducible on
the user's computer. Development initially runs in this execution workspace;
that does not mean processes have been installed on the user's computer. Concrete
Fulcra message and operational metadata layouts remain open. Domain, license,
billing, and public publisher details can be resolved before their respective gates.

OpenAI Secure MCP Tunnel is a documented private-development path, requiring
Platform tunnel permissions, runtime credentials, and target workspace association.
The browser-facing OAuth service is not automatically tunneled. Check this seam
before committing to a local ChatGPT integration. Public directory distribution
still needs a stable publicly reachable HTTPS endpoint. When local services are
stopped, Fulcra retains shared work, but local relay execution cannot continue.

## Workstreams

October2 deployment spike completed across GitHub source/discussions, Nuclino,
Linear, and #eng. Operational Portal previews and existing MCP Cloud Run/state
configuration provide reuse patterns. Existing MCP client IaC allows the loopback
callback rejected by the SDK client; real linking remains unverified. Fulcra-managed
Vercel project provisioning is pending. Follow-up source analysis recommends a
reusable MCP test service with a stable hostname first. Public-repo federation,
reachable ingress, OAuth callback/state isolation and cross-process refresh
coordination need specific work; the current Portal workflow cannot be copied
unchanged. No deployment, milestone attempt, or status promotion occurred. See
history/20261002_fulcra-dev-deployments.md, history/20261002_mcp-preview-design.md
and outstanding-issues.md.

| Workstream | Deliverable | Main milestones |
| --- | --- | --- |
| Foundation and development harness | Authenticated baseline, deployments, real progress dashboard | M1 |
| Identity, invitation, and onboarding | Stable identities, contact acceptance, resumable resource setup | M2–M3 |
| Portable messaging and work exchange | Durable requests, replies, artifacts, provenance, continuation | M3–M4 |
| ChatGPT experience | Packaged skills, buddy list, collaboration/results views | M2, M4, M6 |
| Events and activation | Reusable Fulcra Events lifecycle and durable delivery worker | Separate fork prerequisite, M5 |
| Other harnesses and distribution | Codex and representative-client tests, adapters/instructions, release package | M4, M6 |

Design the core exchange for all clients from the beginning. Verify cross-client
work as soon as the core exists, then perform the full release walkthrough in M6.
Keep background activation separate from basic messaging compatibility.

## Initial task board

| ID | Task | Depends on | Status | Evidence required |
| --- | --- | --- | --- | --- |
| P-01 | Provision private kubla/aicq; prepare local-first stack | User-created repository | Complete setup prerequisite | Private visibility verified; initial content write and issue creation succeeded; local git prepared |
| M1-01 | Start recorded harness run; initialize app from template | Harness health/read-back | Complete; local M1 run verified | Recorded run m1-7abb2258-7b2d-44d0-bb90-7e630b431618; see history/20261001_m1-local-baseline.md |
| M1-02 | Integrate owner dashboard and serve local authenticated baseline | M1-01 | Complete | Verified real owner/test-account browser sign-in, live event/panels, owner-only API and page denial; candidate fdcec13 |
| M2-01 | Package portable plugin, skills, and remote MCP connection | M1 | Local package verified; ChatGPT/tunnel blocked | Installed development plugin with callable authenticated tools |
| M2-02 | Stable identity and resumable owner workspace setup | M2-01 | Real owner reuse/restart verified; separate fresh/interrupted account blocked | Fresh/existing account paths; retry/reconnect reuses actual resources |
| M2-03 | ChatGPT sidebar and thread shell | M2-01 | Tools/UI resource verified locally; host rendering blocked | Actual supported host renders both entrypoints |
| M3-01 | Compare annotation outboxes and shared-folder mailboxes | M2, test principals | Pending | Two-owner retrieval, third-principal denial, revocation, observed ingestion/discovery behavior |
| M3-02 | Invitation acceptance and reciprocal connection | M3-01 | Pending | Intended recipient, interrupted setup recovery, verified narrow shares |
| M4-01 | Durable handoff and ordinary threaded replies | M3 | Pending | Offline/restart retrieval, retry deduplication, both-owner visibility |
| M4-02 | Returned artifact revision and continued work | M4-01 | Pending | Recipient-accessible version, linked result, safe incorporation, later-session continuation |
| M4-03 | Exercise ChatGPT-to-Codex core exchange | M4-02 | Pending | Codex receives, responds, and returns an artifact the ChatGPT agent can use |
| E-01 | Modern MCP protocol prerequisite | Upstream baseline | Complete prerequisite | Published commit 429da58; 132 regression tests passed; no Events capability claimed |
| M5-01 | Generic Fulcra Events lifecycle and durable relay | E-01, M4, durable hosting/storage | Pending | Signed challenge/delivery, auth/filter boundaries, persistence, retry/replay and revocation |
| M5-02 | Real subscribed ChatGPT workflow | M5-01 | Pending | Supported host follows owner policy on arrival; no duplicate work or reply loop |
| M6-01 | Final UI, client walkthroughs, and release package | M4–M5 | Pending | Complete two-owner story, third-harness core test, supported-client matrix, actual review/publication status |

Use smaller child tasks when a row spans multiple changes. No task moves to
verified without inspectable evidence. An incomplete child task keeps the parent
milestone incomplete. No fabricated completion percentages or delivery dates.

## Tracking and sources of truth

Fulcra `workspace/aicq/` is the canonical project record. Repository documentation
mirrors it. Keep:

- `decisions.md`: the user's exact decisions and requirements, appended over time.
- `spec.md` and `plan.md`: intended behavior, milestone criteria, dependencies.
- `workboard.md`: task status, blockers, and evidence references.
- `progress.md` and `overview.md`: active run, current milestone, next action.
- `history/`: per-run results, tested revisions/URLs, commands and observed outcomes.
- Harness annotation: structured lifecycle events that feed the owner dashboard.

Use one AICQ repository for the product, plugin, shared contracts, integration
tests, and docs. Keep the reusable Events contribution in the existing Fulcra MCP
fork. Git commits and eventual focused PRs reference task IDs; GitHub issues can
mirror the board once the product repository exists, without inventing a second
independent status ledger. The private repository exists and issue 1 tracks M1.
Repository creation permission and Git push transport are distinct from the
verified API write capabilities; keep those observations separate.

## Build and evaluation cycle

Choose the earliest incomplete milestone, verify prerequisites, record the run,
implement a bounded change, then evaluate it separately against the spec and
previously working behavior. Record actual outcomes and update the board and
canonical workspace. A deployed page or passing build alone cannot complete an
end-to-end user journey.

Follow the Fulcra starter's role boundaries: Nurse for harness machinery,
Coordinator for run state, Generator for product code, Evaluator for verification.
Roles may run sequentially in one agent. The current defaults remain two retries
and a 15-minute milestone-run timeout; record any necessary override before a run.
Prepare credentials and test access before beginning a timed acceptance run.

## Client experiment candidates

The user reported:

> Nice! On my computer I also have Claude, Claude Code, Hermes, Grok Bot, and Meta Muse to experiment with.

Track ChatGPT and Codex plus those experiment candidates in a capability matrix:
installation, authentication, setup, send/receive, artifact access, continuation,
owner visibility, and optional background activation. Record client versions and
actual observed results. Client presence on the user's computer is a testing
opportunity, not verification or a release commitment for every named client.

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
