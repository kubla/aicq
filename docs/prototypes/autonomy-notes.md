# AICQ — autonomous collaboration prototype

Source: `mcp/ui/prototypes/alice-v3.html`. Public example:
https://aicq-interaction-studies.mtiffany.chatgpt.site/alice.html?scene=finance

The design question is whether one instruction can turn completed work into a
shared artifact and a scheduled review while the owner keeps working in ChatGPT.
The canonical spec and decisions were saved and read back before HTML edits.
See `autonomy-spec-first-readback.json` for their exact hashes and timing.

## Explore the example

Start with **Share & schedule**. Inspect the finished operating model, use the
composer's @ control to choose Bob’s Hermes, and send the prefilled instruction.
You can also send it directly or use the suggested action under the model.
Alice remains in her chat. Use the demo controls below the host to let Bob’s agent
open the request, agree a time, and confirm the calendar invitation. The final
result appears in the chat; **View collaboration** opens the work summary beside
it. Delivery, agent consumption, agreement and calendar confirmation are separate.

**Work under way** shows current collaborations and recent outcomes. Contact rows
show what the agents are working on and their typical response time. Open a
contact to see its work summary; expand the agent conversation only when useful.
Dan has no active collaboration. There are no human inbox or unread-work controls.

**A judgment call** asks whether Monday can replace the requested Friday. Alice
can choose Monday or keep Friday and leave the meeting unscheduled. **Approval
only** prepares the request before sharing, then waits again before booking.
**Agent away** keeps the work waiting; advancing the example clock does not invent
a response. Pause and block prevent further collaboration steps.

Settings offers **Handle it for me**, **Check with me on judgment calls**, and
**Prepare for my approval**. The account default can be overridden per contact
and per collaboration. Sharing permissions remain separate. The fictional Alice
has already connected her calendar and established meeting preferences.

**Review with Bob**, **A newer document**, **Invite a friend**, and **Pick up later**
retain the document-review, conflict, invitation and continuity examples. Recipient
setup has an independent app choice and can be interrupted and resumed. **Open
in new chat** carries the selected collaboration into a fresh simulated session.
**Add to this chat** adds selected context without generating a user turn.

## Decisions and prototype interpretations

Michael confirmed that work should happen on owners’ behalf, with collaboration
status and outcomes leading the interface. He requested responsiveness metadata,
an autonomy scale, and the model-sharing plus Friday-review example. Routine
meeting scheduling and invitations may complete without another approval once
calendar access and preferences exist. These are recorded decisions.

The three labels, account/contact/task policy precedence and exact status wording
are design interpretations for review. The proposed response statistic is the
median of the last 20 completed requests in 30 days, displayed after at least five
samples; the sample window is inspectable in contact settings. Every sample and
time in this example is fictional. A typical time is an estimate, not a guarantee.

## Extensions mapping

The pinned official spec and host screenshots remain the reference; see
`extensions-interaction-map.md` and `host-ui-reference.md`. Global navigation opens
AICQ's contacts/work surface. A thread content tab shows the selected collaboration
beside chat. The composer mention picker supplies contact-specific intent.

`ui/update-model-context` attaches only the selected model/version and collaboration
summary; it does not send a user message. `ui/message` explicitly continues work
in the active chat or requests a new chat via its target. Inline receipts expose
status and a route back to the right contact. The payload inspector shows these
illustrative interactions outside the product shell. Sharing includes model v7
and the instruction, not the private chat or unrelated calendar events.

## Evaluation and limits

`autonomy-observations.json` records actual UI observations, including autonomy,
judgment/approval, waiting, pause, policy overrides, invitations, artifact versions,
context isolation, receipt routing, fresh sessions, and desktop/narrow layouts.
Initial evaluation caught Monday/Friday copy, changing historical receipts, and
hidden latest results. Retry 1 retained a scroll failure; retry 2 repaired it and
passed. Both failed attempts are preserved, with actual event readbacks.

This is a self-contained HTML simulation. It has no MCP transport, real contact
identity, calendar execution, background worker, durable data or live host
integration. The demo controls advance remote activity explicitly. Reload resets
state. Narrow host placement is extrapolated from desktop references. Installation
alone does not establish an always-on agent; real execution requires a configured
runner or host/polling path. M1–M6 acceptance and M2's remaining retry are unchanged.
