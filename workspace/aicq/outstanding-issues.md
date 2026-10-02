# Outstanding issues

## M1

No blocking M1 issue remains. Real owner and authenticated non-owner checks passed.
Four low-severity transitive cookie audit findings remain; compatible updates
cleared high-severity findings without a forced major upgrade.

## M2: Fulcra browser OAuth configuration — Josh/Fulcra help

The reused Fulcra SDK OAuth client `48p3VbMnr5kMuJAUe9gJ9vjmdWLdnqZt` visibly
rejects `http://127.0.0.1:4499/callback` with “Callback URL mismatch.” The configured
redirect URI is absent from its allowed callbacks. A compatible Fulcra application
registration or approved callback configuration is needed. Preserve resource-bound
OAuth and normal client credentials. Do not silently select another host or expose
local services publicly. If browser-reachable gateway hosting is required, defer
that infrastructure to Josh/GCP. Evidence: history/20261001_m2-callback-mismatch.jpg.

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

The isolated second CLI login reused the owner browser SSO. Its verified principal
is the owner; it is not fresh non-owner evidence, and no test bootstrap was written
through it. Automatic approval review rejected clearing the existing Fulcra SSO
session because that could disrupt the owner's browser login. Explicit permission
for that switch is pending. M1's earlier real Google test-account denial remains
valid; it does not establish M2's fresh/interrupted bootstrap acceptance.

M2 has one retry left after the verified local repair. Wait for changed prerequisites;
keep all required host/account checks incomplete and M3–M6 pending.

## Source publication and later gates

Application commits remain local in the private repository. Earlier cloud Git push
failed with HTTP 401; current local push capability has not been retested.
Two-owner exchanges, third-owner isolation, revocation, useful artifacts, client
switching, and actual ChatGPT Events remain unverified. Separate prerequisite
`429da58` is protocol readiness, not Events implementation.
