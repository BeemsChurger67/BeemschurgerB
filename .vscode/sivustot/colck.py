import pygame
from pygame.locals import *

pygame.init()

# Set screen dimensions
screen_width = 700
screen_height = 700

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the character
character_width = 50
character_height = 50
character_x = screen_width // 2 - character_width // 2
character_y = screen_height // 2 - character_height // 2

# Set up the font
font = pygame.font.Font(None, 36)

running = True
text_on_screen = ""

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                text_on_screen = "burger"
        if event.type == KEYUP:
            if not event.key == K_SPACE:
                text_on_screen = ""


    keys = pygame.key.get_pressed()
    if keys[K_w]:
        character_y -= 1
    if keys[K_s]:
        character_y += 1
    if keys[K_a]:
        character_x -= 1
    if keys[K_d]:
        character_x += 1

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), (character_x, character_y, character_width, character_height))

    text_surface = font.render(text_on_screen, True, (0, 0, 0))
    screen.blit(text_surface, (character_x - 10,character_y - 25))

    pygame.display.update()

pygame.quit()