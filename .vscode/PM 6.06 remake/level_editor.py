import pygame
import random

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
FPS = 6000
Sublevel = 0
gen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 6, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 1, 0, 0, 0, 0, 1, 3, 1, 0, 1, 4, 1, 1, 0, 1, 1, 1, 6, 6, 6, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 2, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
SavedLevel = []
mapSize = int(screen.get_height() / 50)
player_image = pygame.image.load("assets/player.png")
player_image = pygame.transform.scale(player_image, (40, 40))
pygame.display.set_caption(f"Sublevel: Level Editor")
holding = False
X = 0
Y = 0
ButtonID = []
selected_mapping = 0
if len(gen) == 0:
    for _ in range(mapSize):
        for _ in range(mapSize):
            gen.append(0)

print(len(gen))
c = 0

def distance(rect1, rect2):
    x1, y1 = rect1.center
    x2, y2 = rect2.center
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def Generate():
    global c, Mouse, holding
    c = 0
    walls = None   
    for A in range(mapSize):
        for B in range(mapSize):
            x = A * 50  
            y = B * 50  
            if gen[c] == 0:
                walls = pygame.draw.rect(screen, (0, 0, 0), (x, y,50,50),width=15)
            if gen[c] == 1:
                walls = pygame.draw.rect(screen, (255, 255, 255), (x, y, 50, 50))
            if gen[c] == 2:
                walls = pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
            if gen[c] == 3:
                walls = pygame.draw.circle(screen, (255, 0, 0), (x + 25, y + 25), 15)
                if pygame.Rect(x + 7.5, y + 7.5, 30,30).collidepoint(Mouse):
                    if holding:
                        print("chicken dawg")
            if gen[c] == 4:
                walls = screen.blit(player_image,(x,y))
            if gen[c] == 5:
                walls = pygame.draw.rect(screen, (50,50,50), (x, y, 50, 50))
                walls = pygame.draw.rect(screen, (50,0,0), (x, y, 50, 40))
            if gen[c] == 6:
                walls = pygame.draw.rect(screen,(255,0,0),(x,y,50,50))
                walls = pygame.draw.rect(screen,(200,0,0),(x + 12.5,y + 12.5,25,25))


            
            if walls and walls.collidepoint(pygame.mouse.get_pos()):
                if holding:
                    gen[c] = selected_mapping
                    if gen[c] == 3:
                        ButtonID.append(1)


            c += 1

def PlayermovementCollision(MoveX, MoveY):
    global X,Y
    X += MoveX
    Y += MoveY

running = True
while running:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("SavedLevel =",gen)
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            holding = True
            print("Left click hold initiated!")
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            holding = False
            print("Left click hold ended!")
    
    Mouse = pygame.mouse.get_pos()

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        PlayermovementCollision(0,-5)
    if key[pygame.K_a]:
        PlayermovementCollision(-5,0)
    if key[pygame.K_d]:
        PlayermovementCollision(5,0)
    if key[pygame.K_s]:
        PlayermovementCollision(0,5)
    screen.fill((25,25,25))
    Generate()

    if selected_mapping == 0:
        pygame.draw.rect(screen, (0,0,0),(mouse[0],mouse[1],50, 50))
    if selected_mapping == 1:
        pygame.draw.rect(screen, (255, 255, 255),(mouse[0],mouse[1],50, 50))
    if selected_mapping == 2:
        walls = pygame.draw.rect(screen, (255, 0, 0), (mouse[0],mouse[1], 50, 50))
    if selected_mapping == 3:
        walls = pygame.draw.circle(screen, (255, 0, 0), (mouse[0],mouse[1]), 15)
    if selected_mapping == 4:
        screen.blit(player_image, (mouse[0],mouse[1]))
    if selected_mapping == 5:
        walls = pygame.draw.rect(screen, (50,50,50), (mouse[0],mouse[1], 50, 40))
        walls = pygame.draw.rect(screen, (50,0,0), (mouse[0],mouse[1], 50, 40))
    if selected_mapping == 6:
        smiler = pygame.draw.rect(screen,(255,0,0),(mouse[0],mouse[1],40,40))
        smiler = pygame.draw.rect(screen,(200,0,0),(mouse[0] + 10,mouse[1] + 10,20,20))

    if key[pygame.K_1]:
        selected_mapping = 0
    if key[pygame.K_2]:
        selected_mapping = 1
    if key[pygame.K_3]:
        selected_mapping = 2
    if key[pygame.K_4]:
        selected_mapping = 3
    if key[pygame.K_5]:
        selected_mapping = 4
    if key[pygame.K_6]:
        selected_mapping = 5
    if key[pygame.K_7]:
        selected_mapping = 6

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()