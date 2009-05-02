from game import conf

""" The screen takes a level object and a player starting point and creates itself based off that 
The screens primary purpose is to keep track of new sprites to add when they are scrolled on screen
For collision detection, and 
This class deals internally with relative positions, but all contact with other classes is done using absolution positions
sugar  
"""

class View():
    """ The View's duty is to keep track of what area on the level is in the current 
    player's view.  It does this by keeping track of the absolute coordinates of the
    left side and right side of the view and updating it when the view needs
    to shift left or right.  It is also in charge of converting absolute coordinates
    to relative coordinates for drawing to the screen.
    """
    def __init__(self, level, tile_group):
        self.level = level
        player_start = self.level.get_player_start_abs_pos_x()
        self.view_left_end_abs_pos = player_start - (conf.SCREEN_WIDTH / 2) # this assumes player starts in the middle
        self.view_right_end_abs_pos = player_start + (conf.SCREEN_WIDTH / 2)

        self.tile_group = tile_group
        self.tile_group.add(*self.level.get_onscreen_tiles(self.view_left_end_abs_pos, self.view_right_end_abs_pos))

    def move_view(self, shift_view_amount):
        self.view_left_end_abs_pos += shift_view_amount
        self.view_right_end_abs_pos += shift_view_amount

    def move_right(self, shift_view_amount):
        self.move_view(shift_view_amount)
        self.tile_group.add(self.level.new_right_tiles(self.view_right_end_abs_pos))
        self.tile_group.remove(self.level.remove_left_tiles(self.view_left_end_abs_pos))

    def move_left(self, shift_view_amount):
        self.move_view(-shift_view_amount)
        self.tile_group.add(self.level.new_left_tiles(self.view_left_end_abs_pos))
        self.tile_group.remove(self.level.remove_right_tiles(self.view_right_end_abs_pos))
        
    def convert_abs_to_view(self, abs_pos):
        return abs_pos - self.view_left_end_abs_pos

    def update_view(self):
        self.level.update_level(self.view_left_end_abs_pos)

    def is_active(self, abs_pos):
        # This may be unecessary because tiles will be removed on move left and move right
        """ This checks to see if the object is on view or close to onview
        It isn't just onview because otherwise player could cheat to have enemy
        pace off view and then not have to fight them
        """
        view_pos = self.convert_abs_to_view(abs_pos)
        if (view_pos > (self.view_right_end_abs_pos + ON_SCREEN_PADDING)) and (view_pos < (self.view_left_end_abs_pos - ON_SCREEN_PADDING)):
            return True
        return False
        
