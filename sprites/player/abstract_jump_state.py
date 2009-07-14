from game import errors
from game.conf import GRAVITY
from pygame.sprite import spritecollide

class AbstractJumpState():
    def __init__(self):
        raise errors.AbstractClassError()

    def jump(self):
        self.frame_count += 1
        return int(round(-self.player.jump_speed + self.frame_count * GRAVITY))
