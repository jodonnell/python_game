import sys, pygame, random, os, Sprite, Player
from conf import *
from pygame.constants import *

pygame.init()

screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT), pygame.FULLSCREEN )
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)


#music = pygame.mixer.Sound(os.path.join('music', 'airfrance.ogg'))
#music.play()
#pygame.mixer.music.load(os.path.join('music', 'air_france.mp3'))
#pygame.mixer.music.play()


################################################################################
# Create all the different sprites and place them randomly with random speed
# Put them in their respective groups
greenFlyers = pygame.sprite.Group();
skullMens = pygame.sprite.Group();

for x in range(NUM_ON_SCREEN):
    startX = random.randint(1, SCREEN_WIDTH - 200)
    startY = random.randint(1, SCREEN_HEIGHT - 200)
    speed = [random.randint(-4, 4), random.randint(-4, 4)]

    if x % 66 == 0:
        imagePath = os.path.join('images', 'skull.png')
        sprint = Sprite.Sprite(startX, startY, speed, imagePath)
        sprint.add( skullMens )
    else:
        imagePath = os.path.join('images', 'greenFlyer.png')
        sprint = Sprite.Sprite(startX, startY, speed, imagePath)
        sprint.add( greenFlyers )

playerGroup = pygame.sprite.Group();
player = Player.Player(200, 200, os.path.join('images', 'player.png'))
player.add( playerGroup )

#################################################################################
# MAIN GAME LOOP
sum_fps = 0;
game_loops = 0;

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_q:
                print sum_fps / game_loops
                sys.exit()
            if event.key == K_LEFT:
                player.moveLeft();
            if event.key == K_UP:
                player.moveUp();
            if event.key == K_DOWN:
                player.moveDown();
            if event.key == K_RIGHT:
                player.moveRight();

        if event.type == pygame.KEYUP:
            if event.key == K_LEFT:
                player.stopMoveLeft();
            if event.key == K_UP:
                player.stopMoveUp();
            if event.key == K_DOWN:
                player.stopMoveDown();
            if event.key == K_RIGHT:
                player.stopMoveRight();


    pygame.sprite.groupcollide(playerGroup, skullMens, True, False)
    pygame.sprite.groupcollide(playerGroup, greenFlyers, False, True)

    skullMens.update()
    greenFlyers.update()
    playerGroup.update()

    screen.fill(BLACK)

    skullMens.draw(screen)
    greenFlyers.draw(screen)
    playerGroup.draw(screen)

    clock.tick_busy_loop(FPS_MAX)
    pygame.display.flip()

#    pygame.display.set_caption("fps: %s" % (str(int(clock.get_fps()))))
    game_loops += 1
    sum_fps += clock.get_fps()

