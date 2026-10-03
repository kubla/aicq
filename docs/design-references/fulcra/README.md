# Fulcra styling for AICQ prototypes

The user requested the Context Web design cues and the Fulcra logo on 2026-10-03.
Both HTML studies now apply this reference. AICQ remains the product name.
These are simulated designs; the reference does not establish live integration.

## Sources

- [Context Web DESIGN.md](https://github.com/kubla/fulcra-design-reference/blob/3f54e39d927b2d954897b82b9ba8ba315ea283ab/context-web/DESIGN.md), authenticated GitHub read, alpha guide. Full snapshot: `context-web-DESIGN.md`.
- [Fulcra logo](https://github.com/ashfulcra/fulcra-tools/blob/c67aa1accbb9ffc7a0a3ab81ea20c21de6969e16/packages/menubar/fulcra_menubar/assets/source/fulcra-logo.svg), authenticated GitHub read. `fulcra-logo-original.svg` preserves the source. Monochrome and mint derivatives retain both path geometries and the 450 × 450 viewBox; only color handling changes.
- Rubik Latin variable font, weights 300–900, from Google Fonts. Bundled as `rubik-latin.woff2`, with `Rubik-OFL.txt`. The HTML embeds the font bytes and SVG paths; opening either study needs no remote asset requests.

Pinned blobs, source links and SHA256 hashes are in `manifest.json`.

## Adopted cues

| Element | AICQ choice |
| --- | --- |
| App typography | Rubik, regular through semibold |
| App panel / raised surface | `#16161D` / `#222227` |
| Action / selection | Mint `#56D6B7` / violet `#7B61FF` |
| Primary / secondary text | White / `#8A8A8E` |
| Dividers | Subtle `#38383A` boundaries |
| Shape | Compact 8px controls, larger 12px panels; hexagons for identity/avatar only |
| Depth | Flat charcoal tones and borders; restrained shadows |
| Brand | Monochrome Fulcra logo in native navigation; mint logo beside AICQ in app content |

Selection also has a border and visible label. Keep retrieval, readiness and
permission states explicit; avatar color does not imply an agent is online.

## Host boundary

Read [the OpenAI host reference](../openai-host/README.md) for the surrounding
window. Use its narrow native rail, content tabs, split chat/app view and composer.
The prototype uses a 52px rail and 44px top bar at its chosen scale. Portal's
72px rail is not a reference for OpenAI navigation. Host controls keep system
type and neutral colors; Fulcra styling applies to app content. Native context
chips and blue send buttons stay in the host palette.

The guide's Font Awesome Pro libraries are not bundled. Generic host outline
icons were authored for these mocks. No new AICQ logo was invented. Simulation
buttons sit outside the depicted host window and remain explicitly labeled.

## Verification and limits

See [UX-P03 evaluation](../../prototypes/fulcra-evaluation.md) for browser
observations and screenshots. Desktop appearance is grounded in official
OpenAI images; narrow layouts are extrapolated. Browser-reported font readiness
and declared family were checked; a platform-font DevTools inspection stalled
and was abandoned. No pixel-perfect or installed-client verification is claimed.

Future mocks should reuse these assets and both design references. Update the
manifest when refreshing sources, and keep past evidence tied to its source hash.
