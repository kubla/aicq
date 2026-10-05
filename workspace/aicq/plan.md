# Draft implementation plan

Status: M1 passed the authenticated local baseline and populated owner dashboard
gate on 2026-10-01. The user authorized continuing milestone by milestone while
sleeping for eight hours. M2 local candidate 9d766b9 passed its repair checks,
but required live ChatGPT/account gates remain blocked. One retry remains.
See history/20261001_m2-local-plugin.md. Public deployment and product messaging
remain pending; the separate MCP protocol-readiness prerequisite still does not
implement Events. Evaluation evidence: history/20261001_m1-local-baseline.md.

## Current design status

UX-P09 (2026-10-05): removed AICQ calendar/meeting preferences and the inert away
badge. The three autonomy modes remain; scheduling is an agent-reported outcome.
Person-only sender invitations contain no platform hint; recipient chooses own app.
Actual desktop and 390px invitation/result journeys, authority/waiting controls
passed after one repaired stale-view reference. Public Site version 6 published.
Cloud responder setup remains a proposal. M2 still incomplete with one retry.
See history/20261005_agent-boundary.md and prototypes/agent-boundary-notes.md.

UX-P07 completed the spec-first autonomy revision; UX-P08 corrected its native
mention/host and artifact details and republished the public worked example.
Evaluate Michael’s feedback on the one-instruction handoff and the level of detail
in collaboration summaries before further product engineering. The labels and
responsiveness calculation remain prototype interpretations. No live calendar
integration or background execution is verified. See
history/20261003_autonomous-collaboration.md and history/20261003_host-realism.md.
M2 remains incomplete with one retry.

## Recorded earlier design steps

UX-P03 (2026-10-03): apply the user's Fulcra Context Web design reference and
Fulcra logo to both existing HTML studies, together with the saved OpenAI host
appearance reference. Preserve their existing simulated interactions. Use a
neutral native host shell and Fulcra styling inside AICQ content. The fixed brand
direction replaces generic styling alternatives for this pass. Acceptance:
inspect both prototypes in a browser, verify logo/font rendering and host/app
styling boundaries, exercise representative existing flows, inspect desktop and
narrow layouts, and record artifacts/source provenance. User design validation
and live host/account acceptance remain open. Independent UX-P03 uses the
existing annotation and separate state, two retries, and a 45-minute timeout
override recorded before RUN_START. It does not consume M2's remaining retry.

2026-10-03 direction: make future mockups visually realistic using installed Bits
& Bolts/host inspection, or web screenshots if inspection fails. The installed app
was blocked by Computer Use policy. Saved the authorized official-image fallback
and concrete reference rules in `host-ui-reference.md`. Apply the reference in
UX-P03; the reference-gathering task itself did not restyle the prototypes.

UX-P02 (2026-10-02): match prototype interactions to the user-requested OpenAI
MCP Extensions specification, pinned at ca16cb3bc015baaa1b849082d8755bbef18770cb.
Explore global navigation, thread tabs, inline/fullscreen resources, visible model
context, explicit active/new-thread messages, mention search, file-resource
conflicts, settings/onboarding and unsupported-host fallbacks. Build a local
self-contained HTML interaction lab with exact illustrative payloads and simulated
host behavior. Acceptance: browser exercises each chosen hook and its capability
limits; documentation separates spec facts from AICQ proposals and live verification.
This independent design run uses the existing annotation, separate UX-P02 state,
two retries, and a 45-minute timeout override recorded before RUN_START. It does
not consume M2 retries or promote any product milestone. Sidebar navigation is
preferred by the user; the spec defines no sidebar display mode.

User direction recorded 2026-10-02: prioritize interaction design with HTML
prototypes before committing to heavyweight software engineering.

UX-P01 is a separate, throwaway design experiment, outside M1–M6. Build one
self-contained HTML prototype with simulated contacts, requests, clarification,
returned revisions, changed-source reconciliation, pause and later continuation.
Evaluate the actual controls and readable states in a browser. The question is
whether an owner can see what was shared, what is happening, and how to use the
returned work. Mechanical browser acceptance is not user validation of the design
or live ChatGPT/Fulcra integration. No M2 retry is consumed or milestone advanced.
Run UX-P01 through the existing owner annotation with sequential Nurse,
Coordinator, Generator and separate Evaluator roles. Timeout override: 30 minutes
for this prototype and browser evaluation, recorded before RUN_START; two retries
remain the default for this experiment. Keep its run state separate from M2.

The user wants both agent conversation and exchanges beyond chat, designed from
the owner experience backward. Use the [first-experience walkthrough](first-experience.md)
to sketch a review request, clarification, returned artifact, and later-session
continuation. Compare messaging patterns after this design is concrete. This is
planning work; M1 remains the first application implementation milestone.

The [workboard](workboard.md) expands the milestones into workstreams and initial
tasks with evidence requirements. The user created private `kubla/aicq`; API
read/write access is verified, though agent-side repository creation and normal
Git push failed. Issue 1 tracks M1. Hosting is local-first; defer GCP to Josh if
integration requires substantial infrastructure. Client candidates are recorded there.

## Harness

Follow [Fulcra App Starter](https://github.com/fulcradynamics/community-skills/blob/main/skills/fulcra-app-starter/SKILL.md)
and its [harness control flow](https://github.com/fulcradynamics/community-skills/blob/main/skills/fulcra-app-starter/references/harness-control-flow.md).

Every milestone runs through generation and a separate evaluation pass with real
tool evidence, then progress/history updates. One agent may execute the roles
sequentially. Only the Nurse role creates or repairs harness machinery.

Configuration: two milestone retries (three attempts total), two harness repair
retries (three attempts total), and a 15-minute timeout per milestone run.

Override recorded 2026-10-01 (America/New_York): the initial local M1 run has a
60-minute timeout to cover dependency installation, dashboard integration, and
browser authentication/evaluation in one sequential role run. Retry limits remain
unchanged. Subsequent runs return to 15 minutes unless an override is recorded. A blocked required check leaves the milestone incomplete.

Override recorded 2026-10-01: initial M2 run has a 60-minute timeout for local
MCP gateway setup, plugin packaging, and ChatGPT/tunnel integration evaluation.
Retry limits remain two; this does not relax any required acceptance gate.

Complete Fulcra authentication, upload the plan, spec and exact
user decisions to `workspace/aicq/`, and initialize progress/history. Bootstrap
the harness annotation, mint a run ID, and record/read back RUN_START before
cloning or writing application code. Use the actual template README values:
it currently names `PUBLIC_FULCRA_API_ENDPOINT` and uses port 6173; the skill's
example environment variable and test port are not authoritative over the template.

## M1 — Working local baseline and harness dashboard

Customize the official Svelte template's owner shell, verify sign-in, serve a
reproducible local baseline, and integrate the owner-only harness dashboard during
the same run. The user's local-first hosting direction replaces the starter's
deployed-baseline target with the local target for this milestone. Keep all
recording, evaluation, and owner-access requirements. Public hosting is deferred.

Acceptance: real browser sign-in and authenticated UI work; harness events can
be written and read back; the locally served dashboard displays those actual events,
overview and evaluation result; owner navigation works; a different account is
denied owner-only access. Record actual target URLs/revisions and observed results.
Deployment, a build, or invented dashboard records cannot establish completion.

M1 is complete after recorded run m1-7abb2258-7b2d-44d0-bb90-7e630b431618.
Browser sign-in, live data, canonical panels, navigation, and authenticated
non-owner denial passed; see progress.md and the M1 history for evidence.

## M2 — Plugin shell and account linking

Expose the MCP endpoint, sidebar and thread entrypoints; connect the MCP App UI;
prove OpenAI-compatible account linking and stable AICQ owner/agent identity.
Package an onboarding skill that resumes an invitation and initializes missing
owner-scoped application resources using authenticated Fulcra MCP operations.
Test OpenAI's documented Secure MCP Tunnel for developer-mode access to a local
MCP server. It needs Platform tunnel access and a runtime API key, plus the intended
workspace association. OAuth discovery can traverse the tunnel, but its browser
authorization endpoints and callbacks still need reachable URLs. Do not claim
the tunnel by itself solves auth or public distribution. If resolving these
requires substantial infrastructure work, record the blocker and pause that work
until the user can get Josh's help with GCP; do not silently choose another host.

Acceptance: install a development plugin in ChatGPT, open both entrypoints, link
the intended Fulcra account, survive refresh/reconnect without changing identity,
and reject unauthorized or wrong-audience credentials. Retest the M1 experience.
Verify fresh-account bootstrap, existing-account reuse, and interrupted/repeated
setup recovery. Pairwise sharing and the first useful reply are evaluated in the
subsequent two-owner milestones.

## M3 — Contact and mailbox feasibility

Use two test owners to establish a contact connection and reciprocal, isolated
Fulcra message streams. Measure write-to-query delay and discovery behavior.

Acceptance: both owners inspect the same exchange; a third owner cannot read
it; unrelated conversations stay isolated; revocation blocks future retrieval;
schema/sharing limits are documented. Validate actual supported API contracts.
If the mailbox approach fails these gates, record the evidence and propose a
Fulcra resource-layout revision before implementing messaging features.

## M4 — Durable agent messaging

Implement contact resolution, explicit-content handoffs, offline inbox retrieval,
reply threading, versioned artifacts, returned proposals, receipts and owner controls.

Acceptance: “share this with Alice's agent” resolves an authorized Alice, delivers
the chosen content, appears to both owners and can receive a threaded reply.
Disconnect the recipient, send, restart services, and verify later retrieval.
Complete the proposed review walkthrough: return an inspectable artifact revision
linked to the original request, let the sending agent use it under owner direction,
and retrieve the result and unresolved questions in a later session.
Exercise repeated sends, uncertain persistence, duplicate discovery, attachment
permissions, ambiguous names and blocked contacts. Do not report an agent
acknowledgment until the recipient explicitly consumes the message.

## M5 — Subscribed message-triggered work

Implement MCP Events discovery and subscription lifecycle plus a persistent
delivery worker in the existing Fulcra MCP server fork. Keep generic Fulcra change
events reusable upstream; choose their scope after validating the messaging model.
AICQ owns message interpretation and response policies. Commit `429da58` establishes
MCP 2 protocol readiness with regression coverage; Events are still unimplemented.
Owners opt into monitored conversations and response policies.

Acceptance: real ChatGPT Work subscription verifies its callback; a matching
message triggers the configured workflow; an unrelated or unauthorized message
does not. Verify restart recovery, expiration/refresh, revocation, duplicate and
out-of-order deliveries, and bounded agent reply loops. Confirm offline messages
remain retrievable when no supported subscription exists.

## M6 — Usability and distribution

Refine the ICQ-inspired roster and transcript, onboarding, deep links and native
settings. Add desktop composer mentions with a capability-aware fallback.
Package the portable plugin, document remote MCP and CLI-backed setup paths,
and run two-owner acceptance walkthroughs across supported harnesses.

Acceptance: both owners can connect, send, observe, pause and resume through the
intended ChatGPT experience; the full tool workflow remains usable without optional
extensions; setup and hosting requirements are documented. Public listing or
publication must use the chosen account and comply with the actual platform flow.
Verify a ChatGPT agent sends a handoff to a Codex agent, Codex returns a usable
artifact, and both owners can inspect the exchange. Exercise the core workflow
in a representative additional MCP-capable harness and verify continuation after
switching harnesses without creating another owner identity or losing context.
Document the exact tested clients and each client's background-execution support.

## Later transport work

Further runtime-specific activation adapters, multiple named agents per owner,
and group exchanges remain separate milestones. Core Codex and
compatible-harness participation is part of the product requirements above.
The first release must not claim verified interoperability with runtimes that
have not been exercised.

## UX-P04 — Prototype sharing Site

Register a new ChatGPT Site, package the existing UX-P03 HTML studies with
minimal navigation, metadata and the sourced Fulcra favicon, and publish the
static-only sharing edition. Include no credentials, private canonical records,
backend bindings or real messaging. Follow native Sites workflow; evaluate
packaged routes, JavaScript syntax, source/archive identity and deployment status.
No new visual QA is required for unchanged evaluated mockups. Use independent
UX-P04 state, existing owner annotation, default 15-minute timeout and two retries.
Keep M2 incomplete and its retry unchanged. Prepare source before the publishing
run; record actual registration/push/save/deployment evidence and readbacks.

## UX-P05 — Alice's installed ChatGPT experience

Build one coherent self-contained HTML example at /alice.html on the existing
Site, preserving prior studies. Use the recorded Fulcra identity and OpenAI host
references. Include global home, grouped contacts, thread pane, context attachment
versus explicit host turn, mentions, plain agent messaging, selected-artifact
review, waiting/retrieval/clarification, returned revision and changed-source
reconciliation, pause/resume and later-session continuity. Include generated
mock invitation link/copy, recipient preview, sign-in/setup simulation, explicit
acceptance, interrupted/repeated setup and owner-visible contact readiness.
Include artifact inspection and owner settings/block/revoke where meaningful.
Simulation controls and full state inspection stay outside the host shell; no
real private transcript access, identity linking, sending or runtime activation.

User specifies a single worked experience; do not generate unrelated visual
alternatives. Use in-memory state and a pure reducer. Default two retries; record
45-minute timeout override before RUN_START for implementation, separate browser
review, Sites publication and canonical delivery. Independent UX-P05 does not
consume M2's remaining retry. Acceptance: actual browser walkthroughs across
happy path, invitation/resume, conflict, isolation of selected context, contact
navigation and narrow layout; exact source/deployment evidence and readbacks.

## UX-P06 — Product copy realism pass (2026-10-03)

User requested all realism mistakes corrected in Alice’s worked example, including
third-person narration on her invitation page. Audit app/host dialogs, chat replies,
settings, files, notifications, recipient setup and action labels. Address the current
user directly, use concrete status/action language, and move prototype-only steps
and explanations outside the depicted product. Preserve interactive flows and
existing Site routes/audience; publish the correction to /alice.html. Evaluate
actual invitation, recipient, exchange and conflict surfaces plus responsive layout.
Nurse/Coordinator/Generator/Evaluator operate sequentially. UX-P06 uses two retries
and a 30-minute run timeout override, recorded and read back before RUN_START.
No M2 retry or product milestone promotion.

## UX-P07 — Autonomous collaboration and one-instruction handoff (2026-10-03)

Update the canonical spec before prototype implementation, following the user's
confirmed direction: work/outcomes lead, autonomy governs collaboration, and
routine authorized calendar coordination completes without another approval.
Then revise Alice’s /alice.html example on the existing public Site. Preserve
invitation, artifact/version, pause/block, context and host-layout behavior. Add
a finished financial-model chat, desktop @ selection, one instruction sharing
the selected model and arranging an in-person Friday review, ongoing work,
confirmed outcome, and inspectable decision/waiting states. Contact rows show
current work and observed typical responsiveness. No real calendar or delivery.

Acceptance: separately evaluate the spec for contradictions, then exercise the
prototype in a browser: autonomous completion, judgment call, approval-only,
unavailable agent, contact navigation, artifact scope, pause/resume, invitation,
existing review/conflict and desktop/narrow layouts. Save screenshots and actual
observations; publish only the reviewed source. Simulation controls stay outside
the host. UX-P07 uses existing owner annotation, independent state, two retries
and a **60-minute timeout override**, recorded/read back before RUN_START.
This does not consume M2’s retry or promote M1–M6. Preserve public Site access.

## UX-P08 — Host and mention realism pass (2026-10-03)

Michael requested @AICQ highlighting like ChatGPT keywords/skills, followed by
a search for other visual or interaction mistakes. Use the saved official host
references, especially composer mentions, thread chrome and context attachment.
Preserve the autonomous collaboration, invitation and document flows. Correct
mention rendering in the composer and sent text, keyboard behavior, host icon
semantics, relevant copy/status details and responsive layout. Publish the
reviewed example to the existing public Site without changing audience.

Nurse, Coordinator, Generator and Evaluator work sequentially under the existing
owner annotation. Two retries remain the default; record a **45-minute per-run
timeout override** before RUN_START for the visual audit, browser verification,
publication and evidence delivery. UX-P08 is independent of M1–M6; no M2 retry
is consumed. Acceptance requires actual desktop/narrow observations of typed
mentions, selected mentions, editing, sending, context, calendar outcomes and
representative invitation/artifact continuity; record exact source and publication.


## UX-P09 — Agent boundary and friend invitations (2026-10-05)

Apply Michael’s calendar, unattended-work and invitation feedback to the canonical
spec first, then the Alice worked example. AICQ transports selected messages,
artifacts and collaboration updates. Tools, calendars and private preferences
belong to participating agents/products. Remove calendar/meeting-preference settings
and the inert Work while I’m away badge. Preserve the three autonomy modes.
Sender invitations collect a person and introduction, never the friend’s platform;
recipient app selection belongs to the recipient. Preserve resumed/revoked setup.

Cloud responder setup is a proposal, not a confirmed Codex capability or provisioned
service. Do not pretend to launch a worker. The current pass removes the redundant
badge; an eventual responder setup must identify the executor, credentials, scope,
cost and lifecycle separately from permission to act.

Run sequential Nurse, Coordinator, Generator and separate Evaluator roles using
the existing owner annotation and independent UX-P09 state. Record/read back this
**45-minute timeout override** before RUN_START; retain two retries. Acceptance:
settings have autonomy and no calendar/away controls; platform-neutral sender and
invitation URL; recipient chooses its own app; scheduling is an agent-reported
outcome with no AICQ calendar API/state; retained approval/judgment, pause/block,
invitation acceptance/revocation and desktop/narrow browser journeys work. Publish
the reviewed HTML to the existing public Site. M2 remains incomplete with one retry.


## DOC-P01 — Engineer-readable product specification (2026-10-05)

Michael requested a concise, illustrated spec suitable for fellow Fulcra software
engineers after the successful demo. Rewrite the existing spec around the current
Alice experience, preserving approved decisions and separating proposed mechanics
from verified implementation. Link historical requirements and architecture rather
than repeating them in the main reading path. Make the root README point to the
current spec and prototype. No prototype code, hosting, or product milestone work.

Nurse/Coordinator/Generator/separate Evaluator roles run sequentially with the
existing owner annotation and independent DOC-P01 state. Record/read back this
**45-minute timeout override** before RUN_START; retain two retries. Acceptance:
compare the rewrite against the complete prior spec and current decisions; preserve
identity, isolation, autonomy, invitation, durability, artifacts, portability and
activation contracts; verify diagrams, image/link paths, readability and accurate
status. Save review evidence and byte-verify canonical writes. M2 remains incomplete
with one retry; M3–M6 remain pending. The previous spec stays in linked history.


DOC-P01 completed after one documentation-only legibility retry. Requirement
coverage, three images, two rendered diagrams, 34 relative links/anchors and
whitespace checks passed. Canonical content was byte-verified; private GitHub
spec/README and branch head matched candidate `d1a5075`. See
history/20261005_spec-readability.md. No product milestone or M2 retry changed.


## DOC-P02 — Fulcra-only backend (2026-10-05)

Michael requires AICQ to be built strictly on Fulcra. Remove backend alternatives
and fallback transport proposals from the current spec and design documents;
retain original decisions/history with explicit supersession notices. Choices
between Fulcra resource layouts remain open. Evaluate consistency, relative links
and unchanged product status; sync/read back canonical records and publish the
existing private branch. Sequential roles use the existing annotation, separate
DOC-P02 state, default 15-minute timeout and two retries. No M2 retry is used.


## DOC-P03 — Product spec and writing pass (2026-10-05)

Michael requests the specifics and spirit of his writing rules: remove development
status, implementation/verification commentary and status links from the spec;
frame AICQ as making Fulcra’s agent-to-agent communication accessible to everyday
ChatGPT users through OpenAI MCP Extensions. Use the unpinned Extensions repository.
Preserve behavioral contracts and illustrations. Provisional choices stay in design
records instead of being silently promoted to requirements. Keep product work states.
Sequential roles, existing annotation, independent DOC-P03 state, default 15-minute
timeout and two retries. Evaluate prose, requirements, links and status separation;
byte-verify canonical writes and publish the existing private branch. M2 unchanged.


DOC-P03 completed with no retries. Full prior-spec comparison and writing review
passed. Product invariants and unchanged images/diagrams retained; status/pinned
references removed from the spec. Current spec is 2,233 words. Canonical bytes and
terminal events were read back. See history/20261005_spec-contract.md.
