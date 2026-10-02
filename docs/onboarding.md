# Invitation and first-use setup

Status: design proposal incorporating the user's clarification about post-signup
setup. No AICQ setup skill or bootstrap tool has been implemented or tested yet.

## User direction

> A freshly signed up user would need to issue the fulcra commands necessary to make new data rows or whatever; thIs can be done via MCP or CLI, either with instructions or an installable skill or plugin

Web signup and authorization establish the authenticated owner. AICQ then uses
ordinary authenticated Fulcra operations to initialize its application resources.
Do not invent a separate account-creation endpoint or assume that signup creates
AICQ contacts, message channels, artifacts, or subscriptions.

## Proposed recipient flow

1. The invitation introduces the inviter and a specific collaboration. Before
   recipient verification, show only an introduction approved for that preview.
2. The invitee installs AICQ and signs up or signs in through browser authorization.
   Preserve the invitation through setup; reopening its link resumes progress.
3. The packaged setup skill reads the authenticated owner identity and inspects
   any existing AICQ workspace. It creates missing application resources using
   MCP tools. Code-agent users can use the equivalent authenticated CLI workflow.
4. The recipient accepts the identified contact connection. The setup workflow
   creates a dedicated outbound channel and narrowly shares it with that peer.
   It also checks for the inviter's reciprocal share. Each owner's resources are
   created under that owner's credentials and authorization.
5. Read back the workspace manifest, channel metadata, and incoming/outgoing share
   scope. A write receipt alone does not establish a usable two-way connection.
6. Open the pending request in the recipient's agent session. Initial work runs
   with the recipient's direction. Optional Events subscriptions have their own
   supported setup and response policy.

Proposed visible progress: Signed in; Preparing your workspace; Connecting with
Bob; Ready. If one side is missing, report the specific pending step and provide
a resume action. Preserve created resources rather than restarting all setup.

## Existing primitives

Source inspection of the Fulcra MCP fork verifies these tool definitions:

- `get_user_info`, `get_data_catalog`, and `annotations_catalog` for discovery.
- `create_data_type(base_type="moment", ...)` and `record_data(..., note=...)`
  for a dedicated annotation outbox and serialized message envelopes.
- `list_files`, `read_file`, and `write_file` for a file-based workspace/mailbox.
- `create_share` and `list_shares` for narrowly scoped peer access and verification.
- `get_records` or file reads for content read-back.

These tools establish available building blocks, not verified fresh-account
onboarding. Choose annotation outboxes or shared-folder mailboxes after the
two-owner feasibility evaluation; the setup skill should follow the chosen schema.

## Resuming safely

The same authenticated owner can onboard from ChatGPT, Codex, or another compatible
harness. Reuse existing owner resources and contact connections, with separate
client authentication. Package the common setup workflow as a portable skill;
provide remote MCP configuration and CLI-backed instructions for other hosts.
UI and unattended execution are optional host integrations, not prerequisites
for sending, retrieving, replying, or continuing an exchange.

Keep a versioned owner-scoped manifest of actual resource IDs and completed setup
steps. Validate existing resources and peer permissions before reuse; names alone
do not establish the intended channel. Recover an uncertain create outcome before
retrying. A setup skill alone cannot guarantee atomic or exactly-once creation;
implementation must handle repeated runs and concurrent sessions explicitly.

Keep contact acceptance distinct from permission for unattended agent responses.
Connecting a peer exposes only the dedicated exchange, never unrelated records.
No step needs users to copy Fulcra IDs, type IDs, or handshakes by hand.

## Acceptance checks

Test a fresh account through its first useful reply, an existing account through
reuse, interrupted setup through resume, and repeated setup without duplicate
contacts or channels. Confirm both owners can inspect the exchange, a third owner
cannot retrieve it, and optional background work remains disabled until configured.
The starter's authenticated baseline and dashboard remain the first implementation
milestone; this document is planning, not a completed application milestone.
