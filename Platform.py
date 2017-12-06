# source of tiles file: https://opengameart.org/content/platformer-art-deluxe

from SpriteSheets import *

GRASS_LEFT = (576, 720, 70, 70)
GRASS_RIGHT = (576, 576, 70, 70)
GRASS_MIDDLE = (504, 576, 70, 70)
STONE_PLATFORM_LEFT = (432, 720, 70, 40)
STONE_PLATFORM_MIDDLE = (648, 648, 70, 40)
STONE_PLATFORM_RIGHT = (792, 648, 70, 40)


class Platform(pygame.sprite.Sprite):

    def __init__(self, sprite_location):
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet('tiles_spritesheet.png')
        self.image = sprite_sheet.get_image(sprite_location[0], sprite_location[1],
                                            sprite_location[2], sprite_location[3])
        self.rect = self.image.get_rect()
