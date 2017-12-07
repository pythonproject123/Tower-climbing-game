from SpriteSheets import *

# NAME = (x_coordinate, y_coordinate, width, height)
COIN = (7.8, 13.5, 48.7, 56.3)


class Coin_Sprite(pygame.sprite.Sprite):

    def __init__(self, sprite_location):
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet('coin.png')
        self.image = sprite_sheet.get_image(sprite_location[0], sprite_location[1],
                                            sprite_location[2], sprite_location[3])
        self.rect = self.image.get_rect()