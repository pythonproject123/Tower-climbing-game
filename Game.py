from Player import *
import level
import time


def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [800, 600]
    screen = pygame.display.set_mode(size)

    #pygame.display.set_caption("Platformer with sprite sheets")

    # Create the player
    player = Player('test')

    # Create all the levels
    level_list = [level.LevelOne(player)]
    #level_list.append(level.LevelTwo(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = 600 - player.rect.height
    active_sprite_list.add(player)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Game loop
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop
            if not player.alive:
                pygame.font.init()
                font = pygame.font.SysFont('Comic Sans MS', 30)
                textSurf = font.render('Game Over!', True, (0, 0, 0))
                textRect = textSurf.get_rect()
                textRect.center = (400, 300)
                screen.blit(textSurf, textRect)
                pygame.display.update()
                time.sleep(2)
                done = True

            if  player.won:
                pygame.font.init()
                font = pygame.font.SysFont('Comic Sans MS', 30)
                textSurf = font.render('Well Done!', True, (0, 0, 0))
                textRect = textSurf.get_rect()
                textRect.center = (400, 300)
                screen.blit(textSurf, textRect)
                pygame.display.update()
                time.sleep(2)
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_SPACE:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        active_sprite_list.update()
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list) - 1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


if __name__ == "__main__":
    main()
