import pygame

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
