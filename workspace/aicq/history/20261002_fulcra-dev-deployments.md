# Fulcra developer and test deployments: research spike

Research date: October 2, 2026. Checked GitHub documentation/source, GitHub issues and PR discussions, authenticated Nuclino, Linear, and Slack #eng. Normal client authentication was used. No deployments, infrastructure changes, secret retrieval, external messages, or AICQ milestone retries occurred.

## Recommendation for AICQ

Use Fulcra's existing Cloud Run machinery for a dedicated AICQ test gateway. Portal proves the PR-preview workflow operates, and the MCP module supplies a relevant Python/OAuth/state pattern. AICQ still needs its own service, hostname, repository deployment federation, and HTTPS callback registration; an existing Portal or MCP service is not a spare deployment slot. Prepare those changes for Josh through the normal infrastructure PR/Atlantis process. This is a research recommendation, not a provider decision or deployment authorization.

First investigate local callback authentication with the existing MCP public client configuration. The failed login used the SDK client, whose callback list is empty; IaC already allows the loopback callback on the MCP client. This corrects the earlier diagnosis that new registration is necessarily required for local testing. A real exchange and refresh remain unverified.

Vercel is already Fulcra's documented app-template hosting option, and Leif/Greg are building Fulcra-managed project provisioning now. The dashboard can follow that path after its adapter/build check. The provisioning API and credential wiring are still unmerged, so do not depend on them to unblock M2 today. DNS delegation for `my.devfulcra.com` has actually been applied, but that alone does not deploy an app or authenticate its gateway.

Keep owner/test-account data and the harness in the production tenant for recorded acceptance unless another environment is explicitly chosen. Dev Cloud Run can use production API configuration, as Portal previews do; dev Auth0 changes account identity. Hosting can remove the Secure MCP Tunnel prerequisite, but ChatGPT login, installation, rendering, account linking, and refresh still need acceptance. M1 remains complete; M2 remains incomplete with one retry left.

## Findings from GitHub

Fulcra already has a concrete Cloud Run testing path. Portal uses a PR comment to deploy a no-traffic tagged revision on the dev service, optionally configured against the production API. Two October 1 runs prove this workflow executes successfully. The MCP service has its own Cloud Run module and durable GCS-backed OAuth state. Adapting these patterns is a better-supported Fulcra-native candidate than adopting an unrelated host solely to escape tunneling. This is a recommendation from the observed source; AICQ does not yet have its own registered service or deployment permissions.

A separate discovery changes the diagnosis of the loopback callback failure: Fulcra's production **MCP Server OAuth client** explicitly allows `http://127.0.0.1:4499/callback`. Its **SDK OAuth client** has an empty callback list. AICQ's overnight attempt used the SDK client. The source supports investigating client selection before concluding a new allowlist entry is required. This does not prove current Auth0 tenant state matches IaC or that a different client can be adopted without a live exchange check.

### Repository identity and access

There is no accessible literal `fulcradynamics/fulcra` repository: both the GitHub connector and normal authenticated `gh` returned 404. The organization has separate repositories for platform services, infrastructure, and documentation. Authenticated `gh` successfully read private `infrastructure`, `portal`, `fulcra-platform-local`, `developer-docs`, and `terraform-modules` sources. The connector's installed-repository search did not expose those private organization sources; the CLI did.

Normal CLI identity is `kubla`. On October 2, GitHub reports `pull/push` on infrastructure and `pull` only on Portal. Active `eng` team membership could not be verified: the membership endpoint reported that the current token lacks `admin:org` scope. No expanded token scope was requested. Repo write access is therefore not proof the deployment comment would be authorized.

Source snapshots read:

| Repository | Main commit | Commit date |
|---|---|---|
| [infrastructure](https://github.com/fulcradynamics/infrastructure/tree/4f26f9560299a177129d56932739cb6e83c00bde) | `4f26f9560299a177129d56932739cb6e83c00bde` | October 1, 2026, 21:30:42 UTC |
| [portal](https://github.com/fulcradynamics/portal/tree/ac40b9b7e9c85af370d309504104ba22ca038418) | `ac40b9b7e9c85af370d309504104ba22ca038418` | September 25, 2026, 17:06:43 UTC |
| [app-template-svelte](https://github.com/fulcradynamics/app-template-svelte/tree/613a3d817df7933e73b6fb9cbda86fd7377b8e6b) | `613a3d817df7933e73b6fb9cbda86fd7377b8e6b` | September 18, 2026, 22:54:30 UTC |
| [fulcra-platform-local](https://github.com/fulcradynamics/fulcra-platform-local/tree/21a094deb40671d12db97cbee9a006b95068fa77) | `21a094deb40671d12db97cbee9a006b95068fa77` | September 30, 2026, 17:22:58 UTC |
| [fulcra-context-mcp](https://github.com/fulcradynamics/fulcra-context-mcp/tree/9efe894e15ebb612298e41341a232e713c459505) | `9efe894e15ebb612298e41341a232e713c459505` | September 29, 2026, 17:30:57 UTC |
| [developer-docs](https://github.com/fulcradynamics/developer-docs/tree/57cbef843fed262b6c1d9b9f2afc92755d3caffe) | `57cbef843fed262b6c1d9b9f2afc92755d3caffe` | June 7, 2025, 17:31:45 UTC |

### Portal: operational PR previews on Cloud Run

**Explicit source and verified run metadata.** Portal's README says it is SvelteKit, containerized, and deployed on Cloud Run. The deploy workflow runs from the default branch when someone comments on an open PR. Commands are:

```text
/preview dev
/preview prod
/deploy dev
```

`/preview <environment>` uses the dev preview service, with runtime configuration from the named GitHub environment; `/preview prod` therefore runs a PR build on a dev Cloud Run revision **against production Auth0/API**. It adds `--no-traffic --tag pr-<number>`, resolves the tag URL from Cloud Run, and reports it through a GitHub deployment. `/deploy <environment>` instead deploys the PR head to that environment's actual service. It is not an isolated preview and should not be casually substituted. [Workflow commands and authorization](https://github.com/fulcradynamics/portal/blob/ac40b9b7e9c85af370d309504104ba22ca038418/.github/workflows/deploy.yml#L1-L117), [deploy implementation](https://github.com/fulcradynamics/portal/blob/ac40b9b7e9c85af370d309504104ba22ca038418/.github/workflows/deploy.yml#L243-L294).

The workflow requires active membership in `fulcradynamics/eng`, an existing target/config GitHub environment, and a successful CI run for the PR head. It resolves the head image by digest, avoiding a movable tag at deploy time. Configuration is read anew and explicitly written on every deploy, preventing a prior preview's backend overrides from carrying into a later deploy. CI tags images `pr-<number>-<short-head-sha>`; current CI's required build dependency is its `lint` job, despite a deployment comment saying "test". [CI](https://github.com/fulcradynamics/portal/blob/ac40b9b7e9c85af370d309504104ba22ca038418/.github/workflows/ci.yml), [CI gate and image resolution](https://github.com/fulcradynamics/portal/blob/ac40b9b7e9c85af370d309504104ba22ca038418/.github/workflows/deploy.yml#L172-L211).

Prerequisites include repository `GCP_WORKLOAD_IDENTITY_PROVIDER`, `CONTAINER_IMAGE_PATH`, CI app ID/private-key secret for membership checks, and GitHub environment variables `GCP_PROJECT_ID`, `GCP_REGION`, `CLOUD_RUN_SERVICE`, `FULCRA_ENVIRONMENT`, `PUBLIC_AUTH0_DOMAIN`, `PUBLIC_AUTH0_CLIENT_ID`, and `PUBLIC_FULCRA_API_ENDPOINT`. Portal also needs its Font Awesome npm token for its own build; AICQ does not automatically inherit that Portal-specific requirement. GitHub federation grants the particular repo/environment `roles/run.developer` on its service and `roles/iam.serviceAccountUser` on the runtime identity. [Workflow](https://github.com/fulcradynamics/portal/blob/ac40b9b7e9c85af370d309504104ba22ca038418/.github/workflows/deploy.yml), [Cloud Run deployment IAM](https://github.com/fulcradynamics/terraform-modules/blob/70cd3cf04c36ae768057b9f76b59a71e0d44ea2c/cloudrun_service/iam.tf#L89-L115).

The configured dev Portal domain is `portal-dev.fulcradynamics.com`, with `fulcra-dev.us.auth0.com` and `https://api.devfulcra.com/`. Its module explicitly sets `public=true`, permitting the service's `run.app` URL rather than requiring all access through the load balancer. [Dev Portal configuration](https://github.com/fulcradynamics/infrastructure/blob/4f26f9560299a177129d56932739cb6e83c00bde/tf/dev/context-webapp/terragrunt.hcl#L9-L24), [public ingress setting](https://github.com/fulcradynamics/terraform-modules/blob/70cd3cf04c36ae768057b9f76b59a71e0d44ea2c/services/portal/service.tf#L17-L32).

This is recently implemented and operating, rather than hypothetical advice:

- [Portal PR223](https://github.com/fulcradynamics/portal/pull/223), merged September 24, 2026, introduced GitHub Actions lint/build/publish and PR-comment dev deployment.
- [Infrastructure PR161](https://github.com/fulcradynamics/infrastructure/pull/161), merged September 24, introduced Portal environment variables and public dev Cloud Run access specifically for tagged previews.
- [PR227](https://github.com/fulcradynamics/portal/pull/227) shows `/preview prod` [comment](https://github.com/fulcradynamics/portal/pull/227#issuecomment-5938269511) at October 1, 18:48:14 UTC. [Run36909562519](https://github.com/fulcradynamics/portal/actions/runs/36909562519) succeeded; its jobs were "Check Command", "Load prod config", and "Preview on dev (prod config)". [An earlier run36892216689](https://github.com/fulcradynamics/portal/actions/runs/36892216689) at 16:28 UTC also succeeded.
- The PR advertises [its tagged preview](https://pr-227---dev-portal-vht7o43xrq-uw.a.run.app/). This research verified the PR and successful job metadata, not the preview application's runtime behavior.
- [Cleanup workflow](https://github.com/fulcradynamics/portal/blob/ac40b9b7e9c85af370d309504104ba22ca038418/.github/workflows/pr-cleanup.yml) removes the PR revision tag and associated images when the PR closes.

### Python services and MCP: Fulcra's existing deployment machinery

**Observed deployed-service configuration.** The MCP dev stack points to the pinned `services/mcp-service` module at commit `4128cfc6c3d512578f5f81d7a877dc2a7b9f1d86`. Its values are:

| Setting | Dev | Production |
|---|---|---|
| Issuer/base URL | `https://mcp.devfulcra.com` | `https://mcp.fulcradynamics.com` |
| Upstream tenant | `fulcra-dev.us.auth0.com` | `fulcra.us.auth0.com` |
| Upstream public client ID | `oaNZ1MO0egGo6IsogOZKoEhHmzgtcbIl` | `tc92NeNkAg748rlxBbm79cKdG9AOAbfc` |
| Upstream API audience | `https://api.devfulcra.com/` | `https://api.fulcradynamics.com/` (module default) |

These IDs are public configuration, not credentials. [Dev source](https://github.com/fulcradynamics/infrastructure/blob/4f26f9560299a177129d56932739cb6e83c00bde/tf/dev/mcp/terragrunt.hcl), [production source](https://github.com/fulcradynamics/infrastructure/blob/4f26f9560299a177129d56932739cb6e83c00bde/tf/prod/mcp/main.tf), [API default](https://github.com/fulcradynamics/terraform-modules/blob/4128cfc6c3d512578f5f81d7a877dc2a7b9f1d86/services/mcp-service/variables.tf#L78-L81).

The module provisions Cloud Run with ingress through the internal/load-balancer path and a writable GCS client-state bucket mounted at `/clients`; it disables metadata caching with `metadata-cache-ttl-secs=0` and gives the runtime service account `roles/storage.objectUser` on that bucket. Runtime variables are `OIDC_SERVER_URL`, `OIDC_CLIENT_ID`, `FULCRA_OIDC_DOMAIN`, `FULCRA_API`, `STATE_PATH=/clients`, and `LOG_FORMAT=json`. The inspected module's secret map is empty. [Cloud Run/state module](https://github.com/fulcradynamics/terraform-modules/blob/4128cfc6c3d512578f5f81d7a877dc2a7b9f1d86/services/mcp-service/cloudrun.tf), [runtime config](https://github.com/fulcradynamics/terraform-modules/blob/4128cfc6c3d512578f5f81d7a877dc2a7b9f1d86/services/mcp-service/config.tf).

The upstream server's persisted state includes dynamic client registrations, credential grants, access tokens, and refresh tokens; its source explicitly discusses multiple Cloud Run instances and reloading grants after another instance refreshes credentials. This is directly relevant to AICQ's reused gateway. Durable GCS mounts alone do not prove pending in-memory authorization transactions survive restarts or route correctly across replicas, nor do they prove every file-lock/rename assumption of AICQ's exact pinned gateway works with GCS FUSE. Those remain evaluation requirements. [Persistence model](https://github.com/fulcradynamics/fulcra-context-mcp/blob/9efe894e15ebb612298e41341a232e713c459505/fulcra_mcp/provider.py#L52-L76).

The MCP container uses Python3.14, installs with `uv sync --locked`, and starts `uv run fulcra-context-mcp`. HTTP mode listens on `0.0.0.0`, `settings.port` (default4499). AICQ currently binds its HTTP gateway to loopback, so hosting it requires explicit listening/port configuration; copying a Dockerfile is insufficient. [Dockerfile](https://github.com/fulcradynamics/fulcra-context-mcp/blob/9efe894e15ebb612298e41341a232e713c459505/Dockerfile), [settings](https://github.com/fulcradynamics/fulcra-context-mcp/blob/9efe894e15ebb612298e41341a232e713c459505/fulcra_mcp/settings.py), [HTTP startup](https://github.com/fulcradynamics/fulcra-context-mcp/blob/9efe894e15ebb612298e41341a232e713c459505/fulcra_mcp/main.py#L307-L324).

The older MCP image pipeline uses Cloud Build on commit and PR, with PR images in `us-west1-docker.pkg.dev/fulcra-artifacts/services/mcp`. Its PR trigger has `comment_control=COMMENTS_ENABLED` and publishes `pr-<PR_NUMBER>-<REF_NAME>` tags. The deployment trigger on registry publication **excludes `pr-` and `latest` tags**, so building a PR image is not automatic preview deployment. [MCP build definitions](https://github.com/fulcradynamics/infrastructure/blob/4f26f9560299a177129d56932739cb6e83c00bde/tf/artifacts/cloudbuild.tf#L94-L110), [PR build module](https://github.com/fulcradynamics/infrastructure/blob/4f26f9560299a177129d56932739cb6e83c00bde/tf/artifacts/modules/cloudbuildv2_publish_on_pr/main.tf), [deployment filter](https://github.com/fulcradynamics/terraform-modules/blob/4128cfc6c3d512578f5f81d7a877dc2a7b9f1d86/cloudrun_service_deploy/deploy.tf).

[Infrastructure PR120](https://github.com/fulcradynamics/infrastructure/pull/120), May 13, 2026, said there was no dev MCP server and PR builds were useful for manual production deployment. That is historical advice: today's repository contains a dev MCP stack. Its actual running state was not checked through GCP.

The newer GHA approach also applies to Python services: [Infrastructure PR162](https://github.com/fulcradynamics/infrastructure/pull/162) configures `input-service` GitHub deployments and removes its old Cloud Build image triggers. An [Atlantis apply receipt](https://github.com/fulcradynamics/infrastructure/pull/162#issuecomment-5818005500), September 24, records all three stacks successfully applied, including dev Cloud Run federated deployer IAM and its GitHub environment. This supports reusing the pattern for AICQ, not commandeering an existing service.

### OAuth callback failure: the upstream client distinction

**Explicit IaC and matching implementation.** The production `Fulcra SDK` client is native and has `callbacks=[]`. The `Fulcra MCP Server` client is SPA and explicitly allows both `http://localhost:4499/callback` and `http://127.0.0.1:4499/callback`, plus `https://mcp.fulcradynamics.com/callback`. It enables `authorization_code`, `implicit`, and `refresh_token`. Google, Apple, and username/password connections are attached. [SDK client](https://github.com/fulcradynamics/infrastructure/blob/4f26f9560299a177129d56932739cb6e83c00bde/tf/prod/auth0/apps.tf#L183-L223), [MCP client and allowlists](https://github.com/fulcradynamics/infrastructure/blob/4f26f9560299a177129d56932739cb6e83c00bde/tf/prod/auth0/apps.tf#L284-L351). This file was last changed September 14, 2026, at commit `4c1af8725711104898e85ed91dc89887554de67d`.

The hosted gateway constructs `FulcraAPI` with the configured client ID, tenant, and audience, obtains an authorization-code URL, then calls the normal code exchange with the same redirect URI. No client secret is explicitly passed in that code, no upstream client-secret setting is present in `Settings`, and the MCP Terraform runtime secret map is empty. This is source evidence for a public-client integration, not a promise that an ID-only switch meets all PKCE/grant requirements or matches live Auth0 configuration. Do not retrieve a secret merely because the callback failed. [Provider construction/exchange](https://github.com/fulcradynamics/fulcra-context-mcp/blob/9efe894e15ebb612298e41341a232e713c459505/fulcra_mcp/provider.py#L354-L390), [settings](https://github.com/fulcradynamics/fulcra-context-mcp/blob/9efe894e15ebb612298e41341a232e713c459505/fulcra_mcp/settings.py), [module config](https://github.com/fulcradynamics/terraform-modules/blob/4128cfc6c3d512578f5f81d7a877dc2a7b9f1d86/services/mcp-service/config.tf).

A new AICQ HTTPS hostname is not in the inspected MCP client's callback list. A dedicated app/client or approved addition will still be needed for that hostname. The existing loopback entry may enable local upstream OAuth testing immediately after checking the exact adapter configuration; cloud hosting remains necessary for ChatGPT to reach an MCP service on the Mac without a tunnel.

Do not replace the hosted MCP OAuth login with a raw CLI access token. [MCP PR36](https://github.com/fulcradynamics/fulcra-context-mcp/pull/36), merged September 22, documents that the hosted service issues its own opaque tokens and stdio reads separate local CLI credentials. [PR32](https://github.com/fulcradynamics/fulcra-context-mcp/pull/32), September 17, reports real stdio tests but explicitly leaves hosted sign-in and token-refresh coverage incomplete. Transport reachability, local stdio acceptance, and browser OAuth acceptance remain different checks.

### Svelte app template: supported Vercel route without callback registration

**Explicit template documentation.** The Svelte template's README directly supports Vercel previews: import Git repo, set `PUBLIC_AUTH0_DOMAIN`, `PUBLIC_AUTH0_CLIENT_ID`, `PUBLIC_FULCRA_API_ENDPOINT`, then automatic push deployments; or use `vercel login`, `vercel link`, `vercel env add <name>`, `vercel deploy` (preview), `vercel deploy --prod` (production). The API endpoint must be externally reachable. Device-flow login and logout without a `returnTo` mean the template's dashboard login needs no callback URL allowlist. This applies to the dashboard's device flow, **not the MCP gateway authorization-code flow**. [Template deployment guidance](https://github.com/fulcradynamics/app-template-svelte/blob/613a3d817df7933e73b6fb9cbda86fd7377b8e6b/README.md#L44-L91).

The template defaults to `adapter-auto`, detecting supported platforms. AICQ currently uses `adapter-node` for the authenticated local baseline, so a Vercel deployment is not automatically equivalent to importing the original template; it needs the appropriate adapter/build check. Self-hosted Node/Docker is explicitly supported via `adapter-node`, `npm run build`, `node build`. [Template adapters](https://github.com/fulcradynamics/app-template-svelte/blob/613a3d817df7933e73b6fb9cbda86fd7377b8e6b/README.md#L44-L73).

A new related **proposal**, not a verified deployment facility, exists: [Infrastructure PR166](https://github.com/fulcradynamics/infrastructure/pull/166), opened September 30 and still unmerged at research time, wires dev user-service to a Vercel team, domain `my.devfulcra.com`, and Secret Manager `dev-vercel-api-token`; it depends on [terraform-modules PR33](https://github.com/fulcradynamics/terraform-modules/pull/33), with production handled separately by [PR168](https://github.com/fulcradynamics/infrastructure/pull/168). Its body says nothing applied. This is about user-service provisioning Vercel projects and issuing project-scoped tokens, not proof a ready AICQ environment exists. Follow [Linear PLAT-487](https://linear.app/fulcradynamics/issue/PLAT-487/infrastructure-add-vercel-credential-secrets-to-user-service) for current status.

### Local platform tests are a different tool

`fulcra-platform-local` documents Docker/Compose, Tilt, GitHub organization/SSH access, Google Cloud SDK/private Artifact Registry auth, DuckDB, and uv. Environment settings are supplied from the named **fulcra-platform-local Environment Variables** item in the 1Password eng vault. `tilt up` clones services and starts the local stack; `uv run python -m pytest -vvv` runs its integration suite. [README](https://github.com/fulcradynamics/fulcra-platform-local/blob/21a094deb40671d12db97cbee9a006b95068fa77/README.md).

These tests bypass Auth0 by creating local users directly. Ingestion requires matching pre-provisioned KMS keys, and fixtures write to a shared development GCS bucket. The README explicitly tells developers to assert per-run records rather than count accumulated shared data. AICQ does not need the entire platform merely to exercise its real-account MCP/API calls, and bypassed-auth tests cannot satisfy M2's fresh-account browser OAuth gate. [Integration-test guidance](https://github.com/fulcradynamics/fulcra-platform-local/blob/21a094deb40671d12db97cbee9a006b95068fa77/test/README.md).

### Infrastructure change process and remaining prerequisites

The current infrastructure README points to `tf/` as OpenTofu/Terragrunt managed by Atlantis; `terraform/` is legacy. Configuration changes go through a GitHub PR, automatic plans, approval, and apply by an `eng` member. Promotable service modules live in `terraform-modules`, referenced by immutable commit SHA. State is in GCS; secrets are SOPS/GCP-KMS-encrypted. GitHub organization config and organization-level GCP project setup have separate manual-human rules; do not confuse a service PR with authorization to create projects or alter org membership. [Current infra overview](https://github.com/fulcradynamics/infrastructure/blob/4f26f9560299a177129d56932739cb6e83c00bde/README.md), [change process](https://github.com/fulcradynamics/infrastructure/blob/4f26f9560299a177129d56932739cb6e83c00bde/tf/README.md), [GitHub manual rules](https://github.com/fulcradynamics/infrastructure/blob/4f26f9560299a177129d56932739cb6e83c00bde/tf/github/README.md), [GCP project rules](https://github.com/fulcradynamics/infrastructure/blob/4f26f9560299a177129d56932739cb6e83c00bde/tf/gcp-projects/README.md).

## Findings from Nuclino

Authenticated through Fulcra's Google SAML SSO using the work account. Engineering Wiki's [Build & Deployment Process](https://app.nuclino.com/Fulcra-Dynamics/Engineering-Wiki/Build-Deployment-Process-7848f821-84af-4d1c-9229-0516aa1ce8eb) describes commit/tag Cloud Build triggers, SHA/release-tagged Artifact Registry images, and PubSub-triggered deployments in each environment's GCP project. Targets are typically Cloud Run or Container-Optimized VMs. It links the legacy `terraform/artifacts/cloudbuild.tf` path. This remains useful architectural background and matches MCP's older pipeline; current Portal/input-service source and successful runs establish their newer GitHub Actions process. Nuclino is not a universal current command guide.

The [August24 template plan](https://app.nuclino.com/Fulcra-Dynamics/Engineering-Wiki/Week-of-2026-08-24-9c7369d3-bbe0-4f80-9f56-be426cee18c1) explicitly proposed separate dev/prod Auth0 apps, a Svelte template, and deployment scripts. It is labelled WIP. Its browser-only/static-hosting idea applies to dashboard code, not AICQ's Python gateway. Full-content searches for dev and preview did not reveal an engineering PR-preview runbook; the direct source is Josh's Slack announcement below.

## Findings from Linear

| Item | Observed state | What it establishes |
|---|---|---|
| [PLAT-460](https://linear.app/fulcradynamics/issue/PLAT-460/dont-reply-to-deploy-comments-in-github-pull-requests) | Done | Josh explicitly says surface repositories let eng members build/deploy using `/gcbrun`, `/deploy`, `/preview`; bots should not acknowledge those commands. Each repository's workflow owns their precise behavior. |
| [PLAT-319](https://linear.app/fulcradynamics/issue/PLAT-319/post-an-ephemeral-preview-url-on-every-coder-loop-pull-request-and-its) | Backlog | Broader automatic preview URL posting on coder-loop PRs/issues remains incomplete. Its September18 description predates Portal's merged workflow. |
| [PLAT-203](https://linear.app/fulcradynamics/issue/PLAT-203/eng-unblock-ephemeral-environment-deploy-for-portal-review) | In Progress, possibly-done label | Records Greg's September14 branch-length deployment blocker. This older issue is not evidence that the September24 numeric PR-tag workflow remains broken. |
| [PLAT-464](https://linear.app/fulcradynamics/issue/PLAT-464/app-starter-skill-create-vercel-account) | Done | App-starter guidance now requires authenticated Vercel CLI rather than relying on anonymous short-lived deployments. |
| [PLAT-473](https://linear.app/fulcradynamics/issue/PLAT-473/set-up-vercel-deployment-to-a-fulcra-domain) | In Progress | Fulcra-managed Vercel apps/domains are an active intended product capability. |
| [PLAT-485](https://linear.app/fulcradynamics/issue/PLAT-485/user-service-add-endpoints-to-create-deploy-projects-and-get-access) | In Review | Proposed project CRUD and fresh one-day project-scoped tokens under `/user/v1/deploy`. [user-service PR129](https://github.com/fulcradynamics/user-service/pull/129) is open, not merged, at this research pass. |
| [PLAT-487](https://linear.app/fulcradynamics/issue/PLAT-487/infrastructure-add-vercel-credential-secrets-to-user-service) | In Review | Vercel credential/Cloud Run wiring is pending. Leif's September30 comment distinguishes mocked tests/draft artifacts from rollout and lists missing activation prerequisites. |
| [PLAT-533](https://linear.app/fulcradynamics/issue/PLAT-533/infrastructure-set-up-ns-records-for-myfulcraai-to-point-to-vercel) | In Review in Linear | Source evidence is newer than this status: [infra PR167](https://github.com/fulcradynamics/infrastructure/pull/167) merged October1 and its [Atlantis apply receipt](https://github.com/fulcradynamics/infrastructure/pull/167#issuecomment-5941027931) records successful `my.devfulcra.com` NS delegation to Vercel. Live DNS resolution and production delegation were not checked. |

PLAT-485 proposes `<name>.<userid>.<domain>` and ownership checks on each project route. These are proposed API contracts, not callable endpoints verified here. DNS success cannot stand in for merged/provisioned service integration.

## Findings from Slack #eng

Read the authenticated native Slack workspace, focused on `in:eng preview` and `in:eng vercel`, expanding the relevant message and opening the current POC thread. No messages, reactions, or deployment commands were sent.

- **Josh, September23, 21:18 ET:** [direct preview runbook](https://fulcradynamics.slack.com/archives/C032WJQ63B2/p1790212698647689). On Portal PRs, `/deploy dev` puts the latest PR image on `context.devfulcra.com`; `/preview dev` or `/preview prod` creates a tagged dev-portal deployment with its own URL. Tags are cleaned up when the PR closes. This matches current code and successful October1 runs.
- **Josh, September23, 19:30 ET:** [infrastructure announcement](https://fulcradynamics.slack.com/archives/C032WJQ63B2/p1790206228649069) links infra PR161 and explains public dev Cloud Run access is for tagged previews.
- **Leif, October1, 15:19 ET:** [Vercel POC discussion](https://fulcradynamics.slack.com/archives/C032WJQ63B2/p1790882395426609?thread_ts=1790881863.990349). Leif and Greg had a local deployment POC and draft PRs and asked Brandon/Josh to discuss the setup. The thread has one reply containing that request; it does not establish completed rollout.

## Concrete next work and limits

1. Check the exact pinned gateway's upstream configuration against the production MCP client ID/tenant/audience already recorded in source. Test a normal local browser code exchange and refresh with separately authenticated principals. No infrastructure mutation is inherently required for the already-listed loopback URI, but live tenant state remains unverified.
2. Prepare a bounded dedicated AICQ dev-service proposal for Josh: image/build workflow, GitHub repository/environment federation, browser-reachable HTTPS origin/callback, authenticated MCP route, durable private state, listening host/port, and explicit owner/test-account API environment. Reuse the patterns above and record state/restart/multiple-instance requirements before deployment.
3. Verify whether Fulcra-managed Vercel provisioning has merged and activated before choosing it for the dashboard. A direct authenticated Vercel deployment is separately documented, but no Vercel credentials or deployment rights were checked here.
4. After prerequisites are real, run the earliest incomplete milestone through the recorded roles and required live acceptance. Preserve the remaining retry until then. A different host does not prove OAuth correctness or ChatGPT rendering.

This spike verified source/configuration, merged/applied receipts, and successful workflow metadata. It did not inspect GCP live resources, Auth0 live admin state, preview-page runtime behavior, or Vercel token values. No new provider account, org permission, service, public endpoint, or harness event was created. Source publication and infrastructure application remain separate later actions.
