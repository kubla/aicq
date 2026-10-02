# GitHub repository access checks

This is setup evidence, not an AICQ application milestone run or completion.

The user selected a private repository at `kubla/aicq` and preferred enabling
the agent to create it instead of creating it manually.

Observed results:

- `gh api repos/kubla/aicq` returned HTTP 404 with the initial integration.
- `gh repo create kubla/aicq --private` returned `Resource not accessible by
  integration (createRepository)`.
- REST `POST /user/repos`, with `private: true`, also returned HTTP 403.
- Separate GitHub CLI browser authorization completed as kubla.
- Subsequent REST creation still returned the same HTTP 403. `gh auth status`
  reported no OAuth scopes; the API response identified a GitHub App.
- Managed environment status was current and connected with unrestricted HTTP
  policy, but no configured secret bindings or outbound identities. This does
  not establish the source of the effective GitHub credential.
- At the user's explicit request, a `gh auth refresh --hostname github.com
  --scopes repo` browser flow was started and completed successfully. The user
  confirmed completion. `gh auth status` still reported no scopes; the repository
  lookup still returned HTTP 404, and REST creation still returned the same HTTP
  403 integration-permission error. No remote repository was created.

No device codes, tokens, credential file contents, or cookies are recorded here.
The local planning repository exists and is clean. No remote AICQ repository has
been confirmed, no files have been pushed there, and no application code exists.

## Follow-up: existing repository writes

The user created private kubla/aicq. Repository metadata confirmed `private: true`
and push/admin access. The following actions succeeded:

- Read the existing Fulcra MCP fork and its aicq/mcp-events branch.
- Create a temporary aicq/access-check-20261002 branch at 429da58, then delete it.
- Read the empty AICQ repository over Git with `git ls-remote`.
- Write the initial .gitignore through the contents API, producing commit
  fff7e6becf434ee57685fd455141d1e50ec6041c.
- Create https://github.com/kubla/aicq/issues/1 to track M1.

Ordinary `git push --set-upstream origin main` failed with HTTP 401. Prepared
source publication will use Git Data API operations, then verify the remote
commit/tree against the local source. These setup actions do not complete M1.
