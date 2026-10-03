# UX-P08 — native host and mention realism

Public example: https://aicq-interaction-studies.mtiffany.chatgpt.site/alice.html?scene=finance
Source: `mcp/ui/prototypes/alice-v3.html`. SHA256:
`fb3733278a122ccf8273a691bebf4d14830e17aaf255ee236233d075a0af9b53`.

Michael requested realistic @AICQ highlighting and a broader detail audit. The
reference is the unchanged official OpenAI MCP Extensions screenshots, especially
`05-composer-mention.png`, `02-thread-tray.png` and
`08-model-context-attachments.png`. They show blue inline plugin text, neutral
pickers, monochrome host controls and a removable Context chip. They are pinned
documentation images, not current installed-client observations. No new live
client capture is claimed.

## Corrections

- @AICQ is blue inline text in both the editable draft and the sent user message.
  The contact picker sits above the composer with neutral resource rows. Selecting
  a contact inserts one token, preserves the rest of the draft, and shows the
  selected recipient in understated metadata rather than a second mention pill.
  Removing the token clears that metadata. Repeated selection does not duplicate
  it. Search Enter selects a contact; Escape dismisses the picker; no-result
  searches have an empty state.
- Enter sends a nonempty instruction; Shift+Enter adds a line. The native textarea
  retains cursor, selection, copying and typing, with a synchronized display layer
  for highlighting. Empty send is disabled. Composer controls use native-style
  configuration/model indicators, @ and microphone icons. Dictation is outside
  this HTML prototype and its button is disabled; no microphone permission or
  recording occurs.
- The history icon opens Chats instead of starting a new session. New conversation
  remains a separate control. Context uses an icon and removable native chip; its
  popover identifies the selected model/version and summary. Drafts survive these
  controls. Host focus colors, response-action icons, tool activity and user-bubble
  widths follow the neutral host reference. Duplicate SVG attributes were removed.
- The .xlsx model opens as a read-only spreadsheet preview, with Summary,
  Assumptions and Sensitivity sheets, row/column headings and consistent figures.
  Prose documents retain their edit/version-conflict behavior. A spreadsheet
  preview does not pretend to be a plain-text .xlsx editor.
- Prepared directions are described as prepared, rather than sent. Receipt labels
  and the inspector reflect the actual simulated work status. Launch-review
  summaries use the current document date: October 15 in the normal review and
  October 20 in the newer-document case. Historical messages retain their original
  content. Scroll position is retained when inspecting the current conversation;
  new chat results move to the latest result.

## Evaluation

The initial evaluation caught Escape dismissal, a wrong inspector label, and
overwide solo user bubbles. Retry 1 repaired them and caught the pre-existing
October 15/20 summary contradiction. Both failed reviews and their observations
are preserved. Final retry repaired the source-derived summary and passed the
actual browser checks. No failed candidate was published.

`host-realism-observations.json` includes typed/selected/deleted/repeated mentions,
keyboard sending, continued ChatGPT work, selected context and draft continuity,
history, spreadsheet sheets, approval-only preparation, autonomous coordination,
ordinary and changed-document reviews, independent recipient platform/acceptance,
status inspection and responsive measurements. Final narrow-width journey showed
the latest result at the bottom with no page/footer overflow at 390px. Resizing an
existing chat preserves its pixel scroll position; users may need to scroll to the
latest chat result after resizing. No console errors; Node syntax and diff checks
passed. This is mechanical and visual prototype evaluation, not user design signoff.

The exact reviewed HTML was copied to the existing Site checkout; native Sites
source push, archive-backed save and publication receipt are retained separately.
Public audience and previous study routes were preserved. All agent, calendar,
identity and background behavior remains fictional and simulated. M2 acceptance
and its remaining retry are unchanged.
