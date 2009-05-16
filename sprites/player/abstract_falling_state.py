from game import errors
from game.conf import GRAVITY
from pygame.sprite import spritecollide

class AbstractFallingState():
    def __init__(self):
        raise errors.AbstractClassError()

    def fall(self, level):
        move = self._get_falling_movement_distance(level)

        if move == 0:
            self.grounded()
            return

        self.frame_count += 1
        self.player.rect.top += move

    def _get_falling_movement_distance(self, level):
        """Looks at move and sees if player can move that far, if not returns the max amount
        the player is allowed to move, the amount of the move is determined by gravity and the classic
        physics formula velocity initial + time * acceleration"""
        # v initial must not be 0 or this transitions to grounded state
        velocity = old_velocity = int(round(1 + self.frame_count * GRAVITY))
        self.player.rect.top += velocity

        collides = spritecollide(self.player, level.tile_group, False)
        if collides:
            velocity = self._get_falling_movement_until_collision(collides, velocity)

        self.player.rect.top -= old_velocity
        return velocity

    def _get_falling_movement_until_collision(self, collides, move):
        """Given a list of tiles that collide with the player finds the one farthest to the top
        and returns the number of pixels the player can move until it is within the tile"""
        floors = [floor for floor in collides if self.player.rect.bottom >= floor.rect.top]
        if floors:
            floors.sort(lambda x,y: x.rect.top - y.rect.top)
            move += floors[0].rect.top - self.player.rect.bottom
        return move
