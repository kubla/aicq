# Fulcra MCP Events contribution

## Working checkout and upstream baseline

- Upstream: https://github.com/fulcradynamics/fulcra-context-mcp
- Existing fork: https://github.com/kubla/fulcra-context-mcp
- Local checkout: `/workspace/fulcra-context-mcp`
- Development branch: `aicq/mcp-events`
- Inspected upstream commit: `9efe894e15ebb612298e41341a232e713c459505`
- Frozen environment: FastMCP 3.4.7, MCP Python SDK 1.28.0, Fulcra API 0.1.42.
- Baseline validation: `uv sync --frozen`; `uv run --frozen pytest -q` produced
  **127 passed in 5.66s**. This validates the unchanged server, not Events support.

A fork creation attempt received HTTP 403 from GitHub's integration permissions.
A subsequent exact lookup verified that the user's existing fork already exists
with the expected upstream parent; it can be reused without creating another.

## Contribution boundary

Add general Fulcra change subscriptions and a durable delivery relay. Keep AICQ
contact resolution, stable agent addresses, conversation semantics and UI in AICQ.
Other Fulcra applications should benefit from Events without adopting AICQ.

The source already provides a hosted OAuth gateway, persisted upstream grants,
credential refresh coordination, shared folder APIs and update discovery.
Reuse those seams rather than replacing authentication or routing unrelated tools.

## First event

Proposed event: `fulcra.file.changed`, with filters for an authorized owner or
shared peer and a normalized folder prefix. Payloads contain a stable file/version
reference, change kind and occurrence time. Retrieve contents through existing
read tools. AICQ watches its selected mailbox paths and turns new message files
into its application workflow. Generic subscriptions must not expose all of the
owner's data by default.

Only advertise changes the source API can actually report. Test upload, replace,
delete, restoration and shared-folder behavior before documenting their coverage.
File shares cannot be assumed to provide time-bounded authorization.

## Protocol compatibility is the first gate

The current pinned SDK's latest protocol version is `2025-11-25`; it has no
`server/discover` or `events/subscribe` handlers. OpenAI requires `2026-07-28`.
An ordinary tool named `subscribe` will not activate the ChatGPT integration.
Changing a version constant or adding an Events capability without implementing
the negotiated protocol would be an incorrect claim of support.

Assess a supported SDK upgrade first. If an adapter is required, keep it isolated,
explicitly implement the required discovery/request/response contracts, and prove
wire compatibility through actual HTTP requests and ChatGPT integration. Preserve
legacy initialize, tools and authentication behavior with the existing test suite.
Advertise Events only once that gate passes. Leave stdio unchanged initially.

## Durable relay

1. Authenticate and authorize discovery and subscription requests using the
   existing hosted provider; derive a stable owner principal through verified
   identity, independent of a particular access token.
2. Validate event arguments, folder boundaries, access to the requested peer,
   HTTPS callback destinations and signing secrets. Verify the callback challenge
   before persisting an active subscription.
3. Persist subscriptions, grant references, granted expiry, discovery cursors,
   event journal and delivery attempts. A replacement login/token must not create
   a different owner identity. Revocation of the underlying grant stops delivery.
4. Discover changes through authorized Fulcra API queries. Server-side polling is
   a bridge option, not a claim that Fulcra has native push hooks. OpenAI's client
   receives webhooks; it does not poll this integration. If Fulcra later supplies
   native notifications, replace the source adapter without changing the contract.
5. Deduplicate overlapping discovery windows with stable source/version IDs and
   create durable outbox entries before advancing progress. Distinguish an upload
   receipt from data that is actually queryable. Track shared peers fairly rather
   than repeatedly scanning only the first 20 used by the interactive helper.
6. Recheck access before delivering. Sign one serialized payload using Standard
   Webhooks, preserve the event ID on retries, bound retry/backoff and honor
   non-retryable responses. HTTP 2xx means callback receipt, not completed work.
7. Support idempotent subscription identity, refresh/secret rotation, expiration,
   unsubscribe and replay with a cursor that cannot skip pending events.

The existing server explicitly targets multi-instance Cloud Run operation. A
process-local loop or SQLite database on ephemeral local disk is insufficient
for that production model. Choose shared durable storage and worker coordination
with leases before enabling a hosted relay. A single-process development store
must be clearly labeled and must not be presented as production readiness.

## Evaluation required before upstream proposal

- Protocol discovery and all subscription methods over authenticated HTTP.
- Existing OAuth, tool calls, CORS and stateless transport remain compatible.
- Correct event filtering and rejection of unauthenticated or unauthorized owners.
- Callback verification, destination validation, signatures and secret rotation.
- Restart recovery, overlapping windows, duplicate/out-of-order delivery,
  subscription refresh and expiry, replay and revoked sharing.
- Two real accounts sharing a folder: a peer write reaches only the authorized
  subscription and becomes readable through the existing tool.
- A real subscribed ChatGPT Work chat receives an event and follows its owner's
  configured instruction; stopping monitoring halts delivery.
- No response loop when AICQ writes a reply or acknowledgment.

Prepare focused commits on the fork and then an upstream pull request after the
integration is proven. The user's suggestion to push to main is a future outcome
conditional on quality, not an immediate merge operation.

## Current status

Fulcra authentication succeeded and the canonical planning workspace has been
uploaded. Harness annotation `MomentAnnotation/51f5fa9c-a6c7-4ee5-a0e3-f602496e3bed`
was created, and a factual preflight source-review record was written and read back.
This is not a completed application milestone.

The fork now contains a protocol migration commit, `429da58`, upgrading to FastMCP
4.0.10 and MCP 2.2.0, removing the obsolete private session patch, permitting
modern browser routing headers, and adding authenticated HTTP regression checks.
`uv run --frozen pytest -q`: **132 passed, 3 existing-field deprecation warnings
in 6.36s**. `git diff --check` passed. Modern discovery, tool listing, tool
execution and rejection of an invalid credential were exercised through the ASGI
HTTP application; existing legacy transport and tool tests passed.

Events handlers, live subscriptions and ChatGPT activation are not implemented.
The upgraded server does not advertise Events. The app baseline and dashboard
remain pending, and no upstream merge or live deployment has been performed.
