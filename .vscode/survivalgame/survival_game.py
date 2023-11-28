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
player = load("assets/player.png")
player = scale(player, (60, 60))
tree = load("assets/tree.png")
tree = scale(tree, (150, 200))
hotbar = load("assets/Hotbar.png")
hotbar = scale(hotbar, (750, 75))
inventory = load("assets/Inventory.png")
inventory = scale(inventory, (500, 500))
craftbgicon = load("assets/craftbg.png")
craftbgicon = scale(craftbgicon, (48, 48))
woodicon = load("assets/woodicon.png")
woodicon = scale(woodicon, (48, 48))
stickicon = load("assets/stickicon.png")
stickicon = scale(stickicon, (48, 48))
woodenaxeicon = load("assets/woodenaxeicon.png")
woodenaxeicon = scale(woodenaxeicon, (48, 48))
swordicon = load("assets/placeholdersword.png")
swordicon = scale(swordicon, (48, 48))
swordiconbig = scale(swordicon, (62, 62))
swordattack = load("assets/placeholderattacksword.png")
swordattack = scale(swordattack, (60, 240))
zombie1 = load("assets/zombie1.png")
zombie1 = scale(zombie1, (60, 60))

def treeplace(x, y, id, hp, lv):
    global wood
    screen.blit(tree, (x - playerx, y - playery))
    if mousex > x - playerx and mousex < (x - playerx + 150):
        if mousey > y - playery and mousey < (y - playery + 200):
            if mouse_click == True:
                treeHp[id] = round(treeHp[id] - DMG[1], 1)
            if treeHp[id] + (treeLv[id] * 5) < 0.1:
                treeIdx[id] = random.randint(-2000, 2000)
                treeIdy[id] = random.randint(-2000, 2000)
                treeHp[id] = random.randint(20 + lv * 5, 35 + lv * 5)
                wood += random.randint(6 + (lv * 2),10 + (lv * 2))
                treeLv[id] += 1
            
            iddis = font2.render(f"ID: {id}", True, (255, 255, 255))
            screen.blit(iddis, (x - playerx + 40, y - playery - 20))
            hpdis = font2.render(f"HP: {hp + (lv * 5)}", True, (255, 255, 255))
            screen.blit(hpdis, (x - playerx + 40, y - playery - 40))
            lvdis = font2.render(f"Lv: {lv}", True, (255, 255, 255))
            screen.blit(lvdis, (x - playerx + 40, y - playery - 60))
def attack(damage,sprite,speed):
    global angle2, mx2, my2, tog
    sword_pos = screen.get_rect().center
    sword_rect = swordattack.get_rect(center=sword_pos)
    dx, dy = mx2 - sword_rect.centerx, my2 - sword_rect.centery
    angle = math.degrees(math.atan2(-dy, dx)) - correction_angle + angle2
    rot_image = pygame.transform.rotate(swordattack, angle)
    rot_image_rect = rot_image.get_rect(center=sword_rect.center)
    screen.blit(rot_image, rot_image_rect.topleft)
    if not angle2 < -55: 
        angle2 -= 4
        tog = 1
    else:
        angle2 = 55
        tog = 0
        mx2, my2 = pygame.mouse.get_pos()
RecipeAm = 2

playerx = random.randint(-2000, 2000)
playery = random.randint(-2000, 2000)
run = True
Speed = 3.5
treeIdx = []
treeIdy = []
treeHp = []
treeLv = []
wood = 1110
stick = 1110
stone = 1111
NumberOfTrees = 100
Time = 0
Daynumber = 0
enemyidx = []
enemyidy = []
enemyhp = []

DMG = [0,0]
sword = 0
axepower = 0.2
sworddamage = 0
for i in range(NumberOfTrees):
    treeIdx.append(random.randint(-2000, 2000))
    treeIdy.append(random.randint(-2000, 2000))
    treeLv.append(random.randint(1,4))
    treeHp.append(random.randint(20 + treeLv[i] * 5, 35 + treeLv[i] * 5))

def Show_Recipe(Image,material,materialAmount,materialGive,materialGiveAmount,x,y,req):
    global mousex, mousey, clicked, mouse_click, wood, stone, stick
    screen.blit(craftbgicon,(x,y))
    screen.blit(Image,(620,100))
    if mousex > x and mousex < x + 48:
        if mousey > y and mousey < y + 48:
            screen.blit(font1.render(f"{req}", True, (255, 255, 255)),(x,y - 4))
            if mouse_click == True:
                if clicked == False:
                    print("yes")
                    if material == 0:
                        wood -= materialAmount
                    if material == 1:
                        stick -= materialAmount
                    if material == 2:
                        stone -= materialAmount
                    if material == 3:
                        material -= materialAmount
                    if material == 4:
                        material -= materialAmount
                    if material == 5:
                        material -= materialAmount



                    if materialGive == 0:
                        wood += materialGiveAmount
                    if materialGive == 1:
                        stick += materialGiveAmount
                    if materialGive == 2:
                        stone += materialGiveAmount
                    if materialGive == 3:
                        materialGive += materialGiveAmount
                    if materialGive == 4:
                        materialGive += materialGiveAmount
                    if materialGive == 5:
                        material += materialGiveAmount
                    clicked = True

debug_status = False
clock = pygame.time.Clock()
mouse_click = False  # Variable to track the click state
toggle_var = False  # Toggle variable for 'E' key
Itemlist = [wood,stick,stone]
angle2 = 55
mx2, my2 = pygame.mouse.get_pos()
tog = 0
while run:
    DMG = sworddamage, axepower
    screen.fill((0, 100, 0))
    clock.tick(FPS)
    fpsgiver = int(clock.get_fps())
    mousex, mousey = pygame.mouse.get_pos()
    key = pygame.key.get_pressed()

    if playerx > -1999:
        if key[pygame.K_a] == True:
            playerx -= Speed
    if playerx < 1999:
        if key[pygame.K_d] == True:
            playerx += Speed
    if playery > -1999:
        if key[pygame.K_w] == True:
            playery -= Speed
    if playery < 1999:
        if key[pygame.K_s] == True:
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
                toggle_var = not toggle_var  # Toggle the variable on 'E' key press
    for i in range(NumberOfTrees):
        treeplace(treeIdx[i], treeIdy[i], i, treeHp[i], treeLv[i])

    screen.blit(hotbar, (125, 625))
    if sword == 1:
        screen.blit(swordiconbig, (130, 630))

    player_pos = screen.get_rect().center
    player_rect = player.get_rect(center=player_pos)
    mx, my = pygame.mouse.get_pos()
    dx, dy = mx - player_rect.centerx, my - player_rect.centery
    angle = math.degrees(math.atan2(-dy, dx)) - correction_angle
    rot_image = pygame.transform.rotate(player, angle)
    rot_image_rect = rot_image.get_rect(center=player_rect.center)
    screen.blit(rot_image, rot_image_rect.topleft)
    if mouse_click == False:
        clicked = False
        mx2, my2 = pygame.mouse.get_pos()
        angle2 = 55
    if sword == 1:
        sworddamage = 4
        if mouse_click == True or tog == 0 or angle2 != 55:
            attack(5,1,2)
    fpsdisplay = font1.render(f"FPS: {fpsgiver}", True, (255, 255, 255))
    screen.blit(fpsdisplay, (2, 0))
    playerpos = font1.render(f"Player Position: ({playerx}, {0 - playery})", True, (255, 255, 255))
    screen.blit(playerpos, (2, 14))
    Daynumberdisplay = font1.render(f"Day: {Daynumber}", True, (255, 255, 255))
    screen.blit(Daynumberdisplay, (2, 28))
    if toggle_var == True:
        screen.blit(inventory,(100,100))
        if wood > 0:
            screen.blit(woodicon,(107,107))
            woodamount = font2.render(f"x{wood}", True, (255, 255, 255))
            screen.blit(woodamount, (107, 130))
        if wood > 1:
            Show_Recipe(stickicon,Itemlist[0],4,Itemlist[1],2,620,100,"2wood")
            #stickcraft = screen.blit(craftbgicon,(620,100))
            #screen.blit(stickicon,(620,100))
            #if mousex > stickcraft.x and mousex < stickcraft.x + 48:
            #    if mousey > stickcraft.y and mousey < stickcraft.y + 48:
            #        screen.blit(font1.render(f"2wood", True, (255, 255, 255)),(620,96))
            #        if mouse_click == True:
            #            if clicked == False:
            #                wood -= 2
            #                stick += 4
            #                clicked = True
        if wood > 4 and stick > 1:
            swordcraft = screen.blit(craftbgicon,(670,100))
            screen.blit(swordicon,(670,100))
            if mousex > swordcraft.x and mousex < swordcraft.x + 48:
                if mousey > swordcraft.y and mousey < swordcraft.y + 48:
                    screen.blit(font1.render(f"5wood", True, (255, 255, 255)),(670,96))
                    screen.blit(font1.render(f"2sticks", True, (255, 255, 255)),(670,106))
                    if mouse_click == True:
                        if clicked == False:
                            if sword == 0:
                                wood -= 5
                                stick -= 2
                            sword = 1
                            clicked = True
        if stick > 0:
            screen.blit(stickicon,(107 + (48 * 1) + (7 * 1), 107))
            stickamount = font2.render(f"x{stick}", True, (255, 255, 255))
            screen.blit(stickamount, (107 + (48 * 1) + (7 * 1), 130))
    pygame.draw.rect(screen, (0, 100, 0), MouseRect)
    mousex, mousey = pygame.mouse.get_pos()
    MouseRect.x = mousex
    MouseRect.y = mousey
    pygame.display.flip()
pygame.quit()
exit()