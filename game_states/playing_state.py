import sys, pygame
from game import conf
from game import errors
from game.level.level import Level
from game.game_states.abstract_game_state import AbstractGameState

class PlayingState(AbstractGameState):
    def __init__(self):
        self.level = Level()

    def update(self):
        self.level.update_screen(self._get_input())

    def draw(self, display):
        display.fill(conf.BLACK)
        self.level.draw_screen(display)
    
#        self.player_group.draw(display)
#        self.tile_group.draw(display)


    def _get_input(self):
        inputs = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    raise errors.ExitGameError() # transition to quit state
                else:
                    inputs.append( (pygame.KEYDOWN, event.key) )

            if event.type == pygame.KEYUP:
                inputs.append( (pygame.KEYUP, event.key) )

        return inputs
