from game import errors
from pygame.sprite import spritecollide

class AbstractMovingLeftState():
    def __init__(self):
        raise errors.AbstractClassError()

    def move_left(self, level):
        "move left"
        move = self._get_left_movement_distance(level)

        if move == 0: # trying to move into wall
            self.animation_index = 0
            return
        
        left_end_of_level = level.get_first_tile().get_left_edge()
        left_edge_of_level_reached = level.view.get_left_end_of_view() + move < left_end_of_level

        if (left_edge_of_level_reached or self.player.is_player_right_of_center()):
            self.player.move_rect_x(move)
        else:
            level.move_view(move)

        self._update_animation()

    def _get_left_movement_distance(self, level):
        """Looks at move and sees if player can move that far, if not returns the max amount
        the player is allowed to move"""
        move = old_move = -self.player.movement_speed
        self.player.rect.left += move

        collides = spritecollide(self.player, level.tile_group, False)
        if collides:
            move = self._get_left_movement_until_collision(collides, move)

        self.player.rect.left -= old_move
        return move

    def _get_left_movement_until_collision(self, collides, move):
        """Given a list of tiles that collide with the player finds the one farthest to the right 
        and returns the number of pixels the player can move until it is within the tile"""
        left_collision_tiles = [tile for tile in collides if self.player.rect.left <= tile.rect.right and tile.rect.top < self.player.rect.bottom]
        if left_collision_tiles:
            left_collision_tiles.sort(lambda x,y: x.rect.right - y.rect.right) # get the colliding tile furthest to the right
            move += left_collision_tiles[0].rect.right - self.player.rect.left
        return move
