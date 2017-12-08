from SpriteSheets import *
from Projectile_Sprite import *
from Enemy_Sprite import *


# Abstract class - do not instantiate
class Enemy(pygame.sprite.Sprite):

    def __init__(self, type, damage):
        self.type = type
        self.damage = damage

    def getType(self):
        return self.type

    def getDamage(self):
        return self.damage


# Sub-classes
class BasicEnemy(Enemy):
    def __init__(self):
        Enemy.__init__(self, "Basic Enemy", 1)


class ShootingEnemy(Enemy):
    # Change dir to have the enemy facing right instead. Defaults to left.
    def __init__(self, proj = None, dir="L"):
        self.dir = dir
        Enemy.__init__(self, "Shooting Enemy", 1)

    def getDirection(self):
        return self.dir

class BossEnemy(Enemy):
    def __init__(self):
        Enemy.__init__(self, "Boss Enemy", 3)


# Cannot jump on this enemy's head to kill it
class Bomb(Enemy):
    def __init__(self):
        Enemy.__init__(self, "Bomb", 1)
