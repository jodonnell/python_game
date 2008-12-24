from game.player.abstract_jumping_state import AbstractJumpingState

class DoubleJumpState(AbstractJumpingState):
    def fall(self):
        self.player.aerial_state.set_aerial_state(self.player.aerial_state.get_falling_no_jump_state())

