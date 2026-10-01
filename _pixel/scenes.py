"""The eight album pictures (112 x 84, four tones) for the About page."""
import math
from paint import Canvas

W, H = 112, 84

MAGPIE = [
    ".....0000...........................",
    "....000000..........................",
    "...00002000.........................",
    "0000000000000.......................",
    "..0000000000000.....................",
    "....00000000000000..................",
    ".....0000000000000000...............",
    ".....00000003333300000..............",
    ".....000000333333111100.............",
    ".....0000003333311111100............",
    ".....33000033331111111110...........",
    ".....333333000011111111100..........",
    ".....3333333300111111111110.........",
    "......33333333300111111111000.......",
    "......3333333333300011111000000.....",
    ".......2333333333300000000011110....",
    "........22333333000........0011110..",
    "..........22200000...........001110.",
    "............0..0...............00110",
    "............0..0.................000",
    "...........00.00....................",
]

FAR_BIRD = [".00.00.", "0..0..0"]

CONTROLLER = [
    "0000000000000000000000",
    "0222222222222222222220",
    "0220222222222222222220",
    "0200022211211220020020",
    "0220222222222220020020",
    "0222222222222222222220",
    "0000000000000000000000",
]

HERO = [  # the little platformer on the TV
    ".00.",
    "0220",
    ".00.",
    "0000",
    ".00.",
    "0..0",
]

SHUTTLE = [
    "0.0.0.0.0",
    "030303030",
    ".0303030.",
    ".0333330.",
    "..03330..",
    "..03330..",
    "...000...",
    "..00000..",
    "..00000..",
    "...000...",
]

FIGURINE = [
    "..00....",
    ".0000...",
    "00200...",
    ".00000..",
    "..000000",
    "..00000.",
    "...0.0..",
    "..00000.",
]


def leaf(c, x0, y0, length, angle, width, v, vein=None):
    a = math.radians(angle)
    ux, uy = math.cos(a), math.sin(a)
    px, py = -uy, ux
    pts_l, pts_r = [], []
    steps = 10
    for i in range(steps + 1):
        t = i / steps
        w = width * math.sin(math.pi * t)
        cx, cy = x0 + ux * length * t, y0 + uy * length * t
        pts_l.append((cx + px * w, cy + py * w))
        pts_r.append((cx - px * w, cy - py * w))
    c.poly(pts_l + pts_r[::-1], v)
    if vein is not None:
        c.line(x0, y0, x0 + ux * length * 0.8, y0 + uy * length * 0.8, vein)


def birding():
    c = Canvas(W, H, 3)
    c.vgrad(0, 60, 3.0, 2.3)
    for x, y in [(84, 10), (93, 6), (100, 13)]:
        c.sprite(x, y, FAR_BIRD, remap={0: 1})
    c.ridge(0, W, 62, 7, 3, 2.0)
    c.ridge(0, W, 72, 6, 11, 1.25)
    c.rect(0, 80, W, H, 1)
    # branch reaching in from the left
    c.line(0, 58, 28, 52, 0, w=3)
    c.line(28, 52, 64, 46, 0, w=2)
    c.line(64, 46, 104, 42, 0)
    c.line(104, 42, 110, 38, 0)
    c.line(20, 54, 14, 40, 0, w=2)
    c.line(14, 40, 9, 30, 0)
    c.line(84, 44, 90, 36, 0)
    for (lx, ly, ln, ang) in [(9, 30, 8, 250), (12, 36, 7, 200), (14, 41, 8, 320),
                              (90, 36, 7, 300), (88, 38, 6, 20), (7, 32, 6, 160)]:
        leaf(c, lx, ly, ln, ang, 2.2, 1)
    c.sprite(42, 25, MAGPIE)
    # viewfinder focus brackets
    x0, y0, x1, y1 = 36, 16, 82, 50
    for (ax, ay, dx, dy) in [(x0, y0, 1, 1), (x1, y0, -1, 1), (x0, y1, 1, -1), (x1, y1, -1, -1)]:
        c.line(ax, ay, ax + dx * 5, ay, 0)
        c.line(ax, ay, ax, ay + dy * 5, 0)
    return c


def gaming():
    c = Canvas(W, H, 1)
    c.rect(0, 62, W, H, 0.5)
    c.radial(57, 70, 46, 2.1, 0.5, ry=14)
    c.rect(0, 0, W, 60, 1.25)
    for x in range(4, W, 8):
        c.rect(x, 0, x + 1, 60, 1)
    c.rect(0, 60, W, 62, 0)
    # stand
    c.rect(24, 54, 88, 58, 0)
    c.rect(27, 58, 30, 66, 0)
    c.rect(82, 58, 85, 66, 0)
    # CRT
    c.rect(30, 20, 84, 54, 2)
    c.frame(30, 20, 84, 54, 0)
    for (x, y) in [(30, 20), (83, 20), (30, 53), (83, 53)]:
        c.put(x, y, 1)
    c.rect(34, 24, 72, 50, 0)
    c.rect(35, 25, 71, 49, 3)
    for (x, y) in [(35, 25), (70, 25), (35, 48), (70, 48)]:
        c.put(x, y, 0)
    # the game on screen
    c.rect(35, 44, 71, 49, 1)
    for x in range(35, 71, 4):
        c.put(x, 44, 2)
        c.put(x + 2, 46, 2)
    c.rect(48, 35, 58, 37, 1)
    c.put(52, 35, 2)
    c.ellipse(63.5, 31.5, 1.5, 2, 2)
    c.sprite(40, 38, HERO)
    c.rect(66, 38, 70, 44, 0)
    c.rect(65, 37, 71, 39, 0)
    # panel
    c.rect(74, 26, 81, 49, 1)
    c.ellipse(77.5, 30.5, 2, 2, 0)
    c.ellipse(77.5, 36.5, 2, 2, 0)
    for y in (41, 43, 45, 47):
        c.rect(75, y, 80, y + 1, 0)
    # antenna
    c.ellipse(57, 20, 6, 2, 0)
    c.line(54, 19, 44, 4, 0)
    c.line(60, 19, 72, 3, 0)
    # controller and cord
    c.line(30, 64, 33, 70, 0)
    c.line(28, 58, 30, 64, 0)
    c.sprite(34, 70, CONTROLLER)
    return c


def writing():
    c = Canvas(W, H, 1.5)
    for y in (5, 18, 31, 64, 79):
        for x in range(W):
            if (x * 7 + y) % 13 < 8:
                c.put(x, y + ((x // 11) % 2), 1)
    # notebook
    c.rect(9, 13, 57, 75, 3)
    c.rect(57, 13, 103, 75, 3)
    c.rect(9, 75, 103, 77, 2)
    c.rect(53, 13, 57, 75, 2.75)
    c.rect(56, 13, 57, 77, 2)
    c.frame(8, 12, 104, 78, 0)
    seed = 7
    for i, y in enumerate(range(22, 72, 6)):
        for x in list(range(13, 52, 2)) + list(range(61, 100, 2)):
            c.put(x, y, 2)
        # handwriting: left page full, right page four lines
        for (xa, xb, full) in [(13, 52, True), (61, 100, i < 4)]:
            if not full:
                continue
            x = xa
            while x < xb - 3:
                seed = (seed * 1103515245 + 12345) & 0x7FFFFFFF
                n = 3 + seed % 8
                end = min(x + n, xb if (i % 3 or xa != 13) else xb - 10)
                if end <= x:
                    break
                for xx in range(x, end):
                    c.put(xx, y - 2 + ((xx + seed) % 3 == 0), 0)
                x = end + 2
    # pen
    c.line(68, 58, 104, 28, 0, w=2)
    c.line(105, 27, 110, 23, 0, w=2)
    c.poly([(63, 63), (68, 57), (70, 59)], 2)
    c.line(96, 32, 90, 37, 2)
    # cup
    c.ellipse(100, 76, 11, 10, 3)
    c.ellipse(100, 76, 8, 7, 0)
    c.ellipse(97, 73, 3, 2, 1)
    c.rect(86, 74, 89, 79, 3)
    return c


def reading():
    c = Canvas(W, H, 2.5)
    c.rect(6, 6, 106, 84, 1.5)
    c.rect(4, 2, 108, 6, 0)
    c.rect(4, 2, 8, 84, 0)
    c.rect(104, 2, 108, 84, 0)
    c.rect(4, 40, 108, 43, 0)
    c.rect(4, 79, 108, 82, 0)
    c.rect(8, 43, 104, 45, 1)
    c.rect(8, 6, 104, 8, 1)

    def shelf(x, base, books):
        for (w, h, v) in books:
            if v == "lean":
                c.poly([(x, base), (x + 5, base), (x + 13, base - 21), (x + 8, base - 23)], 0)
                c.line(x + 4, base - 4, x + 10, base - 18, 2)
                x += 12
                continue
            c.rect(x, base - h, x + w, base, v)
            band = 3 if v < 2 else 0
            c.rect(x, base - h + 3, x + w, base - h + 4, band)
            c.rect(x, base - 5, x + w, base - 4, band)
            if w >= 5:
                c.rect(x + w // 2, base - h + 7, x + w // 2 + 1, base - 9, band if v != 1 else 2)
            x += w
        return x

    x = shelf(9, 40, [(5, 26, 0), (4, 22, 2), (6, 29, 1), (3, 20, 3), (5, 25, 0),
                      (7, 28, 2), (4, 23, 1), (5, 27, 3), ("", "", "lean")])
    c.sprite(x + 4, 32, FIGURINE)
    shelf(x + 16, 40, [(6, 24, 1), (5, 30, 0), (4, 21, 2), (6, 26, 3), (4, 28, 0),
                       (5, 22, 1)])
    x = shelf(9, 79, [(4, 28, 2), (6, 31, 0), (5, 25, 3), (4, 29, 1), (7, 26, 2),
                      (5, 30, 0), (3, 22, 3), (6, 27, 1), (5, 24, 0), (4, 30, 2),
                      (6, 26, 3)])
    # an e-reader leaning on the last book
    c.poly([(x + 2, 79), (x + 16, 79), (x + 22, 52), (x + 8, 52)], 0)
    c.poly([(x + 5, 76), (x + 15, 76), (x + 20, 55), (x + 10, 55)], 3)
    for k in range(4):
        y = 59 + k * 4
        dx = int((y - 55) * 6 / 21)
        c.line(x + 19 - dx - 7, y, x + 19 - dx - 1, y, 1)
    return c


def gardening():
    c = Canvas(W, H, 1.5)
    c.rect(0, 64, W, H, 1.25)
    # window
    c.rect(12, 4, 72, 60, 0)
    for (x0, y0, x1, y1) in [(16, 8, 41, 30), (44, 8, 68, 30), (16, 33, 41, 56), (44, 33, 68, 56)]:
        c.vgrad(y0, y1, 3.0, 2.6, x0, x1)
    c.ellipse(25, 16, 6, 2, 3)
    c.ellipse(30, 15, 4, 2, 3)
    c.ellipse(58, 22, 5, 2, 3)
    c.ellipse(58, 44, 9, 8, 2)
    c.ellipse(52, 48, 7, 6, 2)
    c.rect(56, 50, 58, 56, 1)
    c.ellipse(22, 54, 7, 4, 2)
    c.ellipse(33, 53, 7, 5, 2)
    c.rect(8, 58, 76, 62, 0)
    c.rect(10, 62, 74, 64, 1)
    # pot and plant
    c.poly([(28, 44), (48, 44), (45, 58), (31, 58)], 1)
    c.rect(27, 42, 49, 45, 0)
    for x in range(31, 46, 3):
        c.put(x, 50, 2)
    stems = [(38, 42, 30, 26), (38, 42, 44, 22), (38, 42, 50, 34), (38, 42, 27, 36), (38, 42, 37, 18)]
    for (sx, sy, ex, ey) in stems:
        c.line(sx, sy, ex, ey, 0)
    for (lx, ly, ln, ang, w, v) in [(30, 26, 14, 215, 5.5, 0), (44, 22, 14, 305, 6, 1),
                                    (50, 34, 13, 340, 5, 0), (27, 36, 12, 180, 4.5, 1),
                                    (37, 18, 13, 265, 5.5, 0)]:
        leaf(c, lx, ly, ln, ang, w, v, vein=2)
    # watering can
    c.rect(13, 50, 23, 58, 2)
    c.frame(13, 50, 23, 58, 0)
    c.line(23, 53, 28, 47, 0, w=2)
    c.rect(27, 46, 30, 48, 0)
    c.ring(13, 53, 4, 0, t=1.5)
    c.rect(15, 48, 21, 50, 0)
    # pressed ginkgo in a frame
    c.rect(80, 12, 106, 48, 0)
    c.rect(82, 14, 104, 46, 3)
    cx, cy, r = 93, 36, 10
    for y in range(cy - r, cy + 1):
        for x in range(cx - r, cx + r + 1):
            d = math.hypot(x + 0.5 - cx, y + 0.5 - cy)
            ang = math.degrees(math.atan2(cy - (y + 0.5), x + 0.5 - cx))
            if d <= r and 35 <= ang <= 145 and not (86 <= ang <= 94 and d > r - 4):
                c.put(x, y, 1 if int(ang) % 9 else 2)
    c.line(93, 36, 93, 42, 1)
    c.rect(88, 43, 99, 44, 2)
    return c


def fitness():
    c = Canvas(W, H, 3)
    c.vgrad(0, 58, 3.0, 2.35)
    c.ellipse(24, 14, 9, 3, 3)
    c.ellipse(30, 12, 6, 3, 3)
    c.rect(16, 16, 36, 17, 2.5)
    c.ridge(0, W, 60, 10, 5, 2.0)
    c.ridge(0, W, 67, 5, 17, 1.5)
    c.rect(0, 70, W, H, 1)
    c.rect(0, 70, W, 71, 0)
    for x in range(2, W, 12):
        c.rect(x, 77, x + 6, 78, 3)
    # small-wheel folding bike, parked: little wheels, one long main tube with
    # its hinge, a tall handlepost and a long seatpost
    R, F, wy = 36, 76, 61
    for hx in (R, F):
        c.ring(hx, wy, 8.5, 0, t=2)
        c.ring(hx, wy, 6.5, 1, t=1)
        for a in (0, 60, 120):
            r = math.radians(a)
            c.line(hx - 5 * math.cos(r), wy - 5 * math.sin(r), hx + 5 * math.cos(r), wy + 5 * math.sin(r), 1)
        c.rect(hx - 1, wy - 1, hx + 1, wy + 1, 0)
        # mudguard over the top of the wheel
        for a in range(196, 345, 2):
            r = math.radians(a)
            c.put(hx + 10.5 * math.cos(r), wy + 10.5 * math.sin(r), 1)
    bb = (53, 62)
    c.line(R, wy, bb[0], bb[1], 0, w=2)          # rear frame
    c.line(R, wy, 47, 51, 0, w=2)
    c.rect(46, 50, 50, 53, 1)                    # suspension block
    c.line(bb[0], bb[1], 49, 41, 0, w=2)         # seat tube
    c.line(49, 41, 48, 33, 1, w=2)               # long seatpost
    c.rect(42, 31, 53, 33, 0)                    # saddle
    c.rect(44, 33, 50, 34, 0)
    c.line(49, 49, 70, 45, 0, w=2)               # main tube
    c.rect(58, 45, 61, 49, 1)                    # hinge clamp
    c.line(70, 43, 72, 51, 0, w=2)               # head tube
    c.line(72, 51, F, wy, 0, w=2)                # fork
    c.line(70, 44, 68, 27, 1, w=2)               # handlepost
    c.rect(63, 25, 75, 27, 0)                    # bar
    c.rect(63, 27, 65, 30, 0)
    c.rect(73, 27, 75, 30, 0)
    c.rect(73, 40, 75, 44, 1)                    # front carrier block
    c.rect(75, 37, 86, 49, 2)                    # front bag
    c.frame(75, 37, 86, 49, 0)
    c.rect(75, 37, 86, 41, 1)
    c.rect(79, 41, 82, 43, 0)
    c.ring(bb[0], bb[1], 4.5, 0, t=1.5)          # chainring and crank
    c.line(bb[0], bb[1], 57, 67, 0, w=2)
    c.rect(55, 67, 61, 68, 0)
    # shuttlecock in flight
    c.sprite(96, 8, SHUTTLE)
    for k in range(3):
        c.line(92 - k * 5, 22 + k * 3, 94 - k * 5, 21 + k * 3, 1)
    return c


GUITAR = [
    ".........000..........",
    "........01110.........",
    "........011130........",
    "........0111110.......",
    "........01111130......",
    "........0111110.......",
    "........0111130.......",
    "........011110........",
    ".........0110.........",
    ".........0110.........",
    ".........0130.........",
    ".........0110.........",
    ".........0110.........",
    ".........0110.........",
    ".........0130.........",
    ".........0110.........",
    ".........0110.........",
    ".........0110.........",
    ".........0130.........",
    ".........0110.........",
    ".........0110.........",
    ".........0110.........",
    ".........0130.........",
    ".........0110.........",
    ".........0110.........",
    ".........0110.........",
    "..00.....0130.........",
    ".0220....0110....00...",
    ".02220...0110...0220..",
    ".022220..0110..02220..",
    ".0222220.0110.022220..",
    ".02222220011002222220.",
    ".0222223333333322220..",
    "..022233003333332220..",
    "..022233333333333220..",
    "...02233300333333220..",
    "...02233333333332220..",
    "...022333333300332220.",
    "..0222333333333332220.",
    ".022223333333333322220",
    ".022222333333330322220",
    "0222222233300333222220",
    "0222222223333330222220",
    "0222222222222222222220",
    "0222222220000222222220",
    "0222222222222222222220",
    ".022222222222222222220",
    ".02222222222222222220.",
    "..022222222222222220..",
    "...0222222222222220...",
    "....00022222222000....",
    ".......00000000.......",
]

ERHU = [
    "...00.......",
    "..0220......",
    "..0220......",
    "...020......",
    "...020......",
    "...02000000.",
    "...02033330.",
    "...02000000.",
    "...020......",
    "...020......",
    "...02000000.",
    "...02033330.",
    "...02000000.",
    "...020......",
] + ["..3020......"] * 6 + [".33320......"] + ["..3020......"] * 37 + [
    ".00000000...",
    "0222222220..",
    "0211111120..",
    "0213111120..",
    "0211111120..",
    "0211111120..",
    "0222222220..",
    ".00000000...",
    "...020......",
    "...020......",
    "..00000.....",
]


def music():
    c = Canvas(W, H, 0)
    c.rect(0, 0, W, H, 0.35)
    c.poly([(40, 0), (58, 0), (92, 76), (8, 76)], 1)
    c.poly([(45, 0), (53, 0), (74, 76), (24, 76)], 1.5)
    c.rect(0, 76, W, H, 0.5)
    c.ellipse(50, 78, 38, 5, 2)
    # amp
    c.rect(80, 42, 108, 78, 1)
    c.frame(80, 42, 108, 78, 0)
    c.rect(83, 50, 105, 75, 0.6)
    for x in (84, 88, 92, 96):
        c.rect(x, 45, x + 2, 47, 2)
    c.rect(100, 45, 105, 46, 2)
    # erhu, bow resting across it
    c.sprite(24, 5, ERHU)
    c.line(8, 76, 44, 40, 2)
    c.line(9, 76, 45, 40, 3)
    c.rect(7, 73, 11, 77, 2)
    # guitar on a stand
    c.line(58, 68, 54, 78, 1)
    c.line(70, 68, 74, 78, 1)
    c.sprite(53, 17, GUITAR)
    return c


CLAWD = [  # Claude Code's crab, chin on the lid, arms over the top edge
    "..333333333333..",
    "..330333333033..",
    "..330333333033..",
    "..333333333333..",
    "3333333333333333",
    "33............33",
]

SPARK = [  # the Claude mark
    "...1...",
    ".1.1.1.",
    "..111..",
    "1111111",
    "..111..",
    ".1.1.1.",
    "...1...",
]

JAVA = [
    "..0............",
    ".....00.0.0..00",
    "..0.0.0.0.0.0.0",
    "..0.0.0.0.0.0.0",
    "..0..00..0...00",
    "00.............",
]


def coding():
    c = Canvas(W, H, 0)
    c.rect(0, 0, W, 66, 0.4)
    c.radial(64, 32, 60, 1.5, 0.4, ry=38)
    c.rect(0, 66, W, H, 1)
    c.rect(0, 66, W, 67, 2)
    c.radial(64, 70, 44, 1.9, 1.0, ry=8)
    # MacBook: aluminium rim, black bezel with the notch, the Claude app
    c.rect(32, 10, 97, 57, 2)
    c.rect(33, 11, 96, 56, 0)
    x0, y0, x1, y1 = 35, 13, 94, 54
    c.rect(x0, y0, x1, y1, 3)
    c.rect(61, 13, 69, 15, 0)
    # sidebar: chats, the open one highlighted
    c.rect(x0, y0, 47, y1, 2)
    c.sprite(37, 16, [".1.", "111", ".1."])
    for i, n in enumerate([8, 6, 9, 7, 5, 8]):
        y = 22 + i * 4
        if i == 1:
            c.rect(36, y - 1, 46, y + 2, 3)
        c.rect(37, y, 37 + n, y + 1, 1)
    c.rect(37, 50, 40, 52, 1)
    # the conversation: a question in a bubble, the answer beside the mark
    c.rect(72, 17, 91, 23, 2)
    for (x, y) in [(72, 17), (90, 17), (72, 22), (90, 22)]:
        c.put(x, y, 3)
    c.rect(74, 19, 89, 20, 1)
    c.rect(78, 21, 89, 22, 1)
    c.sprite(50, 25, SPARK)
    for (x, y, n) in [(59, 26, 28), (59, 29, 24), (50, 33, 38), (50, 36, 34), (50, 39, 22)]:
        c.rect(x, y, x + n, y + 1, 1)
    # composer
    c.rect(50, 43, 91, 52, 1)
    c.rect(51, 44, 90, 51, 3)
    c.put(50, 43, 3); c.put(90, 43, 3); c.put(50, 51, 3); c.put(90, 51, 3)
    c.rect(53, 46, 70, 47, 2)
    c.rect(53, 49, 56, 50, 2)
    c.rect(85, 47, 89, 51, 1)
    c.put(87, 48, 3)
    c.rect(86, 49, 89, 50, 3)
    # base, keyboard and trackpad, seen from above
    c.poly([(32, 57), (97, 57), (104, 66), (25, 66)], 2)
    c.poly([(36, 58), (93, 58), (97, 62), (32, 62)], 1)
    for (y, xa, xb) in [(59, 35, 94), (61, 34, 96)]:
        for x in range(xa, xb, 3):
            c.put(x, y, 0)
    c.rect(55, 63, 74, 66, 2.6)
    c.rect(25, 66, 104, 67, 1)
    # Clawd, lying on the lid behind the screen
    c.sprite(72, 5, CLAWD)
    # a Java mug, steaming
    c.ring(4, 59, 4.5, 2, t=1.5)
    c.rect(4, 50, 21, 70, 2)
    c.rect(4, 50, 21, 51, 3)
    c.rect(4, 69, 21, 70, 1)
    c.sprite(5, 56, JAVA)
    for (sx, sy) in [(9, 46), (15, 42)]:
        for k in range(6):
            c.put(sx + (k // 2) % 2, sy - k, 2)
    return c


SCENES = [
    ("birding", birding),
    ("gaming", gaming),
    ("writing", writing),
    ("reading", reading),
    ("gardening", gardening),
    ("fitness", fitness),
    ("music", music),
    ("coding", coding),
]
