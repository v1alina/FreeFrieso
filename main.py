import pygame
import sys

"""
TO DO:
- add sprites
- add collisions
- add arrows
"""


class Game:
    def __init__(self):
        self.running = True
        self.WINDOW_WIDTH = 400
        self.WINDOW_HEIGHT = 400
        self.BACKGROUND_COLOR = (202, 3, 140)
        self.FPS = 60
        self.CAPTION = "Miriso"

    def draw(self, window, players):
        # draw background
        window.fill(self.BACKGROUND_COLOR)

        # draw players
        for player in players:
            player.draw(window, player.picture)

        # update window
        pygame.display.flip()

    def run(self):
        # initiate pygame
        pygame.init()
        print ("/nThis is our game!")

        # create window
        window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption(self.CAPTION)

        # create players
        players = []
        gort = Player((100, self.WINDOW_HEIGHT-50), 'Pictures/run.png')
        liva = Player((50, self.WINDOW_HEIGHT-50), 'Pictures/Gort1.png')
        players.append(gort)
        #players.append(liva)
        #sprite = gort.get_image(24, 24)


        # clock
        clock = pygame.time.Clock()

        # main game loop
        while self.running:

            # limit the frame rate
            clock.tick(self.FPS)

            # draw the background and players on the screen
            self.draw(window, players)

            # event loop
            for event in pygame.event.get():

                # check if window is closed
                if event.type == pygame.QUIT:
                    self.running = False
                    break

                # detects players jumping with 'KEYDOWN' instead of 'key.get_pressed()'
                # so the player only jumps once instead of as long as the key is pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        gort.move("up")
                    elif event.key == pygame.K_w:
                        liva.move("up")

            # check which keys are pressed
            keys = pygame.key.get_pressed()

            # left/right movement for Gort and Liva, respectively
            # resets x_velocity so the player stops moving when the key is no longer pressed
            gort.x_velocity = 0
            if keys[pygame.K_LEFT]:
                gort.move("left")
            if keys[pygame.K_RIGHT]:
                gort.move("right")

            liva.x_velocity = 0
            if keys[pygame.K_a]:
                liva.move("left")
            if keys[pygame.K_d]:
                liva.move("right")

            # update players' positions and velocities
            for player in players:
                player.update(self.FPS)

        # exit the game/program
        pygame.quit()
        sys.exit()


class Player(pygame.sprite.Sprite):
    def __init__(self, start_pos, picture):
        self.x = 0
        self.y = 0
        # convert_alpha is necessary for transparent background
        self.picture = pygame.image.load(picture).convert_alpha()
        self.width = self.picture.get_width()
        self.height = self.picture.get_height()
        self.velocity = 5
        self.x_velocity = 0
        self.y_velocity = 0
        self.fall_count = 0
        self.gravity = 1
        animation_count = 0

    def move(self, direction):
        if direction == "left":
            self.x_velocity = -self.velocity
        elif direction == "right":
            self.x_velocity = self.velocity
        elif direction == "up":
            self.y_velocity = -self.gravity * 16

    def update(self, fps):
        # simulates gravity: increasing fall_count is more acceleration
        # with a minimum of 1 so the first part of falling is not too slow
        self.y_velocity += min(1, (self.fall_count / fps) * self.gravity)
        self.fall_count += 1

        # update the player's position
        # note: the minimum of 350 ensures the player does not fall off the screen
        # replace second line with 'self.y += self.y_velocity' once platforms are added
        self.x += self.x_velocity
        self.y = min(350, self.y + self.y_velocity)


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
