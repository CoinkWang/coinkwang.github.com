---
name: "Coink | DO BOOM! (pixel)"
description: "A four-tone pocket camera with a thermal printer: browse on the LCD, read on torn-off print strips."
colors:
  ground: "#0c1714"
  mid: "#1f3a33"
  shade: "#4f8f7a"
  ink: "#a8e3c7"
  paper: "#d6d9d3"
  print: "#151816"
  print-soft: "#4f544f"
  print-faint: "#a9ada7"
typography:
  pixel-display:
    fontFamily: "Ark Pixel, Ark Pixel Full, PingFang SC, Hiragino Sans GB, Microsoft YaHei, monospace"
    fontSize: "24px"
    fontWeight: 400
    lineHeight: "32px"
    letterSpacing: "0"
  pixel-label:
    fontFamily: "Ark Pixel, Ark Pixel Full, PingFang SC, Hiragino Sans GB, Microsoft YaHei, monospace"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: "20px"
    letterSpacing: "0"
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, PingFang SC, Hiragino Sans GB, Noto Sans CJK SC, Source Han Sans SC, Microsoft YaHei, Helvetica Neue, Arial, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.75
  body-print:
    fontFamily: "-apple-system, BlinkMacSystemFont, PingFang SC, Hiragino Sans GB, Noto Sans CJK SC, Source Han Sans SC, Microsoft YaHei, Helvetica Neue, Arial, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.9
  body-album:
    fontFamily: "-apple-system, BlinkMacSystemFont, PingFang SC, Hiragino Sans GB, Noto Sans CJK SC, Source Han Sans SC, Microsoft YaHei, Helvetica Neue, Arial, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.65
  title:
    fontFamily: "-apple-system, BlinkMacSystemFont, PingFang SC, Hiragino Sans GB, Noto Sans CJK SC, Microsoft YaHei, sans-serif"
    fontSize: "19px"
    fontWeight: 700
    lineHeight: 1.5
  code:
    fontFamily: "JetBrains Mono, ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
    fontSize: "13.5px"
    fontWeight: 400
    lineHeight: 1.7
rounded:
  none: "0px"
spacing:
  lcd-pixel: "2px"
  s-1: "4px"
  s-2: "8px"
  s-3: "12px"
  s-4: "16px"
  s-5: "20px"
  s-6: "24px"
  s-8: "32px"
  s-12: "48px"
  s-16: "64px"
  s-24: "96px"
components:
  button:
    backgroundColor: "{colors.ground}"
    textColor: "{colors.ink}"
    typography: "{typography.pixel-label}"
    rounded: "{rounded.none}"
    padding: "0 16px"
    height: "40px"
  button-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ground}"
  badge:
    backgroundColor: "{colors.mid}"
    textColor: "{colors.ink}"
    typography: "{typography.pixel-label}"
    rounded: "{rounded.none}"
    padding: "0 8px 0 16px"
    height: "22px"
  nav-item:
    textColor: "{colors.ink}"
    typography: "{typography.pixel-label}"
    padding: "0 12px 0 24px"
    height: "44px"
  nav-item-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ground}"
  pagination-current:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ground}"
    typography: "{typography.pixel-label}"
    width: "40px"
    height: "40px"
  print-strip:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.print}"
    typography: "{typography.body-print}"
    rounded: "{rounded.none}"
    padding: "48px 48px 64px"
  print-subhead:
    backgroundColor: "{colors.print}"
    textColor: "{colors.paper}"
    typography: "{typography.pixel-label}"
    padding: "0 8px"
  shot-camera:
    backgroundColor: "{colors.mid}"
    textColor: "{colors.ink}"
    typography: "{typography.pixel-display}"
    rounded: "{rounded.none}"
    padding: "8px 8px 20px"
  shot-print:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.print}"
    typography: "{typography.body-album}"
    rounded: "{rounded.none}"
    padding: "12px 12px 16px"
---

# Design System: Coink | DO BOOM! (pixel)

This file documents the `pixel` theme (`theme_style: pixel` in `_config.yml`), the site's current visual world. The older themes under `_sass/{bugatti,claude,apple,denise,glance,fieldguide}` still exist and remain switchable; they are not part of this system.

## Overview

**Creative North Star: "The Pocket Camera Album"**

The whole blog is a four-tone handheld camera with a thermal printer built in, lit for the dark. Navigation, lists, the About album and every bit of chrome live on the LCD: four tones of one deep teal hue fill every region edge to edge, a dark ground with bright lit ink, with no off-palette greys and no white page underneath. Reading happens on paper. A post body, an About entry and a footnote popup are thermal strips: pale grey paper, near-black print, and a toothed tear along the bottom edge. There is one palette; the screen does not change with the hour.

The density is low and handmade. One bitmap face at two sizes carries the interface; a legible system sans carries the prose. Everything snaps to a 4px unit and a 2px "LCD pixel". Nothing rounds, blurs or glows. Selection is reverse video, with a small triangle cursor sprite on menu-like rows. All pictures (the eight About scenes, the book cover, the magpie, the birds on the header wire, the bird-track divider, the tag ends) are drawn in code by `_pixel/` (`python3 _pixel/build.py`): the scenes are exported in the four screen tones, the wire birds in their own plumage, the cover in the three print inks, and sprites are masks painted by the theme tokens, so the art always uses the same tones as the surface it sits on.

Birds are the recurring signature: a magpie is the brand mark and ends every printed post, real, nameable species sit on the header rule as on a wire (a night heron, spotted dove, light-vented bulbul, hoopoe, kingfisher, red-whiskered bulbul, blackbird, tree sparrow, oriental magpie-robin, long-tailed shrike, Swinhoe's white-eye, barn swallow, white wagtail and red-billed blue-magpie; shuffled afresh on every page load with independently randomized left/right facing, with all 14 species equally frequent (each appears once per round, including the blue-magpie) and no identical neighbours, including across rounds; standing shoulder to shoulder with at least 3 clear pixels per row so tails tuck under the next bird), and bird tracks make up the horizontal rule.

**Key Characteristics:**
- One set of four LCD tones, mapped onto the page roles ground / ink / shade / mid as a lit screen (dark ground, bright ink).
- A separate four-grey thermal-paper set for anything you read at length.
- Ark Pixel at exactly 12px and 24px; system sans for CJK prose.
- A 4px spacing unit; 2px frames drawn as stepped box-shadow outlines with notched corners.
- Reverse video and a triangle cursor for hover, current page and selection.
- Code-drawn pixel art; sprites are one-tone masks painted by tokens. The magpie is drawn in black only; its white patches are whatever light surface it sits on.

## Colors

One deep teal hue at four luminance steps, plus a neutral thermal-paper set. The root declares `color-scheme: dark`, and the browser chrome is tinted with the ground tone (`theme-color`).

### Primary
The four LCD tones, named in the code by luminance `--t0` (darkest) to `--t3` (lightest) and mapped once onto page roles on `:root`:
- **Lit-Teal Ground** (`ground`, t0): every background region (page, header, footer, mobile menu, behind each album picture), the sunken edge of each album screen and its printer slot, the magpie and bars on the header plates, and the 55% footnote scrim.
- **Lit-Teal Mid** (`mid`, t1): the album camera bodies, link underlines, dotted row separators, disabled controls, the pagination hover fill and the 404 viewfinder grid.
- **Lit-Teal Shade** (`shade`, t2): secondary text such as meta lines, footer copy and inactive sidenotes, plus the scrollbar thumb, the divider tracks and the menu key while the menu is open.
- **Lit-Teal Ink** (`ink`, t3): text, frames, the header and footer rules, reverse-video fills, the album labels, and the two header plates (brand and menu key), which stay reversed so the magpie reads in black and white.

### Neutral
Thermal paper is used for post bodies, About prints, footnote popups and the Waline comment box (self-hosted at comments.coink.wang on Vercel + Neon, open to anonymous comments).
- **Thermal Paper** (`paper`): the strip ground.
- **Print Black** (`print`): print text, print subheads in reverse, code blocks, `<pre>` and table header fills, the closing magpie.
- **Faded Print** (`print-soft`): blockquotes, figcaptions, list bullets and markers, the dotted edge of the blank WIP frame.
- **Ghost Print** (`print-faint`): link underlines on paper, inline code backgrounds, table dotted rules.

### Named Rules
**The Four Tones Rule.** A screen region uses only ground, ink, shade and mid, and a strip uses only paper, print, print-soft and print-faint. No other neutral, tint or accent gets added; art is drawn in the same four tones. The one exception is the birds on the header wire: each wears its own plumage colours, a small fixed palette per species in `_pixel/wire.py`, because the birds are what the blog is about and four tones cannot tell a kingfisher from a bulbul. Nothing else borrows those colours.

**The Mid Never Speaks Rule.** Mid is too close to ground to carry text (1.5:1). Use it for underlines, separators, frames and disabled states only. Readable secondary text uses shade (4.8:1 on ground); ink on ground is 12.6:1. Print-faint follows the same rule on paper (1.6:1); print-soft carries secondary print text (5.4:1).

## Typography

**Display / Label Font:** Ark Pixel 12px proportional, simplified Chinese build (SIL OFL, self-hosted; the deployed site preloads a subset cut at deploy time to the characters it uses, with the full font behind it as `Ark Pixel Full`), falling back to PingFang SC / Hiragino Sans GB / Microsoft YaHei.
**Body Font:** the system sans stack (-apple-system, PingFang SC, Noto Sans CJK SC, Microsoft YaHei...).
**Code Font:** JetBrains Mono, self-hosted.

**Character:** A bitmap face for everything you navigate by and a quiet system sans for everything you read. The pixel face looks like it belongs to the camera, while the sans keeps long Chinese prose comfortable.

### Hierarchy
- **Pixel Display** (400, 24px / 32px): h1 and h2, the site name, post titles in the index, year headings, the post title, print titles, the Chinese album labels, Friends rows, 404 code.
- **Pixel Label** (400, 12px / 20px): nav items, buttons, badges, pagination, table headers, meta lines, figcaptions, the English album labels, print subheads and run-on lists (on 18px lines), footer copy, footnote chips.
- **Title** (700, 19 / 17 / 15px for h3 / h4 / h5-h6, line-height 1.5, system sans): in-body subheads.
- **Body** (400, 16px, 1.75): page prose.
- **Body Print** (400, 17px, 1.9): post bodies on the strip, which is at most 680px wide.
- **Body Album** (400, 14px, 1.65; 15px when the card is at least 340px wide): About strip prose.
- **Small sans steps** (15px subtitle, alert and footnote popup, 14px index preview, 13.5px sidenote and code): supporting text in the sans.

### Named Rules
**The Two Sizes Rule.** Ark Pixel appears at exactly 12px or 24px, weight 400, letter-spacing 0, with font smoothing off. Any other size, faux bold or tracking smears the pixel grid.

**The Prose Stays Sans Rule.** Paragraphs, lists of sentences, blockquotes and footnote text never use the pixel face. Pixel type is for interface, headings and short labels only.

## Layout

Content sits in a 1104px wide frame with 16px gutters (24px from 768px up). The header and footer span that frame; each page's reading column keeps its own measure and is centred in it: posts and comments at 680px, the home and tag indexes at 840px, Friends at 640px. From 1200px a post with footnotes is centred together with its 248px sidenote column, so the pair sits in the middle rather than the print alone.

All spacing uses the 4px unit (4, 8, 12, 16, 20, 24, 32, 48, 64, 96px). The 2px LCD pixel is used for frames, rules, underline thickness and focus outlines. Page content uses 32px top and 96px bottom padding; the About album uses 32px top and 64px bottom.

Breakpoints are 480px, 560px, 768px, 900px and 1200px. Below 768px the nav collapses to a 44px three-bar toggle that opens a full-width menu, and the birds on the rule hide while the menu is open. The About album is a static page laid out in CSS columns with 16px gaps: one column on phones, two from 560px, three from 900px, four from 1200px. Cards fill the columns top to bottom in `pixel_order`, which is chosen to balance column heights. On a desktop the whole album aims to fit one screen; on a phone it is one scroll. From 1200px the album heading is visually hidden (kept for screen readers), and footnotes become sidenotes in a 248px column beside the strip. Below that they open as a small torn print centred in the viewport.

**The Integer Scale Rule.** Every pixel of a pixel picture lands on whole device pixels, rendered with `image-rendering: pixelated`. The 112x84 album picture shows at x2 by default, at x3 when its card is at least 344px wide (phones and wide tablet columns), and at x1.5 (three device pixels) on hi-dpi desktops (at least 1200px wide and 2dppx), where the label moves beside the picture to save height. Low-dpi desktops keep x2 with the label underneath and may need a short scroll. The book cover is exempt: it is a 224px wide print shown at up to 112 CSS px (two print dots per CSS pixel) with smooth scaling.

## Elevation & Depth

The system is flat. Nothing casts a shadow, and the PaperCSS shadow utilities are forced off. Depth comes from tone and material instead: mid camera bodies sit on the dark ground, each picture on a screen sunk behind a 2px ground edge, and each paper strip feeds out of a 4px ground slot across the body's foot, covering the 8px lip below it; post strips feed out of a printer slot (an 8px ink bar) above them. `box-shadow` is used only as a drawing tool, for symmetric zero-blur 2px outlines (8px on the 404 viewfinder). Because the outline is drawn on all four sides with no spread, the corners come out notched, the way a pixel frame should. The only translucent layer is the footnote popup scrim.

### Named Rules
**The No Blur Rule.** No blur radius, no glow and no offset shadow anywhere. A frame is four 2px offsets of one tone.

## Shapes

All corners are square (0px radius). The form language is pixel geometry: notched frames, a toothed tear (an 8x4px tooth mask) along the bottom of every paper strip, dotted rules and dotted frames drawn as 2px-on/2px-off gradients, checkerboard dithers (the blockquote bar), square 4px list bullets, and sprites (magpie, tag end, cursor triangle, up arrow, bird tracks) painted through CSS masks. Sprites are one-tone. The magpie's white patches are left unpainted, so it only reads as a magpie on a light surface: an ink plate in the header, paper at the end of a post. The scrollbar thumb is also square.

## Components

### Buttons
Notched keys that reverse on contact.
- **Shape:** square, a 2px ink frame with notched corners, at least 40px tall, 16px horizontal padding, Pixel Label type.
- **Default:** ink on ground.
- **Hover:** reverse video (ground on ink). **Active:** moves down by one LCD pixel (2px). **Disabled:** mid text and a mid frame.
- **Focus:** a 2px ink outline offset by 2px (applies to every control).
- **Cursor variants** (Friends rows): no frame. On hover the triangle cursor appears and the row is reverse video.

### Badges
- **Style:** a pixel price tag, 22px tall: a mid body with ink Pixel Label, its left end a stepped point with a punched hole (the 6x11 `tag-end` sprite at x2), its right corners notched off by one LCD pixel. No outline. A tag that links reverses to ink on hover; on a lit (hovered) index row the tags turn ground, and a hovered one turns shade. In the index meta line the date drops the tag and reads as a plain stamp.

### Cards / Containers
- **Index rows:** each post is a full-width row with a dotted mid separator. On hover or focus-within the whole row reverses and the triangle cursor appears at its left.
- **Alerts:** a framed note in `currentColor`. Danger and warning become a solid print-black block with paper text.
- **Pagination:** 40px square framed cells. The current page is reversed, and hover fills with mid.

### Navigation
- **Header:** on the left a permanently reversed brand plate, 44px tall: the magpie (28x16 at x2: perched, tail as long as the body, legs showing, the eye one unpainted pixel) and the site name in Pixel Display, both ground on ink. On hover the magpie hops up one LCD pixel. Pixel Label items sit on the right, 44px tall. On phones the nav collapses to a menu key, a second 44px ink plate with three ground bars, which turns shade while the menu is open; plate and key share one row down to 375px. Nav hover and the current page (`aria-current`) reverse and show the cursor. A 2px ink rule closes the header and doubles as a wire: a strip of birds in their own plumage colours (`assets/img/pixel/perch.svg`, drawn in `_pixel/wire.py` as integer pixel cells with `shape-rendering="crispEdges"` to avoid bitmap background smoothing in WebKit; black plumage is lifted a step above true black, with a sheen on the crown, so it reads on the ground) sits on it, with tails hanging below; the upright blue-magpie has a long tail dropping 13 pixel rows (26 CSS px) below the wire. `assets/js/perch.js` renders individual SVG birds from generated `perch-birds.js` data, packed by `perch-flock.js` on an integer grid at ×2. Resizing extends the current sequence without reshuffling; the tiled SVG remains a fallback without JavaScript, and the decorative flock stays hidden from assistive technology; the header keeps 64px of sky under the nav so the tallest bird (the hunched night heron, 24 rows with its legs) clears it.
- **Footer:** shade Pixel Label copy above a 2px ink rule; links in ink.

### Print Strip (signature)
The reading surface. Paper ground, print text, square corners and a toothed bottom edge, fed from an 8px ink slot. Inside: Pixel Display headings, sans body, dithered blockquote bars, print-black code blocks and reverse print-black subheads. The post strip ends with the magpie at x2 in print, its white patches left as paper.

### Album Shot (signature)
Each About entry is a static card, all eight on the page at once, with no script or interaction; each card's id is its key, so `about.html#music` deep-links. A dark camera body (mid fill, 8px bezel) holds the 112x84 picture on a screen sunk behind a 2px notched ground edge, and under it the label: Chinese in Pixel Display, English in Pixel Label, both in ink. A 4px ground printer slot runs across the body's foot, 8px above its bottom edge. The paper strip feeds out of it, inset 8px (the slot overhangs it by 2px a side), and covers the lip below it, so the joint between picture and print is one hard line. The strip has a toothed bottom edge, Body Album prose and reverse print subheads. Lists print run-on: inline Pixel Label entries on 18px lines, each led by a 4px print-soft square. The works block is a 3fr/2fr grid with the printed book cover beside a dotted print-soft blank frame for the work in progress.

### Footnote Chips
Superscript numbers are drawn as small reversed print-black chips on the strip, matched by ink chips in the sidenote column.

## Do's and Don'ts

### Do:
- **Do** reference page roles (`--ground`, `--ink`, `--shade`, `--mid`) or paper roles (`--paper`, `--print`, `--print-soft`, `--print-faint`), never raw hex or the raw `--t0`-`--t3` tones.
- **Do** set every pixel label through the `pixel-type` mixin at 12px or 24px.
- **Do** keep spacing on the 4px scale and frames and rules at 2px.
- **Do** show hover, current and selected states as reverse video, adding the triangle cursor on menu-like rows.
- **Do** put long-form reading on a paper strip with the toothed edge, in the system sans.
- **Do** draw new pictures and sprites in `_pixel/` and regenerate them: pictures in the four screen tones, sprites as one-tone masks, each pixel landing on whole device pixels.
- **Do** honour reduced motion, and give every script-driven view a no-script fallback.

### Don't:
- **Don't** round corners, blur, glow, or add offset or soft shadows.
- **Don't** add a fifth tone, an off-palette grey or a brand accent to a screen region (the wire birds' own plumage is the only exception, and it never spreads to text, chrome or other art).
- **Don't** set text in mid or print-faint.
- **Don't** set the pixel face at sizes other than 12 or 24px, bold it, track it, or use it for paragraph prose.
- **Don't** use a white page with black-bordered dialog boxes, the Press Start 2P face, or an RPG stat-sheet look (the NES.css default this world rejects).
- **Don't** load fonts from external CDNs. Fonts are self-hosted for readers in mainland China.
- **Don't** caption drawn birds as real sightings. They are illustrations.
