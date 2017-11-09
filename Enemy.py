#Abstract class
class Enemy():
    def __init__(self, name, type, damage):
        self.name = name
        self.type = type
        self.damage = damage
        self.alive = True

    def hitPlayer(self, player):
        player.hit(self.damage)

    def hit(self):
        self.alive = False
