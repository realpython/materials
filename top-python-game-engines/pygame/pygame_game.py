"""
Complete game in Pygame

This game demonstrates some of the more advanced features of
Pygame, including:
- Using sprites to render complex graphics
- Handling user mouse input
- Basic sound output
"""

# Import and initialize the pygame library
# To find your assets
from pathlib import Path

# To randomize coin placement
from random import randint

# For type hinting
from typing import Tuple

import pygame

# Set the width and height of the output window, in pixels
WIDTH = 800
HEIGHT = 600

# How quickly do you generate coins? Time is in milliseconds
coin_countdown = 2500
coin_interval = 100

# How many coins can be on the screen before you end?
COIN_COUNT = 10


# Define the Player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        """Initialize the player sprite"""
        super(Player, self).__init__()

        # Get the image to draw for the player
        player_image = str(Path.cwd() / "images" / "alien_green_stand.png")
        # Load the image, preserve alpha channel for transparency
        self.surf = pygame.image.load(player_image).convert_alpha()
        # Save the rect so you can move it
        self.rect = self.surf.get_rect()

    def update(self, pos: Tuple):
        """Update the position of the player

        Arguments:
            pos {Tuple} -- the (X,Y) position to move the player
        """
        self.rect.center = pos


# Define the Coin sprite
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        """Initialize the coin sprite"""
        super(Coin, self).__init__()

        # Get the image to draw for the coin
        coin_image = str(Path.cwd() / "images" / "coin_gold.png")

        # Load the image, preserve alpha channel for transparency
        self.surf = pygame.image.load(coin_image).convert_alpha()

        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                randint(10, WIDTH - 10),
                randint(10, HEIGHT - 10),
            )
        )


# Initialize the Pygame engine
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode(size=[WIDTH, HEIGHT])

# Hide the mouse cursor
pygame.mouse.set_visible(False)

# Set up the clock for a decent frame rate
clock = pygame.time.Clock()

# Create a custom event for adding a new coin
ADDCOIN = pygame.USEREVENT + 1
pygame.time.set_timer(ADDCOIN, coin_countdown)

# Set up the coin_list
coin_list = pygame.sprite.Group()

# Initialize the score
score = 0

# Set up the coin pickup sound
coin_pickup_sound = pygame.mixer.Sound(
    str(Path.cwd() / "sounds" / "coin_pickup.wav")
)

# Create a player sprite and set its initial position
player = Player()
player.update(pygame.mouse.get_pos())

# Run until you get to an end condition
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Should you add a new coin?
        elif event.type == ADDCOIN:
            # Create a new coin and add it to the coin_list
            new_coin = Coin()
            coin_list.add(new_coin)

            # Speed things up if fewer than three coins are on-screen
            if len(coin_list) < 3:
                coin_countdown -= coin_interval
            # Need to have some interval
            if coin_countdown < 100:
                coin_countdown = 100

            # Stop the previous timer by setting the interval to 0
            pygame.time.set_timer(ADDCOIN, 0)

            # Start a new timer
            pygame.time.set_timer(ADDCOIN, coin_countdown)

    # Update the player position
    player.update(pygame.mouse.get_pos())

    # Check if the player has collided with a coin, removing the coin if so
    coins_collected = pygame.sprite.spritecollide(
        sprite=player, group=coin_list, dokill=True
    )
    for coin in coins_collected:
        # Each coin is worth 10 points
        score += 10
        # Play the coin collected sound
        coin_pickup_sound.play()

    # Are there too many coins on the screen?
    if len(coin_list) >= COIN_COUNT:
        # This counts as an end condition, so you end your game loop
        running = False

    # To render the screen, first fill the background with pink
    screen.fill((255, 170, 164))

    # Draw the coins next
    for coin in coin_list:
        screen.blit(coin.surf, coin.rect)

    # Then draw the player
    screen.blit(player.surf, player.rect)

    # Finally, draw the score at the bottom left
    score_font = pygame.font.SysFont("any_font", 36)
    score_block = score_font.render(f"Score: {score}", False, (0, 0, 0))
    screen.blit(score_block, (50, HEIGHT - 50))

    # Flip the display to make everything appear
    pygame.display.flip()

    # Ensure you maintain a 30 frames per second rate
    clock.tick(30)

# Done! Print the final score
print(f"Game over! Final score: {score}")

# Make the mouse visible again
pygame.mouse.set_visible(True)

# Quit the game
pygame.quit()
