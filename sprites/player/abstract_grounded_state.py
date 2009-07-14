from game import errors
from pygame.sprite import spritecollide

class AbstractGroundedState():
    def __init__(self, player):
        raise errors.AbstractClassError()
    
    def grounded(self):
        "Check for ground underneath players feet, if not found switch to falling state"
        return 1
