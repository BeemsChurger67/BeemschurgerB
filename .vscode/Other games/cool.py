import pygame, random, time
import math as M
pygame.init()
pygame.font.init()
FPS = 60
pygame.display.set_caption("Tidal Wave by OniLinkGD")
screen = pygame.display.set_mode((1200,500))
screen.fill((255,255,255))
RNG = random.randint
font = pygame.font.SysFont("comicsansms", 15)
load = pygame.image.load
scale = pygame.transform.scale
clock = pygame.time.Clock()
running = True
numLength = 2000
print(M.pi)
A = []
for Nums in range(numLength):
    A.append(1)
Lines = len(A) - 1
Length = 2
Height = 100
Thickness = 1
Division = 2
while running:
    clock.tick(FPS)
    screen.fill((200,200,200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(font.render(f"Screen Size: {screen.get_size()}", True, (0,0,0)),(0,15))
    for I in range(len(A)):
        A[I] += I / Division
    for I in range(Lines):
        pygame.draw.line(screen,(RNG(0,255),RNG(0,255),RNG(0,255)),(Length * I,screen.get_height() / 2 + M.sin(A[I] * 0.1) * Height),(Length * I + Length,screen.get_height() / 2 + M.sin(A[I + 1] * 0.1) * Height),width=Thickness)
    fpsgiver = int(clock.get_fps())
    screen.blit(font.render(f"FPS: {fpsgiver}", True, (0,0,0)),(0,0))
    pygame.display.flip()