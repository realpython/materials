"""
Basic "Hello, World!" program in Pygame

This program is designed to demonstrate the basic capabilities
of Pygame. It will:
- Create a simple game window
- Fill the background with white
- Draw some simple shapes in different colors
- Draw some text in a specified size and color
- Allow you to close the window
"""

# Import and initialize the pygame library
import pygame

pygame.init()

# Set the width and height of the output window, in pixels
WIDTH = 800
HEIGHT = 600

# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a blue circle with a radius of 50 in the center of the screen
    pygame.draw.circle(screen, (0, 0, 255), (WIDTH // 2, HEIGHT // 2), 50)

    # Draw a red-outlined square in the top-left corner of the screen
    red_square = pygame.Rect((50, 50), (100, 100))
    pygame.draw.rect(screen, (200, 0, 0), red_square, 1)

    # Draw an orange caption along the bottom in 60-point font
    text_font = pygame.font.SysFont("any_font", 60)
    text_block = text_font.render(
        "Hello, World! From Pygame", False, (200, 100, 0)
    )
    screen.blit(text_block, (50, HEIGHT - 50))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.

pygame.quit()
