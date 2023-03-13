import pygame
    
        
class Object(pygame.sprite.Sprite):
    def __init__(self, position, image):
        super().__init__()
        self.image = image
        self.rect = image.get_rect()
        self.rect.topleft = position


class Player(Object):
    def __init__(self, position, image):
        super().__init__(position, image)


class Platform(Object):
    def __init__(self, position, image):
        super().__init__(position, image)
