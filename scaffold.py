import sys, pygame
from game.player.control import Control
from game.player.player import Player
from game.conf import *
from game.level.level import Level
from game.level.screen import Screen
from pygame.constants import *


pygame.init()

#screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT), pygame.FULLSCREEN  )
display = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)


################################################################################
# Create all the different sprites and place them randomly with random speed
# Put them in their respective groups

playerGroup = pygame.sprite.Group();
player = Player( (600, 480), Control() )
player.add( playerGroup )

tile_group = pygame.sprite.Group()
level = Level()
screen = Screen(level, tile_group)

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

            elif event.key == K_r:
                screen.move_right(1)
            else:
                inputs.append( (pygame.KEYDOWN, event.key) )

        if event.type == pygame.KEYUP:
            inputs.append( (pygame.KEYUP, event.key) )

    playerGroup.update(inputs)
    
    display.fill(BLACK)
    
    playerGroup.draw(display)
    tile_group.draw(display)

    clock.tick(30)
    pygame.display.flip()
    
    game_loops += 1
    sum_fps += clock.get_fps()

