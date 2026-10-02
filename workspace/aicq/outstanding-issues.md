# Outstanding issues

## GitHub repository creation [resolved by user]

The user selected private `kubla/aicq`. `gh repo create kubla/aicq --private`
failed with `GraphQL: Resource not accessible by integration (createRepository)`.
This is a GitHub integration permission error, not an automatic approval rejection.

Action: create an empty private repository and grant the integration access, or
provide a GitHub connection capable of repository creation. Local preparation can
continue. The user prefers enabling creation. GitHub CLI browser authorization
completed as kubla, but REST `POST /user/repos` still returned HTTP 403 afterward.
Do not ask the user to repeat the same login without evidence it can fix access.
The user subsequently explicitly requested a retry. A CLI refresh requesting
repo scope has been started; wait for its actual result before claiming access.

Result: that explicit-scope refresh completed. Effective scopes remained absent,
lookup returned HTTP 404, and REST creation again returned the same HTTP 403.
No authorization flow remains pending. Local development can proceed; remote
creation requires resolving the effective integration permissions or creating
the repository from another authorized execution environment.

Resolution: the user created private `kubla/aicq`. Verified visibility and
repository access; initial file creation and issue creation succeeded.
No repository-creation capability has been demonstrated by the agent.

## Git push transport [API workaround available]

`git ls-remote origin` succeeded on the new empty repository, but `git push`
failed with HTTP 401 during send-pack. GitHub branch creation/deletion, content
writing, and issue creation through `gh` succeeded. Use the Git Data API for
source publication and verify remote refs/trees. Do not interpret the Git push
failure as proof that other repository writes are unavailable.

## Local ChatGPT connectivity [feasibility gate]

The user selected local-first development and deferred complicated infrastructure
to Josh/GCP. OpenAI documents Secure MCP Tunnel for private developer-mode testing;
it needs tunnel permissions, runtime credentials, and workspace association.
OAuth endpoints and callbacks still need reachable URLs, and public distribution
needs a public HTTPS endpoint. Validate the private-development seam at M2; pause
substantial infrastructure work if it is blocked. No tunnel or local AICQ app has
been configured or tested yet.

## Events protocol migration [resolved prerequisite]

The upstream pinned dependencies support `2025-11-25`, while OpenAI MCP Events
requires `2026-07-28`. Current FastMCP/MCP releases provide a possible migration
path. An isolated upgrade test fails during collection on the private
`ServerSession._received_request` patch. No checkout dependencies were changed.

Action: produce a focused, regression-tested migration before advertising Events.

Resolution: commit `429da58` upgrades to FastMCP 4.0.10 / MCP 2.2.0 and removes the
obsolete patch. The full suite passes 132 tests, including modern HTTP requests.
This establishes protocol readiness, not Events capability.

## Live acceptance gates

The AICQ application, deployed owner dashboard, two-owner mailbox workflow and
real ChatGPT Events lifecycle have not been built or verified. M1 remains pending.
Do not claim production readiness or merge Events to upstream based on baseline tests.
