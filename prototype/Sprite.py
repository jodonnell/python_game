import pygame
from conf import *

################################################################################
# Sprite class
class Sprite(pygame.sprite.Sprite):
    speed = []
    image = '';
    rect = '';
    
    def __init__(self, startX, startY, speed, imagePath):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(imagePath)
        self.image = self.image.convert_alpha()

        self.rect = self.image.get_bounding_rect()
        self.rect = self.rect.move(startX, startY)
        
        self.speed = speed;
    
    def update(self, *args):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed[1] = -self.speed[1]
