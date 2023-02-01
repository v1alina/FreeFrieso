import pygame
from pygame.locals import *

pygame.init()
win = pygame.display.set_mode((400, 400))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            break
