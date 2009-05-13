from pygame.constants import *
import pygame

class Control():
    def __init__(self):
        self.LEFT_KEY = K_LEFT
        self.RIGHT_KEY = K_RIGHT
        self.DOWN_KEY = K_DOWN
        self.JUMP_KEY = K_SPACE

    def get_left_key_pressed(self):
        return (pygame.KEYDOWN, self.LEFT_KEY)

    def get_left_key_released(self):
        return (pygame.KEYUP, self.LEFT_KEY)

    def get_right_key_pressed(self):
        return (pygame.KEYDOWN, self.RIGHT_KEY)

    def get_right_key_released(self):
        return (pygame.KEYUP, self.RIGHT_KEY)

    def get_duck_key_pressed(self):
        return (pygame.KEYDOWN, self.DOWN_KEY)

    def get_duck_key_released(self):
        return (pygame.KEYUP, self.DOWN_KEY)

    def get_jump_key_released(self):
        return (pygame.KEYUP, self.JUMP_KEY)

    def get_jump_key_pressed(self):
        return (pygame.KEYDOWN, self.JUMP_KEY)
