#
# Arcade Platformer
#
# Demonstrating the capbilities of arcade in a platformer game
# Supporting the Arcade Platformer article on https://realpython.com
#
# All game artwork and sounds, except the tile map and victory sound,
# from www.kenney.nl


# Import libraries
import arcade
import pathlib

# Game constants
# Window dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Arcade Platformer"

# Scaling Constants
MAP_SCALING = 1.0

# Player constants
GRAVITY = 1.0
PLAYER_START_X = 65
PLAYER_START_Y = 256

# Assets path
ASSETS_PATH = pathlib.Path(__file__).resolve().parent.parent / "assets"


# Classes
class Platformer(arcade.Window):
    """Platformer class. Derived from arcade.Window,
    manages different aspects of the game.
    """

    def __init__(self) -> None:
        """Create the game view"""
        # First initialize the parent
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These lists will hold different sets of sprites
        self.coins_list = None
        self.background_list = None
        self.walls_list = None
        self.ladders_list = None
        self.goals_list = None
        self.enemies_list = None

        # One sprite for the player, no more is needed
        self.player = None

        # We need a physics engine as well
        self.physics_engine = None

        # Someplace to keep score
        self.score = 0

        # Which level are we on?
        self.level = 1

        # Load up our sounds here
        self.coin_sound = arcade.load_sound(str(ASSETS_PATH / "sounds" / "coin.wav"))
        self.jump_sound = arcade.load_sound(str(ASSETS_PATH / "sounds" / "jump.wav"))
        self.victory_sound = arcade.load_sound(
            str(ASSETS_PATH / "sounds" / "victory.wav")
        )

    def setup(self) -> None:
        """Sets up the game for the current level"""

        # Get the current map based on the level
        map_name = f"platform_level_{self.level:02}.tmx"
        map_path = ASSETS_PATH / map_name

        # What are the names of the layers?
        wall_layer = "ground"
        coin_layer = "coins"
        goal_layer = "goal"
        background_layer = "background"
        ladders_layer = "ladders"

        # Load the current map
        map = arcade.tilemap.read_tmx(str(map_path))

        # Load the layers
        self.background_list = arcade.tilemap.process_layer(
            map, layer_name=background_layer, scaling=MAP_SCALING
        )
        self.goals_list = arcade.tilemap.process_layer(
            map, layer_name=goal_layer, scaling=MAP_SCALING
        )
        self.walls_list = arcade.tilemap.process_layer(
            map, layer_name=wall_layer, scaling=MAP_SCALING
        )
        self.ladders_list = arcade.tilemap.process_layer(
            map, layer_name=ladders_layer, scaling=MAP_SCALING
        )
        self.coins_list = arcade.tilemap.process_layer(
            map, layer_name=coin_layer, scaling=MAP_SCALING
        )

        # Set the background color
        background_color = arcade.color.FRESH_AIR
        if map.background_color:
            background_color = map.background_color
        arcade.set_background_color(background_color)

        # Create the player sprite, if they're not already setup
        if not self.player:
            self.player = self.create_player_sprite()

        # If we have a player sprite, we need to move it back to the beginning
        self.player.center_x = PLAYER_START_X
        self.player.center_y = PLAYER_START_Y
        self.player.change_x = 0
        self.player.change_y = 0

        # Load the physics engine for this map
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            player_sprite=self.player,
            platforms=self.walls_list,
            gravity_constant=GRAVITY,
            ladders=self.ladders_list,
        )

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
# Main
if __name__ == "__main__":
    window = Platformer()
    window.setup()
    arcade.run()
