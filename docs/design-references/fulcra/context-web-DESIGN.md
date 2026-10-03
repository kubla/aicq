---
version: alpha
name: Context Web
description: Design system for the authenticated Context web application, including its shell, dense Timeline instrument, tables, forms, and responsive behavior.
colors:
  primary: "#56D6B7"
  secondary: "#7B61FF"
  secondary-readable: "#9C88FF"
  canvas: "#000000"
  surface: "#16161D"
  surface-raised: "#222227"
  divider: "#38383A"
  divider-strong: "#333333"
  on-surface: "#FFFFFF"
  on-surface-muted: "#8A8A8E"
  info: "#007AFF"
  success: "#34C759"
  error: "#FF3B30"
  warning: "#FFCC00"
  calorie-active: "#B5D656"
  calorie-basal: "#AF52DE"
  calorie-consumed: "#FF2D55"
typography:
  body:
    fontFamily: Rubik
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
  body-compact:
    fontFamily: Rubik
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
  label:
    fontFamily: Rubik
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.25
  title:
    fontFamily: Rubik
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.25
  title-lg:
    fontFamily: Rubik
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
spacing:
  hairline: 0.5px
  xxs: 2px
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  2xl: 24px
  3xl: 32px
  4xl: 40px
  5xl: 48px
  breakpoint-sm: 640px
  breakpoint-md: 768px
  breakpoint-lg: 1024px
  breakpoint-xl: 1280px
  rail-width: 72px
  home-max-width: 1280px
  timeline-min-width: 860px
  timeline-info-width: 192px
  timeline-trend-width: 160px
rounded:
  control: 8px
  card: 8px
  card-lg: 12px
  framework-box: 16px
  full: 9999px
components:
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.card}"
    padding: "{spacing.xl}"
  button-normal:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    rounded: "{rounded.control}"
    padding: 8px 12px
  button-selected:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.control}"
    padding: 8px 12px
  button-destructive:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.control}"
    padding: 8px 12px
  input:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.control}"
    padding: 8px 12px
  table-row:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    height: 44px
  timeline-row:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    width: "{spacing.timeline-min-width}"
---
# Context Web

## Overview

Context Web is a forced-dark analytical application: a sparse shell wrapped around an unusually dense Timeline instrument. It should feel like a personal observatory — calm, exact, and inspectable, with real data doing the work that decoration does in ordinary dashboards.

Home is the spacious, brand-forward exception. Timeline, tables, and forms tighten the density, but every surface speaks the same language: black and charcoal fields, compact Rubik type, mint for ordinary action and current data, violet for selection, and restrained depth.

`authz-interface` and `pool-dashboard-web` are special-purpose exception families. Their tokens and newer framework stacks do not redefine core Portal canon.

## Colors

- **Mint (`#56D6B7`):** The color of ordinary action — links, current-period data, the brand mark, and inactive navigation.
- **Violet (`#7B61FF`):** The color of selection — active navigation, checked controls, tags, paired emphasis, and the gradient endpoint. Substitute `#9C88FF` where dark-field readability demands it.
- **Canvas (`#000000`):** The page field.
- **Panel (`#16161D`):** Cards, tables, navigation, and modals.
- **Raised (`#222227`):** Hover and nested or secondary surfaces.
- **White/gray (`#FFFFFF`, `#8A8A8E`):** Primary text; metadata, axes, and inactive state.
- **Dividers (`#38383A`, `#333333`):** Navigation boundaries; stronger panel and table rules.
- **Blue (`#007AFF`):** Previous period, reference, and information.
- **Green/red/yellow:** Success, error/destructive, and warning.

Reserve the mint→violet gradient for the wordmark, selected subscription actions, and bounded brand emphasis. When everything glows, nothing is live — never wash ordinary panels in gradient.

Chart palettes are contextual, not universal. Net calories speak in lime, purple, and magenta; sleep uses a Viridis-derived stage palette. Mint-for-current against blue-for-previous is the usual comparison pairing, not a law that governs every domain.

## Typography

Use Rubik. The application loads normal and italic weights 300–900, but routine product work should live in regular, medium, and semibold.

- **12px label:** Metadata, axes, compact labels, and dense table/chart support.
- **14px compact body/control:** Most controls, rows, and supporting copy.
- **16px body:** General content and forms.
- **18px title:** Feature and section titles.
- **20–24px strong title:** Page/feature emphasis used selectively.

Buttons set their labels at normal weight — a deliberate departure from DaisyUI's bold default. Preserve that restraint, and keep explicit units and date ranges close to the values they describe.

Align time-series values, table columns, and compact metric comparisons with tabular numerals. True monospace is for code, identifiers, and technical values, never for decorative texture.

## Layout

At 640px and above, the shell is a fixed 72px icon rail and top bar. Below 640px, the rail gives way to a compact top bar and a labeled full-height drawer.

Spacing builds on a 4px basis — 2/4/6/8/12/16/24/32/40/48px — with 0.5px dividers for established hairline relationships.

- Home may occupy a 1280px maximum container and stack summary/history modules into full-width narrow cards.
- Timeline summary cards become a carousel on narrow screens.
- Dataset/date/mode controls stack when narrow.
- The detailed Timeline preserves an 860px minimum analytical canvas with horizontal scrolling.
- A Timeline row reserves 192px for label/info and approximately 160px for trend/delta controls.
- Metric selection is a two-column centered workspace on wide screens and a bottom-anchored single-column sheet below 640px.
- Tables may scroll, but selection, pagination, and named overflow actions must remain reachable.

When reflow would destroy analytical alignment, keep the alignment and let the chart scroll. Fitting every chart into 390px matters less than a discoverable scroll affordance and a nonvisual alternative.

## Elevation & Depth

Depth comes from tone and borders before it comes from shadow: `#000000 → #16161D → #222227`, bounded by `#333333/#38383A` borders and hairline row separators. Ordinary cards, tables, and navigation are flat on purpose.

Backdrop dimming and blur belong to dialogs, subscription surfaces, and tooltips. DaisyUI and third-party structure may remain visible beneath Fulcra overrides, but framework defaults are not design tokens.

Name semantic layers — base, sticky navigation, dropdown, backdrop, dialog — rather than promoting isolated extreme z-index values into a token scale.

The custom 15px scrollbar is a desktop integration detail, not a general component-size rule.

## Shapes

- **8px:** Dominant control and card radius.
- **12px:** Contextual cards and larger sections.
- **16px:** DaisyUI box radius where framework structure remains visible.
- **Full radius:** Pills, badges, circular icon/ellipsis triggers.
- **0.5px:** Default hairline divider.
- **3px rule:** Active desktop rail indicator.
- **Hexagon:** Profile/avatar and brand geometry only.

The rounded rectangle is the workhorse; circles serve compact actions and chart points. The hexagon belongs to identity — do not hexagonize ordinary panels.

## Components

### Shell and navigation

The wide shell pairs a 72px icon rail with a centered route noun, the gradient Context mark, and a hexagonal profile trigger. Inactive navigation is mint; the active item turns violet and gains a 3px right rule. The narrow drawer adds labels without changing the state colors. Icon actions are named, focus is visible, Escape closes, and focus returns.

### Buttons, links, tabs, and chips

Controls are compact and 8px-rounded. Mint is the default outline, text, and link color; violet marks selected and checked; red is destructive. A disabled action must say why it is disabled — as Share Data does when nothing is selected — and selection must read beyond color, through a label, check, or state change.

### Cards and Home

Cards sit at `#16161D` on black with the dominant 8px radius, sparse shadow, and stable label/value/chart regions. Home pairs a spacious brand introduction with dense recent, source, history, and all-time modules and equal feature tiles. Loading preserves the panel geometry behind restrained mint rings.

### Timeline

The control band uses mint-outlined dataset, date, and trend actions with violet Day/Week selection. Each row divides into three zones: label and info, aligned chart, trend and delta. Current-period lines are mint at 1.75px with points; previous-period lines are blue at 1px and 0.75 opacity without points; averages dash at `4,4`. Axes use 11px gray labels over dashed gray gridlines, and a shared hover aligns one cursor and its tooltips across every row.

Pointer hover can never be the only way in. Provide keyboard and touch selection, a concise accessible summary, and a data-table or equivalent detail path.

### Tables and forms

Tables pair compact headers and rows with low-contrast rules, mint links and labels, violet tags, named row selection, pagination, and circular overflow actions. Inputs sit on dark raised surfaces with persistent labels, mint focus and action, violet checked state, muted help text, and red errors. Error and help text are programmatically associated with their fields.

### Dialogs and drawers

Use a compact centered dialog or a large centered workspace. Below 640px, a bottom sheet is right whenever it preserves the actions and reading order. Every dialog specifies its initial focus, containment, Escape and backdrop rules, and focus return.

### Loading and state system

Loading is a mint ring inside a stable panel. Beyond it, the state system needs distinct empty, permission-error, generic-retry, toast, disabled, selected/indeterminate, destructive-confirmation, subscription, and offline treatments. All loading motion has a reduced-motion counterpart.

### Icons and third-party surfaces

Icons are Font Awesome SVG 6.6.0 — Pro Solid as the dominant product weight, Pro Thin for selected feature, empty, and upload roles. Icons inherit semantic color, and every icon-only control carries a name.

Tabulator, FilePond, Tagify, date pickers, Leaflet, Swiper, and Driver keep their library structure under Fulcra theming. Specify the Fulcra surfaces, type, states, focus, and accessibility; do not canonize library DOM or layer hacks.

## Do's and Don'ts

- Do keep the shell sparse and route titles short.
- Do use mint for normal action/current data and violet for selection.
- Do preserve the Timeline's aligned analytical canvas when reflow would destroy meaning.
- Do structure density with stable zones, dividers, labels, and exact units.
- Do load progressively inside stable geometry.
- Do make destructive actions red and confirmation-driven.
- Do specify keyboard, focus, dialog, chart, table, and icon semantics with the visuals.
- Don't turn the app into a soft-shadow card grid or gradient every panel.
- Don't copy extreme z-index values, unused tokens, malformed declarations, or no-op classes into canon.
- Don't collapse Timeline just to fit a phone.
- Don't rely on pointer hover as the only chart interaction.
- Don't suppress browser zoom in the future design contract.
- Don't merge special-purpose Auth0 or pool-dashboard styling into core Portal.
