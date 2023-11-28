import pygame
import random
import math

pygame.init()
pygame.font.init()

FPS = 100
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
pygame.display.set_caption("Survival game")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((0, 100, 0))
font1 = pygame.font.SysFont("comicsansms", 15)
font2 = pygame.font.SysFont("comicsansms", 20)

MouseRect = pygame.Rect((0, 0, 1, 1))
correction_angle = 90

load = pygame.image.load
scale = pygame.transform.scale

player = scale(load("assets/player.png"), (60, 60))
tree = scale(load("assets/tree.png"), (150, 200))
hotbar = scale(load("assets/Hotbar.png"), (750, 75))
inventory = scale(load("assets/Inventory.png"), (500, 500))
craftbgicon = scale(load("assets/craftbg.png"), (48, 48))
woodicon = scale(load("assets/woodicon.png"), (48, 48))
stickicon = scale(load("assets/stickicon.png"), (48, 48))
woodenaxeicon = scale(load("assets/woodenaxeicon.png"), (48, 48))
swordicon = scale(load("assets/placeholdersword.png"), (48, 48))
swordattack = scale(load("assets/placeholderattacksword.png"), (60, 240))
zombie1 = scale(load("assets/zombie1.png"), (60, 60))

NumberOfTrees = 100

def treeplace(x, y, id, hp, lv):
    global wood
    screen.blit(tree, (x - playerx, y - playery))
    
    hover = False
    
    if x - playerx < mousex < x - playerx + 150 and y - playery < mousey < y - playery + 200:
        hover = True
        
        if mouse_click:
            treeHp[id] = round(treeHp[id] - DMG[1], 1)
            if treeHp[id] + (treeLv[id] * 5) < 0.1:
                treeIdx[id] = random.randint(-2000, 2000)
                treeIdy[id] = random.randint(-2000, 2000)
                treeHp[id] = random.randint(20 + lv * 5, 35 + lv * 5)
                wood += random.randint(6 + (lv * 2), 10 + (lv * 2))
                treeLv[id] += 1

    if hover:
        iddis = font2.render(f"ID: {id}", True, (255, 255, 255))
        screen.blit(iddis, (x - playerx + 40, y - playery - 20))
        hpdis = font2.render(f"HP: {hp + (lv * 5)}", True, (255, 255, 255))
        screen.blit(hpdis, (x - playerx + 40, y - playery - 40))
        lvdis = font2.render(f"Lv: {lv}", True, (255, 255, 255))
        screen.blit(lvdis, (x - playerx + 40, y - playery - 60))
def attack(damage, sprite, speed):
    global angle2, mx2, my2
    sword_pos = screen.get_rect().center
    sword_rect = swordattack.get_rect(center=sword_pos)
    dx, dy = mx2 - sword_rect.centerx, my2 - sword_rect.centery
    angle = math.degrees(math.atan2(-dy, dx)) - correction_angle + angle2
    rot_image = pygame.transform.rotate(swordattack, angle)
    rot_image_rect = rot_image.get_rect(center=sword_rect.center)
    screen.blit(rot_image, rot_image_rect.topleft)
    if not angle2 < -55: 
        angle2 -= 4
    else:
        angle2 = 55
        mx2, my2 = pygame.mouse.get_pos()
playerx = 0
playery = 0
run = True
Speed = 3.5

treeIdx = []
treeIdy = []
treeHp = []
treeLv = []

wood = 1110
stick = 1110
stone = 1111

enemyidx = []
enemyidy = []
enemyhp = []

DMG = [0.1, 0.1]
sword = [0, 0, 0]
axepower = 0

for i in range(NumberOfTrees):
    treeIdx.append(random.randint(-2000, 2000))
    treeIdy.append(random.randint(-2000, 2000))
    treeLv.append(random.randint(1, 2))
    treeHp.append(random.randint(20 + treeLv[i] * 5, 35 + treeLv[i] * 5))

debug_status = False
clock = pygame.time.Clock()
mouse_click = False
toggle_var = False

angle2 = 55
mx2, my2 = pygame.mouse.get_pos()

while run:
    screen.fill((0, 100, 0))
    clock.tick(FPS)
    fpsgiver = int(clock.get_fps())
    mousex, mousey = pygame.mouse.get_pos()
    key = pygame.key.get_pressed()
    if -1999 < playerx < 1999:
        if key[pygame.K_a]:
            playerx -= Speed
        if key[pygame.K_d]:
            playerx += Speed
    if -1999 < playery < 1999:
        if key[pygame.K_w]:
            playery -= Speed
        if key[pygame.K_s]:
            playery += Speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_click = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_click = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                toggle_var = not toggle_var

    for i in range(NumberOfTrees):
        treeplace(treeIdx[i], treeIdy[i], i, treeHp[i], treeLv[i])

    screen.blit(hotbar, (125, 625))

    player_pos = screen.get_rect().center
    player_rect = player.get_rect(center=player_pos)
    mx, my = pygame.mouse.get_pos()
    dx, dy = mx - player_rect.centerx, my - player_rect.centery
    angle = math.degrees(math.atan2(-dy, dx)) - correction_angle
    rot_image = pygame.transform.rotate(player, angle)
    rot_image_rect = rot_image.get_rect(center=player_rect.center)
    screen.blit(rot_image, rot_image_rect.topleft)

    if not mouse_click:
        clicked = False
        mx2, my2 = pygame.mouse.get_pos()
        angle2 = 55
    if mouse_click:
        attack(5, 1, 2)

    fpsdisplay = font1.render(f"FPS: {fpsgiver}", True, (255, 255, 255))
    screen.blit(fpsdisplay, (2, 0))

    if toggle_var:
        screen.blit(inventory, (100, 100))
        if wood > 0:
            screen.blit(woodicon, (107, 107))
            woodamount = font2.render(f"x{wood}", True, (255, 255, 255))
            screen.blit(woodamount, (107, 130))
        if wood > 1:
            stickcraft = screen.blit(craftbgicon, (620, 100))
            screen.blit(stickicon, (620, 100))
            if stickcraft.x < mousex < stickcraft.x + 48 and stickcraft.y < mousey < stickcraft.y + 48:
                screen.blit(font1.render(f"2wood", True, (255, 255, 255)), (620, 96))
                if mouse_click:
                    if not clicked:
                        wood -= 2
                        stick += 4
                        clicked = True
        if wood > 4 and stick > 1:
            swordcraft = screen.blit(craftbgicon, (670, 100))
            screen.blit(swordicon, (670, 100))
            if swordcraft.x < mousex < swordcraft.x + 48 and swordcraft.y < mousey < swordcraft.y + 48:
                screen.blit(font1.render(f"5wood", True, (255, 255, 255)), (670, 96))
                screen.blit(font1.render(f"2sticks", True, (255, 255, 255)), (670, 106))
                if mouse_click:
                    if not clicked:
                        if sword[0] == 0:
                            wood -= 5
                            stick -= 2
                        sword[0] = 1
                        clicked = True
        if stick > 0:
            screen.blit(stickicon, (107 + (48 * 1) + (7 * 1), 107))
            stickamount = font2.render(f"x{stick}", True, (255, 255, 255))
            screen.blit(stickamount, (107 + (48 * 1) + (7 * 1), 130))

    playerpos = font1.render(f"Player Position: ({playerx}, {0 - playery})", True, (255, 255, 255))
    screen.blit(playerpos, (2, 14))
    pygame.draw.rect(screen, (0, 100, 0), MouseRect)
    mousex, mousey = pygame.mouse.get_pos()
    MouseRect.x = mousex
    MouseRect.y = mousey
    pygame.display.flip()