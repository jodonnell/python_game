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
            self.level.append(Tile(tile_data[0], (tile_data[1], tile_data[2])))
        # should sort based on tile_data[1]

    def _sort(self):
        self.tiles_ordered_left = self.level[:]
        self.tiles_ordered_left.sort(lambda x,y: x.get_left_edge() > y.get_left_edge())
        self.tiles_ordered_right = self.level[:]
        self.tiles_ordered_right.sort(lambda x,y: x.get_right_edge() > y.get_right_edge())

    def get_onscreen_tiles(self, left_bound, right_bound):
        "Returns a list of onscreen tiles, given two bounds"
        first_tile = None
        last_tile = None

        tile_index = 0
        for tile in self.level:
            if tile.get_right_edge() >= left_bound:
                first_tile = tile_index
                break
            tile_index += 1
            
        tile_index = 0
        for tile in self.level:
            if tile.get_left_edge() >= right_bound:
                last_tile = tile_index
            tile_index += 1
        
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

        if tile_to_check == self.cached_left_tile_index:
            return []

        return self.level[tile_to_check:(self.cached_left_tile_index - 1)]

    def new_right_tiles(self, new_right_bound):
        tile_to_check = self.cached_right_tile_index
        while self.level[tile_to_check + 1].get_left_edge() >= new_right_bound:
            tile_to_check += 1

        if tile_to_check == self.cached_right_tile_index:
            return []

        return self.level[(self.cached_right_tile_index - 1):tile_to_check]


    def remove_left_tiles(self, new_left_bound):
        """ This should give us a list of tiles 
        """
        new_left_tile_index = None
        for tile_to_check in range(self.cached_right_tile_index, self.cached_left_tile_index):
            if self.level[tile_to_check].get_right_edge() < new_left_bound:
                new_left_tile_index = tile_to_check
                break

        if new_left_tile_index == self.cached_right_tile_index:
            raise NoTilesOnScreen()

        if new_left_tile_index is None:
            return []

        old_left_index = self.cached_left_tile_index
        self.cached_left_tile_index = new_left_tile_index

        return self.level[old_left_index, self.cached_left_tile_index]

    def remove_right_tiles(self, new_right_bound):
        """ This should give us a list of tiles 
        """
        new_right_tile_index = None
        for tile_to_check in range(self.cached_left_tile_index, self.cached_right_tile_index):
            if self.level[tile_to_check].get_left_edge() > new_right_bound:
                new_right_tile_index = tile_to_check
                break

        if new_right_tile_index == self.cached_left_tile_index:
            raise NoTilesOnScreen()

        if new_right_tile_index is None:
            return []

        old_right_index = self.cached_right_tile_index
        self.cached_right_tile_index = new_right_tile_index

        return self.level[self.cached_right_tile_index, old_right_index]
