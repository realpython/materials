# Basic arcade program using objects
# Draw shapes on screen

# Imports
import arcade

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Draw Shapes"

# Classes


class Welcome(arcade.Window):
    """Our main welcome window
    """

    def __init__(self):
        """Initialize the window
        """

        # Call the parent class constructor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the background window
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """Called whenever we need to draw our window
        """

        # Clear the screen and start drawing
        arcade.start_render()

        # Draw a blue arc
        arcade.draw_arc_filled(100, 100, 40, 40, arcade.color.BLUE, 0, 125)

        # Draw a red ellipse
        arcade.draw_ellipse_outline(
            300, 100, 60, 30, arcade.color.RED, border_width=2
        )

        # Draw some purple lines
        arcade.draw_line(500, 100, 550, 100, arcade.color.PURPLE)
        arcade.draw_line(500, 90, 550, 90, arcade.color.PURPLE, line_width=2)
        arcade.draw_line(500, 80, 550, 80, arcade.color.PURPLE, line_width=3)

        # Draw an orange parabola
        arcade.draw_parabola_filled(100, 100, 130, 120, arcade.color.ORANGE)

        # Draw a black point
        arcade.draw_point(300, 300, arcade.color.BLACK, 20)

        # Draw a green polygon
        points_list = [
            [500, 300],
            [550, 300],
            [575, 325],
            [550, 350],
            [525, 340],
        ]
        arcade.draw_polygon_outline(
            points_list, arcade.color.GREEN, line_width=5
        )

        # Draw some rectangles
        arcade.draw_rectangle_filled(100, 500, 150, 75, arcade.color.AZURE)
        arcade.draw_lrtb_rectangle_filled(
            150, 250, 575, 525, arcade.color.AMARANTH_PINK
        )
        arcade.draw_xywh_rectangle_filled(
            200, 550, 150, 75, arcade.color.ASPARAGUS
        )

        # Draw some triangles
        arcade.draw_triangle_filled(
            400, 500, 500, 500, 450, 575, arcade.color.DEEP_RUBY
        )


# Main code entry point
if __name__ == "__main__":
    app = Welcome()
    arcade.run()
