import pygame, math, random, time, os
pygame.init()
pygame.font.init()
FPS = 60
pygame.display.set_caption("cat")
screen = pygame.display.set_mode((500,500))
screen.fill((0, 100, 0))

font = pygame.font.SysFont("comicsansms", 15)

directory = os.getcwd()
directory = os.path.join(directory, "images")
load = pygame.image.load
scale = pygame.transform.scale
player = load("sigmacat.png")
player = scale(player,(60,60))

clock = pygame.time.Clock()
running = True
x = 0
y = 0
while running:
    key = pygame.key.get_pressed()
    clock.tick(FPS)
    screen.fill((100, 100, 100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if key[pygame.K_a]:
        x -= 5
    if key[pygame.K_d]:
        x += 5
    if key[pygame.K_w]:
        y -= 5
    if key[pygame.K_s]:
        y += 5
    screen.blit(player,(x,y))
    fpsgiver = int(clock.get_fps())
    screen.blit(font.render(f"FPS: {fpsgiver}", True, (255, 255, 255)),(0,0))
    pygame.display.flip()