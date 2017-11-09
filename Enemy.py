#Abstract class - do not instantiate
class Enemy():
    def __init__(self, type, damage):
        self.type = type
        self.damage = damage
        self.alive = True

    def hitPlayer(self, player):
        player.hit(self.damage)

    def gotHit(self):
        self.alive = False

    def getType(self):
        return self.type
    def getDamage(self):
        return self.damage
    def isAlive(self):
        return self.alive

#Sub-classes
class BasicEnemy(Enemy):
    def __init__(self):
        Enemy.__init__(self, "Basic Enemy", 1)

class ShootingEnemy(Enemy):
    def __init__(self):
        Enemy.__init__(self, "Shooting Enemy", 2)
        range = 10 #Change once we figure out how to work out distances

    def getRange(self):
        return self.range

class BossEnemy(Enemy):
    def __init__(self):
        Enemy.__init__(self, "Boss Enemy", 3)