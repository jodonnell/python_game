from pygame.sprite import spritecollide
from game.conf import PLAYER_FACING_RIGHT


def collide_floor(player, collides, move):
    floors = [floor for floor in collides if player.rect.bottom >= floor.rect.top]
    if floors:
        floors.sort(lambda x,y: x.rect.top - y.rect.top)
        return floors[0].rect.top - player.rect.bottom
    return move

class AbstractFallingState():
    def __init__(self, player):
        self.player = player
        self._right_animation = ()
        self._left_animation = ()

        self.frame_count = 0
        self.animation_index = 0
        self.velocity = -self.player.jump_speed
        self.gravity = .2

    def get_animation(self):
        if self.direction == PLAYER_FACING_RIGHT:
            return self._right_animation
        else:
            return self._left_animation

    def do_action(self, level):
        self.fall(level)

    def jump(self, level):
        "Abstract"
        pass
    
    def fall(self, level):
        move = self.move_max_fall(level)

        self.player.rect.top += move

        if move <= 0:
            return self.grounded()

        self.frame_count += 1

    def grounded(self):
        self.player.aerial_state.set_aerial_state(self.player.aerial_state.get_grounded_state())

    def set_player_direction(self, direction):
        self.direction = direction

    def move_max_fall(self, level):
        move = self.player.jump_speed
        old_rect = self.player.rect
        self.player.rect = self.player.rect.move(0, move)

        collides = spritecollide(self.player, level.tile_group, False)
        
        if collides:
            move = collide_floor(self.player, collides, move)
            move += self.player.jump_speed

        self.player.rect = old_rect
        return move
