from game.conf import PLAYER_FACING_RIGHT
from game.sprites.player.abstract_falling_state import AbstractFallingState
from game.sprites.player.abstract_moving_right_state import AbstractMovingRightState

class FallingRightState(AbstractFallingState, AbstractMovingRightState):
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

    def do_action(self):
        return (self.move_right(), self.fall())
        
    def jump(self):
        pass
    
    def stop_moving_right(self):
        self.player.state.set_state(self.player.state.get_falling_state(self.frame_count))

    def grounded(self):
        self.player.state.set_state(self.player.state.get_move_right_state())

    def set_player_direction(self, direction):
        self.direction = direction

    def _update_animation(self):
        pass

    def move_left(self):
        self.player.state.set_state(self.player.state.get_falling_left_state(self.frame_count))

    def stop_moving_left(self):
        pass

    def duck(self):
        pass
