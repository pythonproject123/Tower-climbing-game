# Source for enemies image - https://dribbble.com/shots/1819732-Evil-flying-monster-sprite-sheets
from SpriteSheets import *

# ENEMY_NAME = (x_coordinate, y_coordinate, width, height, facing_direction)
BASIC_ENEMY = (124, 138, 76, 90)
SHOOTING_ENEMY = (249, 23, 107, 87)
BOSS_ENEMY = (241, 145, 79, 76)
BOMB = (377, 20, 83, 92)


class Enemy_Sprite(pygame.sprite.Sprite):

    def __init__(self, sprite_location, type):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        sprite_sheet = SpriteSheet('enemies.png')
        self.image = sprite_sheet.get_image(sprite_location[0], sprite_location[1],
                                            sprite_location[2], sprite_location[3])
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()

    def getType(self):
        return self.type
