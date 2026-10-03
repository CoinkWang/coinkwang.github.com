"""The birds on the header wire, each in its own plumage.

The one place the pixel theme leaves its four screen tones: every bird is a
species you can name at a glance and wears its own colours, a small fixed
palette per bird. Black plumage is drawn a shade lighter than true black
(with a sheen on the crown) so it still reads against the night ground.
Tails are allowed to hang below the wire. `.` is clear.

build.py exports individual birds to assets/js/perch-birds.js for the random
flock, plus assets/img/pixel/perch.{png,svg} as a static fallback.
"""

# name: (rows, index of the row that lies on the wire, palette)
BIRDS = {
    # 夜鹭: hunched shoulders, broad grey wing, black cap and mantle, red eye,
    # a heavy dagger bill, trailing white plumes and a tucked pale throat.
    "night_heron": ([
        "............KKKKKKK.........",
        "..........KKkkkkkkkk........",
        ".........Kkkkkkkkkkkk.......",
        "........ppkkkkkkkrwwwBBBBBBB",
        "......pppkkkkkkkwwwwwbbbbb..",
        "....pp..kkkkkkkwwwwwwbb.....",
        "...p..kkkkkkkkwwwwwww.......",
        ".....kkkGGgggggwwwwww.......",
        "....kkGGggggggggwwwww.......",
        "...kkGgggggggggggwwww.......",
        "...kGgggggggggggggwww.......",
        "..kGggggggggggggggwww.......",
        "..kGgggggggggggggGwww.......",
        "..kGggggggggggggGGwww.......",
        "...GggggggggggGGGwww........",
        "...GGgggggggGGGGwwww........",
        "..GGGGggggGGGGwwwww.........",
        ".GGGG....wwwwwwwww..........",
        "...........wwwwww...........",
        "............y..y............",
        "............y..y............",
        "............y..y............",
        "............y..y............",
        "...........yy..yy...........",
    ], 24, {'k': '#26333d', 'K': '#3d5361', 'p': '#f2f4ef', 'w': '#cbd3d1', 'g': '#8b9da6', 'G': '#657b87', 'r': '#d63c3c', 'B': '#4b5760', 'b': '#2e373d', 'y': '#d8b24a'}),
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
    # 红耳鹎: tall narrow posture, a needle crest, red ear and long slim tail.
    "red_whiskered_bulbul": ([
        ".....k........",
        ".....kk.......",
        ".....kk.......",
        "....kkk.......",
        "....kkkk......",
        "...kkekk......",
        ".bbkkwrk......",
        "...wwwrkn.....",
        "...wwwknn.....",
        "...wkkwnnn....",
        "....wwnnNn....",
        "....wwnnNnn...",
        "....wwnnnNn...",
        "....wwnnnNn...",
        ".....wwnnNn...",
        ".....wwrnnn...",
        "......rrntt...",
        "......l.lttt..",
        "......l.l.ttt.",
        ".....ll.ll.ttt",
        "...........tTw",
        "............ww",
    ], 20, {'k': '#2a2d31', 'e': '#b9b5a5', 'b': '#454541', 'r': '#df4c4b', 'w': '#eee9df', 'n': '#83705a', 'N': '#ad9677', 't': '#4e4841', 'T': '#c2b9a9', 'l': '#777165'}),
    # 乌鸫: sprinting low, bill thrust forward, tail streaming back and legs apart.
    "blackbird": ([
        "ttt......................",
        ".tttt....................",
        "..tHHtt.........HHHH.....",
        "...ttHHHH.....HHkkYkk....",
        ".....HHHHHHHHHkkkYkYkYYYY",
        "......HHkkgggkkkkkYkkYYY.",
        ".......HkkggGggkkkkkkk...",
        "........kkggggggkkkkkk...",
        ".........kkkkkkkkkkkk....",
        "..........kkkkkkkkkk.....",
        "...........l.....l.......",
        ".........ll.......l......",
        ".......ll..........l.....",
        "......lll..........lll...",
    ], 14, {'H': '#52616a', 'k': '#303b43', 'g': '#3d4951', 'G': '#627078', 'Y': '#e9b94f', 't': '#28333c', 'l': '#746551'}),
    # 麻雀: chestnut cap, white cheek with a black spot, bib and streaked wings.
    "tree_sparrow": ([
        "...cccc...........",
        "..cccccc..........",
        "..ckcccc..........",
        ".bbwwkwwc.........",
        "..bwwkwwcnnn......",
        "...kkwwnnNnnn.....",
        "..wwkwnNnnNnnn....",
        "..wwwwnnwnnNnnn...",
        "..wwwwwnnnnnnttt..",
        "...wwwwnnnnn.tttt.",
        "....wwwwww....tttt",
        ".....l.l..........",
        "....ll.ll.........",
    ], 13, {'c': '#a36640', 'k': '#302c28', 'b': '#6b6051', 'w': '#ded3ba', 'n': '#98764d', 'N': '#534333', 't': '#71604a', 'l': '#b18c70'}),
    # 鹊鸲: a separate white wing stripe, shaded small belly and an upright tail.
    "magpie_robin": ([
        "..............HHHH...",
        ".............Hkkkkk..",
        "............Hkkekkkb.",
        "............Hkkkkkkbb",
        ".t..........Hkkkkkk..",
        ".tt.........kkkkkk...",
        ".twt......HHkkkkkk...",
        "..twt...HHkkwkkkkk...",
        "...twt.HHkkwwkkkkk...",
        "....twtkkkwwkkkksw...",
        ".....tkkkkwkkkksww...",
        "......kkkkkkkssww....",
        ".......kkkkkssww.....",
        "........kksssss......",
        ".........l..l........",
        "........ll.ll........",
    ], 16, {'H': '#4a5d6b', 'k': '#283640', 'e': '#b7c7c9', 'b': '#424d54', 'w': '#edf0e9', 't': '#34424c', 'l': '#738087', 's': '#a7b9b5'}),

    # 棕背伯劳: grey crown, broad black eye-mask, warm back and long black tail.
    "long_tailed_shrike": ([
        ".............gggg...",
        "............gggggg..",
        "...........kkkekkkkb",
        "...........wwkkwwbbb",
        ".........nnnwwwww...",
        ".......nnnnnnwwww...",
        "......nnnnnkkkwww...",
        ".....nnnnkkwkkppp...",
        "....nnnkkkwwkkppp...",
        "...nnnkkkkkkkpppp...",
        "..nnkkkkkkkppppp....",
        "..kkk..pppppppp.....",
        ".kkk......l..l......",
        "kkkk......l..l......",
        "kk.......ll.ll......",
        "k...................",
    ], 15, {'g': '#aeb8b9', 'k': '#303a40', 'e': '#c7cdc7', 'b': '#555956', 'w': '#e2d9c5', 'n': '#c48751', 'p': '#d4b58c', 'l': '#757166'}),
    # 暗绿绣眼: tiny olive body, square white eye-ring, yellow throat and grey belly.
    "swinhoe_white_eye": ([
        "...gggg.......",
        "..ggwwwg......",
        ".bggwkwg......",
        "..ggwwwgnn....",
        "...yyggnnnn...",
        "...yygnNnnnn..",
        "...sssnnNnnnn.",
        "...ssssnnnnntt",
        "....ssssnnnttt",
        ".....sss..ttt.",
        ".....l.l......",
        "....ll.ll.....",
    ], 12, {'g': '#91ad48', 'w': '#f1f0d9', 'k': '#23332b', 'b': '#5d6550', 'y': '#d1c956', 'n': '#708e3d', 'N': '#adbd60', 's': '#c0c7ae', 't': '#5b783d', 'l': '#8c8370'}),
    # 家燕: blue-black crown and folded wings, russet throat and a deep forked tail.
    "barn_swallow": ([
        ".....BBBB..........",
        "....BBkkBB.........",
        "..bbkkekkk.........",
        "....ccckkBB........",
        "....cccwwBB........",
        "....wwwwwBBB.......",
        "....wwwwwwBBk......",
        ".....wwwwwBBk......",
        ".....wwwwwkBBk.....",
        "......wwwwkBBk.....",
        "......l.l..kBBk....",
        "............kkk....",
        "...........kk.kk...",
        "...........kk..kk..",
        "..........kk....kk.",
        "..........k......k.",
        ".........k........k",
    ], 11, {'B': '#416d89', 'k': '#263b50', 'b': '#444b4c', 'e': '#bdced0', 'c': '#b66d4c', 'w': '#d8ccb1', 'l': '#79756e'}),
    # 白鹡鸰: white face, a tiny heart-shaped black bib, grey saddle and a long tail.
    "white_wagtail": ([
        ".............kkkk...",
        "............kwwwww..",
        "............kwwewwb.",
        "............kwwwwwbb",
        "...........ggwwwww..",
        ".........ggggwkwkw..",
        ".......ggggggwkkkw..",
        "......gggkkwkwwkww..",
        ".....ggkkwwkkkwwww..",
        "....gkkkwkkkkwwwww..",
        "...tkkkwwkkkwwwww...",
        "..tkkk....wwwwww....",
        ".tkk.......l..l.....",
        "wkk........l..l.....",
        "wk.........l..l.....",
        "w.........ll.ll.....",
    ], 16, {'k': '#2b3840', 'w': '#e6e9e1', 'e': '#313b3e', 'b': '#555f62', 'g': '#929fa6', 't': '#65737d', 'l': '#7f8b90'}),
    # 红嘴蓝鹊: upright body, red bill and feet, white nape; the long blue
    # tail drops below the wire with a dark band and a white tip.
    "red_billed_blue_magpie": ([
        "..........kkkkk......",
        ".........kkwkkkk.....",
        "........kkkwwkkekrrr.",
        "........kkkwwkkkkrrrr",
        ".......BBBBwwkkkk....",
        "......BBBBBkkkkkw....",
        "......BBBBBBkkwww....",
        ".....BBBBbBBBwwww....",
        ".....BBBbbBBBwwww....",
        ".....BBbbBBBBwwww....",
        ".....BBbbBBBBwwww....",
        ".....BbbBBBBwwww.....",
        ".....bbBBBBwwww......",
        ".....bbBBBwwww.......",
        "....bbBBBBwww........",
        "....bbBBB.r..r.......",
        "....bBBBB.r..r.......",
        "....bBBB.rr..rr......",
        "....bBBB.............",
        "...bbBBB.............",
        "...bbBBB.............",
        "...bbBBB.............",
        "...bBBBB.............",
        "...bBBB..............",
        "..bbBBB..............",
        "..bbBBB..............",
        "..bBBB...............",
        "..bBBB...............",
        "..kkkk...............",
        "..kkkk...............",
        "..wwww...............",
        "...ww................",
    ], 18, {'k': '#2d3641', 'w': '#dce4e4', 'e': '#bdcad1', 'r': '#db654e', 'B': '#668ec0', 'b': '#3d608f'}),

}

# One tile of the strip, left to right. Each bird stands as close to the
# last as it can with at least GAP clear pixels between them on every row,
# so a tail hanging under the wire can tuck beneath the next bird's feet.
# The tile ends the same way before the first bird comes round again, so the
# repeats run on as one unbroken line of birds.
LAYOUT = list(BIRDS)
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
