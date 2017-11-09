import pygame
import Enemy
import Player


class Level:
    world_shift = 0
    level_limit = -1000

    def __init__(self, filename, player, hardmode = False):
        self.background = pygame.image.load(filename).convert()
        self.enemy_list = []
        self.platform_list = []
        self.player = player
        self.hardmode = hardmode

    def getEnemies(self):
        return self.enemy_list
    def getPlatforms(self):
        return self.platform_list
    def getPlayer(self):
        return self.player
    def isHardMode(self):
        return self.hardmode

    def paint(self, screen):
        screen.blit(self.background, (self.world_shift // 3, 0))


class LevelOne(Level):
    def __init__(self, filename, player, hardmode):
        Level.__init__(self, filename, player, hardmode)
        maxCoins = 10
        if hardmode:
            coinsNeeded = 7
        else:
            coinsNeeded = 5
        for i in range(0, 5):
            enemy_list.append(BasicEnemy())


