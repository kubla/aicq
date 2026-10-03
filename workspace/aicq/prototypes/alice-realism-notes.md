# UX-P06 — Product copy and viewpoint realism

Published correction: https://aicq-interaction-studies.mtiffany.chatgpt.site/alice.html
The user identified narrator language in Alice’s invitation page and requested a pass across the entire worked example. The scope is the depicted AICQ/ChatGPT interface: demo framing, remote-agent controls and state inspectors remain outside it and explicitly identify fictional behavior.

## Corrections

| Surface | Correction |
| --- | --- |
| Alice’s invitation | “Invite a friend to connect their agent with yours.” Name, suggested app and message fields. Generated invitation says “Send this link to Morgan.” Copy/revoke are product actions; View as recipient is a demo control. |
| Recipient | Addresses Morgan directly, lets Morgan choose their app, and uses Install AICQ, Continue as Morgan, Set up AICQ and Accept connection. Alice’s navigation/account is absent. Back to Alice and Retry completed setup live outside the product. No simulate suffixes or fictional walkthrough prose appear inside it. |
| Chat and notifications | Normal user/assistant turns and concise state confirmations replace implementation explanations about host turns, evidence, foreground workers and shared-state simulation. |
| Exchanges | In progress replaces Retrieval observed; own-agent headers say You; Continue in chat avoids asking Alice to continue with herself. Use changes and review comparisons name the actual agent rather than hardcoding Bob. Duplicate attach/continue controls were removed. History counts use singular/plural correctly. Replies and clarification defaults follow the selected topic. |
| Settings | Account-level reply/refresh choices are separate from a specific contact’s shared/private permissions and block/restore controls. |
| Files and conflicts | Review changes, Apply changes, Latest version and Autosave off replace narrator/technical process language. Version comparison still preserves the newer launch date. |
| Host details | Response glyphs use native-style copy/feedback/expand icons. Truncated preview text ends with an ellipsis. |

The first narrow recipient screen clipped its card inside the overflow-hidden mock window. Document scrollWidth alone did not catch it. The repair constrains the grid track with minmax(0,1fr) and resets minimum widths. Actual 390px card/stage bounds and screenshot confirmed the full card fits; recipient acceptance still works.

## Evidence

`alice-realism-observations.json` contains 26 actual DOM observations during review and repair, including invite generation, recipient app choice/setup/interruption/acceptance, account settings, blocking, review/clarification/revision/conflicts, file display, later chat, on-topic ordinary replies, own-agent labels and receipt routing after switching contacts. Copy audit found no narrator/simulation phrases in captured product text. No error-level browser logs were observed. Node --check passed. Narrow layouts remain extrapolations from desktop host references.

Screenshots retain both the failed narrow view and its repair. All interaction/authentication/sharing/delivery remains fictional and in memory; realistic presentation does not establish live product behavior. Current user design validation and live host integration remain open. No automated prototype test suite was added.
