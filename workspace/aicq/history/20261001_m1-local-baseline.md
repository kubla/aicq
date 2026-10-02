# M1 local baseline evaluation

Run: `m1-7abb2258-7b2d-44d0-bb90-7e630b431618`. Attempt 1; no retries used.
Started 2026-10-01 22:06:34 America/New_York (2026-10-02 02:06:34 UTC).
Initial M1 timeout override of 60 minutes was uploaded before RUN_START.
Roles executed sequentially: Nurse, Coordinator, Generator, Evaluator.
Candidate revision: `fdcec134f149bb6f95b36c084e58b90ec9d5fd34`.
Target: http://127.0.0.1:6173/ and /harness. No public deployment.

## Implementation

Official Fulcra Svelte template at `613a3d817df7933e73b6fb9cbda86fd7377b8e6b`.
Customized login and authenticated shell; Node build adapter; loopback dev server.
Dashboard reads the existing harness annotation, canonical overview and issues.
Global owner navigation and direct page/data checks use Fulcra-validated identity.
The configured owner ID stays server-only; browser resources cannot choose another
annotation or workspace. Markdown is sanitized with DOMPurify. Failed loads are
visible, and previous data is labeled stale. Credentials are not persisted in
localStorage; the session token uses an HTTP-only cookie.

## Evaluator evidence

- Fresh owner browser sign-in: Sign In, matched device confirmation, Google owner
  selection, Auth0 success, authenticated AICQ shell and owner navigation. Logout
  returned to the login page. A second fresh owner sign-in during evaluation
  restored navigation; Harness Dashboard opened through the global link.
- The dashboard displayed the actual M1 run, all recorded lifecycle/evidence
  strings, canonical overview, and outstanding issues. REVIEW progress event
  `bb82766e-8292-44a2-b4fb-a404d23cb851` was written/read back as record
  `193412c3-23c9-550b-a4b2-8bd62584dbf3`, returned by the live runs API, and visibly
  rendered with its detail and evidence after refresh.
- Live Python HTTP verifier uses the normal Fulcra CLI token in memory. Owner
  runs/overview/issues returned 200 and no-store headers. Unauthenticated and
  invalid-token requests returned 401 on each private data route. A forged owner
  claim returned 401. The owner-report endpoint returned only isOwner=true.
- Separately authenticated Google test account: real browser sign-in completed;
  owner navigation was absent; direct /harness returned HTTP 403 and the owner-only
  message. A temporary same-origin HTML probe used the browser's normal HTTP-only
  cookie. Session check returned 200/authenticated=true; owner check returned
  200/isOwner=false; runs, overview, and issues each returned 403. Screenshot:
  `history/20261001_m1-non-owner-api.jpg`. No test token was copied to the CLI.
- Independent Evaluator checks: npm run check (0 errors, 0 warnings), npm run lint
  (passed), npm test (6 security regression tests passed), npm run build (Node
  adapter success), git diff --check (passed). These unit tests cover forged
  identity, non-owner/unauthenticated denial, fixed resource scope, missing
  canonical files, and safe owner-report output.

Detailed sanitized API outcomes: `history/20261001_m1-api-evidence.json`.
Raw local check/build output is retained under ignored `.local/evaluator-*.log`.
The temporary acceptance probe is removed after checks; screenshots contain no
passwords, tokens, cookies, or device authorization codes.

## Scope and limitations

M1's local authenticated baseline and access-isolated populated dashboard gates
passed. Coordinator MARK_COMPLETE record 981a6512-a9eb-5f15-b706-2b854af87b96
and terminal RUN_COMPLETE record c363bd6f-cab2-5e82-9170-7d380e4ba4a5 were
written, read back, and visibly rendered with their evidence in the owner dashboard.
The updated canonical overview also visibly showed M1 complete and M2 pending.
Screenshot: history/20261001_m1-owner-dashboard.jpg. Public deployment, product
messaging, plugin linking, and Events are later milestones. No substantial M1
infrastructure blocker was found. Dependency audit after compatible fixes has
four low-severity transitive cookie findings; high-severity findings cleared.

The user authorized continuing milestone by milestone while sleeping for eight
hours. A bounded heartbeat in this chat resumes work until 2026-10-02 10:55 UTC
(06:55 America/New_York), preserving all existing harness and local-first gates.
