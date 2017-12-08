import pygame

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def game_intro():
    intro = True

    clock = pygame.time.Clock()
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                quitgame()

        pygame.font.init()
        size = [800, 600]
        screen = pygame.display.set_mode(size)
        screen.fill((250, 235, 215))
        font = pygame.font.SysFont('Comic Sans MS', 30)
        textSurf = font.render('Python Project Game', True, (0, 0, 0))
        textRect = textSurf.get_rect()
        textRect.center = (400, 300)
        screen.blit(textSurf, textRect)

        button("Username", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def quitgame():
    pygame.quit()
    quit()