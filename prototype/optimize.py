import sys, pygame, random, os
pygame.init()

size = width, height = 1024, 640
black = 0, 0, 0

screen = pygame.display.set_mode((width,height), pygame.FULLSCREEN)

pygame.mouse.set_visible(False)

#music = pygame.mixer.Sound(os.path.join('music', 'airfrance.ogg'))
#music.play()
#pygame.mixer.music.load(os.path.join('music', 'air_france.mp3'))
#pygame.mixer.music.play()


NUM_ON_SCREEN = 200
FPS_MAX = 400

class Sprite:
    speed = []
    image = '';
    rect = '';
    
    def __init__(self, startX, startY, speed):
        image = random.randint(1, 2)
        if image == 1:
            imageName = os.path.join('images', 'skull.png')
        else:
            imageName = os.path.join('images', 'greenFlyer.png')
        self.image = pygame.image.load(imageName)
        self.image = self.image.convert_alpha()

        self.rect = self.image.get_rect()
        self.rect = self.rect.move(startX, startY)
        
        self.speed = speed;
    
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]

# each sprite needs to have a different speed, and location
#
#
#

sprites = []
for x in range(NUM_ON_SCREEN):
    startX = random.randint(1, width - 200)
    startY = random.randint(1, height - 200)
    speed = [random.randint(-4, 4), random.randint(-4, 4)]
    
    sprites.append( Sprite(startX, startY, speed) );


clock = pygame.time.Clock()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.unicode == 'q':
                sys.exit()

    screen.fill(black)
    for sprite in sprites:
        sprite.move()
        screen.blit(sprite.image, sprite.rect)


    clock.tick_busy_loop(FPS_MAX)
    pygame.display.flip()
    pygame.display.set_caption("fps: %s" % (str(int(clock.get_fps()))))

    print clock.get_fps()
