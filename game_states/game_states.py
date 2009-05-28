from game.game_states.playing_state import PlayingState

class GameStates():
    """ Keeps track of the current movement state the player is in.  Needs
    to keep track of the direction the player is facing because when the player
    ducks or stands still, the direction they are facing depends on the lateral
    movement that was last made
    """
    def __init__(self, display):
        self.display = display
        self.set_state(self.get_playing_state())

    def update(self):
        """ Does whatever action is appropriate for the current state
        the player is in.
        """
        self.state.update()
        self.state.draw(self.display)

    def set_state(self, state):
        self.state = state

    def get_playing_state(self):
        return PlayingState()

    def get_quit_state(self):
        pass

    def get_menu_state(self):
        pass
