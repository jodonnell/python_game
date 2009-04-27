import os

TILE_PROPERTIES = {
    1:{'image_path': ('images', 'tile.png') }
}

class Tile():
    "A tile has a position, an image, a rect which are loaded based on id"
    def __init__(self, id, position):
        image = pygame.image.load( os.path.join(TILE_PROPERTIES[id]['image_path']) )
        self.image = image.convert_alpha()
        rect = self.image.get_bounding_rect()
        #self.rect = self.rect.move( position[0], position[1] )
        self.right_bound = position[0] + rect.width
        self.left_bound = position[0]

