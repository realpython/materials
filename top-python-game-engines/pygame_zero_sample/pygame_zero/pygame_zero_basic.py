"""
Basic Hello World program in Pygame Zero

This program is designed to demonstrate the basic capabilities
of Pygame Zero. It will:
- Create a simple game window
- Fill the background with white
- Draw some simple shapes in different colors
- Draw some text in a specified size and color
"""

# Import pgzrun allows the program to run in Python IDLE
# You can also run the program from the command line using:
#   `pgzrun pygame_zero_basic.py`
import pgzrun

# Set the width and height of our output window, in pixels
WIDTH = 800
HEIGHT = 600


def draw():
    """Draw is called once per frame to render everything on the screen
    """

    # Clear the screen first
    pgzrun.screen.clear()

    # Set the background color to white
    pgzrun.screen.fill("white")

    # Draw a blue circle with a radius of 50 in the center of the screen
    pgzrun.screen.draw.filled_circle((WIDTH // 2, HEIGHT // 2), 50, "blue")

    # Draw a red outlined square in the top left corner of the screen
    red_square = pgzrun.Rect((50, 50), (100, 100))
    pgzrun.screen.draw.rect(red_square, (200, 0, 0))

    # Draw an orange caption along the bottom in 60 point font
    pgzrun.screen.draw.text(
        "Hello, World! From Pygame Zero!",
        (100, HEIGHT - 50),
        fontsize=60,
        color="orange",
    )


# Run the program
pgzrun.go()
