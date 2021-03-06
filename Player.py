from Platform import *
from SpriteSheets import *


class Player(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.change_x = 0
        self.change_y = 0
        self.walking_frames_l = []
        self.walking_frames_r = []

        # What direction is the player facing?
        self.direction = "R"

        self.level = None

        self.name = name
        self.health = 3
        self.coins = 0
        self.alive = True
        self.won = False

        sprite_sheet = SpriteSheet("p1_walk.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(0, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(66, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 0, 67, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(66, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 93, 72, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 186, 70, 90)
        self.walking_frames_r.append(image)

        # Load all the right facing images, then flip them to face left.
        image = sprite_sheet.get_image(0, 0, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(66, 0, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(132, 0, 67, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 93, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(66, 93, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(132, 93, 72, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 186, 70, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Hit an enemy
        hit = pygame.sprite.spritecollide(self, self.level.enemy_list, True)

        # Report hit to game
        if len(hit) > 0:
            if hit[0].getType() == "Projectile":
                pass
            # Detect if the player jumped on the enemy's head
            elif (hit[0].getType().getType() == "Bomb") or (not (
                    self.rect.bottom <= hit[0].rect.top) and (self.rect.bottom >= hit[0].rect.top + 4)):
                dam = self.hit(hit[0].getType().getDamage())
                if not self.alive:
                    self.kill()
                    return
                for i in range(1, dam+1):
                    sp = self.level.health_bar.sprites()
                    sp[len(sp) - 1].kill()

        # Collect a coin
        if len(pygame.sprite.spritecollide(self, self.level.coins, True)) > 0:
            self.collectCoin()
            redC = self.level.coins_needed.sprites()
            redC[len(redC) - 1].kill()
            if len(self.level.coins_needed.sprites()) == 0:
                self.won = True

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            '''if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x'''

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= 600 - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = 600 - self.rect.height

    def jump(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= 600:
            self.change_y = -10

    def go_left(self):
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        self.change_x = 0

    def hit(self, damage):
        self.health -= damage
        if self.getHealth() <= 0:
            self.alive = False
        return damage

    def collectCoin(self):
        self.coins += 1

    def reset(self):
        self.coins = 0
        self.won = False
        if self.level.hardmode:
            self.health = 1
        else:
            self.health = 3
        self.level.reset()

    def getHealth(self):
        return self.health

    def getCoins(self):
        return self.coins

    def getName(self):
        return self.name
