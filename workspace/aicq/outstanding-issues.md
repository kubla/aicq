# Outstanding issues

## M1 local baseline

No blocking M1 issue remains. Owner and authenticated non-owner checks passed;
see history/20261001_m1-local-baseline.md. Compatible dependency updates cleared
high-severity audit findings. Four low-severity transitive cookie findings remain
in the current SvelteKit/adapter chain; no forced major upgrade was made.

## M2 local ChatGPT connectivity

Secure MCP Tunnel access, runtime credentials, target workspace association, and
browser OAuth reachability require live validation in M2. No AICQ plugin is
installed or linked yet. If the infrastructure seam becomes substantially
complicated, preserve the specific blocker for Josh/GCP.

## GitHub source publication

Earlier cloud Git push failed with HTTP 401; Git Data API publication succeeded.
The local M1 source candidate is committed but not published. Current local
Git push capability has not been retested. Preserve private repository visibility.

## Later acceptance gates

Two-owner mailbox behavior, third-owner isolation, useful work/artifact exchanges,
client switching, and actual ChatGPT Events remain unverified later milestones.
The protocol prerequisite 429da58 is separate from Events implementation.

Earlier repository-creation and SDK-migration issues were resolved as documented
in history/20261002_github-access.md and history/20261002_mcp2-readiness.md.
