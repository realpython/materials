#
# Arcade Platformer
#
# Demonstrating the capbilities of arcade in a platformer game
# Supporting the Arcade Platformer article on https://realpython.com
#
# All game artwork and sounds, except the tile map, from www.kenney.nl
#

# Import libraries
import arcade


# Classes
class Platformer(arcade.Window):
    """Platformer class. Derived from arcade.Window,
    manages different aspects of the game.
    """

    def __init__(self):
        pass

    def setup(self):
        """Sets up the game for the current level"""
        pass

    def on_key_press(self, key: int, modifiers: int):
        """Processes key presses

        Arguments:
            key {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were down at the time
        """

    def on_key_release(self, key: int, modifiers: int):
        """Processes key releases

        Arguments:
            key {int} -- Which key was released
            modifiers {int} -- Which modifiers were down at the time
        """

    def on_update(self, delta_time: float):
        """Updates the position of all screen objects

        Arguments:
            delta_time {float} -- How much time since the last call
        """
        pass

    def on_draw(self):
        """Draws everything"""
        pass


# Main
if __name__ == "__main__":
    window = Platformer()
    window.setup()
    arcade.run()
