"""A python reading a book, drawn by GPT-6 Astra.

Model:  openai/gpt-6-astra
Date:   2026-09-04
Prompt: Write a Python turtle program that draws a python reading a book.

Generated for snake-bench, Real Python's vibe check for new AI models:
https://github.com/devcademy/snake-bench

The code is exactly what the model returned. Nothing was fixed up.
Run it with: python gpt-6-astra-python-reading-a-book.py
"""

import math
import turtle

screen = turtle.Screen()
screen.setup(800, 650)
screen.title("A Python Reading Python")
screen.bgcolor("#fff6df")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

GREEN = "#68ad45"
DARK_GREEN = "#315e32"
LIGHT_GREEN = "#91c85c"
INK = "#354253"


def polygon(points, fill, outline=INK, width=2):
    pen.penup()
    pen.goto(points[0])
    pen.color(outline, fill)
    pen.pensize(width)
    pen.pendown()
    pen.begin_fill()
    for point in points[1:]:
        pen.goto(point)
    pen.goto(points[0])
    pen.end_fill()
    pen.penup()


def ellipse(x, y, rx, ry, fill, outline=INK, width=2):
    points = [
        (
            x + rx * math.cos(math.radians(angle)),
            y + ry * math.sin(math.radians(angle)),
        )
        for angle in range(0, 360, 5)
    ]
    polygon(points, fill, outline, width)


def line(points, color=INK, width=2):
    pen.penup()
    pen.goto(points[0])
    pen.pencolor(color)
    pen.pensize(width)
    pen.pendown()
    for point in points[1:]:
        pen.goto(point)
    pen.penup()


def bezier(p0, p1, p2, p3, steps=60):
    points = []
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        points.append((
            u**3 * p0[0] + 3*u*u*t * p1[0]
            + 3*u*t*t * p2[0] + t**3 * p3[0],
            u**3 * p0[1] + 3*u*u*t * p1[1]
            + 3*u*t*t * p2[1] + t**3 * p3[1],
        ))
    return points


def text(x, y, words, size=18, color=INK):
    pen.penup()
    pen.goto(x, y)
    pen.pencolor(color)
    pen.write(words, align="center", font=("Arial", size, "bold"))


# Ground shadow
ellipse(10, -190, 235, 25, "#e4d7b5", "#e4d7b5")

# Tail curling out from behind the coils
tail = bezier(
    (-80, -160), (-260, -210), (-265, -65), (-200, -105)
)
line(tail, DARK_GREEN, 28)
line(tail, GREEN, 22)

# Broad, overlapping coils
ellipse(15, -156, 182, 46, GREEN, DARK_GREEN, 4)
ellipse(15, -132, 154, 39, LIGHT_GREEN, DARK_GREEN, 4)
ellipse(15, -112, 125, 31, GREEN, DARK_GREEN, 4)

# Raised neck, behind the book
neck = (
    bezier((105, -117), (215, -85), (174, 39), (112, 56))
    + bezier((112, 56), (83, 66), (70, 74), (51, 90))[1:]
)
line(neck, DARK_GREEN, 66)
line(neck, GREEN, 58)

# A few python markings
for x, y, rx, ry in [
    (150, -69, 12, 17),
    (158, -29, 12, 16),
    (143, 10, 14, 11),
    (107, 39, 13, 9),
    (-94, -163, 17, 8),
    (-42, -178, 17, 7),
    (29, -179, 17, 7),
    (100, -167, 17, 8),
]:
    ellipse(x, y, rx, ry, "#4c873b", "#4c873b")

# Head
ellipse(15, 96, 82, 55, LIGHT_GREEN, DARK_GREEN, 4)
ellipse(15, 73, 56, 24, "#b7db7a", "#b7db7a")

# Eyes
for x in (-16, 43):
    ellipse(x, 108, 22, 23, "white", DARK_GREEN, 2)
    # Pupils look down toward the book.
    ellipse(x + 2, 100, 7, 10, INK, INK)
    ellipse(x, 104, 2, 3, "white", "white")

# Round reading glasses
for x in (-16, 43):
    rim = [
        (
            x + 27 * math.cos(math.radians(a)),
            108 + 27 * math.sin(math.radians(a)),
        )
        for a in range(0, 361, 5)
    ]
    line(rim, "#664735", 4)

line([(11, 110), (16, 112)], "#664735", 4)
line([(-43, 114), (-60, 125)], "#664735", 4)
line([(70, 114), (88, 124)], "#664735", 4)

# Nostrils and a contented smile
ellipse(-5, 77, 2, 3, DARK_GREEN, DARK_GREEN)
ellipse(27, 77, 2, 3, DARK_GREEN, DARK_GREEN)
line(
    bezier((-12, 66), (3, 54), (25, 54), (41, 67)),
    DARK_GREEN,
    3,
)

# Open book: blue covers
polygon(
    [(-168, 12), (-8, -14), (0, -27),
     (8, -14), (168, 12), (168, -123),
     (0, -156), (-168, -123)],
    "#396f9d",
    "#244664",
    4,
)

# Left and right pages
polygon(
    [(-156, 24), (-24, 6), (0, -14),
     (0, -143), (-24, -127), (-156, -110)],
    "#fffdf3",
    "#b6aa8a",
)
polygon(
    [(0, -14), (24, 6), (156, 24),
     (156, -110), (24, -127), (0, -143)],
    "#fff8e3",
    "#b6aa8a",
)

# Spine
line([(0, -15), (0, -142)], "#a99a7c", 3)

# Page headings
text(-80, -20, "PYTHON", 17)
text(80, -20, "CHAPTER 1", 12)

# Printed lines follow the angle of each page.
for y in (-39, -55, -71, -87):
    line([(-135, y + 8), (-25, y - 7)], "#a7aaa5", 2)
    line([(25, y - 7), (135, y + 8)], "#a7aaa5", 2)

# Ribbon bookmark
polygon(
    [(15, -130), (29, -127), (29, -173),
     (22, -164), (15, -177)],
    "#df6558",
    "#b94940",
)

text(0, 231, "A little light reading...", 24, DARK_GREEN)
text(0, -246, "Even pythons study Python!", 17, DARK_GREEN)

screen.update()
screen.exitonclick()
