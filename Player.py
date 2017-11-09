class Player():
    def __init__(self, name):
        self.name = name
        self.health = 3
        self.coins = 0

    def hit(self, damage):
        self.health -= damage

    def collectCoin(self):
        self.coins += 1

    def getHealth(self):
        return self.health
    def getCoins(self):
        return self.coins
    def getName(self):
        return self.name

    def jump(self):
        pass #Define jump behavior

    def moveLeft(self):
        pass #Define moving left

    def moveRight(self):
        pass #Define moving right