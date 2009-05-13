from pygame.sprite import spritecollide

def collide_right(player, collides, move):
    right_tiles = [tile for tile in collides if player.rect.right >= tile.rect.left and tile.rect.top < player.rect.bottom]
    if right_tiles:
        right_tiles.sort(lambda x,y: x.rect.left - y.rect.left)
        return move + (right_tiles[0].rect.left - player.rect.right)
    return move


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
        move = self.player.movement_speed 
        right_end_of_level = level.get_last_tile().get_right_edge()
        right_edge_of_level_reached = level.view.get_right_end_of_view() + move > right_end_of_level

        move = self.move_right_max(move, level)

        if move == 0: # trying to move into wall
            self.frame_count = 0
            self.animation_index = 0
            return
        
        if (right_edge_of_level_reached or self.player.is_player_left_of_center()):
            # this will be wrong for movement speeds bigger than 1
            self.player.move_rect_x(move)
        else:
            level.move_view(move)

        self.frame_count += 1
        
        if self.frame_count == 8:
            self.frame_count = 0
            self.animation_index += 1
            if self.animation_index == len(self._animation):
                self.animation_index = 0

        return self.player.movement_speed

    def move_right_max(self, move, level):
        """Looks at move and sees if player can move that far, if not returns the max amount
        the player is allowed to move"""
        tmp = self.player.rect
        self.player.rect = self.player.rect.move(move, 0)
        collides = spritecollide(self.player, level.tile_group, False)

        if collides:
            move = collide_right(self.player, collides, move)

        self.player.rect = tmp
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
