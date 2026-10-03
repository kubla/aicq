# Desktop host reference for AICQ mockups

Use this reference whenever a mockup shows AICQ inside ChatGPT/Codex. Open
[the gallery](index.html) to compare the nine full-resolution screenshots.
Source: [OpenAI MCP Extensions](https://github.com/openai/mcp-extensions/blob/ca16cb3bc015baaa1b849082d8755bbef18770cb/docs/spec.md),
pinned to `ca16cb3bc015baaa1b849082d8755bbef18770cb`. Original image names are retained;
[manifest.json](manifest.json) records URLs, hashes, dimensions and observations.

## Evidence boundary

On 2026-10-03, Computer Use found the running ChatGPT app (`com.openai.codex`),
then rejected selecting it: “Computer Use is not allowed to use the app
'com.openai.codex' for safety reasons.” Its MCP Apps browser surface had no tabs,
and this executor exposed no callable Bits & Bolts app tools. No installed-plugin
interaction or live screenshot was obtained. The user explicitly authorized web
screenshots as the fallback. The nine images here are unchanged OpenAI reference
screenshots, visually inspected in this task. They show **Bits & Bolts Local**;
the installed skill is **Bits & Bolts Remote 1.0.23**. Current client appearance,
light theme, mobile layout and plugin availability remain unverified.

Images retain OpenAI attribution. The purple outlines, purple translucent areas
and labels are documentation annotations. Use the underlying neutral host palette
for mockups. The blue wallpaper is outside the app window. Screenshot pixels
establish appearance; the pinned spec establishes behavior.

## Select the matching surface

| AICQ example | Reference | Host details to reproduce |
| --- | --- | --- |
| Open AICQ from navigation | [Global library](01-global-library.png) | Narrow icon rail, global title above content, permanent app surface, compact floating composer at bottom right |
| Exchange beside current work | [Parts Tray](02-thread-tray.png) | Conversation title on left; app content tab on right with icon, title, close and adjacent plus; vertical divider; composer inside chat column |
| Open an exchanged artifact | [File viewer](03-file-viewer.png) | File link stays in transcript; named viewer tab occupies the right pane; app toolbar inside the pane |
| Select a contact with @ | [Mention picker](05-composer-mention.png) | Results immediately above the composer; plugin heading, resource row, selected mention in composer text |
| Add selected exchange context | [Context popover](08-model-context-attachments.png) | Removable Context chip in composer; anchored popover with titled content items; app selection stays separate |
| Compact receipt / expanded exchange | [Display modes](11-display-modes.png) | Inline host card has plugin header and expand control; expanded content uses the right pane while chat remains visible |
| Choose which document to share | [Resource picker](13-form-resource-picker.png) | Host form card in chat; thumbnails, local-file option, View all and Continue; app can remain open alongside |
| Configure AICQ | [Settings](07-settings-entrypoint.png) | Host plugin detail page and server section; grouped rows with selectors/switches on the right |
| First setup | [Onboarding](12-plugin-onboarding.png) | Centered host dialog, blurred background, close button, defer and setup actions |

These are references for placement and visual hierarchy. AICQ's contact cards,
exchange controls and content remain product design choices. A file-viewer example
does not authorize arbitrary file access or establish an AICQ file handler.

## Build the host shell

1. Start with the native window, icon rail and top bar. At the declared half-size
   normalization, the window is approximately 1600 × 1000, the rail 52 px wide
   and the top bar 44 px high. These are screenshot-derived dimensions, not
   verified CSS pixels or a known device pixel ratio. Scale the whole shell
   consistently for a smaller mock canvas.
2. Use thin monochrome icons, understated hover/selected backgrounds, neutral
   surfaces and subtle dividers. Keep the app icon in the rail and its name in
   the global header. The screenshot does not show an expanded navigation-label
   state; label/tool-tip behavior needs further evidence.
3. For a thread, give chat and app approximately equal space after the rail.
   Put the content tab in the native top bar. Place app headings and navigation
   below that bar, within app content. The tab title describes the view:
   AICQ's proposed title is “Agent exchanges.” Keep the host close/plus/split
   controls distinct from app actions.
4. Keep the composer anchored to its host layout. In the thread reference it
   spans most of the chat column and has rounded corners, an input area, plus,
   configuration/model controls, microphone and circular send button. In the
   global reference it floats compactly at bottom right and expands to contain
   context. It belongs to the associated host conversation.
5. Preserve ordinary transcript typography and generous vertical space:
   right-aligned blue user bubbles, unboxed assistant prose, muted tool/activity
   rows, small response actions. Put AICQ's visual identity inside its content
   region. Keep experiment selectors, payload inspectors and simulator controls
   outside the simulated window.

Exact sampled colors and coordinates are in the manifest. Optional starting
tokens are in [host-tokens.css](host-tokens.css). The thread samples give rail
`#242424`, content `#181818`, divider `#2b2b2b`, composer `#363636` and user bubble
`#223d72`. Global samples differ slightly (`#212121`, `#171717`). Font family,
font weights, radii and spacing tokens are visual approximations; raster images
do not reveal the original font or DOM. Use system sans-serif and visually
compare at equal scale.

## Review every mockup

Compare global and thread screenshots side by side with the corresponding source.
Check rail/top-bar proportions, tab placement, chat/app divider, composer location,
transcript styling, context/mention placement and app-versus-host controls. Verify
the actual interactive prototype in a browser at desktop size and at a narrow
width. Desktop references cannot establish native mobile chrome; label that
layout as an extrapolation until a mobile reference is obtained.

Each output must state whether it is a **mockup**, **official reference** or
**observed installed-client capture**, plus which host/theme it represents. Keep
API compatibility and live AICQ acceptance separate from visual fidelity.

The existing `interaction-v1.html` and `extensions-v2.html` have not received this
fidelity pass. Their behavior evaluation remains valid for their simulated flows;
their generic light host shell is an earlier design study. Use this reference
for the next revision rather than treating either existing shell as authoritative.

## Refreshing this reference

When Computer Use can access the installed client, open the global library, then
the Parts Tray in a benign chat; capture navigation, tab controls, composer,
context popover and mention picker. Record client version, plugin variant,
theme, window dimensions and the actions actually performed. Save new captures
separately with sanitized content and provenance. Retain these pinned source
images for comparison. Verify client-specific appearance before replacing rules.
