import math,sys,time,pygame
pygame.init()
screen = pygame.display.set_mode((640,480),pygame.FULLSCREEN|pygame.DOUBLEBUF|pygame.HWSURFACE)
c=0
while 1:
     c=((c+1)%2)*255
     for event in pygame.event.get():
         if event.type in [2,5,6,12]:
             sys.exit()
     screen.fill((c,c,c))
     pygame.display.flip()
