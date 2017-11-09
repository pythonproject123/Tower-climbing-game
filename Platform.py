import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super.__init__()
        self.image = pygame.image.load('platform.png').convert()
        self.rect = self.image.get_rect()
