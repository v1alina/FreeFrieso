import pygame
import sys

"""
TO DO:
- fix jumping 
- add max jump_count
- horizontal collision
- add masks
- fall on the side off the screen
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

        # draw platforms and players
        platforms.draw(window)
        players.draw(window)

        # update window
        pygame.display.flip()

    def run(self):
        # initiate pygame
        pygame.init()

        # create window
        window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption(self.CAPTION)

        # create players
        players = pygame.sprite.Group()
        gort = Player(50, 50, "blue")
        gort.rect.x = 200
        liva = Player(50, 50, "red")
        liva.rect.x = 50
        players.add(gort)
        players.add(liva)

        # create platforms
        platforms = pygame.sprite.Group()
        platform = Platform(100, 20, "red")
        platform.rect.x = 100
        platform.rect.y = 200
        floor = Platform(400, 10, "green")
        floor.rect.y = 390
        platforms.add(platform)
        platforms.add(floor)

        # clock
        clock = pygame.time.Clock()

        # main game loop
        while self.running:

            # limit the frame rate
            clock.tick(self.FPS)

            # draw the background and players on the screen
            self.draw(window, players, platforms)

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

            # check collision
            for player in players:
                player.check_collision(platforms)

        # exit the game/program
        pygame.quit()
        sys.exit()


class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, color, picture=None):
        super().__init__()
        # convert_alpha is necessary for transparent background
        #self.picture = pygame.image.load(picture).convert_alpha()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = 5
        self.x_velocity = 0
        self.y_velocity = 0
        self.fall_count = 0
        self.gravity = 2

    def move(self, direction):
        if direction == "left":
            self.x_velocity = -self.velocity
        elif direction == "right":
            self.x_velocity = self.velocity
        elif direction == "up":
            self.y_velocity = -self.gravity * 4

    def check_collision(self, objects):
        objects_hit = pygame.sprite.spritecollide(self, objects, False)
        if objects_hit:
            if self.y_velocity < 0:
                self.rect.top = objects_hit[0].rect.bottom
                self.y_velocity *= -1
            elif self.y_velocity > 0:
                self.rect.bottom = objects_hit[0].rect.top
                self.fall_count = 0
                self.y_velocity = 0

    def update(self, fps):
        # simulates gravity: increasing fall_count is more acceleration
        # with a minimum of 1 so the first part of falling is not too slow
        self.y_velocity += min(1, (self.fall_count / fps) * self.gravity)
        self.fall_count += 1

        # update the player's position
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity


class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()


if __name__ == "__main__":
    game = Game()
    game.run()
