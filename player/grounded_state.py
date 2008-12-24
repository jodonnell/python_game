class GroundedState():
    def __init__(self, player):
        self.player = player
    
    def get_animation(self):
        return None

    def do_action(self):
        pass

    def jump(self):
         self.player.aerial_state.set_aerial_state(self.player.aerial_state.get_jumping_state())   

    def fall(self):
        self.player.aerial_state.set_aerial_state(self.player.aerial_state.get_falling_state())
    
    def grounded(self):
        self.player.aerial_state.set_aerial_state(self.player.aerial_state.get_grounded_state())

    def set_player_direction(self, direction):
        pass
