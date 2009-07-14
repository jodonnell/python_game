import pygame

from game.level.tile import Tile
from game import conf


####
# oh fuck what about a tile that is extremely wide
#
# xxxxxxxxxxxxxxxxxxxxxxxxxxx   <-
#    xxxxxxxx
#



# ok the level contains the tiles sorted by the left position AND the 
# right position
#


class NoTilesOnScreen(Exception):
    pass

class Level():
    """ The level is in charge of loading a level and creating a representation of it by loading
    all the different objects into a level.  It also is in charge of finding out what objects
    should be drawn to the screen which it does by adding to the specific groups.
    
    The level loads the whole level into its internal array.  It keeps track of where the view is through
    the function move_view.  Then using the functions get_new_tiles, get_new_enemies, and get_new_power_ups
    it will return 


    OK SO THE LEVEL NOW HAS A SOUL PURPOSE OF RETURNING EVERYHTING ON SCREEN FOR A GIVEN VIEW

    """
    "Notes: THERE MUST ALWAYS BE ONE TILE ON SCREEN (make an assertion about this)"
    def __init__(self):
        level_data = open('data/level1')
        self._tiles = []
        self._enemies = []
        self._power_ups = []

        for tile_data in level_data:
            tile_data = tile_data.split(' ')
            tile_data = [int(x) for x in tile_data]
            if tile_data[0]:
                self._tiles.append(Tile(tile_data[0], (tile_data[1], tile_data[2]))) # this should go to a factory for object creation
            else: # player start
                self._player_start_x = tile_data[1]
                self._player_start_y = tile_data[2]
        
    def get_onscreen_tiles(self, view_left_bound, view_right_bound):
        """ So we have the left and right bounds of the view, we need to return all tiles that are in within
        these bounds.  
        So the left side needs to look at tiles right attributes, the right side needs to look at tiles
        left side
        """
        tiles_group = pygame.sprite.Group()
        for tile in self._tiles:
            if self.is_onscreen(tile, view_left_bound, view_right_bound):
                tiles_group.add(tile)

        return tiles_group


    def get_onscreen_enemies(self, view_left_bound, view_right_bound):
        return []

    def get_onscreen_power_ups(self, view_left_bound, view_right_bound):
        return []

    def is_onscreen(self, sprite, view_left_bound, view_right_bound):
        sprite_to_right_of_view = sprite.get_right_edge() > view_left_bound
        sprite_to_left_of_view = sprite.get_left_edge() < view_right_bound

        if sprite_to_left_of_view and sprite_to_right_of_view:
            return True
        else:
            return False

    def get_first_tile(self):
        return self._tiles[0]

    def get_last_tile(self):
        return self._tiles[-1:][0]

    def get_left_edge_of_level(self):
        return self.get_first_tile().get_left_edge()

    def get_right_edge_of_level(self):
        return self.get_last_tile().get_right_edge()

    def get_player_start_coord(self):
        return (self._player_start_x, self._player_start_y)
