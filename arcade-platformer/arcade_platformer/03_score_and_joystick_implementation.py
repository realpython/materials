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
from os import path, chdir

# Window dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Arcade Platformer"

# Scaling Constants
MAP_SCALING = 1.0
CHARACTER_SCALING = 1.0

# Viewport margins
LEFT_VIEWPORT_MARGIN = 50
RIGHT_VIEWPORT_MARGIN = 300
TOP_VIEWPORT_MARGIN = 150
BOTTOM_VIEWPORT_MARGIN = 150

# Player constants
GRAVITY = 1.0
PLAYER_START_X = 65
PLAYER_START_Y = 256
PLAYER_MOVE_SPEED = 10
PLAYER_JUMP_SPEED = 20

# Joystick control
DEAD_ZONE = 0.1


class Platformer(arcade.Window):
    """Platformer class. Derived from arcade.Window, provides all functionality
    for our game.
    """

    def __init__(self):
        # First initial the parent
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Save the path to our game assets
        self.assets_path = path.join(
            path.dirname(path.abspath(__file__)), "..", "assets"
        )

        # These lists hold different sets of sprites
        self.coins_list = None
        self.background_list = None
        self.walls_list = None
        self.ladders_list = None
        self.goals_list = None
        self.enemies_list = None

        # One sprite for the player, no more is needed
        self.player = None

        # Someplace to keep score
        self.score = 0

        # Which level are we on?
        self.level = 1

        # Load up our sounds here
        self.coin_sound = arcade.load_sound(
            path.join(self.assets_path, "sounds", "coin.wav")
        )
        self.jump_sound = arcade.load_sound(
            path.join(self.assets_path, "sounds", "jump.wav")
        )

        # We need a physics engine as well
        self.physics_engine = None

        # Track the bottom left corner of the current viewport
        self.view_left = 0
        self.view_bottom = 0

        # Check if a joystick is connected
        joysticks = arcade.get_joysticks()

        if joysticks:
            # If so, get the first one
            self.joystick = joysticks[0]
            self.joystick.open()
        else:
            # If not, flag it so we won't use it
            print("There are no Joysticks")
            self.joystick = None

    def setup(self):
        """Sets up the game for the current level
        """

        # Change directory to our assets path
        chdir(self.assets_path)

        # Get the current map based on the level
        map_name = f"platform_level_{self.level:02}.tmx"
        map_path = path.join(".", map_name)

        # What are the names of the layers?
        wall_layer = "ground"
        coin_layer = "coins"
        goal_layer = "goal"
        background_layer = "background"
        ladders_layer = "ladders"

        # Load the current map
        map = arcade.tilemap.read_tmx(map_path)

        # Load the layers
        self.background_list = arcade.tilemap.process_layer(
            map, background_layer, MAP_SCALING
        )
        self.coins_list = arcade.tilemap.process_layer(
            map, coin_layer, MAP_SCALING
        )
        self.goals_list = arcade.tilemap.process_layer(
            map, goal_layer, MAP_SCALING
        )
        self.walls_list = arcade.tilemap.process_layer(
            map, wall_layer, MAP_SCALING
        )
        self.ladders_list = arcade.tilemap.process_layer(
            map, ladders_layer, MAP_SCALING
        )

        # Set the background color
        background_color = arcade.color.AERO_BLUE
        if map.background_color:
            background_color = map.background_color
        arcade.set_background_color(background_color)

        # Find the edge of the map to control viewport scrolling
        self.map_width = (map.map_size.width - 1) * map.tile_size.width

        # Create the player sprite, if they're not already setup
        if not self.player:
            self.player = self.create_player_sprite()

        # If we have a player sprite, we need to move it back to the beginning
        else:
            self.player.center_x = PLAYER_START_X
            self.player.center_y = PLAYER_START_Y

        # Load the physics engine for this map
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player, self.walls_list, GRAVITY, self.ladders_list
        )

    def create_player_sprite(self) -> arcade.AnimatedWalkingSprite:
        """"Creates the animated player sprite
        
        Returns:
            arcade.AnimatedWalkingSprite -- The properly setup player sprite
        """
        # Where are the player images stored?
        texture_path = path.join(self.assets_path, "images", "player")

        # Setup the appropriate textures
        walking_paths = [
            path.join(texture_path, f"alienGreen_walk{x}.png") for x in (1, 2)
        ]
        climbing_paths = [
            path.join(texture_path, f"alienGreen_climb{x}.png") for x in (1, 2)
        ]
        standing_path = path.join(texture_path, "alienGreen_stand.png")

        # Load them all now
        walking_right_textures = [
            arcade.load_texture(texture)
            for texture in walking_paths
        ]
        walking_left_textures = [
            arcade.load_texture(
                texture, mirrored=True
            )
            for texture in walking_paths
        ]

        walking_up_textures = [
            arcade.load_texture(texture)
            for texture in climbing_paths
        ]
        walking_down_textures = [
            arcade.load_texture(texture)
            for texture in climbing_paths
        ]

        standing_right_textures = [
            arcade.load_texture(standing_path)
        ]

        standing_left_textures = [
            arcade.load_texture(
                standing_path, mirrored=True
            )
        ]

        # Create the sprite
        player = arcade.AnimatedWalkingSprite()

        # Add the proper textures
        player.stand_left_textures = standing_left_textures
        player.stand_right_textures = standing_right_textures
        player.walk_left_textures = walking_left_textures
        player.walk_right_textures = walking_right_textures
        player.walk_up_textures = walking_up_textures
        player.walk_down_textures = walking_down_textures

        # Set the player defaults
        player.center_x = PLAYER_START_X
        player.center_y = PLAYER_START_Y
        player.state = arcade.FACE_RIGHT

        # Set the initial texture
        player.texture = player.stand_right_textures[0]

        return player

    def on_draw(self):
        """Draws everything
        """

        arcade.start_render()

        # Draw all the sprites
        self.background_list.draw()
        self.walls_list.draw()
        self.coins_list.draw()
        self.goals_list.draw()
        self.ladders_list.draw()
        self.player.draw()

        # Draw the score in the lower left
        score_text = f"Score: {self.score}"

        # First a black background for a shadow effect
        arcade.draw_text(
            score_text,
            10 + self.view_left,
            10 + self.view_bottom,
            color=arcade.csscolor.BLACK,
            font_size=40,
        )

        # Now in white slightly shifted
        arcade.draw_text(
            score_text,
            15 + self.view_left,
            15 + self.view_bottom,
            color=arcade.csscolor.WHITE,
            font_size=40,
        )

    def on_update(self, delta_time: float):
        """Updates the position of all screen objects
        
        Arguments:
            delta_time {float} -- How much time since the last call
        """

        # First, check for joystick movement
        if self.joystick:
            # Check if we're in the dead zone
            if abs(self.joystick.x) > DEAD_ZONE:
                self.player.change_x = self.joystick.x * PLAYER_MOVE_SPEED
            else:
                self.player.change_x = 0

            if abs(self.joystick.y) > DEAD_ZONE:
                if self.physics_engine.is_on_ladder():
                    self.player.change_y = self.joystick.y * PLAYER_MOVE_SPEED
                else:
                    self.player.change_y = 0

            # Did the user press the jump button?
            if self.joystick.buttons[0] == True:
                if self.physics_engine.can_jump():
                    self.player.change_y = PLAYER_JUMP_SPEED
                    # Play the jump sound
                    arcade.play_sound(self.jump_sound)

        # Update player movement based on the physics engine
        self.physics_engine.update()

        # Restrict user movement so they can't walk off screen
        if self.player.left < 0:
            self.player.left = 0

        # Update the player animation
        self.player.update_animation()

        # Check if we've picked up a coin
        coins_hit = arcade.check_for_collision_with_list(
            self.player, self.coins_list
        )

        for coin in coins_hit:
            # Add the coin score to our score
            self.score += coin.properties["point_value"]

            # Play the coin sound
            arcade.play_sound(self.coin_sound)

            # Remove the coin
            coin.remove_from_sprite_lists()

        # Now check if we're at the ending goal
        goals_hit = arcade.check_for_collision_with_list(
            self.player, self.goals_list
        )

        for goal in goals_hit:
            # Setup the next level
            self.level += 1
            self.setup()

        # Scroll the viewport if necessary
        self.scroll_viewport()

    def on_key_press(self, key: int, modifiers: int):
        """Processes key presses
        
        Arguments:
            key {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were down at the time
        """

        # Check for player left/right movement
        if key in [arcade.key.LEFT, arcade.key.J]:
            self.player.change_x = -PLAYER_MOVE_SPEED
        elif key in [arcade.key.RIGHT, arcade.key.L]:
            self.player.change_x = PLAYER_MOVE_SPEED

        # Check if player can climb up or down
        elif key in [arcade.key.UP, arcade.key.I]:
            if self.physics_engine.is_on_ladder():
                self.player.change_y = PLAYER_MOVE_SPEED
        elif key in [arcade.key.DOWN, arcade.key.K]:
            if self.physics_engine.is_on_ladder():
                self.player.change_y = -PLAYER_MOVE_SPEED

        # Check if we can jump
        elif key == arcade.key.SPACE:
            if self.physics_engine.can_jump():
                self.player.change_y = PLAYER_JUMP_SPEED
                # Play the jump sound
                arcade.play_sound(self.jump_sound)

    def on_key_release(self, key: int, modifiers: int):
        """Processes key releases
        
        Arguments:
            key {int} -- Which key was released
            modifiers {int} -- Which modifiers were down at the time
        """

        # Check for player left/right movement
        if key in [
            arcade.key.LEFT,
            arcade.key.J,
            arcade.key.RIGHT,
            arcade.key.L,
        ]:
            self.player.change_x = 0

        # Check if player can climb up or down
        elif key in [
            arcade.key.UP,
            arcade.key.I,
            arcade.key.DOWN,
            arcade.key.K,
        ]:
            if self.physics_engine.is_on_ladder():
                self.player.change_y = 0

    def scroll_viewport(self):
        """Scrolls the viewport when the player gets close to the edges
        """

        # By default, don't change anything
        changed_viewport = False

        # Scroll left
        # Find the current left boundary
        left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN

        # Are we to the left of this boundary? Then we should scroll left
        if self.player.left < left_boundary:
            self.view_left -= left_boundary - self.player.left
            # But don't scroll past the left edge of the map
            if self.view_left < 0:
                self.view_left = 0
            else:
                changed_viewport = True

        # Scroll right
        # Find the current right boundary
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN

        # Are we right of this boundary? Then we should scroll right
        if self.player.right > right_boundary:
            self.view_left += self.player.right - right_boundary
            # Don't scroll past the right edge of the map
            if self.view_left + SCREEN_WIDTH > self.map_width:
                self.view_left = self.map_width - SCREEN_WIDTH
            else:
                changed_viewport = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.player.top > top_boundary:
            self.view_bottom += self.player.top - top_boundary
            changed_viewport = True

        # Scroll down
        bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.player.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player.bottom
            changed_viewport = True

        if changed_viewport:
            # Only scroll to integers. Otherwise we end up with pixels that
            # don't line up on the screen
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # Do the scrolling
            arcade.set_viewport(
                self.view_left,
                SCREEN_WIDTH + self.view_left,
                self.view_bottom,
                SCREEN_HEIGHT + self.view_bottom,
            )


# Main
if __name__ == "__main__":
    window = Platformer()
    window.setup()
    arcade.run()
