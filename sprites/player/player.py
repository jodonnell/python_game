from game.sprites.sprite import Sprite
from game.sprites.player.moving_states import MovingStates
from game.sprites.player.aerial_states import AerialStates
from game import conf
from game import log
import pygame

MOVE_TOP = 1
CUT_OFF_RIGHT = 1
CUT_OFF_LEFT = 2
logger = log.logging.getLogger('player')

CENTER_OF_SCREEN = 600

class Player(Sprite):
    ''' The player class makes use of the state pattern.
    It contains three sets of states each set contains mutually exclusive behavior.
    For instance the player can be moving left, jumping, and attacking; but cannot
    be simultaneously jumping and falling.
    '''
    def __init__(self, startPos, control):
        """The constructor takes a tuple startPos which will be used as the players starting position, it also takes a control object that contains 
        the players control configuration"""
        self.load_frames()
        self.image = self._STILL_RIGHT_FRAME['image']
        self.control = control

        self.movement_speed = 4
        self.jump_speed = 12

        Sprite.__init__(self, startPos)
        self.rect.left = startPos[0] - self.rect.width

        self.movement_state = MovingStates(self)
        self.aerial_state = AerialStates(self)

   
    def load_frames(self):
        "Loads all the frames for the sprite"
        import os
        HORIZONTAL_FLIP = True
        VERTICAL_FLIP = False

        self._STILL_LEFT_FRAME = self.create_frames(pygame.transform.flip( self.load_image( os.path.join('images', 'golem2.png') ), HORIZONTAL_FLIP, VERTICAL_FLIP))
        self._MOVE_LEFT_FRAME_1 = self.create_frames(pygame.transform.flip( self.load_image( os.path.join('images', 'golem1.png') ), HORIZONTAL_FLIP, VERTICAL_FLIP))
        self._MOVE_LEFT_FRAME_2 = self.create_frames(pygame.transform.flip( self.load_image( os.path.join('images', 'golem3.png') ), HORIZONTAL_FLIP, VERTICAL_FLIP))
        self._DUCK_LEFT_FRAME = self.create_frames(pygame.transform.flip( self.load_image( os.path.join('images', 'golem_duck.png') ), HORIZONTAL_FLIP, VERTICAL_FLIP))

        self._STILL_RIGHT_FRAME = self.create_frames(self.load_image( os.path.join('images', 'golem2.png') ))
        self._MOVE_RIGHT_FRAME_1 = self.create_frames(self.load_image( os.path.join('images', 'golem1.png') ))
        self._MOVE_RIGHT_FRAME_2 = self.create_frames(self.load_image( os.path.join('images', 'golem3.png') ))
        self._DUCK_RIGHT_FRAME = self.create_frames(self.load_image( os.path.join('images', 'golem_duck.png') ))

    def create_frames(self, image, dimension_change_behavior = MOVE_TOP):
        rect = image.get_bounding_rect()
        return {'image':image, 'rect':rect, 'dimension_change_behavior':dimension_change_behavior}

    def load_image(self, image_path):
        "loads the image and converts it to a format that blits quicklp"
        image = pygame.image.load(image_path)
        return image.convert_alpha()
       
    def _is_movement_key(self, input):
        "Returns True if the key pressed or released was a movement key"
        if (input == self.control.get_left_key_pressed() 
            or input == self.control.get_left_key_released() 
            or input == self.control.get_right_key_pressed() 
            or input == self.control.get_right_key_released() 
            or input == self.control.get_duck_key_pressed() 
            or input == self.control.get_duck_key_released() ):
            return True
        else:
            return False
        
    def _is_jumping_key(self, input):
        "Returns True if the key pressed or released was the jump key"
        if input == self.control.get_jump_key_pressed() or input == self.control.get_jump_key_released():
            return True
        else:
            return False

    def process_input(self, inputs, level):
        "Takes a list of player key inputs and processes them"
        for input in inputs:
            if self._is_movement_key(input):
                self.movement_state.process_input(input, level)
            if self._is_jumping_key(input):
                self.aerial_state.process_input(input, level)
            
    def update(self, inputs, level):
        """First processes key events which could change player state.
        Then delegates to the player states to do the correct action for the state they are in.
        Then sets the correct frame for the next screen update."""
        self.process_input(inputs, level)
        self.movement_state.do_action(level)
        self.aerial_state.do_action(level)
        self.change_image(self.movement_state.state.get_animation())
 
    def change_image(self, new_frame):
        """Whenever the image is changed you should go through this method so 
        it will do the correct thing when the old image and the new one
        have different heights or widths"""
        if self.image is not new_frame['image']:
            self.image = new_frame['image']

            rect = new_frame['rect']

            if self.rect.width != rect.width:
                self.rect.width = rect.width

            if rect.height != self.rect.height:
                if new_frame['dimension_change_behavior'] == MOVE_TOP:
                    move_by = self.rect.height - rect.height
                    self.rect.height = rect.height
                    self.rect.move_ip(0, move_by)

    def move_rect_x(self, move):
        self.rect.left += move

    def is_player_left_of_center(self):
        return self.rect.left < conf.SCREEN_WIDTH / 2 - self.rect.width

    def is_player_right_of_center(self):
        return self.rect.left > conf.SCREEN_WIDTH / 2 - self.rect.width
