# Fulcra VM hosting for a single-process MCP development server

Research date: October 2, 2026. Read-only GitHub research and authenticated #eng inspection. No VM was created, no credentials or environment files were opened, and no network or access configuration was changed. Research records were saved in the repository and canonical Fulcra workspace.

## Finding

**Yes: Fulcra has an actual developer VM launch recipe, not merely hypothetical Terraform modules.** Leif's agent-playground GCP project and reusable Hermes machine image provide a concrete precedent for creating a VM, connecting by SSH, and running an agent manually. The newer Shell Beach toolkit generates similar commands for Discord workers. This is the strongest starting point for asking Josh for a small, single-process AICQ MCP development host.

It is **not yet evidence of a self-service public HTTPS app-hosting facility**. The checked recipe supplies a VM image, project/zone, SSH workflow, and limited lifetime. No source or observed host in this pass establishes an available clean AICQ machine, reserved IP, Fulcra hostname, TLS, or MCP callback registration. Those are a smaller, concrete infrastructure request rather than a reason to rebuild the service for Cloud Run first.

## Operational precedent: Leif's agent playground

Authenticated Slack inspection found:

- [April 14 #eng](https://fulcradynamics.slack.com/archives/C032WJQ63B2/p1776182992217399): Leif created the actual `fulcra-agent-playground-spfvm7` project and added `gcp-developers@fulcradynamics.com` as owner. This is observed historical operator reporting, not a check of today's live IAM.
- [August 10 #eng](https://fulcradynamics.slack.com/archives/C032WJQ63B2/p1786406214018279): Leif supplied a blank Hermes machine image and a VM creation recipe, followed by SSH as `fulcra` and `hermes model; hermes`. The VM shuts down after 24 hours.
- [August 27 updated recipe](https://fulcradynamics.slack.com/archives/C032WJQ63B2/p1787861257791929?thread_ts=1787850241.097499): uses image `fulcra-hermes-installed-20260818` and `--max-run-duration=1d`.
- [May 8 #eng](https://fulcradynamics.slack.com/archives/C032WJQ63B2/p1778281683740219?thread_ts=1778279145.529639): agent VMs have external IPs; this does not establish a stable hostname.

The August 10 example was:

```sh
gcloud --project=fulcra-agent-playground-spfvm7 compute instances create \
  --no-service-account --no-scopes --zone=us-central1-a \
  --source-machine-image=fulcra-hermes-installed-20260810 \
  fulcra-hermes-installed-$(date "+%Y%m%d-%H%M%S")
```

This is documentation of an existing recipe, **not a command executed in this spike**. Before reusing it, select the currently maintained image and confirm its shutdown policy, disk lifecycle, running gateways/bots, SSH identity, and absence of inherited credentials. `--no-service-account --no-scopes` is part of the recorded operator recipe; it does not sanitize whatever application credentials may already exist in a machine image.

GitHub confirms the project history: [Infrastructure PR109](https://github.com/fulcradynamics/infrastructure/pull/109) is a **closed, unmerged draft**, not an applied stack. Its proposed project identifier differs from the actual project. The [April 14 maintainer comment](https://github.com/fulcradynamics/infrastructure/pull/109#issuecomment-4246175365) explicitly says the `fulcra-agent-playground-spfvm7` project was created manually instead. Current source search found no agent-playground stack in infrastructure main `4f26f9560299a177129d56932739cb6e83c00bde`. Do not substitute the separate `fulcra-ai` project merely because its name sounds similar.

## Newer operator tooling: Shell Beach

[Toolkit PR6](https://github.com/fulcradynamics/fulcra-toolkit/pull/6), “[PLAT-513] Add deploy-instance worker script”, merged September 29, 2026. Current toolkit main is `45a718dfe34f44da66dacf848106afc89acf3503`. Its Shell Beach README describes scripts for managing Fulcra worker bots.

The helper reads operator-supplied `GCLOUD_PROJECT`, `GCLOUD_ZONE`, `GCLOUD_SOURCE_MACHINE_IMAGE`, `GCLOUD_INSTANCE_NAME_PREFIX`, and Discord guild/channel configuration. It produces:

```text
gcloud compute instances create <prefix-name-timestamp>
  --project=<configured-project>
  --zone=<configured-zone>
  --source-machine-image=<configured-image>
  --max-run-duration=<days>d
  --no-service-account
  --no-scopes
  --metadata=DYNAMIC_CHANNEL_ID=<channel>
```

**It prints the command; it does not create the VM.** The printed “SUCCESS!” is not deployment evidence. The source imports `check_call` but never calls it. It neither provisions a hostname nor installs TLS, an HTTP reverse proxy, or an MCP server. Its exact live image/project defaults were not read from environment files. [Configuration inputs](https://github.com/fulcradynamics/fulcra-toolkit/blob/45a718dfe34f44da66dacf848106afc89acf3503/shell-beach/deploy-instance.py#L12-L18), [command generation and printing](https://github.com/fulcradynamics/fulcra-toolkit/blob/45a718dfe34f44da66dacf848106afc89acf3503/shell-beach/deploy-instance.py#L51-L78).

The earlier [Discord Manager README](https://github.com/fulcradynamics/fulcra-toolkit/blob/45a718dfe34f44da66dacf848106afc89acf3503/fulcra-discord-manager/README.md) documents a related workflow that creates private Discord channels/roles, sends a welcome message, and prints the VM command. That messaging workflow is unnecessary for an MCP development server and was not executed. [PLAT-513](https://linear.app/fulcradynamics/issue/PLAT-513/create-a-deployment-script-for-worker-bots) tracks the newer helper; [PLAT-472](https://linear.app/fulcradynamics/issue/PLAT-472/update-worker-vm-images-to-store-persistent-knowledge-and-preferences) concerns worker-image durable context.

## Existing VM definitions: relevant precedent, not available app hosts

| Source | What it provides | Why it is not proof of a ready AICQ host |
|---|---|---|
| `terraform/modules/stateful_vm` | Single Container-Optimized OS VM managed by a stateful group, persistent data disk, Docker startup | Legacy module; a container/image-oriented service recipe, not a currently documented generic developer VM instance |
| `terraform/modules/vm_service` | One-instance managed group, OS Login, container declaration, runtime account | Replaceable VM service; source does not supply a generic dev hostname or persistent MCP credential disk |
| `terraform/modules/unmanaged_vm_service` | Managed group with ignored version changes and configurable target size | Despite its name, still a group/template facility; no inspected deployment instructions for AICQ |
| Current `jumpbox` stacks | Ubuntu VM, persistent home disk, developer admin login | Database/network access host; do not turn a shared bastion into a public experimental application |
| Current Atlantis VM | One NixOS appliance VM group and load-balanced application | Special-purpose infrastructure control plane with privileged identity; unsuitable to commandeer for AICQ |

The legacy `stateful_vm` README explicitly mounts a persistent disk at `/mnt/disks/data`, presented inside its container at `/data` or a configured path. Its compute source enables OS Login and conditionally attaches a configured public IP; cloud-init pulls a container, uses host networking, and starts it with `--restart=always`. This provides a useful design precedent for keeping OAuth state on a real local persistent filesystem rather than GCS FUSE. It still requires a reviewed host/network/bootstrap choice. [README](https://github.com/fulcradynamics/infrastructure/blob/4f26f9560299a177129d56932739cb6e83c00bde/terraform/modules/stateful_vm/README.md#L1-L6), [network/OS Login](https://github.com/fulcradynamics/infrastructure/blob/4f26f9560299a177129d56932739cb6e83c00bde/terraform/modules/stateful_vm/compute.tf#L124-L153), [Docker bootstrap](https://github.com/fulcradynamics/infrastructure/blob/4f26f9560299a177129d56932739cb6e83c00bde/terraform/modules/stateful_vm/cloud-init.tf#L4-L38).

The module is in the repository's explicitly **legacy** `terraform/` tree. Its compute file last changed in March 2023; cloud-init changed January 2025. Current `terraform-modules` main contains `jumpbox`, but no corresponding generic `stateful_vm`/`vm_service` modules were found in its tree. These are reference options, not the strongest current operational lead. [Current infrastructure layout](https://github.com/fulcradynamics/infrastructure/blob/4f26f9560299a177129d56932739cb6e83c00bde/README.md#L1-L5), [compute maintenance commit](https://github.com/fulcradynamics/infrastructure/commit/c0c09a572ba2b7d9514236a7dd96404211c69ecd), [cloud-init maintenance commit](https://github.com/fulcradynamics/infrastructure/commit/7a3a5ae0762fc156b48c9c2ffe153c23f8aa87d3).

The dev jumpbox stack configures `e2-small`, zone `us-west1-a`, developer group access, and PostgreSQL/jq packages, pinned to `jumpbox` commit `d9920b90e85b41cc3a20f30454e5f9f9a9c18b2e`. That module enables OS Login and grants configured users `roles/compute.osAdminLogin`; its network interface has no public `access_config`. This is developer access to an internal utility host, not public MCP hosting. [Dev stack](https://github.com/fulcradynamics/infrastructure/blob/4f26f9560299a177129d56932739cb6e83c00bde/tf/dev/jumpbox/terragrunt.hcl#L5-L22), [pinned network and login grants](https://github.com/fulcradynamics/terraform-modules/blob/d9920b90e85b41cc3a20f30454e5f9f9a9c18b2e/jumpbox/main.tf#L71-L107).

Atlantis's current stack manages its own NixOS appliance VM and explicitly cannot apply itself under Atlantis. Its backend uses IAP for the control interface, with a separate webhook backend. These establish Fulcra's ability to operate VM-backed services, not permission to host AICQ there. [Appliance README](https://github.com/fulcradynamics/infrastructure/blob/4f26f9560299a177129d56932739cb6e83c00bde/tf/ops/atlantis/README.md), [VM/backend definitions](https://github.com/fulcradynamics/infrastructure/blob/4f26f9560299a177129d56932739cb6e83c00bde/tf/ops/atlantis/main.tf#L45-L148).

## Applying the precedent to AICQ

A manually deployed **one-process server on one dedicated VM** can avoid the immediate cross-instance OAuth state problem and the public-repository GHA federation obstacle. It does not make pending login transactions durable across a process restart, and it does not replace M2's real account, refresh/reconnect, and host acceptance tests.

The narrow request to Josh/Leif should identify:

1. The current agent-playground VM creation/access method and suitable clean image, or a small Ubuntu VM equivalent; confirm actual permissions through normal authentication.
2. A dedicated instance and protected persistent data path for AICQ, rather than a borrowed Hermes bot, jumpbox, or infrastructure appliance.
3. An externally reachable HTTPS origin under an approved Fulcra domain, with reserved-address/routing, firewall and TLS ownership. A raw ephemeral IP is not the complete MCP/OAuth endpoint.
4. An upstream Fulcra Auth0 client with that callback allowed; configure MCP issuer/resource/base URL to the same external origin.
5. A clear shutdown/expiration policy so the documented 24-hour worker defaults do not silently stop an intended development service.

AICQ code and tools may then be installed manually or by a small reviewed script, without waiting for generalized PR previews or multi-instance provider redesign. Prefer this as a development experiment before claiming a final reusable CI/CD design. This research did not execute that bootstrap, inspect live project IAM, reserve an address, verify an existing service, or expose a listener.

## Fulcra hostname routing

Fulcra manages the `devfulcra.com` zone in Google Cloud DNS; the DNS provider uses project `fulcra-dns` and its infrastructure-manager account. This is an existing place to define a Fulcra-owned development hostname. The `my.devfulcra.com` subtree is delegated to Vercel, so a direct VM experiment should request a separately approved name outside that subtree. For example, `aicq-dev.devfulcra.com` is a proposed name, not an allocated or verified endpoint. [Zone and delegation](https://github.com/fulcradynamics/infrastructure/blob/4f26f9560299a177129d56932739cb6e83c00bde/tf/dns/devfulcra.com.tf#L1-L20), [DNS project/provider](https://github.com/fulcradynamics/infrastructure/blob/4f26f9560299a177129d56932739cb6e83c00bde/tf/dns/providers.tf#L10-L14).

Existing service infrastructure can create owned-domain A/AAAA records to a load balancer, provision a managed certificate, and attach it to a certificate map. The newer certificate module accepts the domain, zone, DNS project and load-balancer addresses explicitly. That establishes a reusable DNS/TLS pattern, not an automatic binding between a playground VM and a hostname. [Certificate DNS](https://github.com/fulcradynamics/terraform-modules/blob/70cd3cf04c36ae768057b9f76b59a71e0d44ea2c/load-balancer-certificate/dns.tf#L1-L29), [managed certificate/map entry](https://github.com/fulcradynamics/terraform-modules/blob/70cd3cf04c36ae768057b9f76b59a71e0d44ea2c/load-balancer-certificate/certificates.tf#L12-L32), [parameters](https://github.com/fulcradynamics/terraform-modules/blob/70cd3cf04c36ae768057b9f76b59a71e0d44ea2c/load-balancer-certificate/variables.tf).

For a small manual experiment, the proposal is a dedicated playground VM with stable addressing and a DNS record, plus HTTPS terminated either by a reverse proxy on that VM or approved existing load-balancer routing. Which approach fits the actual playground network/firewall remains unverified. The MCP process can retain loopback binding behind a same-host proxy, with issuer/resource URLs set to the external HTTPS origin.

Once that HTTPS endpoint exists, adding its exact `/callback` URL to the appropriate upstream Fulcra OAuth client's allowlist can be a small independent change. The callback entry does not itself allocate the VM, reserve an address, configure DNS/TLS, or authorize the executing client to provision resources. No self-service DNS/TLS facility was found in the VM helper or launch recipe. The current launch-image availability, operator permissions, billing and live network state were not checked.
