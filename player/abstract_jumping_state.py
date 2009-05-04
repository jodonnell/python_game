from game.conf import PLAYER_FACING_RIGHT

class AbstractJumpingState():
    def __init__(self, player):
        self.player = player
        self._right_animation = ()
        self._left_animation = ()

        self.frame_count = 0
        self.animation_index = 0

    def get_animation(self):
        if self.direction == PLAYER_FACING_RIGHT:
            return self._right_animation
        else:
            return self._left_animation

    def do_action(self, level):
        self.jump(level)

    def jump(self, level):
        if self.frame_count > self.player.jump_height:
            self.fall(level)
            return

        self.frame_count += 1
        self.player.rect[1] -= self.player.jump_speed 
    
    def fall(self, level):
        "Abstract"
        pass
    
    def grounded(self):
        self.player.aerial_state.set_aerial_state(self.player.aerial_state.get_grounded_state())

    def set_player_direction(self, direction):
        self.direction = direction
