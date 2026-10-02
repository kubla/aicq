# Decisions

## Initial project request

# Requirements and decisions

## User requirements

These are excerpts from the user's initial request, preserving their wording:

> I want to start a brand-new software project with the working title AICQ.

> It should work as a ChatGPT plugin: an in-ChatGPT app modeled on the glory days of ICQ instant messaging.

> The chat is for communicating with other agents, not other users.

> Agent-to-agent communication should be monitorable by the human users who own the agents involved.

> It should provide universal agent chat so that, while working on something with ChatGPT, a user can say, “Hey, share this with Alice’s agent,” and that just works. Alice can likewise share with Bob’s agent.

## User ideas under consideration

> My initial idea is to use an open-source Jabber/XMPP backend.

> However, we could use Fulcra for user authentication, account management, and everything except XMPP.

> We could even use Fulcra for messaging, which could elegantly handle agents not being online all the time.

Neither XMPP nor a Fulcra messaging backend has been selected by the user.
No framework, hosting provider, repository destination, or license has been selected.

## Follow-up direction

> I’m excited! The Fulcra MCP server is open source, so we can make a fork implementing MCP Events and if it’s great we can push it to main

Proceed with the Fulcra MCP Events contribution as the delivery foundation for
AICQ. Keep the contribution reusable by other Fulcra clients. Upstream inclusion
is conditional on quality and review; this does not authorize a direct main-branch
push now. Reuse the existing `kubla/fulcra-context-mcp` fork and prepare a separate
development branch.


## Fulcra sign-in

> Done

Context: the user completed browser authorization for the Fulcra CLI.

## Experience before messaging implementation

> but I want to reason backward from a great user experience

When asked which experience AICQ should optimize first:

> Both! It’s easy to put two agents in a chat room, so we gotta help agents exchange more than chat or it doesn’t offer a unique enough value prop

Decision: support both ongoing conversations and useful exchanges beyond chat.
The proposed review walkthrough is a design hypothesis, not approval of a storage
pattern, specific screens, schema, or additional implementation scope.

## Post-signup application setup

> A freshly signed up user would need to issue the fulcra commands necessary to make new data rows or whatever; thIs can be done via MCP or CLI, either with instructions or an installable skill or plugin

Context: browser signup establishes the user; authenticated commands initialize
AICQ-specific resources. MCP and CLI are available implementation paths. A
packaged onboarding skill, resume behavior, and concrete resource schema are
design proposals; no completed onboarding test is claimed.

## Client and harness support

> Good. For ChatGPT we’ll prefer the plugin, but we should support Codex and other agent harnesses as well

Decision: prefer the ChatGPT plugin and also support Codex and other compatible
agent harnesses. Keep core exchanges independent of ChatGPT-specific UI; validate
client integrations and background activation separately.

## Client experiment candidates

> Nice! On my computer I also have Claude, Claude Code, Hermes, Grok Bot, and Meta Muse to experiment with.

Context: these are available experiment candidates on the user's computer. They
have not been verified from this workspace or selected as mandatory release gates.

## Repository destination

> Private kubla/aicq (Recommended)

Context: the user selected this answer to the repository location/visibility
question. Create the new AICQ repository under kubla with private visibility.
The current GitHub integration rejected creation; no hosting choice was supplied.

## Local-first hosting

> Give me some advice here: if we can feasibly do this locally, let’s choose that. If something about that is very complicated, we can stop work until I can get help from Josh on a GCP setup for this

Direction: choose local-first development if feasible. If infrastructure becomes
substantially complicated, pause that work for the user's coordination with Josh
on GCP. This updates M1's target to a real local baseline and owner dashboard;
all authentication, isolation, recording, and evaluation criteria still apply.

## GitHub creation access

> Well I could do that but I’d rather give you the power to do it

Context: the user prefers enabling repository creation over creating the empty
repository manually. GitHub integration GraphQL and REST creation both failed.
A separate GitHub CLI browser authorization has been initiated; it is pending.

## GitHub CLI authorization completion

> Done

Context: the user completed the requested GitHub CLI browser authorization.
CLI authentication confirmed kubla; subsequent REST repository creation was
still rejected with HTTP 403. The authorization is complete, not pending.

## Explicit GitHub permission retry

> Got it. Wanna just try the gh auth again? It may be worth a retry

Context: the user requested another authorization attempt despite the earlier
denial. A CLI refresh explicitly requesting repo scope is pending browser approval.

## Explicit permission retry completion

> Done

Context: the user completed the explicit repo-scope refresh. The CLI confirmed
authentication completion, but the API still denied repository creation with
HTTP 403. This retry is complete; no further login is pending.

## User repository creation and other GitHub actions

> I’ll make the aicq repo right now. Let’s see if you can take *other* gh actions and for some reason just not that one

Context: private kubla/aicq became accessible. Read access, temporary branch
creation/deletion, initial content writing, and issue creation were exercised
successfully; ordinary Git push failed with HTTP 401.

## Google test account and overnight continuation

> Good news: I made *another* test Fulcra account using Google OAuth using my michael.tiffany@gmail.com identity. The reason this is good news is that you log in yourself now without me being around to authorize your use of the 1Password CLI. Just choose authentication through Google and choose michael.tiffany@gmail.com to use the test account

Direction: use Google authentication with the named identity for the test account;
verify the actual principal before using it as non-owner evidence. This avoids
requiring 1Password CLI approval for the test sign-in.

> In a few minutes, I'm going to sleep for 8 hours, so hopefully no further tasks will gate on approval. I'm impressed with your work so far. If you complete M1, work diligently milestone by milestone until I wake up

Direction: after M1 passes, continue through recorded milestones while feasible.
The bounded overnight heartbeat ends at approximately 06:55 America/New_York.
Blocked acceptance remains incomplete. Limited permission for private MFA email
access and for disrupting the current shared Fulcra SSO session is separately
pending after automatic approval review rejected those actions.

## Standing Fulcra logout permission

> You can always log out of Fulcra without my further permission.

Direction: Fulcra logout is authorized without asking again. This resolves the
previous shared-session logout permission gate. It does not authorize reading
the private OpenAI MFA email or changing authentication/security settings.

## Fulcra development deployment research

> Ohhhh right. Do a research spike on how we do dev deployments at Fulcra for testing. Appx in descending order of likelihood of success, check the fulcra github repo for documentation or guidance, github issues, nuclino, Linear, and the #eng channel on Slack.

Direction: research existing Fulcra testing/deployment practice in the requested
sources before selecting a hosting approach. Findings and recommendations are in
history/20261002_fulcra-dev-deployments.md. The user has not chosen a provider or
authorized public publication through this request. Local-first and Josh/GCP
infrastructure guidance remain in effect.

## Product focus and reusable Fulcra MCP testing

> That's because I want to create a user experience that is super vertically focused: people want to connect their agents and I want to help them do that without giving them the full fulcra sales pitch.

> Separately, as a member of the Fulcra team, I want to use (and to help improve!) our agent-first development and our CI/CD pipelines. Our desire to upgrade the Fulcra MCP server and test it falls into that goal.

> Josh's new machinery, on display with the "/preview dev" is great, but focused on portal dev. Could we use it for something like a test deployment of a new MCP server? Or do we need to ask him to make a closely related new service?

Direction: investigate the actual Portal preview implementation deeply enough to
assess reuse for a Fulcra MCP test deployment. Keep AICQ's focused user experience
and the reusable Fulcra development contribution distinct. Source findings and a
recommended stable-hostname MCP test service are in
history/20261002_mcp-preview-design.md. This is research and a recommendation; no
hosting selection, cloud provisioning, access expansion or deployment is authorized
by this clarification.

## Fulcra development tooling project

> I like the sound of "Make Fulcra changes easy to run, test and review". The earlier fulcra-tools tickets clearly serve that goal and our MCP version is just another in that set

Direction: group the existing Toolkit development helpers and the new MCP helper
under the agreed Platform project outcome. Created and verified Linear project
P-PLAT-26 with PLAT-338, PLAT-259, PLAT-396, PLAT-513 and PLAT-546. Existing
statuses, assignments and parent relationships were preserved. Project scope and
first-release completion criteria are recorded in
history/20261002_toolkit-project-created.md. This tracking change does not select
or deploy AICQ hosting, advance M2, or grant additional infrastructure access.
