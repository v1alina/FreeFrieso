import pygame
import sys
#import numpy as np
import levels
from game_objects import Player
from levels import Level
#import math


class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.caption = "Game Name"
        self.fps = 60

    def run(self):

        # window settings
        window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption(self.caption)

        # clock
        clock = pygame.time.Clock()

        # create players
        players = pygame.sprite.Group()
        gort = Player(
            (100, 100),
            pygame.transform.scale(pygame.image.load("assets/images/Gort1.png").convert_alpha(), (100, 100))
        )
        players.add(gort)

        # create platforms
        platforms = Level.load(0)

        # main game loop
        while self.running:
            
            # limit the frame rate
            clock.tick(self.fps)

            # draw
            self.draw(window, players, platforms)

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:

                    # pressing escape terminates the program
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        pygame.quit()
                        sys.exit()

    def draw(self, surface, players, platforms):
        # draw background
        background = pygame.image.load("assets/images/temp_background.jpg")
        surface.blit(background, (0, 0))

        # draw players and platforms
        players.draw(surface)
        platforms.draw(surface)

        # update screen
        pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
