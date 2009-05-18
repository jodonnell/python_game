from game.conf import PLAYER_FACING_RIGHT
from game.sprites.player.abstract_falling_state import AbstractFallingState
from game.sprites.player.abstract_moving_left_state import AbstractMovingLeftState

class FallingLeftState(AbstractFallingState, AbstractMovingLeftState):
    def __init__(self, player, frame_count):
        self.player = player
        self._right_animation = (self.player._STILL_RIGHT_FRAME)
        self._left_animation = (self.player._STILL_LEFT_FRAME)

        self.frame_count = frame_count
        self.animation_index = 0
        self.direction = PLAYER_FACING_RIGHT

    def get_animation(self):
        if self.direction == PLAYER_FACING_RIGHT:
            return self._right_animation
        else:
            return self._left_animation

    def do_action(self, level):
        self.fall(level)
        self.move_left(level)

    def jump(self, level=None):
        pass
    
    def stop_moving_left(self):
        self.player.state.set_state(self.player.state.get_falling_state(self.frame_count))

    def grounded(self):
        self.player.state.set_state(self.player.state.get_move_left_state())

    def set_player_direction(self, direction):
        self.direction = direction

    def _update_animation(self):
        pass

    def move_right(self, level=None):
        self.player.state.set_state(self.player.state.get_falling_right_state(self.frame_count))

    def stop_moving_right(self):
        pass
