import pygame, math, random, time


pygame.init()
pygame.font.init()
FPS = 60
pygame.display.set_caption("Controller game")
screen = pygame.display.set_mode((500,500))
screen.fill((0, 100, 0))

CSMfont = pygame.font.SysFont("comicsansms", 15)

load = pygame.image.load
scale = pygame.transform.scale

clock = pygame.time.Clock()
maxSpeed = 25
x = screen.get_size()[0] / 2 - 12.5
y = screen.get_size()[1] / 2 - 12.5
player = pygame.Rect(x,y,25,25)
xvel = 0
yvel = 0
running = True
while running:
    key = pygame.key.get_pressed()
    clock.tick(FPS)
    screen.fill((0, 100, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player = pygame.Rect(x,y,25,25)
    pygame.draw.rect(screen,"red",player)
    if key[pygame.K_a] and xvel > -maxSpeed:
        xvel -= 0.5
    elif xvel < 0:
        xvel += 0.5
    if key[pygame.K_d] and xvel < maxSpeed:
        xvel += 0.5
    elif xvel > 0:
        xvel -= 0.5
    if key[pygame.K_s] and yvel < maxSpeed:
        yvel += 0.5
    elif yvel > 0:
        yvel -= 0.5
    if key[pygame.K_w] and yvel > -maxSpeed:
        yvel -= 0.5
    elif yvel < 0:
        yvel += 0.5
    
    x += xvel
    y += yvel
    if x > screen.get_size()[0]:
        x -= screen.get_size()[0]
    if x < -25:
        x += screen.get_size()[0]
    if y < -25:
        y += screen.get_size()[1]
    if y > screen.get_size()[1]:
        y -= screen.get_size()[1]
    




    fpsgiver = int(clock.get_fps())
    screen.blit(CSMfont.render(f"FPS: {fpsgiver}", True, (255, 255, 255)),(0,0))
    screen.blit(CSMfont.render(f"Xspeed: {xvel} x: {x}", True, (255, 255, 255)),(0,15))
    screen.blit(CSMfont.render(f"Yspeed: {yvel} y: {y}", True, (255, 255, 255)),(0,30))
    pygame.display.flip()