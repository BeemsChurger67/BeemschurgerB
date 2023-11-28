import pygame
import math
import os
import random
import time
pygame.init()
pygame.font.init()
SCREENWIDTH = 700
SCREENHEIGHT = 700
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
clock = pygame.time.Clock()
FPS = 60
def tower(x,y):
    pygame.draw.rect(screen,(111,111,111),(x - 25,y - 25,50,50),border_radius=16)
    gun = pygame.draw.rect(screen,(75,75,75),(x + 10 - 25,y + 10 - 25,80,30),border_radius=16)
click = False
running = True
while running:
    mx,my = pygame.mouse.get_pos()
    screen.fill((0,111,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.MOUSEBUTTONUP:
        click = False
        print("no")
    if event.type == pygame.MOUSEBUTTONDOWN or click == True:
        click = True
        tower(mx,my)
        print("yes")
    pygame.display.flip()
    clock.tick(FPS)


