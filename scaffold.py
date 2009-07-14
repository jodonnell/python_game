import sys, pygame
from game import conf
from game import errors
from game.game_states.game_states import GameStates

pygame.init()

#display = pygame.display.set_mode( (conf.SCREEN_WIDTH, conf.SCREEN_HEIGHT), pygame.FULLSCREEN  )
display = pygame.display.set_mode( (conf.SCREEN_WIDTH, conf.SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)


#################################################################################
# MAIN GAME LOOP
game_state = GameStates(display)

game_loops = 0
sum_fps = 0

try:
    while 1:
        game_state.update()

        clock.tick(300)
        pygame.display.flip()
    
        game_loops += 1
        sum_fps += clock.get_fps()

except errors.ExitGameError:
    print sum_fps / game_loops
    sys.exit()
