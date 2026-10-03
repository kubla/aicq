# Hosting the retained embedded UI prototype

Date: October 2, 2026. Design assessment and recorded user decision. No deployment or milestone attempt.

## User decision

> I think the embedded UI is an important part of this product idea. Let’s keep it. What kind of hosting does that require? What do we need to host and test a prototype?

Retain the embedded UI. The connector-only proposal that defers it is not selected. Use polling for initial delivery rather than making new Fulcra MCP Events support a prerequisite. Hosting below is a recommendation, not a selected provider or authorization to provision resources.

## What runs

The inspected AICQ source already serves MCP tools, bundled HTML/CSS/JavaScript and OAuth discovery/authorization/token/callback routes in one Python ASGI service. The iframe uses the MCP Apps host bridge for server calls; its current CSP has no external resource or connect domains. There is no requirement for a separately deployed frontend for this bundle. Python requires 3.13 or newer; Node is used to build the bundled UI, not as its runtime server.

The service talks to existing Fulcra API/account/storage capabilities. Fulcra's MCP server needs no new Events handlers for the polling path. No model is hosted by AICQ. The four current tools expose identity/setup and UI entrypoints only; contact messaging and polling tools still need implementation and evaluation.

## Minimum live test environment

- One running Python service behind a reachable HTTPS origin, with `/mcp` plus the browser-visible OAuth routes. A private MCP transport tunnel is another documented test route, but browser authorization reachability remains a separate requirement.
- Private persistent credential storage for established OAuth registrations/grants/tokens. Keep it isolated from other services and out of the image/repository.
- Explicit Fulcra tenant/API/client selection, externally correct issuer/resource URLs, and the exact `<origin>/callback` allowed by the appropriate upstream Fulcra OAuth client. A callback allowlist entry is configuration, not an Events server feature.
- Normal operator access to deploy/read logs/restart and a known host expiration policy.
- ChatGPT developer-mode/plugin access in the intended account/workspace and separately authenticated Fulcra test owners. The existing owner annotation cannot be assumed writable by another owner.

For the current candidate, a dedicated single-process VM with a persistent disk and an HTTPS reverse proxy is the smallest runtime match. Fulcra's playground/Shell Beach recipes supply a precedent, but current live permissions, clean image, DNS/TLS and available instance remain unverified. Request an approved stable hostname; `aicq-dev.devfulcra.com` is only an example. The current loopback listener fits a same-host reverse proxy.

Cloud Run is viable hosting, but adapting this candidate requires container listening/port configuration, durable credential storage and resolving process-local pending OAuth state/refresh coordination. A one-instance setting is not an established solution to those runtime assumptions. General CI/CD and per-PR preview automation can follow a working manual deployment.

## Prototype evidence

First exercise the endpoint and tools with MCP Inspector, then the actual ChatGPT host. A labelled fixture UI can establish rendering/interaction only; it does not establish account linking or messaging acceptance.

For M2, install the development plugin, render both global and thread entrypoints, use real account sign-in/setup, verify fresh/repeated/interrupted setup and refresh/reconnect identity, reject missing/wrong-resource credentials, and rerun relevant M1 checks. Test established identity after restart; pending login transactions may require restarting sign-in after process restart and must not silently swap owners.

For subsequent messaging, verify two-owner narrow sharing, actual send/read/reply and artifact access, catch-up after downtime, deduplication, revocation and a third principal's denial. UI refresh/polling does not itself wake or authorize an inactive agent to perform work. Automatic response scheduling remains a per-runtime capability to configure and evaluate.

## Sources and status

Canonical plan/spec/decisions/progress/workboard and polling/VM/Toolkit hosting history were refreshed through normal Fulcra authentication and matched repository mirrors. Local `mcp/aicq_mcp/server.py`, `auth.py`, `ui-metadata.json`, `mcp/ui/main.ts` and dependency metadata were inspected.

Official OpenAI sources fetched October 2:

- [Build an MCP server](https://developers.openai.com/plugins/build/mcp-server): deployment/runtime requirements and hosted versus tunnel routes.
- [Authentication](https://developers.openai.com/plugins/build/auth): OAuth discovery, issuer/resource binding and client registration.
- [Connect and test](https://developers.openai.com/plugins/deploy/connect-chatgpt): Inspector, developer mode, tool/UI evaluation and installed plugin checks.

M2 remains incomplete. One retry remains. No platform MFA access, callback change, service launch, cloud grant, public publication or message to Josh was performed.
