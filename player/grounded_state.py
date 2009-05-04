from pygame.sprite import spritecollide

class GroundedState():
    def __init__(self, player):
        self.player = player
    
    def get_animation(self):
        return None

    def do_action(self, level):
        self.grounded(level)

    def jump(self, level):
         self.player.aerial_state.set_aerial_state(self.player.aerial_state.get_jumping_state())   

    def fall(self, level):
        self.player.aerial_state.set_aerial_state(self.player.aerial_state.get_falling_state())
    
    def grounded(self, level):
        "Check for ground underneath players feet, if not found switch to falling state"
        tmp = self.player.rect
        self.player.rect = self.player.rect.move(0, 1)
        collides = spritecollide(self.player, level.tile_group, False)
        if not collides:
            self.fall(level)
            
        self.player.rect = tmp

    def set_player_direction(self, direction):
        pass
