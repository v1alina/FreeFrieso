import pygame
from pygame.locals import *

"""
TO DO:
- add clock
- add gravity
- add sprites
- add collisions (platforms and outer boundaries)
- add arrows
"""

class Game:
    def __init__(self):
        self.running = True
        self.window_width = 400
        self.window_height = 400
        self.background_color = (202, 3, 140)
        self.fps = 30

    def run(self):
        pygame.init()

        # create window
        window = pygame.display.set_mode((self.window_width, self.window_height))

        # create players
        gort = Player()
        liva = Player()

        # clock
        clock = pygame.time.Clock()

        # main game loop
        while self.running:

            clock.tick(self.fps)
            # drawing
            window.fill(self.background_color)
            gort.draw(window)
            liva.draw(window)
            pygame.display.flip()

            # event loop
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    pygame.quit()

            # movement for Gort (our player)
            keys = pygame.key.get_pressed()
            if keys[K_LEFT]:
                gort.x -= gort.velocity
            if keys[K_RIGHT]:
                gort.x += gort.velocity
            if keys[K_UP]:
                gort.y -= gort.velocity
            if keys[K_DOWN]:
                gort.y += gort.velocity

            # movement for Liva (my player)
            if keys[K_a]:
                liva.x -= liva.velocity
            if keys[K_d]:
                liva.x += liva.velocity
            if keys[K_w]:
                liva.y -= liva.velocity
            if keys[K_s]:
                liva.y += liva.velocity


class Player:
    def __init__(self):
        self.x = 100
        self.y = 69
        self.width = 20
        self.height = 20
        self.color = "black"
        self.velocity = 1

    def draw(self, window):
        pygame.draw.rect (window, self.color, (self.x, self.y, self.width, self.height))


class Arrow:
    pass


if __name__ == "__main__":
    game = Game()
    game.run()
