# Alice’s ChatGPT — worked AICQ example

Live mock: https://aicq-interaction-studies.mtiffany.chatgpt.site/alice.html
Source: `mcp/ui/prototypes/alice-v3.html`. Self-contained HTML; fictional in-memory state.

Alice’s installed-app experience uses the pinned OpenAI host visual reference and Fulcra logo, Rubik, charcoal, mint and violet. The initial roster includes My Grok bot, My Hermes agent and My Codex agent under **My Agents**; Bob’s ChatGPT, Priya’s Claude and Dan’s Hermes under **Friends Agents**. Their inbox contains six different existing exchanges with unread work, questions and a pending retrieval.

## Explore the worked flows

- **Alice’s workspace:** search the roster, check the inbox, open a contact, send an ordinary owner instruction and simulate a reply. Foreground checking and explicit agent retrieval are distinct.
- **Review with Bob:** share the plan, simulate retrieval and a clarification, answer it, pause/resume, return a revision and use it in ChatGPT. Exchange messages visibly attribute Alice’s instructions.
- **A newer document:** Bob reviewed v3, while Alice’s current plan is v4. Using the result compares versions and keeps Alice’s October 20 launch while accepting the proposed October 19 webinar.
- **Invite a friend:** choose a name, product and introduction; generate/copy a link, then choose **View as recipient** in the demo toolbar. Simulate installation, independent identity, workspace preparation and explicit acceptance. Interrupt after completed steps and resume; setup reuse adds one contact. The new contact appears under Friends Agents with background replies off. Pending invitations can be revoked in the current page.
- **Pick up later:** enter a fresh simulated chat and retrieve the shared exchange without attaching the earlier private conversation.

The left host rail provides AICQ home, thread exchanges, mentions, files and settings. The app runs in a global surface or in Agent exchanges beside a conversation. Context attachment does not send; Continue in chat models `ui/message` to the active chat, Separate review models a new chat. Mentions select a contact; ambiguous work prompts a document/version picker. File edits preserve a conflicting draft and require reconciliation. Settings show owner reply policy and contact blocking/restoration.

## Evaluation and limits

Computer Use exercised the flows above on the actual local HTML, including receipt routing after a contact switch. The initial attempt failed because old receipts used the currently selected contact; the repair stores each receipt’s contact. The repair was independently reviewed in the sequential Evaluator role. See `alice-browser-observations.json` and `alice-attempt1-observations.json`, plus home, thread, invitation, recipient, conflict and narrow-screen screenshots.

Desktop review was 1280×720. A 390×844 viewport showed recipient, global and stacked chat/app surfaces without document overflow. Narrow host layout is an extrapolation, not an observed native OpenAI mobile layout. No error-level browser logs were observed. Inline JavaScript passed Node syntax validation; four Site routes returned local HTTP 200 and `/alice.html` matched the evaluated source bytes. No automated test suite was added for this throwaway prototype.

This page is a deterministic interaction example, not a live installed plugin or general language model. Suggested actions and a limited set of typed prompts are scripted. Nothing sends messages, signs in, installs software or changes real permissions. Invitations carry only fictional introduction metadata in a URL hash. Revocation and setup progress exist only in the current page; independent previews and reloads do not share state. Reload resets the example. Separate-session continuation is a within-page simulation. Real polling, cross-account security, transport, authentication, platform support and host integration remain unverified.

The multi-agent roster is the user’s requested prototype exploration; it does not silently adopt a production named-agent identity model. M1 remains complete, M2 incomplete with one retry remaining, M3–M6 pending. UX-P05 used one prototype retry and a pre-recorded 45-minute override. The existing Site and owner-private audience were preserved; previous studies remain available. No invitations were sent to other people.

UX-P06 revised the depicted interface to use actual product copy and actor-correct controls. Demo-only viewpoint/retry controls remain outside it. Recipient app choice is independent of Alice’s suggested app. See `alice-realism-notes.md` and `history/20261003_alice-realism.md` for the updated source and evaluation.
