from pygame.sprite import spritecollide
from game.conf import PLAYER_FACING_RIGHT

def collide_ceiling(player, collides, move):
    ceilings = [ceiling for ceiling in collides if player.rect.top <= ceiling.rect.bottom]
    if ceilings:
        ceilings.sort(lambda x,y: x.rect.bottom - y.rect.bottom)
        return ceilings[0].rect.bottom - player.rect.top
    return move

class JumpingState():
    def __init__(self, player):
        self.player = player
        self._right_animation = ()
        self._left_animation = ()

        self.frame_count = 0
        self.animation_index = 0
        self.velocity = -self.player.jump_speed
        self.gravity = .1

    def get_animation(self):
        if self.direction == PLAYER_FACING_RIGHT:
            return self._right_animation
        else:
            return self._left_animation

    def do_action(self, level):
        self.jump(level)

    def jump(self, level):
        self.velocity = -self.player.jump_speed + self.frame_count * self.gravity
        move = self.move_max_jump(level)

        if move >= 0:
            self.fall(None)
            return

        self.frame_count += 1
        self.player.rect.top += self.velocity
    
    def move_max_jump(self, level):
        move = self.velocity

        tmp = self.player.rect
        self.player.rect = self.player.rect.move(0, self.velocity)
        collides = spritecollide(self.player, level.tile_group, False)
        
        if collides:
            move = collide_ceiling(self.player, collides, self.velocity)
            move += self.velocity

        self.player.rect = tmp
        return move

    def fall(self, level=None):
        self.player.aerial_state.set_aerial_state(self.player.aerial_state.get_falling_state())
    
    def grounded(self):
        self.player.aerial_state.set_aerial_state(self.player.aerial_state.get_grounded_state())

    def set_player_direction(self, direction):
        self.direction = direction
