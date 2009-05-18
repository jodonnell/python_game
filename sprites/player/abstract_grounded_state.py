from game import errors
from pygame.sprite import spritecollide

class AbstractGroundedState():
    def __init__(self, player):
        raise errors.AbstractClassError()
    
    def grounded(self, level):
        "Check for ground underneath players feet, if not found switch to falling state"
        self.player.rect.bottom += 1
        collides = spritecollide(self.player, level.tile_group, False)
        if not collides:
            self.fall(level)
        
        self.player.rect.bottom -= 1
