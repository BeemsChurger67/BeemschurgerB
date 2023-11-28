import pygame, math, random, time, os


pygame.init()
pygame.font.init()
FPS = 60
pygame.display.set_caption("cube simulation")
screen = pygame.display.set_mode((900,900))
screen.fill((0, 100, 0))

font = pygame.font.SysFont("comicsansms", 15)

directory = os.getcwd()
directory = os.path.join(directory, "Assets")
osPath = os.path.join
load = pygame.image.load
scale = pygame.transform.scale
#ExampleImage = scale(load(osPath(directory, "Example.png")),(100,100))
cubeW = []
cubeH = []
x = []
y = []
xSpeed = []
direction = []
yVel = []
Color = []
cubeAmount = 1

cubeW.append(75)
cubeH.append(75)
x.append(screen.get_size()[0] / 2 - 75)
y.append(screen.get_size()[1] / 2 - 75)
xSpeed.append(15)
direction.append(1)
yVel.append(0)
Color.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
def clone():
    global cubeAmount
    cubeW.append(75)
    cubeH.append(75)
    x.append(screen.get_size()[0] / 2 - 75)
    y.append(screen.get_size()[1] / 2 - 75)
    xSpeed.append(random.randint(5,25))
    direction.append(random.randint(1,2))
    yVel.append(random.randint(5,25))
    Color.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
    cubeAmount += 1
gravity = 0.5
extraBounce = 5
BounceDivision = 0
xSpeedGain = 0
SizeGain = [0,0]
FPSincrease = 0

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in range(cubeAmount):
        cube = pygame.Rect(x[i],y[i],cubeW[i],cubeH[i])
        pygame.draw.rect(screen,("white"),(cube[0] - 5,cube[1] - 5,cube[2] + 10,cube[3] + 10))
        pygame.draw.rect(screen,(Color[i]),cube)
    for b in range(cubeAmount):
        for i in range(xSpeed[b]):
            cube = pygame.Rect(x[b],y[b],cubeW[b],cubeH[b])
            if direction[b] == 1:
                x[b] += 1
                if x[b] > screen.get_width() - cubeW[b]:
                    direction[b] = 2
                    xSpeed[b] += xSpeedGain
                    cubeW[b] += SizeGain[0]
                    FPS += FPSincrease
                    if random.randint(1,4) == 4:
                        clone()
                    break
            else:
                x[b] -= 1
                if x[b] < 0:
                    direction[b] = 1
                    xSpeed[b] += xSpeedGain
                    cubeW[b] += SizeGain[0]
                    FPS += FPSincrease
                    if random.randint(1,4) == 4:
                        clone()
                    break
        if xSpeed[b] == 0:
            xSpeed[b] = direction[b] * 3
        
        yVel[b] += gravity
        y[b] += yVel[b]
        if y[b] > screen.get_height() - cubeH[b]:
            yVel[b] -= yVel[b] * 2 + extraBounce / (BounceDivision + 1)
            cubeH[b] += SizeGain[1]
            FPS += FPSincrease
            y[b] -= 2
        if y[b] < 0:
            for i in range(int(yVel[b] - yVel[b] * 2)):
                y[b] += 1
                yVel[b] -= yVel[b] * 2 + extraBounce
                cubeH[b] += SizeGain[1]
                FPS += FPSincrease
    fpsgiver = int(clock.get_fps())
    screen.blit(font.render(f"FPS: {fpsgiver}", True, (255, 255, 255)),(0,0))
    screen.blit(font.render(f"xSpeed: {xSpeed}", True, (255, 255, 255)),(0,15))
    screen.blit(font.render(f"yVel: {yVel}", True, (255, 255, 255)),(0,30))
    screen.blit(font.render(f"Size: {cubeW,cubeH}", True, (255, 255, 255)),(0,45))
    screen.blit(font.render(f"CubeAmount: {cubeAmount}", True, (255, 255, 255)),(0,60))
    pygame.display.flip()