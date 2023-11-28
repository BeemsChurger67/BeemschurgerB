import pygame
import random
import math
import pygame.font
from SavedLevels import SavedLevel
ButtonID = []
pygame.font.init()
pygame.init()
font = pygame.font.Font(None, 36)
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
FPS = 120
Sublevel = 1
health = 100000
gen = []
Rgen = SavedLevel
gen = Rgen
print(Rgen)
mapSize = int(screen.get_width() / 50)
player = pygame.image.load("assets/player.png")
player = pygame.transform.scale(player, (40, 40))
smile = pygame.image.load("assets/bigsmile.png")
smile = pygame.transform.scale(smile, (40, 40))
smiler = pygame.image.load("assets/smilerpm.png")
smiler = pygame.transform.scale(smiler, (50, 50))
smilerwall = pygame.image.load("assets/bigsmile.png")
smilerwall = pygame.transform.scale(smilerwall, (50, 50))
player_rect = player.get_rect(center=(300, 300))
pygame.display.set_caption(f"PM 6:06 | Sublevel: {Sublevel}")
pygame.display.set_icon(smile)
buttonPressed = False
start = True
X = 0
Y = 0
enemyX = []
enemyY = []
start = True
enemyXS = []
enemyYS = []

def distance(point1, point2):
    x1, y1 = point1[0] + point1[2] / 2, point1[1] + point1[3] / 2
    x2, y2 = point2[0] + point2[2] / 2, point2[1] + point2[3] / 2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


c = 0
smilersGenr = False
newG = 0
def GenerateNmove(MoveX, MoveY, emoveX, emoveY,id):
    global X, Y, start, buttonPressed, holding, gen, Sublevel, smilersGenr, D, health, newG, enemyX, enemyY
    c = 0
    walls = None
    for A in range(mapSize):
        for B in range(mapSize):
            x = A * 50
            y = B * 50
            if gen[c] == 1:
                walls = pygame.draw.rect(screen, (255, 255, 255), (x, y, 50, 50))
                xg, yg = A, B
                if pygame.Rect(x, y, 50, 50).colliderect(pygame.Rect(X + MoveX, Y + MoveY, 40 + MoveX, 40 + MoveY)):
                    X -= MoveX / 2
                    Y -= MoveY / 2
            if gen[c] == 2:
                walls = pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
                xg, yg = A, B
                if pygame.Rect(x, y, 50, 50).colliderect(pygame.Rect(X + MoveX, Y + MoveY, 40 + MoveX, 40 + MoveY)):
                    X -= MoveX / 2
                    Y -= MoveY / 2
                if buttonPressed == True:
                    gen[c] = 0
            if gen[c] == 3:
                walls = pygame.draw.circle(screen, (255, 0, 0), (x + 25, y + 25), 15)
                if distance(pygame.Rect(x + 25, y + 25, 30, 30),
                            pygame.Rect(X, Y, 40, 40)) < 70:
                    if pygame.Rect(x + 7.5, y + 7.5, 30, 30).collidepoint(Mouse):
                        if holding:
                            buttonPressed = True
            if gen[c] == 4:
                if start:
                    X, Y = x, y
                    start = False
                    buttonPressed = False
            if gen[c] == 5 or health < 0:
                walls = pygame.draw.rect(screen, (50, 50, 50), (x, y, 50, 50))
                walls = pygame.draw.rect(screen, (50, 0, 0), (x, y, 50, 40))
                if health < 0:
                    Sublevel -= 1
                    health == 100
                    break
                if pygame.Rect(x, y, 50, 50).colliderect(pygame.Rect(X, Y, 40, 40)):
                    health = 0
                    smilersGenr = False
                    newG = 1
                    health = 100
                    buttonPressed = False
                    start = True
                    Sublevel += 1
                    gen = SavedLevel
                    print(SavedLevel)
                    if not id == None:
                        print(D)
                        print(len(enemyY))
                        enemyX = enemyXS
                        enemyY = enemyYS
                        enemyXS.clear()
                        enemyYS.clear()
                    newG = 0
            if gen[c] == 6:
                if smilersGenr == False:
                    enemyX.append(x)
                    enemyY.append(y)
                    enemyXS.append(x)
                    enemyYS.append(y)
                    print(enemyX)
                    print("next")
                    print(enemyY)
                    
            c += 1
    X += MoveX / 2
    Y += MoveY / 2
    if id == None:
        pass
    elif smilersGenr == True:
        enemyX[int(id)] += emoveX
        enemyY[int(id)] += emoveY
    smilersGenr = True


holding = None
timer = pygame.time.Clock()
time_elapsed = 0
update_interval = 1000
def rotate_player_towards_mouse(player_pos):
    mouse_pos = pygame.mouse.get_pos()
    dx = mouse_pos[0] - player_pos[0]
    dy = mouse_pos[1] - player_pos[1]
    angle = math.degrees(math.atan2(dy, dx))
    rotated_player_image = pygame.transform.rotate(player, -angle - 90)
    rotated_player_rect = rotated_player_image.get_rect(center=player_pos)
    return rotated_player_image, rotated_player_rect


running = True
while running:
    Rgen = SavedLevel
    Mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            holding = True

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            holding = False

    pygame.display.set_caption(f"PM 6:06 | Sublevel: {Sublevel}")
    screen.fill((0, 0, 0))
    text = font.render(f"Health: {health}/100", True, (255, 255, 255))
    screen.blit(text, (10, 10))
    for D in range(len(enemyX)):
        screen.blit(smiler, (enemyX[D], enemyY[D]))
        if distance((enemyX[D], enemyY[D], 50, 50), (X, Y, 40, 40)) < 250:
            if X > enemyX[D]:
                GenerateNmove(0, 0, 0.5 * Sublevel / 3 + 1, 0,D)
            else:
                GenerateNmove(0, 0, -0.5 * Sublevel / 3 - 1, 0,D)
            print(D)
            print(len(enemyY))
            if Y > enemyY[D]:
                GenerateNmove(0, 0, 0, 0.5 * Sublevel / 3 + 1,D)
            else:
                GenerateNmove(0, 0, 0, -0.5 * Sublevel / 3 - 1,D)
            if distance((enemyX[D], enemyY[D], 50, 50), (X, Y, 40, 40)) < 20:
                health -= 1
    time_delta = timer.tick()
    time_elapsed += time_delta
    if health < 99:
        if time_elapsed >= update_interval:
            health += 1
            time_elapsed = 0

    key = pygame.key.get_pressed()
    GenerateNmove(0, 0, 0, 0,None)
    if key[pygame.K_w]:
        GenerateNmove(0, -5, 0, 0,None)
    if key[pygame.K_a]:
        GenerateNmove(-5, 0, 0, 0,None)
    if key[pygame.K_d]:
        GenerateNmove(5, 0, 0, 0,None)
    if key[pygame.K_s]:
        GenerateNmove(0, 5, 0, 0,None)
    rotated_player, rotated_player_rect = rotate_player_towards_mouse((X + 20, Y + 20))
    screen.blit(rotated_player, rotated_player_rect)
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()