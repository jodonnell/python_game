from game import conf
import pygame
from game.sprites.player.player import Player
from game.sprites.player.control import Control


""" The screen takes a level object and a player starting point and creates itself based off that 
The screens primary purpose is to keep track of new sprites to add when they are scrolled on screen
For collision detection, and 
This class deals internally with relative positions, but all contact with other classes is done using absolution positions
sugar  
"""

class View():
    """ The View's duty is to keep track of what area on the level is in the current 
    player's view.  It does this by keeping track of the absolute coordinates of the
    left side and right side of the view and updating it when the view needs
    to shift left or right.  It is also in charge of converting absolute coordinates
    to relative coordinates for drawing to the screen.
    """
    def __init__(self, level):
        self.level = level
        self._player_group = pygame.sprite.Group()
        self._tile_group = pygame.sprite.Group()
        self._enemy_group = pygame.sprite.Group()
        self._power_up_group = pygame.sprite.Group()
        
        # this assumes player starts in the middle
        self._view_left_end_abs_pos = self.level.get_player_start_coord()[0] - (conf.SCREEN_WIDTH / 2)
        self._view_right_end_abs_pos = self.level.get_player_start_coord()[0] + (conf.SCREEN_WIDTH / 2)

        self._player = Player( ( (conf.SCREEN_WIDTH / 2), self.level.get_player_start_coord()[1] ), Control() )
        self._player_group.add( self._player )

        onscreen_tiles = self.level.get_onscreen_tiles(self.get_view_left_end(), self.get_view_right_end())
        self.set_tile_group(onscreen_tiles)

    def update_player(self, inputs):
        self._player.process_input(inputs)
        unimpeded_movement = self._player.update_player()
        impeded_movement = self._check_for_collisions(unimpeded_movement)
        self._player.update_player_pos(impeded_movement)
        self._move_view(impeded_movement)


    def _move_view(self, move):
        "This moves the view and updates whats onscreen"
        tile_group = self.level.get_onscreen_tiles(self.get_view_left_end(), self.get_view_right_end())
        enemy_group = self.level.get_onscreen_enemies(self.get_view_left_end(), self.get_view_right_end())
        power_up_group = self.level.get_onscreen_power_ups(self.get_view_left_end(), self.get_view_right_end())

        self.set_tile_group(tile_group)


    def _check_for_collisions(self, unimpeded_movement):
        # need to get players pos
        x_move, y_move = unimpeded_movement
        
        # reposition player
        # get all collides
        # find the collision that would have happened first
        # make adjustments
        

        if y_move > 0:
            pass
        return unimpeded_movement

    def draw(self, display):
        self._player_group.draw(display)
        self._tile_group.draw(display)

    def get_view_left_end(self):
        return self._view_left_end_abs_pos

    def get_view_right_end(self):
        return self._view_right_end_abs_pos

    def update_screen(self):
        pass

    def move_view(self, move):
        pass

    def set_tile_group(self, tiles):
        self._tile_group = tiles

    def add_enemy_group(self, enemies):
        pass
    
    def add_power_up_group(self, power_ups):
        pass

    def is_player_left_of_center(self):
        pass
    
    def is_player_right_of_center(self):
        pass

    def _move_right(self, move):
        "Determines whether the screen or the player needs to move right and then takes that action"
        right_end_of_level = self.level.get_right_edge_of_level()
        right_edge_of_level_reached = self.view.get_right_end_of_view() + move > right_end_of_level

        if (right_edge_of_level_reached or self.view.is_player_left_of_center()):
            self.view.move_player_rect_x(move)
        else:
            self._move_view(move)

    def _move_left(self, move):
        "Determines whether the screen or the player needs to move left and then takes that action"
        left_end_of_level = self.level.get_left_edge_of_level()
        left_edge_of_level_reached = self.view.get_left_end_of_view() + move < left_end_of_level

        if (left_edge_of_level_reached or self.player.view.is_player_right_of_center()):
            self.view.move_player_rect_x(move)
        else:
            self._move_view(move)


    

#        self.tile_group = tile_group
#        self.tile_group.add(*self.level.get_onscreen_tiles(self.view_left_end_abs_pos, self.view_right_end_abs_pos))

    def move_view(self, shift_view_amount):
        self.view_left_end_abs_pos += shift_view_amount
        self.view_right_end_abs_pos += shift_view_amount

    def move_right(self, shift_view_amount):
        self.move_view(shift_view_amount)
#        self.tile_group.add(self.level.new_right_tiles(self.view_right_end_abs_pos))
#        self.tile_group.remove(self.level.remove_left_tiles(self.view_left_end_abs_pos))

    def move_left(self, shift_view_amount):
        self.move_view(-shift_view_amount)
#        self.tile_group.add(self.level.new_left_tiles(self.view_left_end_abs_pos))
#        self.tile_group.remove(self.level.remove_right_tiles(self.view_right_end_abs_pos))
        
    def convert_abs_to_view(self, abs_pos):
        return abs_pos - self.view_left_end_abs_pos

    def update_view(self):
        self.level.update_level(self.view_left_end_abs_pos)
