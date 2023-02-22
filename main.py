import pygame
from pygame.locals import *

"""
TO DO:
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
        gort = Player((100, self.window_height-20))
        liva = Player((50, self.window_height-20))

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
                gort.move("LEFT")
            if keys[K_RIGHT]:
                gort.x += gort.velocity
                gort.picture = pygame.transform.flip(gort.picture, True, False)
                gort.move("RIGHT")
            if keys[K_UP]:
                gort.move("UP")
            if keys[K_DOWN]:
                gort.move("DOWN")


            # movement for Liva (my player)
            if keys[K_a]:
                liva.move("LEFT")
            if keys[K_d]:
                liva.move("RIGHT")
            if keys[K_w]:
                liva.move("UP")
            if keys[K_s]:
                liva.move("DOWN")

            # update hitboxes
            gort.hitbox = pygame.Rect(gort.x, gort.y, gort.width, gort.height)
            liva.hitbox = pygame.Rect(liva.x, liva.y, liva.width, liva.height)

            # check collision
            if gort.hitbox.colliderect(liva.hitbox):
                print("hit")


class Player:
    def __init__(self, start_pos):
        self.x, self.y = start_pos
        self.width = 20
        self.height = 20
        self.color = "black"
        self.picture = pygame.image.load('Pictures/Gort1.png')
        self.picture.convert()
        self.velocity = 3
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, direction):
        if direction == "LEFT":
            if self.x < self.velocity:
                self.x = 0
            else:
                self.x -= self.velocity
        elif direction == "RIGHT":
            if self.x + self.width > 400 - self.velocity:
                self.x = 400 - self.width
            else:
                self.x += self.velocity
        elif direction == "UP":
            if self.y < self.velocity:
                self.y = 0
            else:
                self.y -= self.velocity
        elif direction == "DOWN":
            if self.y + self.height > 400 - self.velocity:
                self.y = 400 - self.height
            else:
                self.y += self.velocity

    def draw(self, window):
            #gort_pic = pygame.image.load('Pictures/Gort1.png')
            #gort_pic.convert()
            rect = self.picture.get_rect()
            rect.center = self.x, self.y
            RED = (255, 0, 0)
            pygame.draw.rect(window, RED, rect, 1)
            window.blit(self.picture, rect)

            #pygame.draw.rect (window, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))


class Arrow:
    pass


if __name__ == "__main__":
    game = Game()
    game.run()
