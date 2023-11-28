import pygame
import os
import math
import time
import random
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800,700))
pygame.display.set_caption("Ruoho Game 'real'")
load = pygame.image.load
scale = pygame.transform.scale
FPS = 60
clock = pygame.time.Clock()
directory = os.getcwd()
directory = os.path.join(directory, "images")
print(directory)
ruohotitle = load(os.path.join(directory, "ruoholistic.png"))
ruohotitle = scale(ruohotitle,(500,500))
methampheta = load(os.path.join(directory, "metamfetamiini.png"))
methampheta = scale(methampheta,(50,50))
player = load(os.path.join(directory, "player.png"))
player = scale(player,(60,60))
pygame.display.set_icon(ruohotitle)
metham = 0
correction_angle = 270
multiplier = 1
X = 0
Y = 0
player_pos = [100, 100]  # Replace with your own player position
methaX = random.randint(150,800)
methaY = random.randint(0,700)
player_pos = pygame.math.Vector2(400, 300)
speed = 4
def methamphetamine():
    global metham, methaX, methaY
    methamphetamined = screen.blit(methampheta,(methaX,methaY))
    if methamphetamined.collidepoint(player_pos):
        methaX = random.randint(150,700)
        methaY = random.randint(0,60)
        metham += 1 * multiplier
clicking = 0
running = True
while running:
    screen.fill((0,111,0))
    keys = pygame.key.get_pressed()
    pygame.draw.rect(screen,(0,0,0),(0,0,150,700))
    pygame.draw.rect(screen,(100,100,100),(0,0,140,700))
    screen.blit(pygame.font.Font(None, 34).render("Ruoho game", True, (0,0,0)), (0, 0))
    screen.blit(pygame.font.Font(None, 20).render(f"methamphetamine: {metham}", True, (0,0,0)), (0, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # show methamphetamine
    methamphetamine()
    # Move the player based on key inputs
    if keys[pygame.K_w]:
        player_pos.y -= speed
    if keys[pygame.K_s]:
        player_pos.y += speed
    if keys[pygame.K_a]:
        player_pos.x -= speed
    if keys[pygame.K_d]:
        player_pos.x += speed
    # Calculate the angle between the player and the mouse
    mouse_pos = pygame.mouse.get_pos()
    dx = mouse_pos[0] - player_pos.x
    dy = mouse_pos[1] - player_pos.y
    angle = math.degrees(math.atan2(-dy, dx))

    # Rotate the player image
    rotated_player_image = pygame.transform.rotate(player, angle - 90)
    rotated_player_rect = rotated_player_image.get_rect()

    multiplierupgrade = pygame.draw.rect(screen,(0,0,0),(0,300,150,75))
    pygame.draw.rect(screen,(0,0,200),(0,307.5,140,60))
        

    # Blit the rotated player image onto the screen
    screen.blit(rotated_player_image, (player_pos.x - rotated_player_rect.width / 2, player_pos.y - rotated_player_rect.height / 2))

    # Update the display
    clock.tick(FPS)
    pygame.display.flip()
