from game import errors
from game.conf import GRAVITY
from pygame.sprite import spritecollide

class AbstractJumpState():
    def __init__(self):
        raise errors.AbstractClassError()

    def jump(self, level):
        move = self._get_jump_movement_distance(level)

        if move == 0:
            self.fall()
            return

        self.frame_count += 1
        self.player.rect.top += move
    
    def _get_jump_movement_distance(self, level):
        """Looks at move and sees if player can move that far, if not returns the max amount
        the player is allowed to move, the amount of the move is determined by gravity and the classic
        physics formula velocity initial + time * acceleration"""
        velocity = old_velocity = int(round(-self.player.jump_speed + self.frame_count * GRAVITY))
        self.player.rect.top += velocity

        collides = spritecollide(self.player, level.tile_group, False)
        if collides:
            velocity = self._get_jump_movement_until_collision(collides, velocity)

        self.player.rect.top -= old_velocity
        return velocity

    def _get_jump_movement_until_collision(self, collides, move):
        """Given a list of tiles that collide with the player finds the one farthest to the bottom
        and returns the number of pixels the player can move until it is within the tile"""
        ceilings = [ceiling for ceiling in collides if self.player.rect.top <= ceiling.rect.bottom]
        if ceilings:
            ceilings.sort(lambda x,y: x.rect.bottom - y.rect.bottom)
            move += ceilings[0].rect.bottom - self.player.rect.top
        return move
