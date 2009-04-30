from game.level.tile import Tile

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
    "Notes: THERE MUST ALWAYS BE ONE TILE ON SCREEN (make an assertion about this)"
    def __init__():
        level_data = open('data/level1')
        self.level = []
        for tile_data in level_data:
            tile_data = tile_data.split(' ')
            self.level.append(Tile(tile_data[0], (tile_data[1], tile_data[2]))) # this should go to a factory for object creation
        # should sort based on tile_data[1]

    def _sort(self):
        self.tiles_ordered_left = self.level[:]
        self.tiles_ordered_left.sort(lambda x,y: x.get_left_edge() > y.get_left_edge())
        self.tiles_ordered_right = self.level[:]
        self.tiles_ordered_right.sort(lambda x,y: x.get_right_edge() > y.get_right_edge())

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

        return self.level[first_tile, last_tile]

    def new_left_tiles(self, new_left_bound):
        """ Called when the screen moves left.
        We have the last index for the leftern most tile so start there
        Decrement towards zero until a tile is found that is no longer
        within the new bound"""
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
        while self.level[tile_to_check + 1].get_left_edge() >= new_right_bound:
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

        return self.level[old_left_index, self.cached_left_tile_index - 1]

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
    
    def get_player_start_pos_x(self):
        "returns the x coord of the player start"
        pass

    def get_player_start_abs_pos_x(self):
        "returns the players starting position in absolute coordinates"
        pass


--------------
|           x|
|
|
-------------
