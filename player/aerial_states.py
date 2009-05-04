from game.player.jumping_state import JumpingState
from game.player.double_jump_state import DoubleJumpState
from game.player.grounded_state import GroundedState
from game.player.falling_state import FallingState
from game.player.falling_no_jump_state import FallingNoJumpState

class AerialStates():
    """ Keeps track of the current movement state the player is in.  Needs
    to keep track of the direction the player is facing because when the player
    ducks or stands still, the direction they are facing depends on the lateral
    movement that was last made
    """
    def __init__(self, player):
        self.player = player
#        self.set_aerial_state(self.get_falling_state())
        self.set_aerial_state(self.get_grounded_state())

    def process_input(self, input, level):
        """Given an input tuple which contains KEYUP or KEYDOWN event
        and the key press, sets the state
        """
        if input == self.player.control.get_jump_key_pressed():
            self.state.jump(level)

        if input == self.player.control.get_jump_key_released():
            self.state.fall(level)

    def do_action(self, level):
        """ Does whatever action is appropriate for the current state
        the player is in.
        """
        self.state.do_action(level)

    def set_aerial_state(self, aerial_state):
        self.state = aerial_state

    def get_jumping_state(self):
        return JumpingState(self.player)

    def get_falling_state(self):
        return FallingState(self.player)

    def get_double_jump_state(self):
        return DoubleJumpState(self.player)

    def get_grounded_state(self):
        return GroundedState(self.player)

    def get_falling_no_jump_state(self):
        return FallingNoJumpState(self.player)

    def set_player_direction(self, direction):
        "When the player changes direction the state must be notified so it displays the correct frame"
        self.state.set_player_direction(direction)
