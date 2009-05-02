import sys, pygame
from game.player.control import Control
from game.conf import *
from game.level.level import Level
from pygame.constants import *


pygame.init()

#display = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT), pygame.FULLSCREEN  )
display = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)


################################################################################
# Create all the different sprites and place them randomly with random speed
# Put them in their respective groups


level = Level()

#################################################################################
# MAIN GAME LOOP
game_loops = 0
sum_fps = 0

# keep track of the different tile groups and have them recalculate there different 
# positions then on update convert them to relative screen coordinates
#

while 1:
    inputs = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_q:
                print sum_fps / game_loops
                sys.exit()

            elif event.key == K_r:
                screen.move_right(30)
            elif event.key == K_e:
                screen.move_left(30)
            else:
                inputs.append( (pygame.KEYDOWN, event.key) )

        if event.type == pygame.KEYUP:
            inputs.append( (pygame.KEYUP, event.key) )

    display.fill(BLACK)

    level.update_screen(inputs)
    
#    playerGroup.draw(display)
#    tile_group.draw(display)

    level.draw_screen(display)

    clock.tick(300)
    pygame.display.flip()
    
    game_loops += 1
    sum_fps += clock.get_fps()

