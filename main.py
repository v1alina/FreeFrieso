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

    def redrawWindow(self, window, players):
        # draw background
        window.fill(self.background_color)

        # draw players
        for player in players:
            player.draw(window, player.picture)

        # update window
        pygame.display.flip()

    def run(self):
        pygame.init()

        # create window
        window = pygame.display.set_mode((self.window_width, self.window_height))

        # create players
        players = []
        gort = Player((100, self.window_height-50), 'Pictures/run.png')
        liva = Player((50, self.window_height-50), 'Pictures/Gort1.png')
        players.append(gort)
        #players.append(liva)
        #sprite = gort.get_image(24, 24)


        # clock
        clock = pygame.time.Clock()

        # main game loop
        while self.running:

            clock.tick(self.fps)
            self.redrawWindow(window, players)

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


class Player(pygame.sprite.Sprite):
    def __init__(self, start_pos, picture):
        self.x, self.y = start_pos
        self.picture = pygame.image.load(picture).convert_alpha()
        self.width = self.picture.get_width()
        self.height = self.picture.get_height()
        self.velocity = 3
        self.left = False
        self.right = True
        self.sprites = []


    def move(self, direction):
        if direction == "LEFT":
            self.left = True
            self.right = False
            if self.x < self.velocity:
                self.x = 0
            else:
                self.x -= self.velocity
        elif direction == "RIGHT":
            self.left = False
            self.right = True
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


    def get_image(self, sheet, width, height):
        image = pygame.Surface((width,height)).convert_alpha()
        image.blit(sheet,(0,0),(0,0, width, height))
        return image

    def draw(self, window,image):
        rect = self.get_image(image, 30,30).get_rect()
        #rect = self.picture.get_rect()
        #rect.topleft = self.x, self.y
        #pygame.draw.rect(window, "red", rect, 1)
        #self.picture = pygame.transform.flip(self.picture, False, True)
        window.blit(self.get_image(image, 30,30), rect)


class Arrow:
    pass


if __name__ == "__main__":
    game = Game()
    game.run()
