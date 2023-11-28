import pygame, math, random, time, os
from Map import minimap
pygame.init()
pygame.font.init()
print("Game made by beemschurger67")
FPS = 60
pygame.display.set_caption("ok")
screen = pygame.display.set_mode((800,800))
screen.fill((0, 100, 0))
font = pygame.font.SysFont("Calibri", 20)
directory = os.getcwd()
directory = os.path.join(directory, "Assets")
osPath = os.path.join
file_count = len(os.listdir(directory))
print(file_count)
file_names = os.listdir(directory)
load = pygame.image.load
scale = pygame.transform.scale
jumpscare = scale(load(osPath(directory, "19.png")),(screen.get_size()))
FileList = []
FileList.clear()
for file_name in file_names:
    FileList.append(scale(load(osPath(directory, file_name)),(100,100)))
print(file_names)
#ExampleImage = scale(load(osPath(directory, "Example.png")),(100,100))
clock = pygame.time.Clock()
dave = [pygame.Rect(screen.get_size()[0] / 2 - 25,screen.get_size()[1] / 2 - 25,51,51),pygame.Rect(screen.get_size()[0] / 2 - 25,screen.get_size()[1] / 2 - 25,51,51)]
rng = random.randint
for i in range(len(minimap)):
    minimap[i][0] *= 100
    minimap[i][1] *= 100
def collisionFunc(moveX,moveY,player):
    global x,y,running,speed,minimap,dave, checkpoint, TestMode, orgspeed, communistBgD
    superDave = pygame.Rect(dave[player][0] + moveX, dave[player][1] - moveY, dave[player][2], dave[player][3])
    for i in range(len(minimap)):
        TileType = minimap[i][4]
        DisplayMinimap = [minimap[i][0] - x[player], minimap[i][1] - y[player], minimap[i][2], minimap[i][3]]
        if TestMode == False:
            if superDave.colliderect(DisplayMinimap):
                x[player] -= moveX
                y[player] += moveY
                if TileType == 2 or TileType == 10:
                    hp[player] -= rng(0,1000000)
                    if hp[player] <= 0:
                        hp[player] = 100
                        x[player] = checkpoint[0]
                        y[player] = checkpoint[1]
                if TileType == 3:
                    x[player] += moveX
                    y[player] -= moveY
                if TileType == 5:
                    x[player] += moveX * 2
                    y[player] -= moveY * 2
                if TileType == 6:
                    x[player] += moveX * rng(-50,50)
                    y[player] -= moveY * rng(-50,50)
                if TileType == 7:
                    running = False
                if TileType == 8:
                    x[player] = minimap[i][5] * 100 + x[player]
                    y[player] = minimap[i][6] * 100 + y[player]
                if TileType == 9:
                    x[player] += moveX
                    y[player] -= moveY
                    checkpoint = x[player], y[player]
                    hp[player] = 100
                if TileType == 10:
                    x[player] += moveX
                    y[player] -= moveY
                if TileType == 11:
                    TestMode = True
                    orgspeed = 18
                if TileType == 12:
                    communistBgD[0] = True
                    communistBgD[1] = 0
                    x[player] += moveX
                    y[player] -= moveY
                    
        else:
            pass
communistBgD = [False,0,1]
checkpoint = [0,0]
x = [-50,-50]
y = [-50,-50]
hp = [100,100]
movingObjects = []
ObjectFrame = []
ObjectFrameLimit = []
MoveLimit = 100
MoveFrame = 1
orgspeed = 3
TestMode = False
speed = [orgspeed,orgspeed]
for a in range(len(minimap)):
    if minimap[a][4] == 10:
        ObjectFrame.append(0)
        ObjectFrameLimit.append(len(minimap[a]) - 5)
        adder = []
        for b in range(len(minimap[a]) - 5):
            adder.append(minimap[a][b + 5])
        movingObjects.append(adder)
print(movingObjects)
print(ObjectFrame)
print(ObjectFrameLimit)
print(MoveLimit)
print(MoveFrame)
running = True
while running:
    key = pygame.key.get_pressed()
    clock.tick(FPS)
    screen.fill((0, 100, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if key[pygame.K_LSHIFT] or key[pygame.K_LCTRL]:
        speed[0] = orgspeed * 2
    else:
        speed[0] = orgspeed

    if key[pygame.K_RSHIFT] or key[pygame.K_RCTRL]:
        speed[1] = orgspeed * 2
    else:
        speed[1] = orgspeed
    if key[pygame.K_a]:
        collisionFunc(-speed[0], 0,0)
        x[0] -= speed[0]
    if key[pygame.K_d]:
        collisionFunc(speed[0], 0,0)
        x[0] += speed[0]
    if key[pygame.K_s]:
        collisionFunc(0, -speed[0],0)
        y[0] += speed[0]
    if key[pygame.K_w]:
        collisionFunc(0, speed[0],0)
        y[0] -= speed[0]
    collisionFunc(0, 0, 0)
    collisionFunc(0, 0, 1)

    #print(x[0],y[0],"-----",x[1],y[1])
    if key[pygame.K_LEFT]:
        collisionFunc(-speed[1], 0,1)
        x[1] -= speed[1]
    if key[pygame.K_RIGHT]:
        collisionFunc(speed[1], 0,1)
        x[1] += speed[1]
    if key[pygame.K_DOWN]:
        collisionFunc(0, -speed[1],1)
        y[1] += speed[1]
    if key[pygame.K_UP]:
        collisionFunc(0, speed[1],1)
        y[1] -= speed[1]
    MovNum = -1
    MoveFrame += 1
    for i in range(len(minimap)):
        DisplayMinimap = [minimap[i][0] - x[0], minimap[i][1] - y[0], minimap[i][2], minimap[i][3]]
        if minimap[i][4] == 1:
            screen.blit(FileList[1],(DisplayMinimap))
        elif minimap[i][4] == 2:
            screen.blit(FileList[0],(DisplayMinimap))
        elif minimap[i][4] == 3:
            screen.blit(FileList[1],(DisplayMinimap))
        elif minimap[i][4] == 4:
            pygame.draw.rect(screen,("black"),(DisplayMinimap))
            screen.blit(font.render(f"{minimap[i][5]}", True, (255, 255, 255)),(DisplayMinimap))
        elif minimap[i][4] == 5:
            screen.blit(FileList[2],(DisplayMinimap))
        elif minimap[i][4] == 6:
            screen.blit(FileList[3],(DisplayMinimap))
        elif minimap[i][4] == 7:
            screen.blit(FileList[4],(DisplayMinimap))
        elif minimap[i][4] == 8:
            screen.blit(FileList[5],(DisplayMinimap))
        elif minimap[i][4] == 9:
            screen.blit(FileList[6],(DisplayMinimap))
        elif minimap[i][4] == 10:
            MovNum += 1
            screen.blit(FileList[7],(DisplayMinimap))
            for c in range(len(ObjectFrame)):
                minimap[i][0] += movingObjects[MovNum][ObjectFrame[c]][0] / len(ObjectFrame)
                minimap[i][1] += movingObjects[MovNum][ObjectFrame[c]][1] / len(ObjectFrame)
            if MoveFrame >= MoveLimit:
                for d in range(len(ObjectFrame)):
                    ObjectFrame[d] += 1
                    if ObjectFrame[d] > ObjectFrameLimit[d] - 1:
                        ObjectFrame[d] = 0
                MoveFrame = 1
        elif minimap[i][4] == 11:
            screen.blit(FileList[8],(DisplayMinimap))
        elif minimap[i][4] == 12:
            screen.blit(FileList[9],(DisplayMinimap))
    pygame.draw.rect(screen,("blue"),dave[0])
    pygame.draw.rect(screen,("green"),(dave[1][0] - x[0] + x[1],dave[1][1] - y[0] + y[1],50,50))
    pygame.draw.rect(screen,("black"),(dave[1][0] - x[0] + x[1] - 5,dave[1][1] - y[0] + y[1] - 25,70,19))
    pygame.draw.rect(screen,("black"),(365,350,70,19))
    screen.blit(font.render(f"Hp: {hp[0]}", True, (255, 255, 255)),(365,350))
    screen.blit(font.render(f"Hp: {hp[1]}", True, (255, 255, 255)),(dave[1][0] - x[0] + x[1],dave[1][1] - y[0] + y[1] - 25))

    fpsgiver = int(clock.get_fps())
    if fpsgiver < 25:
        screen.blit(font.render(f"FPS: {fpsgiver}", True, (rng(0,255),0,0)),(rng(0,10),rng(0,10)))
    else:
        screen.blit(font.render(f"FPS: {fpsgiver}", True, (0,255,0)),(0,0))
    screen.blit(font.render(f"p1: {(x[0] + 325) / 100:.2f} {(y[0] + 325) / 100:.2f}", True, (255, 255, 255)),(0,15))
    screen.blit(font.render(f"p2: {(x[1] + 325) / 100:.2f} {(y[1] + 325) / 100:.2f}", True, (255, 255, 255)),(0,30))
    screen.blit(font.render(f"checkpoint: {(checkpoint[0] + 325) / 100,(checkpoint[1] + 325) / 100}", True, (0, 255, 0)),(0,45))
    if TestMode == True:
        screen.blit(font.render(f"BuildXY: {(x[0] + 325) / 100:.0f} {(y[0] + 325) / 100:.0f}", True, (0, 255, 0)),(0,60))
        screen.blit(font.render("Build mode = True", True, (0, 0, 0)),(0,90))
    if communistBgD[0] == True and communistBgD[1] <= communistBgD[2]:
        communistBgD[1] += 1
        screen.blit(jumpscare,(0,0))
    pygame.display.flip()