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
        gort = Player ()
        print("uwu")


        # create window
        window = pygame.display.set_mode((self.window_width, self.window_height))

        # main game loop
        while self.running:
            window.fill(self.background_color)
            gort.draw (window)
            pygame.display.flip()
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





class Player:
    def __init__(self):
        self.x = 100
        self.y = 69
        self.width = 20
        self.height = 20
        self.color = (0,0,0)
        self.velocity = 3

    def draw(self, window):

        pygame.draw.rect (window, self.color, (self.x, self.y, self.width, self.height))

class Arrow:
    pass

if __name__ == "__main__":
    game = Game()
    game.run()
