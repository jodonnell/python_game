from game import conf

""" The screen takes a level object and a player starting point and creates itself based off that 
The screens primary purpose is to keep track of new sprites to add when they are scrolled on screen
For collision detection, and 
"""

class screen():
    def __init__(self, level):
        self.level = level
        player_start = self.level.get_player_start_pos()
        self.screen_left_end_abs_pos = player_start - (conf.SCREEN_WIDTH / 2)
        self.screen_right_end_abs_pos = player_start + (conf.SCREEN_WIDTH / 2)
        tile_group.add(self.level.get_onscreen_tiles(self.screen_left_end_abs_pos, self.screen_right_end_abs_pos))

    def move_right(self, shift_screen_amount):
        self.screen_left_end_abs_pos += shift_screen_amount
        self.screen_right_end_abs_pos += shift_screen_amount
        tile_group.add(self.level.new_right_tiles())
        tile_group.remove(self.level.remove_left_tiles())

    def move_left(self, shift_screen_amount):
        self.screen_left_end_abs_pos -= shift_screen_amount
        self.screen_right_end_abs_pos -= shift_screen_amount
        tile_group.add(self.level.new_left_tiles())
        tile_group.remove(self.level.remove_right_tiles())
        
    def convert_abs_to_screen(self, abs_pos):
        return abs_pos - self.screen_left_end_abs_pos

    def is_active(self, abs_pos):
        """ This checks to see if the object is on screen or close to onscreen
        It isn't just onscreen because otherwise player could cheat to have enemy
        pace off screen and then not have to fight them
        """
        screen_pos = self.convert_abs_to_screen(abs_pos)
        if (screen_pos > (self.screen_right_end_abs_pos + ON_SCREEN_PADDING)) and (screen_pos < (self.screen_left_end_abs_pos - ON_SCREEN_PADDING)):
            return True
        return False
        
