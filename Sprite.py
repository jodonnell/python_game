import pygame
from game.conf import *

################################################################################
# Sprite class
class Sprite(pygame.sprite.Sprite):
    rect = '';
    
    def __init__(self, start):
        ''' Constructor for the Sprite class
        imagePath - a string containing the path to the image file
        start - a tuple containing starting X and Y coords
        speed - an array containing the starting X and Y speed
        '''
        pygame.sprite.Sprite.__init__(self)
        
        startX, startY = start;
        self.rect = self.image.get_bounding_rect()
        self.rect = self.rect.move(startX, startY)
    
    def update(self, *args):
        ''' When this is called the all updates to the object should be done
        Currently moves the object based on the speed of the object 
        Takes args but does nothing with them, will most likely remove
        '''
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed[1] = -self.speed[1]
