from game.sprites.player.moving_left_state import MovingLeftState
from game.sprites.player.moving_right_state import MovingRightState
from game.sprites.player.ducking_state import DuckingState
from game.sprites.player.still_state import StillState
from game.sprites.player.jumping_state import JumpingState
from game.sprites.player.falling_state import FallingState
from game.sprites.player.jumping_right_state import JumpingRightState
from game.sprites.player.jumping_left_state import JumpingLeftState
from game.sprites.player.falling_right_state import FallingRightState
from game.sprites.player.falling_left_state import FallingLeftState

from game.conf import PLAYER_FACING_RIGHT, PLAYER_FACING_LEFT

class States():
    """ Keeps track of the current movement state the player is in.  Needs
    to keep track of the direction the player is facing because when the player
    ducks or stands still, the direction they are facing depends on the lateral
    movement that was last made
    """
    def __init__(self, player):
        self.player = player
        self.direction = PLAYER_FACING_RIGHT
        self.set_state(self.get_still_state())

    def process_input(self, input):
        """Given an input tuple which contains KEYUP or KEYDOWN event
        and the key press, sets the state
        """
        if input == self.player.control.get_left_key_pressed():
            self.state.move_left()
            self.direction = PLAYER_FACING_LEFT

        if input == self.player.control.get_left_key_released():
            self.state.stop_moving_left()

        if input == self.player.control.get_right_key_pressed():
            self.state.move_right()
            self.direction = PLAYER_FACING_RIGHT

        if input == self.player.control.get_right_key_released():
            self.state.stop_moving_right()

        if input == self.player.control.get_duck_key_pressed():
            self.state.duck()

        if input == self.player.control.get_duck_key_released():
            self.state.stop_ducking()

        if input == self.player.control.get_jump_key_pressed():
            self.state.jump()

        if input == self.player.control.get_jump_key_released():
            self.state.fall()

    def do_action(self):
        """ Does whatever action is appropriate for the current state
        the player is in.
        """
        return self.state.do_action()

    def set_state(self, state):
        self.state = state

    def get_move_left_state(self):
        return MovingLeftState(self.player)

    def get_move_right_state(self):
        return MovingRightState(self.player)

    def get_ducking_state(self):
        return DuckingState(self.player, self.direction)

    def get_still_state(self):
        return StillState(self.player, self.direction)

    def get_jumping_state(self, frame_count=0):
        return JumpingState(self.player, frame_count)

    def get_falling_state(self, frame_count=0):
        return FallingState(self.player, frame_count)

    def get_jumping_right_state(self, frame_count=0):
        return JumpingRightState(self.player, frame_count)

    def get_jumping_left_state(self, frame_count=0):
        return JumpingLeftState(self.player, frame_count)

    def get_falling_right_state(self, frame_count=0):
        return FallingRightState(self.player, frame_count)

    def get_falling_left_state(self, frame_count=0):
        return FallingLeftState(self.player, frame_count)
