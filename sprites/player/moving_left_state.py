from game.sprites.player.abstract_moving_left_state import AbstractMovingLeftState
from game.sprites.player.abstract_grounded_state import AbstractGroundedState

class MovingLeftState(AbstractMovingLeftState, AbstractGroundedState):
    "The state when the player is moving left."
    def __init__(self, player):
        self.player = player
        self._animation = (self.player._STILL_LEFT_FRAME, self.player._MOVE_LEFT_FRAME_1, self.player._MOVE_LEFT_FRAME_2, self.player._STILL_LEFT_FRAME)
        
        self.frame_count = 0
        self.animation_index = 0

    def get_animation(self):
        return self._animation[self.animation_index]

    def do_action(self):
        x_move = self.move_left()
        y_move = self.grounded()
        return (x_move, y_move)

    def _update_animation(self):
        """Updates the frame count and animation"""
        self.frame_count += 1
        
        if (self.frame_count % 8) == 0:
            self.animation_index += 1
            if self.animation_index == len(self._animation):
                self.animation_index = 0
        
    def move_right(self):
        "transition state to move right"
        self.player.state.set_state(self.player.state.get_move_right_state())

    def stop_moving_left(self):
        "transition state to not moving"
        self.player.state.set_state(self.player.state.get_still_state())

    def stop_moving_right(self):
        "player held down both left and right, ignore"
        pass

    def duck(self):
        "transition to ducking state"
        self.player.state.set_state(self.player.state.get_ducking_state())

    def stop_ducking(self):
        "player held down multiple buttons, ignore"
        pass

    def jump(self):
        self.player.state.set_state(self.player.state.get_jumping_left_state())

    def fall(self):
        self.player.state.set_state(self.player.state.get_falling_left_state())
