#source of tiles file: https://opengameart.org/content/platformer-art-deluxe

from SpriteSheets import *


class Platform(pygame.sprite.Sprite):

    def __init__(self):
        super.__init__()
        sprite_sheet = SpriteSheet('tiles_spritesheet.png')
        self.image = sprite_sheet.get_image(14*8, 14*6, 14, 14)
        self.rect = self.image.get_rect()
