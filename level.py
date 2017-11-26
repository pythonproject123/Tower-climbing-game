from Enemy import *
import Player
from Platform import *


class Level:
    world_shift = 0
    level_limit = -1000

    def __init__(self, filename, player, hardmode=False):
        self.background = pygame.image.load(filename).convert()
        self.enemy_list = pygame.sprite.Group()
        self.platform_list = pygame.sprite.Group()
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
        screen.fill(0, 0, 255)
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
    def __init__(self, filename, player, hardmode):
        Level.__init__(self, filename, player, hardmode)
        maxCoins = 10
        if hardmode:
            coinsNeeded = 7
        else:
            coinsNeeded = 5
        for i in range(0, 5):
            self.enemy_list.append(BasicEnemy())

        self.background = pygame.image.load("level1.png").convert()
        self.background.set_colorkey(255, 255, 255)
        self.level_limit = -2500

        level = [[Platform.GRASS_LEFT, 500, 500],
                 [Platform.GRASS_MIDDLE, 570, 500],
                 [Platform.GRASS_RIGHT, 640, 500],
                 [Platform.GRASS_LEFT, 800, 400],
                 [Platform.GRASS_MIDDLE, 870, 400],
                 [Platform.GRASS_RIGHT, 940, 400],
                 [Platform.GRASS_LEFT, 1000, 500],
                 [Platform.GRASS_MIDDLE, 1070, 500],
                 [Platform.GRASS_RIGHT, 1140, 500],
                 [Platform.STONE_PLATFORM_LEFT, 1120, 280],
                 [Platform.STONE_PLATFORM_MIDDLE, 1190, 280],
                 [Platform.STONE_PLATFORM_RIGHT, 1260, 280]]

        for platform in level:
            block = Platform.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
