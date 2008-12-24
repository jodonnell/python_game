from game.player.abstract_falling_state import AbstractFallingState

class FallingState(AbstractFallingState):
    def jump(self):
        self.player.aerial_state.set_aerial_state(self.player.aerial_state.get_double_jump_state())
