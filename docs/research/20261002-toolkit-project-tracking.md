# Where Fulcra toolkit deployment helpers are tracked

Research date: 2026-10-02. Scope: authenticated GitHub metadata, issue/PR records and file history, plus live Linear issues and project membership. The resulting Platform ticket PLAT-546 was created and read back. No deployment or external message was performed.

## Finding

The repository is a collection of developer utilities; it does not establish a single managed project for all its tools. The related work is tracked through **Platform (`PLAT`) Linear tickets and linked GitHub PRs**. A new MCP deployment-helper ticket can reasonably target this repository, but its Linear project should follow the actual Platform backlog/project decision rather than a similarly named project elsewhere.

The [repository metadata](https://github.com/fulcradynamics/fulcra-toolkit) describes it as “A collection of miscellanous utilities Fulcra developers may find useful.” The authenticated GitHub API reports `has_issues: true` and `has_projects: false`. On the research date, the all-state issues endpoint returned six records, all pull requests and no standalone GitHub issues. This is evidence of the observed tracking convention, not a rule prohibiting GitHub issues.

## Portal helper lineage

[Toolkit PR #2, “Add portal dev tool”](https://github.com/fulcradynamics/fulcra-toolkit/pull/2), was authored by [Leif Meyer (`lancelets`)](https://github.com/lancelets), opened September 18, 2026 and merged at 17:53:57 UTC that day. Its description explicitly imports the old `fulcradynamics/portal-dev-tool` repository as a directory because that repository was being archived, and adds image-tag truncation for Cloud Run's resource-name limit. The PR title contains no Linear identifier and the PR has no comments/linkback. The migration ticket must therefore be established through Linear, rather than inferred from this PR's title.

The import is recorded in [commit `2deed755`](https://github.com/fulcradynamics/fulcra-toolkit/commit/2deed75553102b4dfe812883a10ac9a10ffdb214): its Git subtree metadata identifies the original helper commit as `54267388d77282eac1e8fa3f9ba2498f2bf66908`. The [original repository](https://github.com/fulcradynamics/portal-dev-tool) is currently archived; its all-state GitHub issues endpoint returned no records. Its last push was November 19, 2024, so the helper predates the September 2026 toolkit migration.

[Infrastructure PR #149, “fulcra-toolkit: add github repo”](https://github.com/fulcradynamics/infrastructure/pull/149), also by Leif, merged September 18, 2026 at 18:04:58 UTC. This supplies the infrastructure-side repository setup lineage. Its body is empty and does not itself identify a Linear project.

The subsequent Portal-specific adjustment was [toolkit PR #5, “Update 'DEV_PUBLIC_FULCRA_API_ENDPOINT' to correct api URL”](https://github.com/fulcradynamics/fulcra-toolkit/pull/5), recorded in [commit `361e71d6`](https://github.com/fulcradynamics/fulcra-toolkit/commit/361e71d6276bf501d369e77413cfef79bea11528) on September 23, 2026. Its author handle is `gklei`. This is maintenance evidence, not proof of current ticket ownership.

## Worker helper lineage

The adjacent Discord/worker tooling carries explicit Platform ticket identifiers:

- [PR #1, “PLAT-259 Add fulcra discord manager”](https://github.com/fulcradynamics/fulcra-toolkit/pull/1), opened September 17, 2026 by Leif. Its description says the initial script sets up a Fulcra Hermes demo VM plus Discord channel, role and invite link.
- [PR #4, “[PLAT-396] Add Discord category support to channel creation”](https://github.com/fulcradynamics/fulcra-toolkit/pull/4), opened September 21, 2026 by Leif and still open when inspected. It adds `FULCRA_MANAGER_CATEGORY_ID` support.
- [PR #6, “[PLAT-513] Add deploy-instance worker script”](https://github.com/fulcradynamics/fulcra-toolkit/pull/6), opened September 28 and merged September 29, 2026, authored by Leif. The implementation is [commit `45a718df`](https://github.com/fulcradynamics/fulcra-toolkit/commit/45a718dfe34f44da66dacf848106afc89acf3503).

The [Linear bot comment on PR #6](https://github.com/fulcradynamics/fulcra-toolkit/pull/6#issuecomment-5900209490), posted September 29, 2026, explicitly links [PLAT-513, “Create a deployment script for worker bots”](https://linear.app/fulcradynamics/issue/PLAT-513/create-a-deployment-script-for-worker-bots), and [PLAT-472, “Update worker VM images to store persistent knowledge and preferences in Fulcra”](https://linear.app/fulcradynamics/issue/PLAT-472/update-worker-vm-images-to-store-persistent-knowledge-and-preferences). This is direct ticket lineage; the PR author alone is not proof of the ticket's current assignee or project.

## Bounded duplicate check

Authenticated GitHub issue searches on October 2, 2026 found no MCP manual deployment-helper issue in the searched scope:

- `org:fulcradynamics "MCP" "deploy" "helper"`: zero results.
- `org:fulcradynamics "MCP" "portal-dev"`: two incidental infrastructure PRs, concerning authentication and a dev load balancer, not a helper ticket.
- `repo:fulcradynamics/fulcra-toolkit "deploy"`: only worker-helper PR #6.
- `repo:fulcradynamics/fulcra-context-mcp "manual" "deploy"`: one unrelated authentication-challenge PR.

Linear searches for `fulcra-toolkit`, `portal-dev-tool`, `MCP deploy`, `+MCP +deployment`, and Platform issues matching `deploy` also found no matching manual MCP helper ticket. This is a bounded duplicate check, not proof of absence under every possible title.

## Live Linear confirmation and recommendation

The existing helper tickets establish a clear Platform team convention, without an owning Linear project:

| Ticket | Observed tracking | Evidence |
|---|---|---|
| [PLAT-338: Move portal-dev-tool script to fulcra-toolkit](https://linear.app/fulcradynamics/issue/PLAT-338/move-portal-dev-tool-script-to-fulcra-toolkit) | Platform, Done, Leif Meyer; no project or parent | Description links toolkit PR #2 and infrastructure PR #149 directly |
| [PLAT-513: Create a deployment script for worker bots](https://linear.app/fulcradynamics/issue/PLAT-513/create-a-deployment-script-for-worker-bots) | Platform, Done, Leif Meyer; no project; parent PLAT-472 | Description links toolkit PR #6 |
| [PLAT-472: Update worker VM images to store persistent knowledge and preferences in Fulcra](https://linear.app/fulcradynamics/issue/PLAT-472/update-worker-vm-images-to-store-persistent-knowledge-and-preferences) | Platform, Done, Leif Meyer; no project | Parent context for worker deployment and Fulcra workspace persistence |

[PLAT-319](https://linear.app/fulcradynamics/issue/PLAT-319) covers posting preview URLs on coder-loop PRs/issues in the **Company OS** project. That is adjacent automation work, not evidence that Company OS owns a manual Toolkit helper. [PLAT-214](https://linear.app/fulcradynamics/issue/PLAT-214) concerns automatic CLI/MCP runtime testing in **Establish release standards for published skills**, another distinct scope.

The **Fulcra Developer Plugins** project belongs to the Devs team, has no description or lead, and returned no issues when queried by both its name and UUID. No observed link connects it to these Toolkit helpers. The similarly broad **Backend** Platform project also supplies no evidence of helper ownership. Neither should be selected merely from its name.

Recommendation: use **Platform Backlog**, implementation repository **fulcra-toolkit**, and related links to PLAT-338 and PLAT-513. Leave project and assignee unset until the team chooses them. Existing assignments show Leif's contribution history, not a current commitment to build the new helper.

## Ticket created and verified

[PLAT-546: Toolkit: add a manual MCP development deployment helper](https://linear.app/fulcradynamics/issue/PLAT-546/toolkit-add-a-manual-mcp-development-deployment-helper) was created at 2026-10-02 16:50:54 UTC and read back through Linear. It is in Platform Backlog, unassigned, with no project or parent, and related to PLAT-338 and PLAT-513.

Its scope is a manual Cloud Run helper using normal operator credentials, a tested image digest, stable HTTPS service origin, explicit Fulcra/OAuth configuration and isolated persistent state. Acceptance requires actual linking, authenticated tool access, refresh/reconnect, restart identity and credential rejection evidence. Process-local login and multiple-instance limitations must be documented. Automated PR previews remain subsequent work. AICQ M2 remains incomplete; this ticket does not establish deployment or consume its final retry.
