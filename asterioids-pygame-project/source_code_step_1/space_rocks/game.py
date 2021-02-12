import pygame


class SpaceRocks:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))

    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Space Rocks")

    def _handle_input(self):
        pass

    def _process_game_logic(self):
        pass

    def _draw(self):
        self.screen.fill((0, 0, 255))
        pygame.display.flip()
