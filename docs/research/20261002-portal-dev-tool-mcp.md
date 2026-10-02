# Is portal-dev-tool the right model for an MCP dev helper?

Research date: October 2, 2026. Read-only inspection of toolkit commit `45a718dfe34f44da66dacf848106afc89acf3503` and Portal commit `ac40b9b7e9c85af370d309504104ba22ca038418`. No cloud commands, deployments, credentials retrieval, or configuration changes were performed.

## Answer

**Yes. `portal-dev-tool` is a much closer model for a minimal manual MCP deployment helper than the full GitHub preview controller.** It is a small operator script that deploys an existing container image through normal authenticated `gcloud`. Adapting the helper does not require implementing GitHub federation, a new CI pipeline, or general PR-preview automation first.

It is still a **Cloud Run** helper, not a VM launcher. The script's simplicity reduces deployment orchestration work; it does not solve the MCP gateway's callback configuration, durable credential storage, or process-local OAuth transactions. A single-process VM remains a different option if the intent is to preserve those runtime assumptions for initial testing.

## What the helper actually does

The [README](https://github.com/fulcradynamics/fulcra-toolkit/blob/45a718dfe34f44da66dacf848106afc89acf3503/portal-dev-tool/README.md#L1-L11) documents `deploy`, `list`, `delete`, and `list-tags`. The script's actual deploy interface is:

```text
portal-dev.sh deploy <image-tag> [prod|dev]
```

Missing the optional selector chooses **production API/Auth0 configuration**, although the Cloud Run service is created in the **dev** GCP project. Explicit `dev` selects the dev tenant/API. This separation matters for testing accounts and data. [Selector and config](https://github.com/fulcradynamics/fulcra-toolkit/blob/45a718dfe34f44da66dacf848106afc89acf3503/portal-dev-tool/portal-dev.sh#L3-L14), [default selection](https://github.com/fulcradynamics/fulcra-toolkit/blob/45a718dfe34f44da66dacf848106afc89acf3503/portal-dev-tool/portal-dev.sh#L31-L45).

It creates a service named `portal-<image-tag-suffix>`, truncating the suffix to 56 characters and removing a final dash. The full, untruncated tag still selects the container image. It calls `gcloud run deploy` with `--ingress=all`, `--allow-unauthenticated`, the image tag, a `pull_request` label, region `us-west1`, and a complete Portal environment-variable list. [Deploy implementation](https://github.com/fulcradynamics/fulcra-toolkit/blob/45a718dfe34f44da66dacf848106afc89acf3503/portal-dev-tool/portal-dev.sh#L47-L63).

Here `--allow-unauthenticated` is the Cloud Run invocation policy. It does not mean the application's Fulcra account checks disappear. An MCP equivalent must retain application OAuth and account isolation while making discovery and the service endpoint reachable by external MCP clients.

There is no `--tag` or `--no-traffic` in this script: it creates separate services per image-derived name. A new image tag generally gives a new service/origin; redeploying the same service name updates that service. This is different from Portal's newer GitHub previews, which put `pr-<number>` tags on revisions of one `dev-portal` service. The helper does not extract or persist the returned service URL, create a custom DNS record, register an Auth0 callback, or configure TLS explicitly. The HTTPS service URL comes from Cloud Run, not a Fulcra-domain provisioner. Google documents a permanent service URL that survives revision changes and automatic HTTPS/TLS, so a deliberately stable MCP service name can be tested without custom DNS initially. A service in a Fulcra-owned GCP project and a Fulcra-branded hostname are different claims; the latter is an optional mapping. These Google sources were verified during this spike. [Service URLs](https://docs.cloud.google.com/run/docs/managing/services), [automatic HTTPS](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run).

`list-tags` enumerates already published PR images from the Portal Artifact Registry path; the helper does not build, test, or publish an image. `list` filters dev-project services by the `pull_request` label; `delete` deletes the supplied service. Unlike deployment, list/delete omit an explicit region. Cleanup is manual; no close-PR hook, revision/image/state retention policy, or protected service allowlist is implemented. [Management commands](https://github.com/fulcradynamics/fulcra-toolkit/blob/45a718dfe34f44da66dacf848106afc89acf3503/portal-dev-tool/portal-dev.sh#L67-L108).

## Prerequisites and what is Portal-specific

The script requires `bash`, `gcloud`, normal operator authentication, and `jq` for listing tags. The operator must already have appropriate dev-project deployment/invocation-policy permissions and access to the existing image in `fulcra-artifacts`. The script neither provisions these permissions nor checks active engineering team membership. Its README does not document an exact minimal IAM role set; current live operator access was not checked.

The hardcoded Portal image path, service-name prefix, `PUBLIC_*` Auth0/API variables, Intercom ID, and `PORTAL_INSTANCE` are frontend-specific. An MCP helper would substitute:

- MCP image path and a deliberate test service name, preferably a stable name for the first test endpoint.
- `FULCRA_ENVIRONMENT` selecting HTTP mode, externally correct `OIDC_SERVER_URL`, upstream `OIDC_CLIENT_ID`, `FULCRA_OIDC_DOMAIN`, and `FULCRA_API`.
- Explicit server listening/port settings, protected persistent `STATE_PATH`, runtime identity and storage policy.
- The selected host origin's allowed upstream Auth0 callback, with matching issuer/resource metadata.

A stable test service name avoids generating a new callback/installation origin for every image tag. Its actual service URL must be known and configured before authenticated testing; merely substituting the image path leaves the gateway advertising an incorrect issuer/callback. The current helper supplies no durable volume or transaction storage; those remain runtime requirements.

## Compared with the GitHub `/preview` controller

| Manual toolkit helper | Portal GitHub controller |
|---|---|
| Operator runs authenticated gcloud locally | Trusted default-branch comment workflow with eng membership gate and federated authentication |
| Caller supplies an image tag; no CI check | Resolves current PR-head SHA and requires its successful CI run |
| Deploys movable tag directly | Resolves tag to digest, deploys digest, records full source SHA |
| Separate service per image-derived name | Tagged no-traffic revision on existing dev preview service |
| Config selected locally, defaults production backend | Explicit target/config GitHub environments |
| Manual list/delete | GitHub deployment receipt and PR-close cleanup |

The controller is stronger reusable CI/CD machinery, but its public-repository federation issue does **not** block a separately authorized manual operator deployment. That distinction makes the first hosting experiment smaller than the earlier full automation proposal. [Controller authorization/target](https://github.com/fulcradynamics/portal/blob/ac40b9b7e9c85af370d309504104ba22ca038418/.github/workflows/deploy.yml#L31-L113), [CI/digest gate](https://github.com/fulcradynamics/portal/blob/ac40b9b7e9c85af370d309504104ba22ca038418/.github/workflows/deploy.yml#L190-L245), [tagged deploy and receipt](https://github.com/fulcradynamics/portal/blob/ac40b9b7e9c85af370d309504104ba22ca038418/.github/workflows/deploy.yml#L250-L297).

## Minimal next step

For a **Cloud Run experiment**, adapt a small manual helper to deploy a known tested MCP image by digest to one dedicated stable test service, using existing operator access. Arrange callback/base URL and isolated durable state, then verify real linking and a tool call. Keep the full CI/CD migration as a subsequent reusable improvement. Do not claim a cap of one instance makes process-local login state durable or guarantees every OAuth request reaches the same process.

For a **VM experiment**, use Leif's agent-playground creation/access recipe and a stable HTTPS origin, then run one MCP process with a real persistent local state directory. `portal-dev-tool` is a useful interface model, but its commands and runtime are not the VM implementation.

No choice was implemented in this spike. The user's “perhaps easier” intuition is supported for manual deployment orchestration; the remaining OAuth/runtime checks determine whether Cloud Run or a dedicated VM is the quickest successful first test.
