import pygame
import math
import random

pygame.init()
pygame.font.init()
font0 = pygame.font.Font(None, 90)
font1 = pygame.font.Font(None, 30)
font2 = pygame.font.Font(None, 25)
font3 = pygame.font.Font(None, 20)
Rarities = [
    "None",
    "Common-",
    "Common",
    "Common+",
    "Common++",
    "Uncommon-",
    "Uncommon",
    "Uncommon+",
    "Uncommon++",
    "Beginner-",
    "Beginner",
    "Beginner+",
    "Beginner++",
    "Rare-",
    "Rare",
    "Rare+",
    "Rare++",
    "Epic-",
    "Epic",
    "Epic+",
    "Epic++",
    "Legendary-",
    "Legendary",
    "Legendary+",
    "Legendary++",
    "Mythical-",
    "Mythical",
    "Mythical+",
    "Mythical++",
    "Divine-",
    "Divine",
    "Divine+",
    "Divine++",
    "Ultimate-",
    "Ultimate",
    "Ultimate+",
    "Ultimate++",
    "Superior-",
    "Superior",
    "Superior+",
    "Superior++",
    "Exalted-",
    "Exalted",
    "Exalted+",
    "Exalted++",
    "Apex-",
    "Apex",
    "Apex+",
    "Apex++",
    "Primordial-",
    "Primordial",
    "Primordial+",
    "Primordial++",
    "Master-",
    "Master",
    "Master+",
    "Master++",
    "Transcendent-",
    "Transcendent",
    "Transcendent+",
    "Transcendent++",
    "Ethereal-",
    "Ethereal",
    "Ethereal+",
    "Ethereal++",
    "Celestial-",
    "Celestial",
    "Celestial+",
    "Celestial++",
    "Mythic-",
    "Mythic",
    "Mythic+",
    "Mythic++",
    "Finite-",
    "Finite",
    "Finite+",
    "Finite++",
    "Infinite-",
    "Infinite",
    "Infinite+",
    "Infinite++",
    "Legendary God-",
    "Legendary God",
    "Legendary God+",
    "Legendary God++",
    "Ascended-",
    "Ascended",
    "Ascended+",
    "Ascended++",
    "Supreme-",
    "Supreme",
    "Supreme+",
    "Supreme++",
    "Mythical God-",
    "Mythical God",
    "Mythical God+",
    "Mythical God++",
    "Divine Entity-",
    "Divine Entity",
    "Divine Entity+",
    "Divine Entity++",
    "Emperor of Divinity-",
    "Emperor of Divinity",
    "Emperor of Divinity+",
    "Emperor of Divinity++",
    "Eternal-",
    "Eternal",
    "Eternal+",
    "Eternal++",
    "Omnipotent-",
    "Omnipotent",
    "Omnipotent+",
    "Omnipotent++",
    "Demonicallypotent-",
    "Demonicallypotent",
    "Demonicallypotent+",
    "Demonicallypotent++",
    "Miracle of Miracles-",
    "Miracle of Miracles",
    "Miracle of Miracles+",
    "Miracle of Miracles++",
]
clock = pygame.time.Clock()
Rarity = 0
Luck = 4
highestrarity = 0
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
def luckloop():
    global I, Rarity, Luck

    while True:
        if I >= len(Rarities):
            I = len(Rarities) - 1

        if random.randint(1, round(Luck / 3 + 1)) == 1:
            Rarity = I
            I = 0
            break
        else:
            I += 1
I = 0
while running:
    screen.fill((75, 75, 75))
    mx, my = pygame.mouse.get_pos()
    screen.blit(font1.render(f"Rarity: [{Rarities[Rarity]}]", True, (0, 0, 0)), (1, 0))
    screen.blit(font1.render(f"RNG: [{Rarity}]", True, (0, 0, 0)), (1, 20))
    screen.blit(font1.render(f"highest RNG: [{highestrarity}]", True, (0, 0, 0)), (1, 40))
    screen.blit(font1.render(f"Luck: [{Luck}]", True, (0, 0, 0)), (1, 60))
    if Rarity > highestrarity:
        highestrarity = Rarity
    Raritybutton = pygame.draw.rect(screen, (100, 100, 100), (250, 400, 200, 100),border_radius=15)
    pygame.draw.rect(screen, (0, 0, 0), (250, 400, 200, 100), width=7,border_radius=15)
    screen.blit(font0.render(f"Roll", True, (0, 0, 0)), (Raritybutton.x + Raritybutton.width / 2 - 60, Raritybutton.y + Raritybutton.height / 2 - 30))

    Luckbutton = pygame.draw.rect(screen, (100, 100, 100), (100, 500, 200, 100),border_radius=15)
    pygame.draw.rect(screen, (0, 0, 0), (100, 500, 200, 100), width=7,border_radius=15)
    screen.blit(font0.render(f"Luck", True, (0, 0, 0)), (Luckbutton.x + Luckbutton.width / 2 - 60, Luckbutton.y + Luckbutton.height / 2 - 30))
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
                luckloop()
            if Luckbutton.collidepoint(mx, my):
                Luck += 1
                    
    pygame.display.flip()

pygame.quit()
exit()