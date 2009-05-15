from pygame.sprite import spritecollide

class MovingRightState():
    "The state when the player is moving right."
    def __init__(self, player):
        self.player = player
        self._animation = (self.player._STILL_RIGHT_FRAME, self.player._MOVE_RIGHT_FRAME_1, self.player._MOVE_RIGHT_FRAME_2, self.player._STILL_RIGHT_FRAME)
        
        self.frame_count = 0
        self.animation_index = 0

    def get_animation(self):
        return self._animation[self.animation_index]

    def do_action(self, level):
        return self.move_right(level)

    def move_right(self, level):
        "move right"
        move = self._get_movement_distance(level)

        if move == 0: # trying to move into wall
            self.frame_count = 0
            self.animation_index = 0
            return
        
        right_end_of_level = level.get_last_tile().get_right_edge()
        right_edge_of_level_reached = level.view.get_right_end_of_view() + move > right_end_of_level

        if (right_edge_of_level_reached or self.player.is_player_left_of_center()):
            self.player.move_rect_x(move)
        else:
            level.move_view(move)

        self._update_animation()

    def _update_animation(self):
        """Updates the frame count and animation"""
        self.frame_count += 1
        
        if self.frame_count == 8:
            self.frame_count = 0
            self.animation_index += 1
            if self.animation_index == len(self._animation):
                self.animation_index = 0

    def _get_movement_distance(self, level):
        """Looks at move and sees if player can move that far, if not returns the max amount
        the player is allowed to move"""
        move = old_move = self.player.movement_speed
        self.player.rect.left += move

        collides = spritecollide(self.player, level.tile_group, False)
        if collides:
            move = self._get_movement_until_collision(collides, move)

        self.player.rect.left -= old_move
        return move

    def _get_movement_until_collision(self, collides, move):
        """Given a list of tiles that collide with the player finds the one farthest to the left
        and returns the number of pixels the player can move until it is within the tile"""
        right_collision_tiles = [tile for tile in collides if self.player.rect.right >= tile.rect.left and tile.rect.top < self.player.rect.bottom]
        if right_collision_tiles:
            right_collision_tiles.sort(lambda x,y: x.rect.left - y.rect.left)
            move += right_collision_tiles[0].rect.left - self.player.rect.right
        return move

    def move_left(self, level):
        "transition state to move right"
        self.player.movement_state.set_movement_state(self.player.movement_state.get_move_left_state())

    def stop_moving_right(self):
        "transition state to not moving"
        self.player.movement_state.set_movement_state(self.player.movement_state.get_still_state())

    def stop_moving_left(self):
        "player held down both left and right, ignore"
        pass

    def duck(self):
        "transition to ducking state"
        self.player.movement_state.set_movement_state(self.player.movement_state.get_ducking_state())

    def stop_ducking(self):
        "player held down multiple buttons, ignore"
        pass
