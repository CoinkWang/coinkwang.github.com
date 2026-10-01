---
version: 1
slug: "layouts-about-html"
primary_target: "_layouts/about.html"
related_targets: ["_sass/pixel.scss","_includes/header.html","_layouts/home.html","_layouts/post.html"]
---

# About — pocket camera album (theme_style: pixel)

Scope: the new `pixel` theme site-wide (header, footer, home, post, tag, links, 404) with About as the signature surface. Visitor mode: Experience on About; Read on posts and lists.

Audience: a stranger who just finished one article and wants to know who wrote it. Job: leave with a specific picture of Coink's eight interests. Content fixed (PRODUCT.md): eight interests, game list, music list, the book + cover, 失眠权 WIP, 小红书 link. No new facts.

## Direction contract

THESIS: The blog is a 4-tone pocket camera's album. Browsing happens on the LCD; reading happens on thermal-printer strips torn off the camera. Refuses the NES.css default: white page, black pixel-border dialog boxes, Press Start 2P, RPG stat sheet.

OWN-WORLD: Four LCD tones only (ink, shade, mid, screen) flooding every region, plus the same four as thermal grays on print strips; no off-palette neutrals. Ark Pixel 12px at exactly 12 and 24px, all spacing on a 4px unit. Selection is reverse video and a ▶ cursor; frames are stepped pixel corners, never radius or blur. One palette only, the lit-teal night screen (revision 2026-10-01: the hour palettes and the footer switcher were removed at the owner's request). Body prose on strips is a legible system sans.

STORY: The visitor sees the album page: eight hand-drawn pixel photos, each on its own camera body with the strip it printed hanging underneath, reads across them, and leaves knowing Coink is a birder, gamer, writer and musician.

FIRST VIEWPORT: Revision 2026-10-01 (owner's request: no interaction; on a desktop everything fits one screen, on a phone one scroll). Four columns of cards on desktop, filled top to bottom in `pixel_order` to balance heights; each card is a lit camera body with the picture and its 观鸟 Birding label, and the entry's thermal strip beneath it. No primary action: nothing to click, everything is printed. Hi-dpi desktops show pictures at x1.5 (3 device px) with the label beside them; the page heading is screen-reader only from 1200px. Phones: one column, pictures at x3. Deep links `about.html#key` scroll to the card.

FORM: Pocket camera album with thermal printer, my grounded list position 6 of 7, seed key 602c0de0. Raises: stepped print-out of lists (miura), hour palettes (cityscape), one bitmap face two sizes on a 4px unit (cracktro), WIP as an undeveloped blank frame (seven-segment), four tones at page scale (single hue). Signature: every picture already printed, its strip hanging under the camera (the feed animation went with the interaction).

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

## Unresolved
- Bird species list does not exist; drawn birds are illustration, never captioned as sightings.
