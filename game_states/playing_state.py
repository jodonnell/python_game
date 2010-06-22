import sys, pygame
from game import conf
from game import errors
from game.level.level import Level
from game.level.view import View
from game.sprites.player.player import Player
from game.sprites.player.control import Control
from game.game_states.abstract_game_state import AbstractGameState


# this class should be a singleton
class PlayingState(AbstractGameState):
    """ The playing state holds both a level and a view object.  Its purpose is to coordinate between the level and the view to find out 
    what is onscreen and keep both objects up to date"""
    def __init__(self):
        # the level needs to return player_group, tile_groups, enemy_groups, power up groups and pass them to the view
        level = Level()
        self.view = View(level)

    def update(self):
        self.view.update_player(self._get_input())
        self.view.update_screen()

    def draw(self, display):
        display.fill(conf.BLACK)
        self.view.draw(display)

    def _get_input(self):
        "Gets all the inputs form pygame that we care about and put return them in an array"
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
