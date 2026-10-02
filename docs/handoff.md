# Local execution handoff

Purpose: let a locally running Codex, Claude Code, or another compatible harness
continue the AICQ project from recorded state. No laptop connection has been
configured and no subagents have been started on the user's computer.

## Transfer

Obtain the repository once published, or a source archive prepared from this local
checkout. Do not include CLI credential stores or runtime secret files. Open the
project in the destination harness and read root `AGENTS.md` before making changes.
Authenticate that client separately to Fulcra, then read `workspace/aicq/` to obtain
the current decisions, spec, plan, progress, workboard, and relevant history.

Check out the recorded revision, inspect unfinished changes and blockers, and resume
the earliest incomplete milestone. Use actual source and test evidence to reconcile
state. The new agent does not automatically inherit this conversation or its secrets.

## Current checkpoint

- Product and implementation organization are documented; no app milestone has begun.
- Local git repository initialized; the user created private `kubla/aicq`.
- GitHub CLI browser authorization completed as kubla, but subsequent REST repository
  creation still returned HTTP 403 `Resource not accessible by integration`.
  Subsequent branch creation/deletion, initial AICQ content writing, and issue
  creation succeeded. Standard Git push failed with HTTP 401; use the verified
  GitHub API publication path until that transport is resolved.
- Local-first hosting was selected. Evaluate OpenAI Secure MCP Tunnel and OAuth
  reachability at the integration gate; defer substantial infrastructure to Josh/GCP.
- Existing Fulcra planning authentication and harness annotation are available here.
  The destination client must authenticate separately.
- The separate Fulcra MCP fork has the tested protocol prerequisite; Events are pending.

Remote command access would require an explicitly configured and authorized
connection to the laptop. Running a local harness from this checkpoint is a separate
execution path; spawning a subagent here continues to use this workspace.
