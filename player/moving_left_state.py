from pygame.sprite import spritecollide

def collide_left(player, collides, move):
    left_tiles = [tile for tile in collides if player.rect.left <= tile.rect.right and tile.rect.top < player.rect.bottom]
    if left_tiles:
        left_tiles.sort(lambda x,y: x.rect.right - y.rect.right)
        return move + (left_tiles[0].rect.right - player.rect.left)
    return move


class MovingLeftState():
    "The state when the player is moving left."
    def __init__(self, player):
        self.player = player
        self._animation = (self.player._STILL_LEFT_FRAME, self.player._MOVE_LEFT_FRAME_1, self.player._MOVE_LEFT_FRAME_2, self.player._STILL_LEFT_FRAME)
        
        self.frame_count = 0
        self.animation_index = 0

    def get_animation(self):
        return self._animation[self.animation_index]

    def do_action(self, level):
        self.move_left(level)

    def move_left(self, level):
        "move left"
        move = -self.player.movement_speed
        left_end_of_level = level.get_first_tile().get_left_edge()
        left_edge_of_level_reached = level.view.get_left_end_of_view() + move < left_end_of_level

        move = self.move_left_max(move, level)

        if move == 0: # trying to move into wall
            self.frame_count = 0
            self.animation_index = 0
            return
        
        if (left_edge_of_level_reached or self.player.is_player_right_of_center()):
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

    def move_left_max(self, move, level):
        """Looks at move and sees if player can move that far, if not returns the max amount
        the player is allowed to move"""
        tmp = self.player.rect
        self.player.rect = self.player.rect.move(move, 0)
        collides = spritecollide(self.player, level.tile_group, False)

        if collides:
            move = collide_left(self.player, collides, move)

        self.player.rect = tmp
        return move

    def move_right(self, level):
        "transition state to move right"
        self.player.movement_state.set_movement_state(self.player.movement_state.get_move_right_state())

    def stop_moving_left(self):
        "transition state to not moving"
        self.player.movement_state.set_movement_state(self.player.movement_state.get_still_state())

    def stop_moving_right(self):
        "player held down both left and right, ignore"
        pass

    def duck(self):
        "transition to ducking state"
        self.player.movement_state.set_movement_state(self.player.movement_state.get_ducking_state())

    def stop_ducking(self):
        "player held down multiple buttons, ignore"
        pass
