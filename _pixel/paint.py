"""Tiny 4-tone pixel painter for the `pixel` theme.

Tones are luminance steps: 0 = darkest ink, 3 = lightest screen. Fractional
tones are ordered-dithered with a 4x4 Bayer matrix, the way the pocket camera
renders a gradient. Palettes are applied later (CSS / canvas), so every
picture follows the visitor's hour.
"""
import math
import struct
import zlib

BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]


def dither(v, x, y):
    if v is None:
        return None
    if isinstance(v, int):
        return v
    base = int(math.floor(v))
    frac = v - base
    bump = 1 if BAYER[y % 4][x % 4] < round(frac * 16) else 0
    return max(0, min(3, base + bump))


class Canvas:
    def __init__(self, w, h, fill=3):
        self.w, self.h = w, h
        self.px = [[dither(fill, x, y) for x in range(w)] for y in range(h)]

    def put(self, x, y, v):
        x, y = int(x), int(y)
        if 0 <= x < self.w and 0 <= y < self.h and v is not None:
            self.px[y][x] = dither(v, x, y)

    def get(self, x, y):
        if 0 <= x < self.w and 0 <= y < self.h:
            return self.px[y][x]
        return None

    def rect(self, x0, y0, x1, y1, v):
        for y in range(int(y0), int(y1)):
            for x in range(int(x0), int(x1)):
                self.put(x, y, v)

    def frame(self, x0, y0, x1, y1, v, t=1):
        self.rect(x0, y0, x1, y0 + t, v)
        self.rect(x0, y1 - t, x1, y1, v)
        self.rect(x0, y0, x0 + t, y1, v)
        self.rect(x1 - t, y0, x1, y1, v)

    def ellipse(self, cx, cy, rx, ry, v):
        for y in range(int(cy - ry) - 1, int(cy + ry) + 2):
            for x in range(int(cx - rx) - 1, int(cx + rx) + 2):
                dx = (x + 0.5 - cx) / max(rx, 0.01)
                dy = (y + 0.5 - cy) / max(ry, 0.01)
                if dx * dx + dy * dy <= 1.0:
                    self.put(x, y, v)

    def ring(self, cx, cy, r, v, t=1):
        for y in range(int(cy - r) - 2, int(cy + r) + 3):
            for x in range(int(cx - r) - 2, int(cx + r) + 3):
                d = math.hypot(x + 0.5 - cx, y + 0.5 - cy)
                if r - t <= d <= r:
                    self.put(x, y, v)

    def poly(self, pts, v):
        ys = [p[1] for p in pts]
        for y in range(int(min(ys)), int(math.ceil(max(ys))) + 1):
            sy = y + 0.5
            xs = []
            n = len(pts)
            for i in range(n):
                (x0, y0), (x1, y1) = pts[i], pts[(i + 1) % n]
                if (y0 <= sy < y1) or (y1 <= sy < y0):
                    xs.append(x0 + (sy - y0) * (x1 - x0) / (y1 - y0))
            xs.sort()
            for a, b in zip(xs[0::2], xs[1::2]):
                for x in range(int(round(a)), int(round(b))):
                    self.put(x, y, v)

    def line(self, x0, y0, x1, y1, v, w=1):
        x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
        dx, dy = abs(x1 - x0), -abs(y1 - y0)
        sx, sy = (1 if x0 < x1 else -1), (1 if y0 < y1 else -1)
        err = dx + dy
        while True:
            for ox in range(w):
                for oy in range(w):
                    self.put(x0 + ox, y0 + oy, v)
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x0 += sx
            if e2 <= dx:
                err += dx
                y0 += sy

    def vgrad(self, y0, y1, v0, v1, x0=0, x1=None):
        x1 = self.w if x1 is None else x1
        for y in range(int(y0), int(y1)):
            t = (y - y0) / max(1, (y1 - y0 - 1))
            for x in range(int(x0), int(x1)):
                self.put(x, y, v0 + (v1 - v0) * t)

    def radial(self, cx, cy, r, v_in, v_out, ry=None):
        ry = ry or r
        for y in range(int(cy - ry), int(cy + ry) + 1):
            for x in range(int(cx - r), int(cx + r) + 1):
                d = math.hypot((x + 0.5 - cx) / r, (y + 0.5 - cy) / ry)
                if d <= 1:
                    self.put(x, y, v_in + (v_out - v_in) * d)

    def sprite(self, x, y, rows, flip=False, remap=None):
        for j, row in enumerate(rows):
            if flip:
                row = row[::-1]
            for i, ch in enumerate(row):
                if ch in "0123":
                    v = int(ch)
                    if remap:
                        v = remap.get(v, v)
                    self.put(x + i, y + j, v)

    def ridge(self, x0, x1, base, amp, seed, v, step=3):
        """A bumpy silhouette (tree line, hills) from `base` down to the bottom."""
        h = []
        s = seed
        for x in range(x0, x1):
            s = (s * 1103515245 + 12345) & 0x7FFFFFFF
            h.append(s % 1000 / 1000.0)
        # smooth into clumps
        prof = []
        for i in range(len(h)):
            k = h[max(0, i - step):i + step + 1]
            prof.append(sum(k) / len(k))
        for i, x in enumerate(range(x0, x1)):
            top = int(base - amp * (0.5 + 0.5 * math.sin(i / 5.3 + seed) * 0.6 + (prof[i] - 0.5) * 1.4))
            for y in range(top, self.h):
                self.put(x, y, v)

    def pack(self):
        """2 bits per pixel, row-major, base64 — decoded by pixel-album.js."""
        import base64
        flat = [v for row in self.px for v in row]
        out = bytearray()
        for i in range(0, len(flat), 4):
            b = 0
            for k in range(4):
                b = (b << 2) | (flat[i + k] if i + k < len(flat) else 0)
            out.append(b)
        return base64.b64encode(bytes(out)).decode()


def write_png(path, canvas, palette, scale=1):
    w, h = canvas.w * scale, canvas.h * scale
    raw = bytearray()
    for y in range(h):
        raw.append(0)
        for x in range(w):
            raw.extend(palette[canvas.px[y // scale][x // scale]])
    def chunk(t, d):
        c = struct.pack(">I", len(d)) + t + d
        return c + struct.pack(">I", zlib.crc32(t + d) & 0xFFFFFFFF)
    png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
    png += chunk(b"IDAT", zlib.compress(bytes(raw), 9)) + chunk(b"IEND", b"")
    with open(path, "wb") as f:
        f.write(png)


def write_png_rgba(path, w, h, pixels):
    """pixels: rows of (r, g, b, a) tuples."""
    raw = bytearray()
    for row in pixels:
        raw.append(0)
        for px in row:
            raw.extend(px)
    def chunk(t, d):
        c = struct.pack(">I", len(d)) + t + d
        return c + struct.pack(">I", zlib.crc32(t + d) & 0xFFFFFFFF)
    png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0))
    png += chunk(b"IDAT", zlib.compress(bytes(raw), 9)) + chunk(b"IEND", b"")
    with open(path, "wb") as f:
        f.write(png)


def hexrgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
