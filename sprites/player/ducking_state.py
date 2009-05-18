from game.conf import PLAYER_FACING_RIGHT, PLAYER_FACING_LEFT

class DuckingState():
    "The state when the player is standing still."

    def __init__(self, player, direction):
        self.player = player
        
        if direction == PLAYER_FACING_RIGHT:
            self._animation = self.player._DUCK_RIGHT_FRAME
        else:
            self._animation = self.player._DUCK_LEFT_FRAME
        
    def get_animation(self):
        return self._animation

    def do_action(self, level):
        pass

    def move_left(self, level):
        "move left"
        self.player.state.set_state(self.player.state.get_move_left_state())

    def move_right(self, level):
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
        pass

    def stop_ducking(self):
        "stand up"
        self.player.state.set_state(self.player.state.get_still_state())
