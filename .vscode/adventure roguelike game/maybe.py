import pygame, math, random, time


pygame.init()
pygame.font.init()
FPS = 60
pygame.display.set_caption("Your game name here")
screen = pygame.display.set_mode((500,500))
screen.fill((0, 100, 0))

font = pygame.font.SysFont("comicsansms", 15)
playerpos = [0,0]
load = pygame.image.load
scale = pygame.transform.scale

clock = pygame.time.Clock()
running = True
while running:
    key = pygame.key.get_pressed()
    clock.tick(FPS)
    screen.fill((0, 100, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen,(255,255,255),(playerpos[0],playerpos[1],25,25))

    fpsgiver = int(clock.get_fps())
    screen.blit(font.render(f"FPS: {fpsgiver}", True, (255, 255, 255)),(0,0))
    pygame.display.flip() 