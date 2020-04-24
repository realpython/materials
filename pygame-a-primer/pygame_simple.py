# Simple pygame program

# Import and initialize the pygame library
import pygame

pygame.init()

# Setup the window we'll use for drawing
screen = pygame.display.set_mode([500, 500])

# Run until the user asks us to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# We're done, so we can quit now.
pygame.quit()
