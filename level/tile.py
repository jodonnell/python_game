import os

TILE_PROPERTIES = {
    1:{'image_path': ('images', 'tile.png') }
}

class Tile():
    "A tile has a position, an image, a rect which are loaded based on id"
    def __init__(self, id, abs_pos):
        image = pygame.image.load( os.path.join(TILE_PROPERTIES[id]['image_path']) )
        self.image = image.convert_alpha()
        rect = self.image.get_bounding_rect()
        #self.rect = self.rect.move( position[0], position[1] )
        self._right_bound = position[0] + rect.width
        self._left_bound = position[0]

    def get_left_edge(self):
        return self._left_bound

    def get_right_edge(self):
        return self._right_bound
