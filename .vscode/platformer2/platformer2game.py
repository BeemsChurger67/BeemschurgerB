import pygame,os,time,random
pygame.init()
pygame.font.init()
SCREENWIDTH = 1000
SCREENHEIGHT = 700
fps = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
running = True
X = SCREENWIDTH / 2
Y = 0
Yvel = 1
speed = 4
while running:
    screen.fill((0,0,155))
    key = pygame.key.get_pressed()
    platform = pygame.draw.rect(screen,(0,0,0),(300,500,300,50),border_radius=16)
    if key[pygame.K_a]:
        for A in range(speed):
            if player.colliderect(platform):
                X -= 1
            else:
                X += 1
    if key[pygame.K_d]:
        for A in range(speed):
            if player.colliderect(platform):
                X += 1
            else:
                X -= 1
    for A in range(int(Yvel + 1)):
        player = pygame.draw.rect(screen,(111,111,111),(X,Y,25,50),border_radius=16)
        if player.colliderect(platform):
            Yvel = 0
            break
        else:
            Y += 1
    Yvel += 0.5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(fps)
    pygame.display.flip()
    