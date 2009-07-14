from game.conf import PLAYER_FACING_RIGHT, PLAYER_FACING_LEFT
from game.sprites.player.abstract_grounded_state import AbstractGroundedState

class StillState(AbstractGroundedState):
    "The state when the player is standing still."

    def __init__(self, player, direction):
        self.player = player
        
        if direction == PLAYER_FACING_RIGHT:
            self._animation = self.player._STILL_RIGHT_FRAME
        else:
            self._animation = self.player._STILL_LEFT_FRAME
        
    def get_animation(self):
        return self._animation

    def do_action(self):
        return (0, self.grounded())

    def move_left(self):
        "move left"
        self.player.state.set_state(self.player.state.get_move_left_state())

    def move_right(self):
        "transition state to move right"
        self.player.state.set_state(self.player.state.get_move_right_state())

    def stop_moving_left(self):
        "player held down multiple buttons, ignore"
        pass

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
         self.player.state.set_state(self.player.state.get_jumping_state())   

    def fall(self):
        self.player.state.set_state(self.player.state.get_falling_state())
