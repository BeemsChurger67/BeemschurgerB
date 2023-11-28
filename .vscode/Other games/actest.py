import pygame, sys
from pygame.locals import *

pygame.init()

screen_width = 500
screen_height = 300

pelialue = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

FPS = 144
FramePerSec = pygame.time.Clock()
mouse = pygame.mouse.get_pos()
player = pygame.Rect(mouse[0],mouse[1],50, 50)

enemy = pygame.Rect(250,150, 30, 30)
enemy_speed = [1,1]
max_speed = 256
player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image,(50,50))
enemy_image = pygame.image.load("goofyenemy.png")
enemy_image = pygame.transform.scale(enemy_image,(50,50))
explosion = pygame.image.load("burgershack.png")
explosion.convert()
while True:
  
  for event in pygame.event.get():
    if event.type == MOUSEMOTION:
      mouse = event.pos
      player = pygame.Rect(mouse[0],mouse[1],30, 30)
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  pelialue.fill("#00cccc")
  pygame.draw.ellipse(pelialue, "yellow", (30, 30, 80, 80))
  enemy.move_ip(enemy_speed)
  if enemy.right > screen_width:
    if abs(enemy_speed[0]) < max_speed:
      enemy_speed[0] *= -1.1
    else:
        enemy_speed[0] *= -1.1
  if enemy.left < 0:
    if abs(enemy_speed[0]) < max_speed:
      enemy_speed[0] *= -1.1
    else:
      enemy_speed[0] *= -1.1
  if enemy.bottom > screen_height:
    if abs(enemy_speed[0]) < max_speed:
      enemy_speed[1] *= -1.1
    else:
      enemy_speed[1] *= -1.1
  if enemy.top < 0:
    if abs(enemy_speed[0]) < max_speed:
      enemy_speed[1] *= -1.1
    else:
      enemy_speed[1] *= -1.1
  pygame.draw.rect(pelialue,"#b38600",(0,250,screen_width,50))
  pelialue.blit(enemy_image, enemy)
  

  if pygame.Rect.colliderect(player, enemy) == True:
    print("osuma")
    explosion = pygame.transform.scale(explosion,(150,100))
    player.move_ip(-75,-50)
    pelialue.blit(explosion,player)
    pygame.display.update()
    break
  
    
  else:
    pelialue.blit(player_image, player)
  
  
  
  
  
  
  pygame.display.update()
  FramePerSec.tick(FPS)