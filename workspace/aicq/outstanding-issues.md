# Outstanding issues

## M1

No blocking M1 issue remains. Real owner and authenticated non-owner checks passed.
Four low-severity transitive cookie audit findings remain; compatible updates
cleared high-severity findings without a forced major upgrade.

## M2: Fulcra browser OAuth client selection and gateway hosting

The reused Fulcra SDK OAuth client `48p3VbMnr5kMuJAUe9gJ9vjmdWLdnqZt` visibly
rejects `http://127.0.0.1:4499/callback` with “Callback URL mismatch.” The configured
redirect URI is absent from that client's allowed callbacks. October2 deployment
research found production IaC already allows this exact loopback callback on the
separate Fulcra MCP Server public client `tc92NeNkAg748rlxBbm79cKdG9AOAbfc`.
First verify the pinned gateway's client/tenant/audience configuration and a real
code exchange/refresh. Live Auth0 state and successful AICQ linking remain unverified;
a new local callback registration is not yet established as necessary.

For reusable Fulcra MCP testing, a separate test service/hostname, callback
registration, scoped repository federation and isolated storage need
Josh/Fulcra/GCP help. The current provider admits only private repos while MCP is
public; widening it in place affects an organization-wide registry admin binding.
The existing dev MCP service restricts direct ingress. Current MCP OAuth pending
transactions and refresh locks are process-local; a shared GCS mount does not
supply transactional writes or locking. Stable test hosting and the MCP fixes are
recommendations, not implemented or live-evaluated changes. See
history/20261002_mcp-preview-design.md. Existing
Portal Cloud Run PR previews have successful runs; MCP supplies a persistent state
pattern. Neither is an existing AICQ deployment. Vercel app-template deployment is
documented, while Fulcra-managed project/token provisioning remains unmerged.
Leif's Agent Playground project (`fulcra-agent-playground-spfvm7`) provides an
existing manual GCE testing recipe; broader CI/CD work is optional for this route.
A Fulcra-owned hostname is feasible through existing DNS management, but no
playground VM-to-public-HTTPS setup or current executing-client permissions have
been verified. Establish VM/storage, stable addressing, TLS/ingress and the exact
upstream callback before claiming hosting is unblocked. See
history/20261002_fulcra-vm-hosting.md.

Preserve resource-bound OAuth and normal client credentials. No provider was selected
or public exposure configured. Evidence: history/20261001_m2-callback-mismatch.jpg
and history/20261002_fulcra-dev-deployments.md.

## M2: Platform and ChatGPT access

OpenAI Platform Google sign-in reached email MFA for michael.tiffany@gmail.com.
No verification email was read and no code was submitted. Automatic approval
review rejected opening Gmail for that authentication material; explicit limited
permission has been requested, or the user can finish MFA themselves.

No Secure MCP Tunnel, runtime credential, or target ChatGPT workspace association
has been created or verified. ChatGPT is logged out; no development plugin is
installed. The tunnel's browser OAuth endpoint/callback reachability also needs
live validation. The portable local archive is callable through stdio, but that
does not prove ChatGPT installation, host UI rendering, linking, or refresh.

## M2: separate fresh test owner

The first isolated CLI login reused owner SSO and was not non-owner evidence.
The user subsequently authorized Fulcra logout without further permission.
After logout, a new normal Google device login selected michael.tiffany@gmail.com.
Read-only checks now verify a distinct test owner, with AICQ setup incomplete.
No bootstrap resources were written; fresh/interrupted setup acceptance still
needs its recorded evaluation. See history/20261002_test-account-authentication.md.

M2 has one retry left after the verified local repair. Wait for changed prerequisites;
keep all required host/account checks incomplete and M3–M6 pending.

## Source publication and later gates

Application commits remain local in the private repository. Earlier cloud Git push
failed with HTTP 401; current local push capability has not been retested.
Two-owner exchanges, third-owner isolation, revocation, useful artifacts, client
switching, and actual ChatGPT Events remain unverified. Separate prerequisite
`429da58` is protocol readiness, not Events implementation.
