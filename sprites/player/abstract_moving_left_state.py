from game import errors
from pygame.sprite import spritecollide

class AbstractMovingLeftState():
    def __init__(self):
        raise errors.AbstractClassError()

    def move_left(self):
        "move left"
        return -self.player.movement_speed
