"""A python reading a book, drawn by Claude Opus 5.

Model:  anthropic/claude-opus-5
Date:   2026-09-08
Prompt: Write a Python turtle program that draws a python reading a book.

Generated for snake-bench, Real Python's vibe check for new AI models:
https://github.com/devcademy/snake-bench

The code is exactly what the model returned. Nothing was fixed up.
Run it with: python claude-opus-5-python-reading-a-book.py

Note: this script ended with status 'error' when we ran it.
"""

"""
A Python reading a book
=======================
A picture drawn entirely with Python's standard `turtle` module.

Run with:   python python_reading_a_book.py
(needs a desktop / graphical display)
"""

import math
import turtle

# ----------------------------------------------------------------- palette
SKY, FLOOR, SHADOW = "#e9f1fa", "#dae5d1", "#c6d4bc"
SNAKE, SNAKE_D, SPOT = "#5aa45f", "#22402d", "#3a7f4d"
TONGUE = "#e0555f"
COVER, COVER_D = "#95403c", "#5f2726"
PAGE, PAGE_D, INK = "#fcf7e8", "#ded4b8", "#9d9682"
GOLD, DARK, WHITE = "#e0a33f", "#25313a", "#ffffff"

# ----------------------------------------------------------------- screen
screen = turtle.Screen()
screen.setup(width=900, height=760)
screen.title("A Python reading a book")
screen.bgcolor(SKY)
screen.tracer(0)

pen = turtle.Turtle(visible=False)          # line / polygon artist
pen.speed(0)
pen.penup()

blobber = turtle.Turtle(visible=False)      # stamps soft round blobs
blobber.shape("circle")
blobber.speed(0)
blobber.penup()


# ================================================================= helpers
def rot(x, y, deg):
    """Rotate (x, y) around the origin."""
    a = math.radians(deg)
    c, s = math.cos(a), math.sin(a)
    return (x * c - y * s, x * s + y * c)


def ellipse_pts(cx, cy, rx, ry, deg=0.0, steps=72):
    pts = []
    for i in range(steps + 1):
        a = 2 * math.pi * i / steps
        x, y = rot(rx * math.cos(a), ry * math.sin(a), deg)
        pts.append((cx + x, cy + y))
    return pts


def cubic(p0, p1, p2, p3, steps=60):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u**3*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t**3*p3[0]
        y = u**3*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t**3*p3[1]
        pts.append((x, y))
    return pts


def _cr(p0, p1, p2, p3, n):
    """One Catmull-Rom segment between p1 and p2."""
    out = []
    for j in range(n):
        t = j / n
        t2, t3 = t * t, t * t * t
        x = 0.5 * (2*p1[0] + (-p0[0]+p2[0])*t +
                   (2*p0[0]-5*p1[0]+4*p2[0]-p3[0])*t2 +
                   (-p0[0]+3*p1[0]-3*p2[0]+p3[0])*t3)
        y = 0.5 * (2*p1[1] + (-p0[1]+p2[1])*t +
                   (2*p0[1]-5*p1[1]+4*p2[1]-p3[1])*t2 +
                   (-p0[1]+3*p1[1]-3*p2[1]+p3[1])*t3)
        out.append((x, y))
    return out


def smooth_closed(pts, n=10):
    N, out = len(pts), []
    for i in range(N):
        out += _cr(pts[(i-1) % N], pts[i], pts[(i+1) % N], pts[(i+2) % N], n)
    out.append(out[0])
    return out


def smooth_open(pts, n=10):
    p = [pts[0]] + list(pts) + [pts[-1]]
    out = []
    for i in range(1, len(p) - 2):
        out += _cr(p[i-1], p[i], p[i+1], p[i+2], n)
    out.append(p[-1])
    return out


def resample(pts, step=6.0):
    """Keep points roughly `step` pixels apart."""
    out = [pts[0]]
    for p in pts[1:]:
        if math.hypot(p[0]-out[-1][0], p[1]-out[-1][1]) >= step:
            out.append(p)
    if out[-1] != pts[-1]:
        out.append(pts[-1])
    return out


def polygon(pts, fill, outline=None, width=3):
    pen.pensize(width)
    pen.color(outline if outline else fill, fill)
    pen.penup(); pen.goto(pts[0]); pen.pendown()
    pen.begin_fill()
    for p in pts[1:]:
        pen.goto(p)
    pen.goto(pts[0])
    pen.end_fill()
    pen.penup()


def line(pts, color, width=2):
    pen.pensize(width); pen.color(color)
    pen.penup(); pen.goto(pts[0]); pen.pendown()
    for p in pts[1:]:
        pen.goto(p)
    pen.penup()


def ring(cx, cy, r, color, width=3):
    line(ellipse_pts(cx, cy, r, r, 0, 48), color, width)


def blob(x, y, length, thick, color, tilt=0.0):
    """Stamp a soft ellipse: `length` along `tilt`, `thick` across it."""
    blobber.settiltangle(tilt)
    blobber.color(color)
    blobber.shapesize(thick / 20.0, length / 20.0, 1)
    blobber.goto(x, y)
    blobber.stamp()


# ================================================================= backdrop
def draw_backdrop():
    polygon([(-470, -390), (470, -390), (470, -305), (-470, -305)], FLOOR)
    line([(-470, -305), (470, -305)], SHADOW, 3)
    polygon(ellipse_pts(0, -318, 330, 26), SHADOW)          # soft shadow


def draw_pile(x, base):
    """A stack of books that have already been read."""
    books = [(128, 26, "#4a6f8a", -6), (114, 22, "#7d9b52", 5),
             (120, 20, "#b3803f", -3)]
    y = base
    for w, h, c, dx in books:
        polygon([(x+dx-w/2, y), (x+dx+w/2, y),
                 (x+dx+w/2, y+h), (x+dx-w/2, y+h)], c, DARK, 2)
        line([(x+dx-w/2+7, y+h*0.55), (x+dx+w/2-7, y+h*0.55)], PAGE, 3)
        y += h


def draw_mug(x, base):
    ring(x + 30, base + 26, 13, "#c96a5a", 8)               # handle
    polygon([(-25, 0), (-27, 44), (27, 44), (25, 0)],       # body
            "#c96a5a", COVER_D, 2) if False else None
    body = [(x-25, base), (x-27, base+44), (x+27, base+44), (x+25, base)]
    polygon(body, "#c96a5a", COVER_D, 2)
    line([(x-26, base+30), (x+26, base+30)], "#f0e2d6", 5)
    polygon(ellipse_pts(x, base+44, 27, 7), "#f4ede2", COVER_D, 2)
    for dx in (-8, 8):                                      # steam
        line(smooth_open([(x+dx, base+52), (x+dx-9, base+66),
                          (x+dx+7, base+80), (x+dx-4, base+96)], 8),
             "#cfdbe6", 3)


# ==================================================================== snake
def tail_points():
    return cubic((330, -138), (368, -210), (322, -248), (246.2, -234.2), 70)


def coil_points():
    """A pile of coils: three and a half turns spiralling upward."""
    pts, T, N = [], 3.528, 1600
    for i in range(N + 1):
        t = T * i / N
        a = math.radians(10 - 360 * t)          # clockwise
        rx = 250 - 32 * t                       # coils get tighter...
        ry = 62 - 6 * t
        cy = -245 + 46 * t                      # ...and climb
        pts.append((rx * math.cos(a), cy + ry * math.sin(a)))
    return pts


def neck_points():
    return cubic((-137, -83), (-180, 25), (-145, 135), (-70, 158), 140)


def body_width(s):
    if s < 0.08:
        return 13 + 33 * (s / 0.08)             # thin tail tip
    if s < 0.80:
        return 46                               # fat middle
    if s < 0.92:
        return 46 - 4 * ((s - 0.80) / 0.12)
    return 42 - 8 * ((s - 0.92) / 0.08)          # slender neck


def draw_snake_body():
    path = resample(tail_points() + coil_points()[1:] + neck_points()[1:], 6.0)
    n = path.__len__()
    widths = [body_width(i / (n - 1)) for i in range(n)]

    side, a, chunk = 1, 0, 90
    while a < n - 1:
        b = min(a + chunk, n - 1)
        # dark outline pass for this piece of the coil...
        for i in range(a, b + 1):
            x, y = path[i]
            blob(x, y, widths[i] + 11, widths[i] + 11, SNAKE_D)
        # ...then the green fill (reaching a little back to hide the seam)
        for i in range(max(0, a - 6), b + 1):
            x, y = path[i]
            blob(x, y, widths[i], widths[i], SNAKE)
        # ...then the markings
        for i in range(a + 12, b - 10, 15):
            x, y = path[i]
            x0, y0 = path[max(0, i - 4)]
            x1, y1 = path[min(n - 1, i + 4)]
            ang = math.degrees(math.atan2(y1 - y0, x1 - x0))
            w = widths[i]
            ox, oy = rot(0, side * w * 0.20, ang)
            blob(x + ox, y + oy, w * 0.9, w * 0.42, SPOT, ang)
            side = -side
        a = b


# ===================================================================== head
HEAD_C, HEAD_A = (-40, 156), -22          # centre, tilt (snout points down-right)


def hp(u, v):
    x, y = rot(u, v, HEAD_A)
    return (HEAD_C[0] + x, HEAD_C[1] + y)


def draw_head():
    outline = [(-72, 2), (-64, 30), (-24, 44), (28, 40), (62, 28), (80, 10),
               (82, -2), (46, -22), (-4, -32), (-52, -32), (-74, -16)]
    polygon(smooth_closed([hp(u, v) for u, v in outline], 8), SNAKE, SNAKE_D, 4)

    p = hp(-34, 26); blob(p[0], p[1], 40, 15, SPOT, HEAD_A + 8)
    p = hp(4, 32);   blob(p[0], p[1], 32, 13, SPOT, HEAD_A - 2)

    line(smooth_open([hp(80, 2), hp(52, -14), hp(8, -25), hp(-34, -28)], 8),
         SNAKE_D, 3)                                            # mouth
    p = hp(72, 8); blob(p[0], p[1], 9, 5, SNAKE_D, HEAD_A)       # nostril

    eye = hp(30, 14)
    polygon(ellipse_pts(eye[0], eye[1], 12, 11, HEAD_A), WHITE, SNAKE_D, 2)
    pup = hp(34, 13)
    polygon(ellipse_pts(pup[0], pup[1], 6, 6), DARK)
    gl = hp(37, 17)
    polygon(ellipse_pts(gl[0], gl[1], 2.5, 2.5), WHITE)

    ring(eye[0], eye[1], 18, DARK, 4)                            # spectacles
    line([hp(12, 20), hp(-30, 27), hp(-52, 26)], DARK, 4)        # temple arm
    line([hp(48, 8), hp(66, 2)], DARK, 3)                        # bridge


def draw_tongue():
    line(smooth_open([hp(78, -4), hp(92, -12), hp(102, -18)], 8), TONGUE, 5)
    line([hp(102, -18), hp(124, -12)], TONGUE, 4)
    line([hp(102, -18), hp(117, -34)], TONGUE, 4)


# ===================================================================== book
BOOK_C, BOOK_A = (55, -10), -6


def bp(u, v):
    x, y = rot(u, v, BOOK_A)
    return (BOOK_C[0] + x, BOOK_C[1] + y)


def draw_book():
    cover = [(-168, -46), (0, -70), (168, -46), (168, 84), (0, 60), (-168, 84)]
    polygon([bp(*p) for p in cover], COVER, COVER_D, 3)

    block = [(-160, -40), (0, -63), (160, -40), (160, 78), (0, 54), (-160, 78)]
    polygon([bp(*p) for p in block], PAGE_D)

    polygon([bp(*p) for p in [(-152, -34), (0, -56), (0, 50), (-152, 72)]],
            PAGE, PAGE_D, 2)
    polygon([bp(*p) for p in [(152, -34), (0, -56), (0, 50), (152, 72)]],
            PAGE, PAGE_D, 2)
    line([bp(0, -56), bp(0, 50)], PAGE_D, 3)                 # spine crease

    # lines of "text" that follow the tilt of each page
    for sign in (-1, 1):
        for k, h in enumerate((36, 22, 8, -6, -20, -34)):
            u0, u1 = 18 * sign, (140 if k != 5 else 100) * sign
            y0 = h - 0.1447 * u0 * sign * sign * (1 if sign < 0 else -1)
            # shift: pages rise towards their outer edge
            y0 = h + 0.1447 * abs(u0)
            y1 = h + 0.1447 * abs(u1)
            line([bp(u0, y0), bp(u1, y1)], INK, 3)

    polygon([bp(*p) for p in [(-6, -56), (8, -58), (6, -108), (0, -96),
                              (-9, -102)]], GOLD, COVER_D, 2)   # bookmark


# ================================================================ lettering
def draw_words():
    pen.color("#8698a8")
    for text, (x, y), size in [("def", (252, 100), 15),
                               ("yield", (312, 152), 13),
                               ("import", (238, 205), 12)]:
        pen.goto(x, y)
        pen.write(text, align="center", font=("Courier New", size, "italic"))


def draw_titles():
    pen.color(DARK)
    pen.goto(0, 300)
    pen.write("A Python Reading a Book", align="center",
              font=("Georgia", 26, "bold"))
    pen.color("#5d6b76")
    pen.goto(0, 268)
    pen.write("(recursion is his favourite chapter)", align="center",
              font=("Georgia", 13, "italic"))


# ===================================================================== main
def main():
    draw_backdrop()
    draw_pile(-330, -312)
    draw_mug(280, -312)
    draw_snake_body()      # tail, coils and neck, all one long tube
    draw_book()            # held in front of the coils
    draw_head()            # peering down over the pages
    draw_tongue()
    draw_words()
    draw_titles()
    screen.update()
    turtle.done()


if __name__ == "__main__":
    main()
