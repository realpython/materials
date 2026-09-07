"""A python reading a book, drawn by Claude Fable 5.1.

Model:  anthropic/claude-fable-5.1
Date:   2026-09-04
Prompt: Write a Python turtle program that draws a python reading a book.

Generated for snake-bench, Real Python's vibe check for new AI models:
https://github.com/devcademy/snake-bench

The code is exactly what the model returned. Nothing was fixed up.
Run it with: python claude-fable-5-1-python-reading-a-book.py
"""

import math
import turtle

# ---------------------------------------------------------------- setup
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("#f7f1e1")
screen.title("A Python Reading a Book")
screen.tracer(0)                      # draw instantly, then update once

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

SNAKE_DARK = "#2e7d32"
SNAKE_LIGHT = "#9ccc65"
SNAKE_OUTLINE = "#1b4d1e"
COIL_X = -290                         # center of the coiled body


# -------------------------------------------------------------- helpers
def jump(x, y, heading=None):
    """Move without drawing, optionally set heading."""
    t.penup()
    t.goto(x, y)
    if heading is not None:
        t.setheading(heading)
    t.pendown()


def polygon(points, fill, outline=None):
    t.color(outline or fill, fill)
    t.pensize(2)
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.begin_fill()
    for p in points[1:]:
        t.goto(p)
    t.goto(points[0])
    t.end_fill()


def arc(radius, extent, w_start, w_end, steps=30):
    """Draw an arc whose pen width tapers smoothly from w_start to w_end."""
    for i in range(steps):
        t.pensize(w_start + (w_end - w_start) * i / (steps - 1))
        t.circle(radius, extent / steps)


# ---------------------------------------------------------------- scene
def draw_table():
    polygon([(-400, -215), (400, -215), (400, -300), (-400, -300)],
            "#c9a46c", "#a67c48")
    t.color("#a67c48")
    t.pensize(3)
    jump(-400, -215)
    t.goto(400, -215)


def draw_book():
    # hard cover
    polygon([(-175, -215), (0, -235), (175, -215),
             (175, -95), (0, -115), (-175, -95)],
            "#7a3b1e", "#4d240f")
    # left and right pages (slightly tilted toward the spine)
    polygon([(-160, -200), (-4, -222), (-4, -118), (-160, -98)],
            "#fffaf0", "#d8cfbf")
    polygon([(4, -222), (160, -200), (160, -98), (4, -118)],
            "#fffaf0", "#d8cfbf")
    # spine
    t.color("#4d240f")
    t.pensize(3)
    jump(0, -235)
    t.goto(0, -115)

    # lines of "text" on each page
    t.color("#666666")
    t.pensize(2)
    lengths = [105, 90, 110, 70, 100, 85]
    for i, length in enumerate(lengths):
        d = 18 + 13 * i                 # distance below the top edge
        # left page: top edge runs from (-160,-98) to (-4,-118)
        x0 = -145
        x1 = x0 + length
        jump(x0, -118 - d + (-4 - x0) * 20 / 156)
        t.goto(x1, -118 - d + (-4 - x1) * 20 / 156)
        # right page: top edge runs from (4,-118) to (160,-98)
        x0 = 20
        x1 = x0 + length
        jump(x0, -118 - d + (x0 - 4) * 20 / 156)
        t.goto(x1, -118 - d + (x1 - 4) * 20 / 156)


def draw_body(scale, color):
    """Coiled body that spirals outward, then rises into a neck over the book."""
    t.color(color)
    jump(COIL_X, -140, 0)
    widths = [6, 12, 18, 24, 30, 34]
    radii = [20, 35, 50, 65, 80]
    for i, r in enumerate(radii):
        arc(r, 180, widths[i] * scale, widths[i + 1] * scale)
    # neck: up and then arching over toward the book
    arc(-70, 180, 34 * scale, 34 * scale)
    arc(-160, 75, 34 * scale, 34 * scale)


def draw_head():
    hx, hy = t.position()
    ang = math.radians(t.heading())
    fx, fy = math.cos(ang), math.sin(ang)          # forward direction
    px, py = -fy, fx                               # perpendicular (left)

    cx, cy = hx + 18 * fx, hy + 18 * fy            # head center
    t.penup()
    t.goto(cx, cy)
    t.dot(66, SNAKE_OUTLINE)
    t.dot(60, SNAKE_DARK)
    # snout
    t.goto(cx + 22 * fx, cy + 22 * fy)
    t.dot(44, SNAKE_OUTLINE)
    t.dot(40, SNAKE_DARK)
    # lighter "chin"
    t.goto(cx + 26 * fx, cy + 26 * fy)
    t.dot(24, SNAKE_LIGHT)

    # eyes (looking down at the book) with reading glasses
    eyes = []
    for side in (-1, 1):
        ex = cx + 10 * fx + side * 13 * px
        ey = cy + 10 * fy + side * 13 * py
        eyes.append((ex, ey))
        t.goto(ex, ey)
        t.dot(16, "white")
        t.goto(ex + 3 * fx, ey + 3 * fy)
        t.dot(7, "black")
        # glasses rim
        t.color("black")
        t.pensize(2)
        jump(ex, ey - 11, 0)
        t.circle(11)
    (e1x, e1y), (e2x, e2y) = eyes
    # bridge of the glasses
    jump(e1x + 11 * px, e1y + 11 * py)
    t.goto(e2x - 11 * px, e2y - 11 * py)
    # temple arms going back along the head
    jump(e2x + 11 * px, e2y + 11 * py)
    t.goto(e2x + 11 * px - 26 * fx, e2y + 11 * py - 26 * fy)
    jump(e1x - 11 * px, e1y - 11 * py)
    t.goto(e1x - 11 * px - 26 * fx, e1y - 11 * py - 26 * fy)

    # forked tongue
    t.color("#e53935")
    t.pensize(3)
    tx, ty = cx + 42 * fx, cy + 42 * fy
    jump(tx, ty, math.degrees(ang))
    t.forward(18)
    fork = t.position()
    t.left(30)
    t.forward(9)
    jump(*fork, math.degrees(ang))
    t.right(30)
    t.forward(9)

    return cx, cy


def draw_thought_bubble(head_x, head_y):
    t.penup()
    t.color("#555555", "white")
    # trail of small bubbles from the head
    for (bx, by, r) in [(head_x + 26, head_y + 36, 8),
                        (head_x + 46, head_y + 66, 12)]:
        t.goto(bx, by)
        t.dot(r * 2 + 4, "#555555")
        t.dot(r * 2, "white")
    # main bubble
    bx, by, r = -40, 100, 68
    t.goto(bx, by)
    t.dot(r * 2 + 4, "#555555")
    t.dot(r * 2, "white")
    t.color("#1a237e")
    t.goto(bx, by + 2)
    t.write("import", align="center", font=("Courier", 13, "bold"))
    t.goto(bx, by - 20)
    t.write("antigravity", align="center", font=("Courier", 13, "bold"))


def draw_caption():
    t.penup()
    t.goto(0, 235)
    t.color("#4d240f")
    t.write("A Python reading a book", align="center",
            font=("Georgia", 20, "italic"))


# ----------------------------------------------------------------- draw
draw_table()
draw_book()
draw_body(1.0, SNAKE_OUTLINE)          # dark outline pass (slightly wider)
draw_body(0.85, SNAKE_DARK)            # main body color
draw_body(0.35, SNAKE_LIGHT)           # dorsal stripe
cx, cy = draw_head()
draw_thought_bubble(cx, cy)
draw_caption()

screen.update()
turtle.done()
