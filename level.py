from Enemy import *
import Player
from Platform import *
from Enemy_Sprite import *
import pygame


class Level:
    world_shift = 0
    level_limit = 0

    def __init__(self, player):
        self.background = None
        self.enemy_list = pygame.sprite.Group()
        self.platform_list = pygame.sprite.Group()
        self.player = player
        self.hardmode = False

    def getEnemies(self):
        return self.enemy_list

    def getPlatforms(self):
        return self.platform_list

    def getPlayer(self):
        return self.player

    def isHardMode(self):
        return self.hardmode

    def draw(self, screen):
        screen.fill((0, 0, 255))
        screen.blit(self.background, (self.world_shift // 3, 0))
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def update(self):
        self.platform_list.update()
        self.enemy_list.update()

    def shift_world(self, shift_x):
        self.world_shift += shift_x
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x


class LevelOne(Level):
    def __init__(self, player):
        Level.__init__(self, player)
        self.hardmode = False
        maxCoins = 10
        if self.hardmode:
            coinsNeeded = 7
        else:
            coinsNeeded = 5

        self.background = pygame.image.load("level1.png").convert()
        self.background.set_colorkey((255, 255, 255))
        self.level_limit = -2500

        level = [[GRASS_LEFT, 500, 500],
                 [GRASS_MIDDLE, 570, 500],
                 [GRASS_RIGHT, 640, 500],
                 [GRASS_LEFT, 800, 400],
                 [GRASS_MIDDLE, 870, 400],
                 [GRASS_RIGHT, 940, 400],
                 [GRASS_LEFT, 1000, 500],
                 [GRASS_MIDDLE, 1070, 500],
                 [GRASS_RIGHT, 1140, 500],
                 [STONE_PLATFORM_LEFT, 1120, 280],
                 [STONE_PLATFORM_MIDDLE, 1190, 280],
                 [STONE_PLATFORM_RIGHT, 1260, 280]]

        enemies = [[BASIC_ENEMY, 600, 420],
                   [BASIC_ENEMY, 750, 500],
                   [BASIC_ENEMY, 1000, 420],
                   [BASIC_ENEMY, 1200, 500]]

        for enemy in enemies:
            basic = BasicEnemy()
            en = Enemy_Sprite(enemy[0], basic)
            en.rect.x = enemy[1]
            en.rect.y = enemy[2]
            self.enemy_list.add(en)

        for platform in level:
            block = Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
