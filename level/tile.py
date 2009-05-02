import os
import pygame
from game.Sprite import Sprite

TILE_PROPERTIES = {
    1:{'image_path': ('images', 'tile.png') }
}

class Tile(Sprite):
    "A tile has a position, an image, a rect which are loaded based on id"
    def __init__(self, id, abs_pos):
        image = pygame.image.load( os.path.join(*TILE_PROPERTIES[id]['image_path']) )
        self.image = image.convert_alpha()
        rect = self.image.get_bounding_rect()
        self._right_bound = abs_pos[0] + rect.width
        self._left_bound = abs_pos[0]

        Sprite.__init__(self, abs_pos)

    def get_left_edge(self):
        return self._left_bound

    def get_right_edge(self):
        return self._right_bound

    def update(self, view):
        self.rect.left = view.convert_abs_to_view(self._left_bound)
