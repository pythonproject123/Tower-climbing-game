from Enemy import *
from Platform import *
from Enemy_Sprite import *
from Heart_Sprites import *
from Coin_Sprite import *

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
                type = ShootingEnemy()

                p = Projectile_Sprite(PROJECTILE, type)
                if type.getDirection() == "L":
                    p.rect.x = enemy[1] - 30
                    p.boundary = p.rect.y - 20
                else:
                    p.rect.x = enemy[1] + 50
                    p.boundary = p.rect.y + 20
                p.origPos = p.rect.x
                p.rect.y = enemy[2] + 55
                p.player = self.player
                p.level = self
                self.enemy_list.add(p)

            elif enemy[0] == BOSS_ENEMY:
                type = BossEnemy()
            elif enemy[0] == BOMB:
                type = Bomb()

            en = Enemy_Sprite(enemy[0], type)
            if len(enemy) > 3 and enemy[3] == "R":
                en.image = pygame.transform.flip(en.image, True, False)

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
            elif 10 > i >= 5:
                coins_need.append([COIN, (60 * (i - 5)), 120])
            else:
                coins_need.append([COIN, (60 * (i - 10)), 180])

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

    def reset(self):
        self.enemy_list = pygame.sprite.Group()
        self.platform_list = pygame.sprite.Group()
        self.health_bar = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.coins_needed = pygame.sprite.Group()


class LevelOne(Level):
    def __init__(self, player):
        Level.__init__(self, player)
        Level.hardmode = False
        if self.isHardMode():
            self.coinsNeeded(5)
        else:
            self.coinsNeeded(5)

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

        enemies = [[BASIC_ENEMY, 600, 420],  # Add optional "R" or "L" argument to change facing direction.
                   [BASIC_ENEMY, 750, 500],  # Defaults to left-facing
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

class LevelTwo(Level):
    def __init__(self, player):
        Level.__init__(self, player)
        Level.hardmode = False
        if self.isHardMode():
            self.coinsNeeded(7)
        else:
            self.coinsNeeded(5)

        self.background = pygame.image.load("level2.png").convert()
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

        enemies = [[BASIC_ENEMY, 600, 420],      # Add optional "R" or "L" argument to change facing direction.
                   [BASIC_ENEMY, 750, 500],      # Defaults to left-facing
                   [BOMB, 1000, 420],
                   [BOSS_ENEMY, 1200, 500]]

        lv_coins = [[COIN, 500, 420],
                    [COIN, 750, 300],
                    [COIN, 1200, 200],
                    [COIN, 1025, 350],
                    [COIN, 1220, 450],
                    [COIN, 1000, 250],
                    [COIN, 850, 325]]

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

class LevelThree(Level):
    def __init__(self, player):
        Level.__init__(self, player)
        Level.hardmode = False
        if self.isHardMode():
            self.coinsNeeded(10)
        else:
            self.coinsNeeded(7)

        self.background = pygame.image.load("level3.png").convert()
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
                   [BOMB, 1000, 420],				#add more enemies
                   [BOMB, 1200, 500]]
	           #[BOSS_ENEMY ,  ,  ],
                   #[SHOOTING_ENEMY,  ,  ]]

        lv_coins = [[COIN, 500, 420],
                    [COIN, 750, 300],
                    [COIN, 1200, 200],
                    [COIN, 1025, 350],
                    [COIN, 1220, 450]
                    [COIN, 1000, 250],      #fix these numbers
                    [COIN, 850, 325]]
                    #[COIN, , ],
                    #[COIN, , ],
                    #[COIN, , ]]

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

        # Add a 2nd custom moving platform
        block = MovingPlatform([648, 648, 70, 40])
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

class LevelFour(Level):
    def __init__(self, player):
        Level.__init__(self, player)
        Level.hardmode = False
        if self.isHardMode():
            self.coinsNeeded(5)
        else:
            self.coinsNeeded(7)

        self.background = pygame.image.load("level4.png").convert()
        self.background.set_colorkey((255, 255, 255))
        self.level_limit = -2500

        platforms = [[GRASS_LEFT, 500, 550],
                     [GRASS_MIDDLE, 570, 550],
                     [GRASS_RIGHT, 640, 550],
                     [GRASS_LEFT, 780, 525],
                     [GRASS_MIDDLE, 850, 525],
                     [GRASS_RIGHT, 920, 525],
                     [STONE_PLATFORM_LEFT, 1400, 400],
                     [STONE_PLATFORM_RIGHT, 1470, 400],
                     [STONE_PLATFORM_MIDDLE, 1600, 320],
                     [STONE_PLATFORM_LEFT, 1650, 200],
                     [STONE_PLATFORM_RIGHT, 1720, 200],
                     [STONE_PLATFORM_LEFT, 1400, 100],
                     [STONE_PLATFORM_RIGHT, 1470, 100],
                     [STONE_PLATFORM_MIDDLE, 1250, 100]]

        enemies = [[BASIC_ENEMY, 500, 470],  # Add optional "R" or "L" argument to change facing direction.
                   [BOMB, 780, 445],  # Defaults to left-facing
                   [BOMB, 1470, 320],
                   [SHOOTING_ENEMY, 1720, 100],
                   [BOSS_ENEMY, 1400, 10]]

        lv_coins = [[COIN, 600, 400],
                    [COIN, 750, 300],
                    [COIN, 1400, 330],
                    [COIN, 1600, 260],
                    [COIN, 1470, 50],
                    [COIN, 1250, 50]]

        self.addEnemies(enemies)
        self.addCoins(lv_coins)
        self.addCoinsNeeded()
        self.addHearts()
        self.addPlatforms(platforms)

        # Add a custom moving platform
        block = MovingPlatform([648, 648, 70, 40])
        block.rect.x = 1000
        block.rect.y = 450
        block.boundary_left = 1000
        block.boundary_right = 1350
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)