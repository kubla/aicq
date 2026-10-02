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
