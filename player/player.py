from game.Sprite import Sprite
from game.player.moving_states import MovingStates
from game.player.aerial_states import AerialStates
from game.conf import *
import pygame

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
        self.image = self._STILL_RIGHT_FRAME
        self.control = control

        self.movement_speed = 4
        self.jump_speed = 4
        self.jump_height = 40

        Sprite.__init__(self, startPos)
        self.movement_state = MovingStates(self)
        self.aerial_state = AerialStates(self)
   
    def load_frames(self):
        "Loads all the frames for the sprite"
        import os

        self._STILL_LEFT_FRAME = pygame.transform.flip( self.load_image( os.path.join('images', 'golem2.png') ), 1, 0)
        self._MOVE_LEFT_FRAME_1 = pygame.transform.flip( self.load_image( os.path.join('images', 'golem1.png') ), 1, 0)
        self._MOVE_LEFT_FRAME_2 = pygame.transform.flip( self.load_image( os.path.join('images', 'golem3.png') ), 1, 0)

        self._STILL_RIGHT_FRAME = self.load_image( os.path.join('images', 'golem2.png') )
        self._MOVE_RIGHT_FRAME_1 = self.load_image( os.path.join('images', 'golem1.png') )
        self._MOVE_RIGHT_FRAME_2 = self.load_image( os.path.join('images', 'golem3.png') )

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

    def process_input(self, inputs):
        "Takes a list of player key inputs and processes them"
        for input in inputs:
            if self._is_movement_key(input):
                self.movement_state.process_input(input)
            if self._is_jumping_key(input):
                self.aerial_state.process_input(input)
            
    def update(self, *args):
        """First processes key events which could change player state.
        Then delegates to the player states to do the correct action for the state they are in.
        Then sets the correct frame for the next screen update."""
        self.process_input(args[0])
        self.movement_state.do_action()
        self.aerial_state.do_action()
        self.image = self.movement_state.state.get_animation()
#        self.rect = self.rect.move(self.speed)
        
