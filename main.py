import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        self.running = True
        self.window_width = 400
        self.window_height = 400
        self.background_color = (202, 3, 140)

    def run(self):
        pygame.init()

        # create window
        window = pygame.display.set_mode((self.window_width, self.window_height))

        # main game loop
        while self.running:
            window.fill(self.background_color)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    pygame.quit()



class Player:
    pass

class Arrow:
    pass

if __name__ == "__main__":
    game = Game()
    game.run()
