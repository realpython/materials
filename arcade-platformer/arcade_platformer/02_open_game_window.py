"""
Arcade Platformer

Demonstrating the capbilities of arcade in a platformer game
Supporting the Arcade Platformer article on https://realpython.com

All game artwork from www.kenney.nl
Game sounds and tile maps by author
"""

import arcade
import pathlib

# Game constants
# Window dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Arcade Platformer"

# Assets path
ASSETS_PATH = pathlib.Path(__file__).resolve().parent.parent / "assets"


class Platformer(arcade.Window):
    def __init__(self) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These lists will hold different sets of sprites
        self.coins = None
        self.background = None
        self.walls = None
        self.ladders = None
        self.goals = None
        self.enemies = None

        # One sprite for the player, no more is needed
        self.player = None

        # We need a physics engine as well
        self.physics_engine = None

        # Someplace to keep score
        self.score = 0

        # Which level are we on?
        self.level = 1

        # Load up our sounds here
        self.coin_sound = arcade.load_sound(
            str(ASSETS_PATH / "sounds" / "coin.wav")
        )
        self.jump_sound = arcade.load_sound(
            str(ASSETS_PATH / "sounds" / "jump.wav")
        )
        self.victory_sound = arcade.load_sound(
            str(ASSETS_PATH / "sounds" / "victory.wav")
        )

    def setup(self):
        """Sets up the game for the current level"""
        pass

    def on_key_press(self, key: int, modifiers: int):
        """Arguments:
        key {int} -- Which key was pressed
        modifiers {int} -- Which modifiers were down at the time
        """

    def on_key_release(self, key: int, modifiers: int):
        """Arguments:
        key {int} -- Which key was released
        modifiers {int} -- Which modifiers were down at the time
        """

    def on_update(self, delta_time: float):
        """Updates the position of all game objects

        Arguments:
            delta_time {float} -- How much time since the last call
        """
        pass

    def on_draw(self):
        pass


if __name__ == "__main__":
    window = Platformer()
    window.setup()
    arcade.run()
