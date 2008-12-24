import sys, pygame, random, os, Sprite
from player.control import Control
from player.player import Player
from conf import *
from pygame.constants import *


pygame.init()

screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT), pygame.FULLSCREEN  )
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)


################################################################################
# Create all the different sprites and place them randomly with random speed
# Put them in their respective groups

playerGroup = pygame.sprite.Group();
player = Player( (600, 480), Control() )
player.add( playerGroup )

#################################################################################
# MAIN GAME LOOP
game_loops = 0
sum_fps = 0

while 1:
    inputs = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_q:
                print sum_fps / game_loops
                sys.exit()
            else:
                inputs.append( (pygame.KEYDOWN, event.key) )

        if event.type == pygame.KEYUP:
            inputs.append( (pygame.KEYUP, event.key) )

    playerGroup.update(inputs)
    
    screen.fill(BLACK)
    
    playerGroup.draw(screen)

    clock.tick(30)
    pygame.display.flip()
    
    game_loops += 1
    sum_fps += clock.get_fps()

