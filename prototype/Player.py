import Sprite
from conf import *

class Player(Sprite.Sprite):
    def __init__(self, startX, startY, imagePath):
        Sprite.Sprite.__init__(self, startX, startY, [0, 0], imagePath)
        self.movingLeft = False
        self.movingRight = False
        self.movingDown = False
        self.movingUp = False
   
    def moveLeft(self):
        self.speed[0] = -2
        self.movingLeft = True
        self.movingRight = False

    def moveRight(self):
        self.speed[0] = 2
        self.movingRight = True
        self.movingLeft = False

    def moveUp(self):
        self.speed[1] = -2
        self.movingUp = True
        self.movingDown = False

    def moveDown(self):
        self.speed[1] = 2
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
        
