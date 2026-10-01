"""One-tone pixel sprites for the `pixel` theme, emitted as SVG masks.

Every mask is coloured by CSS (`background: var(--ink)`), so the sprites use
the same tokens as everything else. `#` is a lit pixel.
"""

MAGPIE = [  # the brand: a magpie perched, facing right. # black; o white, left
            # unpainted so the light surface behind shows through; the eye
            # is a single unpainted pixel
    "....................####....",
    "...................######...",
    "...................##.######",
    "..................########..",
    ".................#######....",
    "............############....",
    "...........##ooooo######....",
    ".........##oooooo######.....",
    "........##############......",
    ".......#######oooooo##......",
    ".....########ooooooo#.......",
    "...#####.####oooooo#........",
    ".#####......#######.........",
    "###...........#..#..........",
    "..............#..#..........",
    ".............##.##..........",
]


def layer(rows, ch):
    """The pixels marked `ch`, as a one-tone mask."""
    return ["".join("#" if c == ch else "." for c in r) for r in rows]


FOOTPRINTS = [  # a trail of three-toed tracks
    "#.#.#...........#.#.#...........",
    ".###.............###............",
    "..#...............#.............",
    "..#....#.#.#......#.....#.#.#...",
    "........###..............###....",
    ".........#................#.....",
    ".........#................#.....",
]

UP = [
    ".......##.......",
    "......####......",
    ".....######.....",
    "....########....",
    "...##########...",
    "..############..",
    "......####......",
    "......####......",
    "......####......",
    "......####......",
    "......####......",
]

CURSOR = [
    "#...",
    "##..",
    "###.",
    "####",
    "###.",
    "##..",
    "#...",
]

# The pointed end of a tag, with its punched hole; the body is a plain fill
TAG_END = [
    ".....#",
    "....##",
    "...###",
    "..####",
    ".#####",
    "##.###",
    ".#####",
    "..####",
    "...###",
    "....##",
    ".....#",
]

TEETH_TOP = [".##.", "####"]
TEETH_BOTTOM = ["####", ".##."]


def svg(rows):
    h = len(rows)
    w = max(len(r) for r in rows)
    d = []
    for y, row in enumerate(rows):
        x = 0
        while x < len(row):
            if row[x] == "#":
                s = x
                while x < len(row) and row[x] == "#":
                    x += 1
                d.append("M%d %dh%dv1h-%dz" % (s, y, x - s, x - s))
            else:
                x += 1
    return ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 %d %d' "
            "shape-rendering='crispEdges'><path d='%s'/></svg>" % (w, h, "".join(d))), w, h


def all_masks():
    out = {}
    out["magpie"] = layer(MAGPIE, "#")
    out["tracks"] = FOOTPRINTS
    out["up"] = UP
    out["cursor"] = CURSOR
    out["tag-end"] = TAG_END
    out["teeth-top"] = TEETH_TOP
    out["teeth-bottom"] = TEETH_BOTTOM
    return out
