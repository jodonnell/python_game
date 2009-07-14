from game import errors
from pygame.sprite import spritecollide

class AbstractMovingRightState():
    def __init__(self):
        raise errors.AbstractClassError()

    def move_right(self):
        "move right"
        return self.player.movement_speed
