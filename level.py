from Enemy import *
import Player
from Platform import *
from Enemy_Sprite import *
from Heart_Sprites import *
from Coin_Sprite import *
import pygame

from Projectile_Sprite import *


class Level:
    world_shift = 0
    level_limit = 0

    def __init__(self, player):
        self.background = None
        self.enemy_list = pygame.sprite.Group()
        self.platform_list = pygame.sprite.Group()
        self.health_bar = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.coins_needed = pygame.sprite.Group()
        self.player = player
        self.hardmode = False
        self.coinsNeeded

    def getEnemies(self):
        return self.enemy_list

    def getPlatforms(self):
        return self.platform_list

    def getPlayer(self):
        return self.player

    def isHardMode(self):
        return self.hardmode

    # Define number of coins needed to win
    def coinsNeeded(self, num):
        self.coinsNeeded = num

    def draw(self, screen):
        screen.fill((0, 0, 255))
        screen.blit(self.background, (self.world_shift // 3, 0))
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.health_bar.draw(screen)
        self.coins.draw(screen)
        self.coins_needed.draw(screen)

    def update(self):
        self.platform_list.update()
        self.enemy_list.update()
        self.coins.update()

    def shift_world(self, shift_x):
        self.world_shift += shift_x
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for coin in self.coins:
            coin.rect.x += shift_x

    def addEnemies(self, enemies):
        for enemy in enemies:
            if enemy[0] == BASIC_ENEMY:
                type = BasicEnemy()
            elif enemy[0] == SHOOTING_ENEMY:
                type = ShootingEnemy("L")
                p = Projectile_Sprite(PROJECTILE)
                if type.getDirection() == "R":
                    p.rect.x = enemy[1] + 30
                else:
                    p.rect.x = enemy[1] - 30
                p.rect.y = enemy[2] + 55
                self.enemy_list.add(p)
            elif enemy[0] == BOSS_ENEMY:
                type = BossEnemy()
            elif enemy[0] == BOMB:
                type = Bomb()
            en = Enemy_Sprite(enemy[0], type)

            en.rect.x = enemy[1]
            en.rect.y = enemy[2]
            self.enemy_list.add(en)

    def addCoins(self, lv_coins):
        for coin in lv_coins:
            c = Coin_Sprite(coin[0])
            c.rect.x = coin[1]
            c.rect.y = coin[2]
            self.coins.add(c)

    def addHearts(self):
        hearts = []
        if self.isHardMode():
            for i in range(0, 1):
                hearts.append([LITTLE_HEART, (60 * i), 0])
        else:
            for i in range(0, 3):
                hearts.append([LITTLE_HEART, (60 * i), 0])

        for heart in hearts:
            h = Heart_Sprite(heart[0])
            h.rect.x = heart[1]
            h.rect.y = heart[2]
            self.health_bar.add(h)

    def addCoinsNeeded(self):
        coins_need = []
        for i in range(0, self.coinsNeeded):
            if i < 5:
                coins_need.append([COIN, (60 * i), 60])
            elif i >= 5 and i < 10:
                coins_need.append([COIN, (60 * (i-5)), 120])
            else:
                coins_need.append([COIN, (60 * (i-10)), 180])

        for coin in coins_need:
            c = Coin_Sprite(coin[0])
            c.rect.x = coin[1]
            c.rect.y = coin[2]
            self.coins_needed.add(c)

    def addPlatforms(self, platforms):
        for platform in platforms:
            block = Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)


class LevelOne(Level):
    def __init__(self, player):
        Level.__init__(self, player)
        Level.hardmode = False
        if self.isHardMode():
            self.coinsNeeded(5)
        else:
            self.coinsNeeded(3)

        self.background = pygame.image.load("level1.png").convert()
        self.background.set_colorkey((255, 255, 255))
        self.level_limit = -2500

        platforms = [[GRASS_LEFT, 500, 500],
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
                   [BOMB, 1000, 420],
                   [BOMB, 1200, 500]]

        lv_coins = [[COIN, 500, 420],
                    [COIN, 750, 300],
                    [COIN, 1200, 200],
                    [COIN, 1025, 350],
                    [COIN, 1220, 450]]

        self.addEnemies(enemies)
        self.addCoins(lv_coins)
        self.addCoinsNeeded()
        self.addHearts()
        self.addPlatforms(platforms)

        # Add a custom moving platform
        block = MovingPlatform([648, 648, 70, 40])
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)