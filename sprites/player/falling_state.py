from game.sprites.player.abstract_falling_state import AbstractFallingState
from game.conf import PLAYER_FACING_RIGHT

class FallingState(AbstractFallingState):
    def __init__(self, player):
        self.player = player
        self._right_animation = ()
        self._left_animation = ()

        self.frame_count = 0
        self.animation_index = 0
        self.velocity = -self.player.jump_speed
        self.gravity = .2

    def get_animation(self):
        if self.direction == PLAYER_FACING_RIGHT:
            return self._right_animation
        else:
            return self._left_animation

    def do_action(self, level):
        self.fall(level)

    def jump(self, level):
        pass

    def grounded(self):
        self.player.aerial_state.set_aerial_state(self.player.aerial_state.get_grounded_state())

    def set_player_direction(self, direction):
        self.direction = direction
