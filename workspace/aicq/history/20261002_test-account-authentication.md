# Test-account authentication prerequisite

The user supplied standing authorization: “You can always log out of Fulcra
without my further permission.” The earlier automatic rejection of clearing
the shared browser SSO session no longer prevents this action.

Personal Chrome's Fulcra Auth0 logout returned OK. A new normal SDK device flow
opened the sign-in page; Google account michael.tiffany@gmail.com was explicitly
selected. The browser showed the device connected successfully. The separate
client stored credentials privately in ignored .local/test-client-config/fulcra/,
without copying browser credentials or changing the owner CLI credential store.

Read-only AICQ identity checks returned Fulcra principal
81359eb8-9c06-47e3-92d2-ac80b053c40c, distinct from the project owner. Derived
owner e346c544-8c73-5d3e-9cd6-a83ccfb68776 and agent
7e734bde-fe01-5026-9371-712b37b0b39a were returned; setup_complete=false.
Sanitized receipt: 20261002_test-account-identity.json.

This resolves the principal/authentication prerequisite only. No bootstrap
resource was written, no new M2 attempt was started, and no retry was consumed.
M2 fresh/interrupted setup, real ChatGPT installation/rendering, and OAuth
linking/refresh remain unverified. The Fulcra callback mismatch and OpenAI
Platform access gates remain. No OpenAI MFA email was read or code submitted.
Overnight automation remains paused; no further logout permission is required.
