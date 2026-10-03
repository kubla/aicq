# Draft implementation plan

Status: M1 passed the authenticated local baseline and populated owner dashboard
gate on 2026-10-01. The user authorized continuing milestone by milestone while
sleeping for eight hours. M2 local candidate 9d766b9 passed its repair checks,
but required live ChatGPT/account gates remain blocked. One retry remains.
See history/20261001_m2-local-plugin.md. Public deployment and product messaging
remain pending; the separate MCP protocol-readiness prerequisite still does not
implement Events. Evaluation evidence: history/20261001_m1-local-baseline.md.

## Next design step

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
storage revision before implementing messaging features.

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
group exchanges, and an XMPP bridge remain separate milestones. Core Codex and
compatible-harness participation is part of the product requirements above.
The first release must not claim verified interoperability with runtimes that
have not been exercised.
