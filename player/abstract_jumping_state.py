from pygame.sprite import spritecollide
from game.conf import PLAYER_FACING_RIGHT


def collide_ceiling(player, collides, move):
    ceilings = [ceiling for ceiling in collides if player.rect.top <= ceiling.rect.bottom]
    if ceilings:
        ceilings.sort(lambda x,y: x.rect.bottom - y.rect.bottom)
        return ceilings[0].rect.bottom - player.rect.top
    return move

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
        move = self.move_max_jump(level)

        if move >= 0:
            self.fall(level)
            return

        if self.frame_count > self.player.jump_height:
            self.fall(level)
            return

        self.frame_count += 1
        self.player.rect[1] -= self.player.jump_speed 
    
    def move_max_jump(self, level):
        move = -self.player.jump_speed
        tmp = self.player.rect
        self.player.rect = self.player.rect.move(0, -self.player.jump_speed)
        collides = spritecollide(self.player, level.tile_group, False)
        
        if collides:
            move = collide_ceiling(self.player, collides, move)

        self.player.rect = tmp
        return move


    def fall(self, level):
        "Abstract"
        pass
    
    def grounded(self):
        self.player.aerial_state.set_aerial_state(self.player.aerial_state.get_grounded_state())

    def set_player_direction(self, direction):
        self.direction = direction
