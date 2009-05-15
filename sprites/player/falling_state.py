from pygame.sprite import spritecollide
from game.conf import PLAYER_FACING_RIGHT, GRAVITY

class FallingState():
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
        pass
    
    def fall(self, level):
        move = self._get_movement_distance(level)

        if move == 0:
            self.grounded()
            return

        self.frame_count += 1
        self.player.rect.top += move

    def _get_movement_distance(self, level):
        """Looks at move and sees if player can move that far, if not returns the max amount
        the player is allowed to move, the amount of the move is determined by gravity and the classic
        physics formula velocity initial + time * acceleration"""
        # v initial must not be 0 or this transitions to grounded state
        velocity = old_velocity = int(round(1 + self.frame_count * GRAVITY))
        self.player.rect.top += velocity

        collides = spritecollide(self.player, level.tile_group, False)
        if collides:
            velocity = self._get_movement_until_collision(collides, velocity)

        self.player.rect.top -= old_velocity
        return velocity

    def _get_movement_until_collision(self, collides, move):
        """Given a list of tiles that collide with the player finds the one farthest to the top
        and returns the number of pixels the player can move until it is within the tile"""
        floors = [floor for floor in collides if self.player.rect.bottom >= floor.rect.top]
        if floors:
            floors.sort(lambda x,y: x.rect.top - y.rect.top)
            move += floors[0].rect.top - self.player.rect.bottom
        return move

    def grounded(self):
        self.player.aerial_state.set_aerial_state(self.player.aerial_state.get_grounded_state())

    def set_player_direction(self, direction):
        self.direction = direction
