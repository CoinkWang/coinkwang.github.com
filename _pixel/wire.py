"""The birds on the header wire, each in its own plumage.

The one place the pixel theme leaves its four screen tones: every bird is a
species you can name at a glance and wears its own colours, a small fixed
palette per bird. Black plumage is drawn a shade lighter than true black
(with a sheen on the crown) so it still reads against the night ground.
Tails are allowed to hang below the wire. `.` is clear.

build.py writes the strip to assets/img/pixel/perch.{png,svg}; _layout.scss
tiles the SVG along the header's bottom rule, which is the wire.
"""

# name: (rows, index of the row that lies on the wire, palette)
BIRDS = {
    # 夜鹭 Black-crowned Night Heron, the hunched pose of the memes: an egg
    # of a body with the head sunk straight into the shoulders, the black
    # cap pulled down to a glaring red eye and running on down the back like
    # a cape, white plumes along it, grey wings, a white bib, a thick bill,
    # and yellow legs showing underneath
    "night_heron": ([
        "........KKKKKK..........",
        "......kkkkkkkkkk........",
        ".....kkkkkkkkkkkk.......",
        "....kkkkkkkkkkkkkk......",
        "...kkpkkkkkkkkrwwwBBBBBB",
        "...kkpkkkkkkwwwwwwbbbbb.",
        "..kkpkkkkkwwwwwwwww.....",
        "..kkpkkkkwwwwwwwwww.....",
        "..kpkkkggwwwwwwwwww.....",
        ".kkpkkgggwwwwwwwwww.....",
        ".kkpkggggGwwwwwwwww.....",
        ".kkkggggGggwwwwwwww.....",
        ".kkgggGgggGgwwwwwww.....",
        ".kggGgggGgggwwwwwww.....",
        ".gggggGgggGgwwwwwww.....",
        ".ggGgggggGggwwwwwww.....",
        "..gggGgggggGwwwwww......",
        "GGggggggGgggwwwwww......",
        "GGG.gggggGggwwwww.......",
        "GG....ggggggwwww........",
        ".......wwwwwwww.........",
        ".........y...y..........",
        ".........y...y..........",
        ".........y...y..........",
        ".........y...y..........",
        "........yyy.yyy.........",
    ], 26, {
        "k": "#26333d", "K": "#3d5361", "p": "#f2f4ef", "w": "#dde4df",
        "g": "#95a1a7", "G": "#6f7c84", "r": "#d63c3c",
        "B": "#4b5760", "b": "#2e373d", "y": "#d8b24a",
    }),
    # 珠颈斑鸠 Spotted Dove: small grey head, pinkish breast, brown back with
    # dark-centred coverts, the black collar strewn with white pearls, a long
    # tail with white corners hanging past the wire
    "spotted_dove": ([
        "...hhh................",
        "..hhhhh...............",
        ".bhkhhh...............",
        "..hhhhh...............",
        "...hhcwcwc............",
        "..pphwcwcwnnnn........",
        ".ppppnnnnnnnnn........",
        ".ppppnnNnnnNnnn.......",
        ".pppppnnnNnnnNnn......",
        "..ppppnnnnnnnnnnn.....",
        "...ppppnnnnnnnnnnn....",
        ".....l.l.....tttttt...",
        "...............tttttt.",
        "................ttttT.",
        "..................tTTT",
    ], 12, {
        "h": "#aaa6ae", "k": "#2a2224", "b": "#4c4040", "c": "#262020",
        "w": "#efe9e0", "p": "#c49a8e", "n": "#8f6d55", "N": "#624838",
        "l": "#c86e66", "t": "#5f4d41", "T": "#e9e3d9",
    }),
    # 白头鹎 Light-vented Bulbul, facing left: a black head with the broad
    # white band across the back of the crown, a white ear spot and throat,
    # a grey-brown breast band, olive back, wings and tail edged yellow-green
    "bulbul": ([
        "...kkkk.........",
        "..kkkkkW........",
        ".kkkkkWWW.......",
        "kkkkkWWWk.......",
        ".WkWWkkkgg......",
        ".WWkkkgggg......",
        ".bbbbggggggg....",
        ".bbbgggygggy....",
        ".wwbggggyggyg...",
        "..wwwgggyggyg...",
        "..wwwwgggyggyy..",
        "...wwwwgggyyyy..",
        "....l.l...gyyy..",
        "...........gyyy.",
        "............gyy.",
    ], 13, {
        "k": "#2a2d31", "W": "#f1f0ea", "g": "#7f8668", "y": "#a9b24c",
        "b": "#9b9486", "w": "#e4e2d9", "l": "#4a4744",
    }),
    # 戴胜 Hoopoe: the cinnamon fan crest, each feather tipped white then
    # black; a long down-curved bill; black-and-white barred wings and tail
    "hoopoe": ([
        ".........kkkk.........",
        ".......kkwwwwkk.......",
        "......kwooooowk.......",
        ".....kwoooooooowk.....",
        ".......oooooooo.......",
        "........ooooooo.......",
        ".........ooooooo......",
        ".........oooookob.....",
        "........ooooooOObbb...",
        "......oooooooOO....bb.",
        "....kwkwkwkwOOO......b",
        "...kwkwkwkwkOOO.......",
        "kkkwkwkwkwkOOO........",
        "wwk.OOOOOOOOO.........",
        "........l.l...........",
        ".......ll.ll..........",
    ], 16, {
        "o": "#e3a06a", "O": "#c98552", "k": "#24201e", "w": "#f2eee6",
        "b": "#5a524b", "l": "#79726b",
    }),
    # 普通翠鸟 Common Kingfisher: blue crown and wings flecked with azure, an
    # azure stripe down the back, orange cheek and breast, white neck patch,
    # a dagger bill (orange underneath, as on a female), red feet
    "kingfisher": ([
        "...BBBB.........",
        "..BcBBcB........",
        "..BookoKKKKKKK..",
        ".BBwBwwrrrrr....",
        ".cBBoooo........",
        ".cBBBooo........",
        ".cBcBooo........",
        ".cBBBoo.........",
        ".BBBooo.........",
        "BB..rr..........",
        "B...............",
    ], 10, {
        "B": "#1f74b6", "c": "#38c7ea", "o": "#e8792f", "w": "#f1f0e8",
        "k": "#141a20", "K": "#353c43", "r": "#d9532c",
    }),
}

# One tile of the strip, left to right. Each bird stands as close to the
# last as it can with at least GAP clear pixels between them on every row,
# so a tail hanging under the wire can tuck beneath the next bird's feet.
# The tile ends the same way before the first bird comes round again, so the
# repeats run on as one unbroken line of birds.
LAYOUT = ["night_heron", "spotted_dove", "bulbul", "hoopoe", "kingfisher"]
GAP = 3


def strip():
    """The tile as rows of hex colours (None = clear), with the wire's row
    index and the number of rows below the wire."""
    above = max(wi for _, wi, _ in BIRDS.values())
    below = max(len(rows) - wi - 1 for rows, wi, _ in BIRDS.values())
    h = above + 1 + below

    def pixels(name):
        rows, wi, palette = BIRDS[name]
        assert len(set(map(len, rows))) == 1, name
        top = above - wi
        return [(i, top + j, palette[ch]) for j, row in enumerate(rows)
                for i, ch in enumerate(row) if ch not in ". "]

    def fits(px, x, taken):
        return all(not any((x + i + d, y) in taken for d in range(-GAP, GAP + 1))
                   for i, y, _ in px)

    taken, placed, x = set(), [], 0
    for name in LAYOUT:
        px = pixels(name)
        while placed and not fits(px, x, taken):
            x += 1
        placed.append((x, px))
        taken |= {(x + i, y) for i, y, _ in px}
        x += 1

    # the tile is as wide as it takes for the first bird to come round again
    first = placed[0][1]
    width = max(i for i, _ in taken) + 1
    while not fits(first, width, taken):
        width += 1

    grid = [[None] * width for _ in range(h)]
    for x0, px in placed:
        for i, y, colour in px:
            grid[y][x0 + i] = colour
    return grid, above, below
