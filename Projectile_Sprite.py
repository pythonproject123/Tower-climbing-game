#Source for projectile image - https://graphicriver.net/item/arcade-shoot-projectiles/4081594
from SpriteSheets import *

# Do not use this projectile in the level directly! It's attached to a particular enemy
# and is put in automatically relative to that enemy when it's added
PROJECTILE = (393.1, 290.6, 8.3, 16.2)


class Projectile_Sprite(pygame.sprite.Sprite):

    def __init__(self, sprite_location):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        sprite_sheet = SpriteSheet('projectile.png')
        self.image = sprite_sheet.get_image(sprite_location[0], sprite_location[1],
                                            sprite_location[2], sprite_location[3])
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect()

    def getType(self):
        return "Projectile"