from game.sprites.player.abstract_falling_state import AbstractFallingState
from game.conf import PLAYER_FACING_RIGHT

class FallingState(AbstractFallingState):
    def __init__(self, player, frame_count):
        self.player = player
        self._right_animation = (self.player._STILL_RIGHT_FRAME)
        self._left_animation = (self.player._STILL_LEFT_FRAME)

        self.frame_count = frame_count
        self.animation_index = 0
        self.velocity = -self.player.jump_speed
        self.gravity = .2
        self.direction = PLAYER_FACING_RIGHT

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
        self.player.state.set_state(self.player.state.get_still_state())

    def move_right(self, level=None):
        self.player.state.set_state(self.player.state.get_falling_right_state(self.frame_count))

    def move_left(self, level=None):
        self.player.state.set_state(self.player.state.get_falling_left_state(self.frame_count))

    def set_player_direction(self, direction):
        self.direction = direction

    def stop_moving_right(self):
        pass

    def stop_moving_right(self):
        pass
