import Sprite
from conf import *

class Player(Sprite.Sprite):
    '''This class is supposed to model a Bubble like character
    The controls work like this.  When the player holds down the right key there player will begin moving right,
    When it is let go they will stop moving right, if the player holds both right and left, the character will not move
    
    The jumping works like this, when you hit the jump key the jump animation starts and then falling kicks in
    '''
    def __init__(self, imagePath, startPos, startSpeed):
        Sprite.Sprite.__init__(self, imagePath, startPos, startSpeed)
        self.movingLeft = False
        self.movingRight = False
        self.movingDown = False
        self.movingUp = False
   
    def moveLeft(self):
        self.speed[0] = -8
        self.movingLeft = True
        self.movingRight = False

    def moveRight(self):
        self.speed[0] = 8
        self.movingRight = True
        self.movingLeft = False

    def moveUp(self):
        self.speed[1] = -8
        self.movingUp = True
        self.movingDown = False

    def moveDown(self):
        self.speed[1] = 8
        self.movingDown = True
        self.movingUp = False

    def stopMoveLeft(self):
        if self.movingLeft:
            self.speed[0] = 0

    def stopMoveRight(self):
        if self.movingRight:
            self.speed[0] = 0

    def stopMoveUp(self):
        if self.movingUp:
            self.speed[1] = 0

    def stopMoveDown(self):
        if self.movingDown:
            self.speed[1] = 0
        
    def update(self, *args):
        self.rect = self.rect.move(self.speed)
        
