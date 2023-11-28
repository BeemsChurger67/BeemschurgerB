import pygame
from numpy import floor
pygame.init()
pygame.display.set_caption("square innit game idfk")
FPS = 144
SCREENHEIGHT = 500
SCREENWIDTH = 700
player = pygame.Rect(SCREENWIDTH / 2 -25,SCREENHEIGHT / 2 - 25,50,50)
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
gamemap = pygame.Rect(0,0,400,100)
running = True
x = 0
y = 0
yvel = 0
def COLLIDE_GROUND():
    global key, yvel, y, player
    yvel = 0
    if key[pygame.K_w] == True:
        y -= 3
        yvel -= 4
def COLLIDE_LOOP():
    global running,cube,y
    running = False
    while player.colliderect(gamemap):
        #Vertical
        player.width = 25
        player.x = SCREENWIDTH / 2 - 12.5
        player.move_ip(0,-1)
        y -= 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.display.update()
    player.width = 50
    y += 1
    player.y = SCREENHEIGHT / 2 -25
    player.x = SCREENWIDTH / 2 -25
    while player.colliderect(gamemap):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.display.update()
    running = True
while running:
    key = pygame.key.get_pressed()
    screen.fill((100,100,255))
    cube = pygame.draw.rect(screen,(0,0,255),player)
    map = pygame.draw.rect(screen,(0,0,0),gamemap)
    gamemap.x = 0 - (x - 150)
    gamemap.y = 0 - (y - 500)
    if not cube.colliderect(gamemap):
        yvel += 0.05
        y += yvel
    else:
        COLLIDE_GROUND()
        COLLIDE_LOOP()
    if cube.colliderect(gamemap):
        while cube.colliderect(gamemap):
            cube.move_ip(0,-2)
    if key[pygame.K_a] == True:
        x -= 1.5
    if key[pygame.K_d] == True:
        x += 1.5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(FPS)
    print("yvel =",yvel)
    print("xy", x,y)
    print(gamemap)
    