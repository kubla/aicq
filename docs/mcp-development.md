# AICQ MCP development

Status: local tools and plugin package implemented; ChatGPT installation and
account linking remain unverified. M2 acceptance is incomplete.

The root portable plugin bundles onboarding and a local stdio server. Run
`npm ci --prefix mcp/ui`, `npm run check --prefix mcp/ui`, and
`npm run build --prefix mcp/ui`, then `python3 scripts/package-plugin.py` to make
the development bundle. These build commands run in the repository; the bundle
already includes the compiled single-file MCP App UI.
Installing it does not start background responses. ChatGPT needs a registered
remote or tunnel connection; a local stdio declaration alone cannot install that
connection in ChatGPT.

## Local credentials and tools

`uv run --project mcp --frozen --no-editable aicq-mcp` uses normal Fulcra CLI credentials for
stdio. Each executing client authenticates separately with `fulcra auth login`.
Use `mcp/scripts/verify_stdio.py --setup` only when creating the owner's private
AICQ resources is intended. Without `--setup`, it performs read-only checks.

`aicq_identity` and `aicq_setup` work without UI. `aicq_open` and `aicq_thread`
accept empty arguments and advertise global/sidebar and thread entrypoints. All
four resolve the verified Fulcra account; callers cannot select another owner.
The UI connects using MCP Apps and OpenAI extensions, uses host theme variables,
and renders tool results with textContent.

The owner address is UUIDv5(NAMESPACE_URL, `urn:aicq:owner:<verified Fulcra UUID>`);
the default agent address is UUIDv5(owner_id, `default-agent`). Both are persisted
in `/aicq/profile.json`. These are implementation choices, independent of labels,
emails, tokens and client threads. A conflicting stored binding fails visibly
and is preserved. `/aicq/settings.json` starts with background responses disabled.
Only missing resources are written; each write is read back. An uncertain write
requires inspection/retry. Invitations remain in explicit handoff state until
contact acceptance is implemented in M3.

## Local HTTP OAuth gateway

The dependency pins `kubla/fulcra-context-mcp` at
`429da58508a179cc425d10728434739ca6620e1a`. Its persisted client/grant/token machinery
and synchronized upstream credential refresh are reused. AICQ adds explicit
resource-bound access/refresh tokens, unique upstream login state, and credentials
bound to authorization codes so overlapping logins cannot swap account bindings.
No Fulcra API token is accepted as an AICQ MCP token. The separate Events fork is
unchanged and does not implement Events.

Configure server-only environment values before launching:

- `FULCRA_ENVIRONMENT=http`
- `OIDC_SERVER_URL=http://127.0.0.1:4499` for local discovery; replace with the
  verified browser-reachable authorization gateway origin for ChatGPT testing.
- `AICQ_RESOURCE_URL` defaults to `<OIDC_SERVER_URL>/mcp`. Set it to the exact
  advertised MCP resource if the final tunnel integration requires another URL.
- `OIDC_CLIENT_ID` must be a Fulcra client supporting authorization-code exchange
  and the exact `<OIDC_SERVER_URL>/callback` callback. The default SDK client is
  not validated for this use and rejected the local callback in the live check.
- `STATE_PATH` must be a private persistent directory, e.g. `.local/oauth-state`;
  it contains gateway credentials. `main` uses umask 077 and binds loopback.
- `PORT=4499`

Start with `uv run --project mcp --frozen --no-editable aicq-mcp`. OAuth discovery is available at
`/.well-known/oauth-authorization-server` and
`/.well-known/oauth-protected-resource/mcp`; MCP uses `/mcp`. Upstream Fulcra
credentials remain in gateway state and are never returned by product tools.

## Infrastructure and evaluation gates

[OpenAI's Secure MCP Tunnel guide](https://developers.openai.com/api/docs/guides/secure-mcp-tunnels)
requires a Platform tunnel ID, runtime key and intended workspace association.
It provides MCP transport, while the browser-facing OAuth service still needs
reachable endpoints. No tunnel, runtime key, target workspace association or
live ChatGPT plugin installation is verified yet. Platform browser sign-in is
waiting for email MFA verification; the personal Chrome ChatGPT session is logged out.

Live Auth0 check: the SDK client `48p3VbMnr5kMuJAUe9gJ9vjmdWLdnqZt` rejected
`http://127.0.0.1:4499/callback` with “Callback URL mismatch.” October2 source
research found that the separate production MCP public client already allows this
callback. Check the exact adapter client/tenant/audience and real exchange before
requesting new local callback registration. A dedicated HTTPS gateway still needs
service/callback/state configuration using Josh's GCP help. See
docs/research/20261002-fulcra-dev-deployments.md for existing deployment patterns.
No alternate host or public exposure has been configured.

Required remaining M2 checks: actual development installation in ChatGPT; both UI
entrypoints rendered by the host; real OAuth sign-in through callback; refresh and
reconnect identity stability; fresh Fulcra test-account and interrupted/repeated
setup; relevant M1 regressions. Local tests and owner stdio success do not pass
these blocked checks.
