#Source for heart image -
# https://gamedev.stackexchange.com/questions/51060/why-should-i-choose-to-design-a-health-bar-rather-than-heart-containers

from SpriteSheets import *

#NAME = (x_coordinate, y_coordinate, width, height)
LITTLE_HEART = (262, 267, 51, 48)
BIG_HEART = (419, 238, 111, 115)


class Heart_Sprite(pygame.sprite.Sprite):

    def __init__(self, sprite_location):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        sprite_sheet = SpriteSheet('healthHeart.png')
        self.image = sprite_sheet.get_image(sprite_location[0], sprite_location[1],
                                            sprite_location[2], sprite_location[3])
        self.rect = self.image.get_rect()