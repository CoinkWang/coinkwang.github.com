"""Cut the pixel font down to the characters the built site actually uses.

Runs after `jekyll build`; the Pages workflow (.github/workflows/pages.yml)
does this on every deploy:

    python3 _pixel/subset_font.py [_site]

It collects every character in the built HTML, CSS and JS (markup and
attribute values included: tooltips such as the friends page's popover-top
are drawn from attributes by CSS), keeps all printable ASCII and the common
CJK punctuation, and writes ark-pixel-subset.woff2 next to the full font in
the built site. Nothing is written to the source tree.

assets/fonts/pixel.css lists the subset first and the full font after it as
'Ark Pixel Full', so a character the subset lacks only costs that page the
full download; nothing ever renders missing. Locally, where the subset is
never built, every page simply uses the full font.

The full font has gaps of its own (旅, 然, 摇 ... and every emoji). Without a
unicode-range a browser downloads it just to find such a character missing,
so the built pixel.css also gets a unicode-range on 'Ark Pixel Full' that
leaves out the site's characters the full font lacks.

Needs fonttools and brotli (pip install fonttools brotli).
"""

import html
import os
import re
import sys

from fontTools import subset
from fontTools.ttLib import TTFont

FONT_DIR = os.path.join("assets", "fonts", "ark-pixel")
FULL = "ark-pixel-12px-proportional-zh_hans.otf.woff2"
SUBSET = "ark-pixel-subset.woff2"

# Always kept, whatever the pages say: new titles in English or with ordinary
# punctuation never fall back to the full font
ALWAYS = (
    "".join(chr(c) for c in range(0x20, 0x7F))
    + "，。、；：？！…—–·“”‘’「」『』（）《》〈〉【】〔〕～￥％＋－＝×÷"
)

# the full face's family line, and the range a previous run added after it
FULL_FACE = re.compile(r"(font-family:\s*['\"]Ark Pixel Full['\"];)(\n\s*unicode-range:[^;]*;)?")


def site_chars(site):
    chars = set(ALWAYS)
    pages = 0
    for root, _, files in os.walk(site):
        for name in files:
            path = os.path.join(root, name)
            if not name.endswith((".html", ".css", ".js")):
                continue
            with open(path, encoding="utf-8", errors="ignore") as f:
                # entities too: &ldquo; and &#x65c5; are characters on screen
                chars |= set(html.unescape(f.read()))
            pages += name.endswith(".html")
    return chars, pages


def unicode_range_without(points):
    """A CSS unicode-range covering everything except `points` (sorted)."""
    spans, start = [], 0
    for p in points:
        if p > start:
            spans.append((start, p - 1))
        start = p + 1
    spans.append((start, 0x10FFFF))
    return ", ".join("U+%X" % a if a == b else "U+%X-%X" % (a, b) for a, b in spans)


def fence_full_font(site, missing):
    css = os.path.join(site, "assets", "fonts", "pixel.css")
    with open(css, encoding="utf-8") as f:
        text = f.read()
    if not FULL_FACE.search(text):
        print("subset_font: no 'Ark Pixel Full' face in %s, left as is" % css)
        return
    rule = r"\1\n  unicode-range: %s;" % unicode_range_without(missing)
    with open(css, "w", encoding="utf-8") as f:
        f.write(FULL_FACE.sub(rule, text, count=1))


def main(site="_site"):
    font_dir = os.path.join(site, FONT_DIR)
    full = os.path.join(font_dir, FULL)
    if not os.path.exists(full):
        print("subset_font: no %s in this build, nothing to do" % full)
        return

    chars, pages = site_chars(site)
    cmap = TTFont(full).getBestCmap()
    unicodes = sorted(ord(c) for c in chars if ord(c) in cmap)
    missing = sorted(ord(c) for c in chars if ord(c) not in cmap)

    options = subset.Options()
    options.flavor = "woff2"
    options.layout_features = ["*"]
    options.name_IDs = ["*"]
    options.notdef_outline = True
    font = subset.load_font(full, options)
    subsetter = subset.Subsetter(options)
    subsetter.populate(unicodes=unicodes)
    subsetter.subset(font)
    out = os.path.join(font_dir, SUBSET)
    subset.save_font(font, out, options)
    fence_full_font(site, missing)

    print(
        "subset_font: %d pages, %d of %d glyphs kept, %.0f KB -> %.0f KB (%s); "
        "%d characters the full font lacks fenced off"
        % (pages, len(unicodes), len(cmap),
           os.path.getsize(full) / 1024, os.path.getsize(out) / 1024, out,
           len(missing))
    )


if __name__ == "__main__":
    main(*sys.argv[1:2])
