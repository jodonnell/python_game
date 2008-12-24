from conf import PLAYER_FACING_RIGHT, PLAYER_FACING_LEFT

class StillState():
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
        pass

    def move_left(self):
        "move left"
        self.player.movement_state.set_movement_state(self.player.movement_state.get_move_left_state())

    def move_right(self):
        "transition state to move right"
        self.player.movement_state.set_movement_state(self.player.movement_state.get_move_right_state())

    def stop_moving_left(self):
        "player held down multiple buttons, ignore"
        pass

    def stop_moving_right(self):
        "player held down both left and right, ignore"
        pass

    def duck(self):
        "transition to ducking state"
        self.player.movement_state.set_movement_state(self.player.movement_state.get_ducking_state())

    def stop_ducking(self):
        "player held down multiple buttons, ignore"
        pass
