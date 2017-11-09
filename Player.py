class Player():
    def __init__(self, name):
        self.name = name
        self.health = 3
        self.coins = 0

    def hit(self, damage):
        self.health -= damage

    def collectCoin(self):
        self.coins += 1