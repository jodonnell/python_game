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
        self.level = Level()

        left_end_of_level = self.level.get_left_edge_of_level()
        right_end_of_level = self.level.get_right_edge_of_level()
        
        self.view = View(self.level.get_player_start_coord(), left_end_of_level, right_end_of_level)

        self.view.set_tile_group(self.level.get_onscreen_tiles(self.view.get_view_left_end(), self.view.get_view_right_end()))

    def update(self):
        move = self.view.update_player(self._get_input())
        if move:
            self._move_view(move)

        self.view.update_screen()

    def draw(self, display):
        display.fill(conf.BLACK)
        self.view.draw(display)

    def _move_view(self, move):
        "This moves the view and updates whats onscreen"
        self.view.move_view(move)

        tile_group = self.level.get_onscreen_tiles(self.view.get_left_side_of_view_abs(), self.view.get_right_side_of_view_abs())
        enemy_group = self.level.get_onscreen_enemies(self.view.get_left_side_of_view_abs(), self.view.get_right_side_of_view_abs())
        power_up_group = self.level.get_onscreen_power_ups(self.view.get_left_side_of_view_abs(), self.view.get_right_side_of_view_abs())

        self.view.set_tile_group(self.level.get_onscreen_tiles())
        self.view.set_enemy_group(self.level.get_new_enemies())
        self.view.set_power_up_group(self.level.get_new_power_ups())

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
