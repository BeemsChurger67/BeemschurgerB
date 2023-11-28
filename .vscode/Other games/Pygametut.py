#Good game
import turtle
import random
import time
import sys
import pygame
pygame.init()
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500

screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
x = 250;
y = 250;
player = pygame.Rect((x, y, 25, 25))

run = True

FPS = 60

while run == True:

    screen.fill((0,0,0))

    pygame.draw.rect(screen,(111,111,111),player)
    player.move_ip(0 - x,0 - y)
    key = pygame.key.get_pressed()
    if(x > 0):
        if key[pygame.K_a] == True:
            x -= 5
    if(x < 475):
        if key[pygame.K_d] == True:
            x += 5
    if(y > 0):
        if key[pygame.K_w] == True:
            y -= 5
    if(y < 475):
        if key[pygame.K_s] == True:
            y += 5
    
    player.move_ip(x,y)
    print("x =",x,"y =",0 - y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(FPS)
pygame.quit()