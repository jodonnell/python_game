import pygame

from game.level.tile import Tile
from game.level.view import View
from game.sprites.player.player import Player
from game.sprites.player.control import Control
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
    """
    "Notes: THERE MUST ALWAYS BE ONE TILE ON SCREEN (make an assertion about this)"
    def __init__(self):
        level_data = open('data/level1')
        self.level = []
        for tile_data in level_data:
            tile_data = tile_data.split(' ')
            tile_data = [int(x) for x in tile_data]
            if tile_data[0]:
                self.level.append(Tile(tile_data[0], (tile_data[1], tile_data[2]))) # this should go to a factory for object creation
            else: # player start
                self._player_start_abs_pos_x = tile_data[1]

        
        self.player_group = pygame.sprite.Group()
        self.player = Player( (conf.SCREEN_WIDTH / 2, conf.SCREEN_HEIGHT / 2), Control() )
        self.player_group.add(self.player)

        self.view = View(self)

        self.tile_group = pygame.sprite.Group()
        self.tile_group.add(*self.get_onscreen_tiles(self.view.view_left_end_abs_pos, self.view.view_right_end_abs_pos))


#     def _sort(self):
#         self.tiles_ordered_left = self.level[:]
#         self.tiles_ordered_left.sort(lambda x,y: x.get_left_edge() > y.get_left_edge())
#         self.tiles_ordered_right = self.level[:]
#         self.tiles_ordered_right.sort(lambda x,y: x.get_right_edge() > y.get_right_edge())

    def get_onscreen_tiles(self, left_bound, right_bound):
        """Returns a list of onscreen tiles, given two bounds
        Also caches the first and last index of the tiles onscreen"""
        for tile_index, tile in enumerate(self.level):
            # if at least a tiny bit of the tile is on the left side of the screen
            if tile.get_right_edge() >= left_bound: 
                first_tile = tile_index
                break
            
        for tile_index, tile in enumerate(self.level):
            # if at least a tiny bit of the tile is on the right side of the screen
            if tile.get_left_edge() >= right_bound:
                last_tile = tile_index
        
        self.cached_left_tile_index = first_tile
        self.cached_right_tile_index = last_tile
        
        return self.level[first_tile:last_tile]

    def new_left_tiles(self, new_left_bound):
        """ Called when the screen moves left.
        We have the last index for the leftern most tile so start there
        Decrement towards zero until a tile is found that is no longer
        within the new bound"""
        tile_to_check = 0
        for tile_to_check in range(self.cached_left_tile_index, 0):
            if self.level[tile_to_check].get_right_edge() >= new_left_bound:
                tile_to_check -= 1
            else:
                break

        if tile_to_check == self.cached_left_tile_index:
            return []

        return self.level[tile_to_check:(self.cached_left_tile_index - 1)]

    def new_right_tiles(self, new_right_bound):
        """ Start from cached right tile and start looking forward in the level
        until you find a tile that is still off screen
        """
        tile_to_check = self.cached_right_tile_index

        if len(self.level) > tile_to_check + 1:
            tile_to_check += 1

        while len(self.level) <= tile_to_check \
                and (self.level[tile_to_check].get_left_edge() >= new_right_bound):
            tile_to_check += 1

        if tile_to_check == self.cached_right_tile_index:
            return []

        return self.level[(self.cached_right_tile_index - 1):tile_to_check]

    def remove_left_tiles(self, new_left_bound):
        """ This should give us a list of tiles that are no longer on screen 
        These tiles will be between the cached left and right bounds so start at the
        right tile """
        new_left_tile_index = None
        for tile_to_check in range(self.cached_right_tile_index, self.cached_left_tile_index):
            if self.level[tile_to_check].get_right_edge() < new_left_bound:
                remove_left_tile_index = tile_to_check
                break

        # this is technically not true, tiles could have been added above
        # but the cache is only updated on removing tiles.  I am going
        # to make the unpleaseant assertion that all tiles will never be 
        # scrolled off screen
        if new_left_tile_index > self.cached_right_tile_index:
            raise NoTilesOnScreen()

        if new_left_tile_index is None:
            return []

        old_left_index = self.cached_left_tile_index
        self.cached_left_tile_index = new_left_tile_index + 1

        return self.level[old_left_index, self.cached_left_tile_index]

    def remove_right_tiles(self, new_right_bound):
        """ We need to start 
        """
        new_right_tile_index = None
        for tile_to_check in range(self.cached_left_tile_index, self.cached_right_tile_index):
            if self.level[tile_to_check].get_left_edge() > new_right_bound:
                tile_remove_index = tile_to_check
                break

        # note assertion in remove_left_tiles
        if new_right_tile_index == self.cached_left_tile_index:
            raise NoTilesOnScreen()

        if new_right_tile_index is None:
            return []

        old_right_index = self.cached_right_tile_index
        self.cached_right_tile_index = tile_remove_index - 1

        return self.level[tile_remove_index, old_right_index]
    
    def get_player_start_abs_pos_x(self):
        "returns the players starting position in absolute coordinates"
        return self._player_start_abs_pos_x


    def update_screen(self, inputs):
        self.player.update(inputs, self)

        for tile_to_update in range(self.cached_left_tile_index, self.cached_right_tile_index):
            self.level[tile_to_update].update(self.view)

    def draw_screen(self, display):
        self.player_group.draw(display)
        self.tile_group.draw(display)

    def get_first_tile(self):
        return self.level[0]

    def get_last_tile(self):
        return self.level[-1:][0]

    def get_right_end_of_view(self):
        return self.view.get_right_end_of_view()

    def get_left_end_of_view(self):
        return self.view.get_left_end_of_view()

    def move_view(self, move):
        self.view.move_view(move)
