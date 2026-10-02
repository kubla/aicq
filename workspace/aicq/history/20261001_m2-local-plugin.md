# M2 local plugin evaluation — incomplete

Date: 2026-10-01 America/New_York / 2026-10-02 UTC.
Candidate `9d766b9`, branch `kublascratchpad/m2-plugin-shell`.
M1 remains complete. M2 has no MARK_COMPLETE; M3–M6 remain pending.

## Recorded process

One agent performed Nurse, Coordinator, Generator, and separate Evaluator roles
sequentially. Nurse reused owner annotation
`MomentAnnotation/51f5fa9c-a6c7-4ee5-a0e3-f602496e3bed`. Initial M2 60-minute
override was uploaded before RUN_START. Retry 1 used the default 15 minutes.
Every recorded event was read back by its actual event ID.

Attempt 1 `m2-2ad50a7c-89bc-444a-b7ab-4548aa1e15d1` started 03:03:18 UTC.
Evaluator tested frozen candidate `9161037`: nine tests, UI/schema checks,
extracted plugin, real owner setup/reuse, both entrypoint calls, and M1 regression
checks passed. A live wrong-resource authorization probe was denied but returned
`server_error` instead of `invalid_target`. Required host/account checks were
blocked. Failed REVIEW `8827d0e9-d9d8-5aa0-add1-ea529d0ebf51` at 03:41:05;
RUN_COMPLETE `884667bd-6042-5ae2-83be-7a983949113a` at 03:41:08.

Retry 1 `m2-fac0fd7f-faf4-44d2-938a-6490e8795e91` started 03:41:12 UTC.
Generator repaired the authorization exception type and added endpoint coverage.
Evaluator separately tested frozen candidate `9d766b9`; local repair passed.
Failed REVIEW `d2f7ed1b-1cc5-55cc-8cd6-5a991825dd0a` at 03:48:29 preserved
blocked required gates; RUN_COMPLETE `078eb55c-81b1-5cac-9a58-96e70cd7a175`
at 03:48:31 closed the attempt. One of two milestone retries is used. One remains;
no timeout or harness repair retry consumed. Further attempts wait for changed
prerequisites.

## Implemented and verified locally

The portable plugin packages onboarding and a stdio MCP configuration. Four tools
provide verified Fulcra identity, resumable private profile/settings setup, and
empty-argument global/thread entrypoints. MCP App HTML bundles the official
MCP Apps and OpenAI extensions SDKs. HTTP transport reuses the immutable Fulcra
OAuth gateway at prerequisite 429da58508a179cc425d10728434739ca6620e1a with AICQ
resource binding, state validation, credential isolation per authorization, and
refresh replay protection. The separate Events fork was not modified.

Actual owner stdio setup created and read back both missing resources. Repetition
reused them. Extracted repaired archive ran the exact manifest command with normal
executing-client Fulcra credentials; two fresh server processes retained owner
`918681bf-aa1a-5a00-9e5e-b2ab5e44c282` and agent
`3f6b6348-6114-5c2e-9e61-da45611b8235`. Both entrypoint tools were called and
the compiled UI resource read. This proves local tools/resource delivery, not
ChatGPT host rendering.

Ten focused tests passed in 0.88 seconds: audience rejection, refresh/restart,
overlapping login isolation, setup repetition/interruption/conflicts/errors,
HTTP authorization, stdio-to-HTTP credential guard, and the OAuth error contract.
Live local discovery passed; missing/invalid bearer requests returned 401.
The repaired live DCR/authorize probe returned 302 with `invalid_target` and
started no upstream login. UI type check/build and official metadata/manifest
validation passed. Evaluator rechecked unchanged M1: type check, lint, six
security tests, Node build, live private API authorization, and actual dashboard
record display passed. Sanitized receipts: 20261001_m2-local-evidence.json.

## Required checks blocked

Auth0 visibly rejected SDK client `48p3VbMnr5kMuJAUe9gJ9vjmdWLdnqZt` redirect
`http://127.0.0.1:4499/callback`: “Callback URL mismatch.” Josh/Fulcra needs to
provide a compatible client/callback registration; if reachable gateway hosting
is needed, defer infrastructure to Josh/GCP. Screenshot:
20261001_m2-callback-mismatch.jpg. No alternate public host was selected.

OpenAI Platform Google login reached MFA. Email verification is offered, but
opening Gmail for the private verification message was rejected by automatic
approval review. No email was read or code submitted. No tunnel, runtime key,
workspace association, or development ChatGPT plugin is verified. ChatGPT is
logged out. Actual host entrypoints and real gateway linking/refresh/reconnect
remain untested.

A separate normal SDK device login used isolated credential storage but reused
owner browser SSO. Its verified principal was the owner; no fresh test-account
resource writes were performed. Automatic approval review rejected clearing
that SSO session because it could disrupt the existing owner login. Explicit
limited permission for both rejected actions is pending. M1's earlier real test
account denial does not satisfy M2 fresh/interrupted bootstrap acceptance.

## Continuation

Keep M2 incomplete and do not advance M3. Preserve the remaining retry for changed
integration prerequisites. Local dashboard remains loopback 6173; MCP HTTP gateway
loopback 4499. Source and package remain local; credentials/state are ignored.
The owner dashboard visibly rendered the latest failed REVIEW, terminal
RUN_COMPLETE, and updated canonical status/issues; screenshot: 20261001_m2-dashboard.jpg.
The authorized in-chat heartbeat is bounded until 2026-10-02 10:55 UTC. Do not
repeat rejected actions without approval or send external messages to Josh.
