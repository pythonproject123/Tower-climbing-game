from SpriteSheets import *


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
    def __init__(self):
        self.range = None
        Enemy.__init__(self, "Shooting Enemy", 2)
        self.range = 10  # Change once we figure out how to work out distances


    def getRange(self):
        return self.range


class BossEnemy(Enemy):
    def __init__(self):
        Enemy.__init__(self, "Boss Enemy", 3)

#Cannot jump on this enemy's head to kill it
class Bomb(Enemy):
    def __init__(self):
        Enemy.__init__(self, "Bomb", 1)
