# source of tiles file: https://opengameart.org/content/platformer-art-deluxe

from SpriteSheets import *

GRASS_LEFT = (576, 720, 70, 70)
GRASS_RIGHT = (576, 576, 70, 70)
GRASS_MIDDLE = (504, 576, 70, 70)
STONE_PLATFORM_LEFT = (432, 720, 70, 40)
STONE_PLATFORM_MIDDLE = (648, 648, 70, 40)
STONE_PLATFORM_RIGHT = (792, 648, 70, 40)


class Platform(pygame.sprite.Sprite):

    def __init__(self, sprite_location):
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet('tiles_spritesheet.png')
        self.image = sprite_sheet.get_image(sprite_location[0], sprite_location[1],
                                            sprite_location[2], sprite_location[3])
        self.rect = self.image.get_rect()


class MovingPlatform(Platform):

    def __init__(self, sprite_sheet):

        Platform.__init__(self, sprite_sheet)

        self.change_x = 0
        self.change_y = 0

        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0

        self.level = None
        self.player = None

    def update(self):

        # Move left/right
        self.rect.x += self.change_x

        # See if the player hit the platform
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # If the player is moving right, set its right side to the left side of the platform he hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise if the player is moving left, do the opposite.
                self.player.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # See if the player hit the platform
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # Reset the player's position based on the top/bottom of the platform.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # Check the boundaries and see if we need to reverse direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
