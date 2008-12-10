import sys, pygame, random, os, Sprite, Player
from conf import *
from pygame.constants import *

pygame.init()

screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT), pygame.FULLSCREEN  )
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

#music = pygame.mixer.Sound(os.path.join('music', 'airfrance.ogg'))
#music.play()
#pygame.mixer.music.load(os.path.join('music', 'air_france.mp3'))
#pygame.mixer.music.play()


################################################################################
# Create all the different sprites and place them randomly with random speed
# Put them in their respective groups

playerGroup = pygame.sprite.Group();
player = Player.Player( os.path.join('images', 'ryu.gif'), (512, 480), [0, 0])
player.add( playerGroup )

wallGroup = pygame.sprite.Group();
wall = Player.Player( os.path.join('images', 'background.gif'), (0, 0), [0, 0])
wall.add( wallGroup )

#################################################################################
# MAIN GAME LOOP
sum_fps = 0;
game_loops = 0;

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_q:
                print sum_fps / game_loops
                sys.exit()
            if event.key == K_LEFT:
                wall.moveLeft();
            if event.key == K_UP:
                wall.moveUp();
            if event.key == K_DOWN:
                wall.moveDown();
            if event.key == K_RIGHT:
                wall.moveRight();

        if event.type == pygame.KEYUP:
            if event.key == K_LEFT:
                wall.stopMoveLeft();
            if event.key == K_UP:
                wall.stopMoveUp();
            if event.key == K_DOWN:
                wall.stopMoveDown();
            if event.key == K_RIGHT:
                wall.stopMoveRight();


#    pygame.sprite.groupcollide(playerGroup, skullMens, True, False)
#    pygame.sprite.groupcollide(playerGroup, greenFlyers, False, True)

    playerGroup.update()
    wallGroup.update()
    
#    screen.fill(BLACK)
    
    wallGroup.draw(screen)
    playerGroup.draw(screen)

    clock.tick(FPS_MAX)
    pygame.display.flip()
    
#    pygame.display.set_caption("fps: %s" % (str(int(clock.get_fps()))))
    game_loops += 1
    sum_fps += clock.get_fps()

