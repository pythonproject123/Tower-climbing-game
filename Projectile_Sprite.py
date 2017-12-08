#Source for projectile image - https://graphicriver.net/item/arcade-shoot-projectiles/4081594
from SpriteSheets import *

# Do not use this projectile in the level directly! It's attached to a particular enemy
# and is put in automatically relative to that enemy when it's added
PROJECTILE = (393.1, 290.6, 8.3, 16.2)


class Projectile_Sprite(pygame.sprite.Sprite):

    def __init__(self, sprite_location, enemy):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        sprite_sheet = SpriteSheet('projectile.png')
        self.image = sprite_sheet.get_image(sprite_location[0], sprite_location[1],
                                            sprite_location[2], sprite_location[3])
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect()

        self.change_x = 1
        self.origPos = 0

        self.player = None
        self.level = None

        self.enemy = enemy
        self.boundary = 0

    def getType(self):
        return "Projectile"

    def update(self):

        # Move left/right
        if self.enemy.getDirection() == "L":
            self.rect.x -= self.change_x
        else:
            self.rect.x += self.change_x

        # See if the player hit the platform
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            self.kill()
            self.player.hit(2)
            for i in range(1, 3):
                sp = self.level.health_bar.sprites()
                sp[len(sp) - 1].kill()
            if not self.player.alive:
                self.player.kill()
                return

        # Check the boundaries and see if we need to reset.
        cur_pos = self.rect.x - self.level.world_shift
        if (self.enemy.getDirection() == "L" and cur_pos < self.boundary) or (
                self.enemy.getDirection() == "R" and cur_pos > self.boundary):
            self.rect.x = self.origPos