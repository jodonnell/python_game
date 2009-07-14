from game import errors
from game.conf import GRAVITY
from pygame.sprite import spritecollide

class AbstractFallingState():
    def __init__(self):
        raise errors.AbstractClassError()

    def fall(self):
        self.frame_count += 1
        return int(round(1 + self.frame_count * GRAVITY))
