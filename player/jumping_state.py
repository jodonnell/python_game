from game.player.abstract_jumping_state import AbstractJumpingState

class JumpingState(AbstractJumpingState):
    def fall(self, level):
        self.player.aerial_state.set_aerial_state(self.player.aerial_state.get_falling_state())
