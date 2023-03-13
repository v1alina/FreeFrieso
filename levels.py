import pygame
import numpy as np
import os
from game_objects import Platform

class Level:

    @classmethod
    def load(cls, level_number):
        # read level into memory
        with open(f"assets/levels/{level_number}.txt", "r") as file:
            level = file.read()

        # get level and block sizes
        level_width = level.index("\n")
        level_height = level.count("\n")

        block_width = pygame.display.get_surface().get_width() / level_width
        block_height = pygame.display.get_surface().get_height() / level_height

        # remove whitespace
        level = level.replace("\n", "")

        # generate platforms
        platforms = pygame.sprite.Group()

        for y in range(level_height):
            for x in range(level_width):
                if level[y * level_width + x] == "#":
                    platforms.add(
                        Platform(
                            np.array([x * block_width, y * block_height]),
                            pygame.Surface((block_width, block_height))
                        )
                    )
    
        # return sprite group
        return platforms
    
    @classmethod
    def generate(cls, width, height):
        
        # create a new level with just an outline
        level = str()

        level += "#" * width + "\n"
        for _ in range(height-2):
            level += f"#{' ' * (width - 2)}#\n"
        level += "#" * width + "\n"

        # counts how many levels there already are and adds 1
        level_number = sum([1 for x in list(os.scandir("assets/levels")) if x.is_file()]) + 1

        # store level as a text file
        with open(f"assets\levels\{level_number}.txt", "w") as file:
            file.write(level)
