from game.sprites.player.moving_left_state import MovingLeftState
from game.sprites.player.moving_right_state import MovingRightState
from game.sprites.player.ducking_state import DuckingState
from game.sprites.player.still_state import StillState
from game.conf import PLAYER_FACING_RIGHT, PLAYER_FACING_LEFT

class MovingStates():
    """ Keeps track of the current movement state the player is in.  Needs
    to keep track of the direction the player is facing because when the player
    ducks or stands still, the direction they are facing depends on the lateral
    movement that was last made
    """
    def __init__(self, player):
        self.player = player
        self.direction = PLAYER_FACING_RIGHT
        self.set_movement_state(self.get_still_state())

    def process_input(self, input, level):
        """Given an input tuple which contains KEYUP or KEYDOWN event
        and the key press, sets the state
        """
        if input == self.player.control.get_left_key_pressed():
            self.state.move_left(level)
            self.direction = PLAYER_FACING_LEFT

        if input == self.player.control.get_left_key_released():
            self.state.stop_moving_left()

        if input == self.player.control.get_right_key_pressed():
            self.state.move_right(level)
            self.direction = PLAYER_FACING_RIGHT

        if input == self.player.control.get_right_key_released():
            self.state.stop_moving_right()

        if input == self.player.control.get_duck_key_pressed():
            self.state.duck()

        if input == self.player.control.get_duck_key_released():
            self.state.stop_ducking()

    def do_action(self, level):
        """ Does whatever action is appropriate for the current state
        the player is in.
        """
        return self.state.do_action(level)

    def set_movement_state(self, movement_state):
        self.state = movement_state

    def get_move_left_state(self):
        return MovingLeftState(self.player)

    def get_move_right_state(self):
        return MovingRightState(self.player)

    def get_ducking_state(self):
        return DuckingState(self.player, self.direction)

    def get_still_state(self):
        return StillState(self.player, self.direction)

