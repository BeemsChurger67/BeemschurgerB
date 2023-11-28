import pygame
import math
import random
from Raritieslist import Rarities

pygame.init()
pygame.font.init()
font0 = pygame.font.Font(None, 90)
font1 = pygame.font.Font(None, 30)
font2 = pygame.font.Font(None, 25)
font3 = pygame.font.Font(None, 20)
clock = pygame.time.Clock()
Rarity = 0
Luck = 4
highestrarity = 0
cash = 10000000
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
def luckloop():
    global I, Rarity, Luck, cash

    while True:
        if I >= len(Rarities):
            I = len(Rarities) - 1

        if random.randint(0, Luck) == round(Luck / 5) + 1:
            print(I)
            Rarity = I
            cash += Rarity
            I = 0
            break
        else:
            I += 1
def betterluckloop():
    global I, Rarity, Luck, cash
    Rarity = random.randint(Luck - 4, Luck + 4)
    if random.randint(0, 100) == 50:
        Rarity += random.randint(3,8)
        if random.randint(0, 100) == 50:
            Rarity += random.randint(3,8)
            if random.randint(0, 100) == 50:
                Rarity += random.randint(3,8)
    if random.randint(0, 100) == 50:
        Rarity += random.randint(3,8)
        if random.randint(0, 100) == 50:
            Rarity += random.randint(3,8)
            if random.randint(0, 100) == 50:
                Rarity += random.randint(3,8)
        



I = 0
while running:
    screen.fill((75, 75, 75))
    mx, my = pygame.mouse.get_pos()
    screen.blit(font1.render(f"cash: [{cash}]", True, (0, 0, 0)), (1, 0))
    screen.blit(font1.render(f"Rarity: [{Rarities[Rarity]}]", True, (0, 0, 0)), (1, 20))
    screen.blit(font1.render(f"RNG: [{Rarity}]", True, (0, 0, 0)), (1, 40))
    screen.blit(font1.render(f"highest RNG: [{highestrarity}],[{Rarities[highestrarity]}]", True, (0, 0, 0)), (1, 60))
    screen.blit(font1.render(f"Luck: [{Luck}]", True, (0, 0, 0)), (1, 80))
    if Rarity > highestrarity:
        highestrarity = Rarity
    Raritybutton = pygame.draw.rect(screen, (100, 100, 100), (250, 400, 200, 100),border_radius=15)
    pygame.draw.rect(screen, (0, 0, 0), (250, 400, 200, 100), width=7,border_radius=15)
    screen.blit(font0.render(f"Roll", True, (0, 0, 0)), (Raritybutton.x + Raritybutton.width / 2 - 60, Raritybutton.y + Raritybutton.height / 2 - 30))

    Luckbutton = pygame.draw.rect(screen, (100, 100, 100), (100, 520, 200, 100),border_radius=15)
    pygame.draw.rect(screen, (0, 0, 0), (100, 520, 200, 100), width=7,border_radius=15)
    screen.blit(font0.render(f"Luck", True, (0, 0, 0)), (Luckbutton.x + Luckbutton.width / 2 - 60, Luckbutton.y + Luckbutton.height / 2 - 30))
    screen.blit(font1.render(f"Costs {(Luck * 10) - 30}", True, (0, 0, 0)), (Luckbutton.x + Luckbutton.width / 2 - 37, Luckbutton.y + Luckbutton.height - 95))
    clock = pygame.time.Clock()
    # Calculate the FPS (thanks chatgpt)
    fps = int(clock.get_fps())
    # Update the window's caption with the FPS value (thanks chatgpt)
    pygame.display.set_caption(f"Button Simulator | FPS: {fps}")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if Raritybutton.collidepoint(mx, my):
                # Action to perform when Raritybutton is clicked
                I = 0
                betterluckloop()
            if Luckbutton.collidepoint(mx, my):
                if cash >= (Luck * 10) - 40:
                    Luck += 1
                    cash -= (Luck * 10) - 50
                    
    pygame.display.flip()

pygame.quit()
exit()