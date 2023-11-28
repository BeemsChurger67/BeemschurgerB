import pygame, math, random, time, os, ctypes
pygame.init()
pygame.font.init()
pygame.mixer.init()
def get_screen_resolution():
    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0)  # 0 corresponds to the width of the primary monitor
    height = user32.GetSystemMetrics(1)  # 1 corresponds to the height of the primary monitor
    return width, height
resolution = get_screen_resolution()
FPS = 60
pygame.display.set_caption("cube simulation")
screen = pygame.display.set_mode((resolution))
print(pygame.display.Info())
screen.fill((0, 100, 0))

# Get and print the screen resolution
resolution = get_screen_resolution()
font = pygame.font.SysFont("calibri", 15)

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
RectValue = []
cubeAmount = 1
bounces = 0
cubeW.append(75)
cubeH.append(75)
x.append(screen.get_size()[0] / 2 - 75)
y.append(screen.get_size()[1] / 2 - 75)
xSpeed.append(15)
direction.append(1)
yVel.append(0)
Color.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
RectValue.append(pygame.Rect(x[cubeAmount - 1],y[cubeAmount - 1],75,75))
def clone(PosX,PosY,width,height):
    global cubeAmount
    cubeW.append(width)
    cubeH.append(height)
    x.append(PosX)
    y.append(PosY)
    xSpeed.append(random.randint(5,25))
    direction.append(random.randint(1,2))
    yVel.append(random.randint(5,25))
    Color.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
    RectValue.append(pygame.Rect(x[cubeAmount],y[cubeAmount],75,75))
    cubeAmount += 1
gravity = 0.5
extraBounce = 1
BounceDivision = 0
xSpeedGain = 5
SizeGain = [0,0]
FPSincrease = 0
on = False
clock = pygame.time.Clock()
running = True
while running:
    key = pygame.key.get_pressed()
    clock.tick(FPS)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #sound = pygame.mixer.Sound("epicclick.mp3")
    if key[pygame.K_SPACE]:
        on = True
    if on == True:
        for i in range(cubeAmount):
            cube = pygame.Rect(x[i],y[i],cubeW[i],cubeH[i])
            #pygame.draw.rect(screen,("white"),(cube[0] - 5,cube[1] - 5,cube[2] + 10,cube[3] + 10))
            #pygame.draw.rect(screen,(Color[i]),cube)
            pygame.draw.circle(screen,(Color[i]),(x[i]+75/2,y[i]+75/2),75 / 2)
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
                        bounces += 1
                        #sound.play()
                        if random.randint(1,4) == 4:
                            clone(x[b],y[b],75,75)
                        break
                else:
                    x[b] -= 1
                    if x[b] < 0:
                        direction[b] = 1
                        xSpeed[b] += xSpeedGain
                        cubeW[b] += SizeGain[0]
                        FPS += FPSincrease
                        bounces += 1
                        #sound.play()
                        if random.randint(1,4) == 4:
                            clone(x[b],y[b],75,75)
                        break
            if xSpeed[b] == 0:
                xSpeed[b] = direction[b] * 3
            
            yVel[b] += gravity
            y[b] += yVel[b]
            if y[b] > screen.get_height() - cubeH[b]:
                yVel[b] -= yVel[b] * 2 + extraBounce / (BounceDivision + 1)
                cubeH[b] += SizeGain[1]
                FPS += FPSincrease
                y[b] += yVel[b]
                bounces += 1
                #sound.play()
                if random.randint(1,4) == 4:
                    clone(x[b],y[b],75,75)
            if y[b] < 90:
                for i in range(int(yVel[b] - yVel[b] * 2)):
                    y[b] += 1
                if random.randint(1,4) == 4:
                    clone(x[b],y[b],75,75)
                    bounces += 1
                    yVel[b] -= yVel[b] * 2 + extraBounce
                cubeH[b] += SizeGain[1]
                bounces += 1
                FPS += FPSincrease
                #sound.play()
            #for j in range(cubeAmount):
            #    if RectValue[b - 1].colliderect(RectValue[j - 1]):
            #        print(f"{RectValue[b-1][0],RectValue[b-1][1]}/{RectValue[j - 1][0],RectValue[j - 1][1]}")
                
        #for i in range(cubeAmount):
        #    RectValue[i][0] = x[i]
        #    RectValue[i][1] = y[i]
        #print(f"Cubeamount^2: {cubeAmount ^ 2} ||| CubeAmount: {cubeAmount} ||| RectValue: {RectValue}")
        fpsgiver = int(clock.get_fps())
        screen.blit(font.render(f"FPS: {fpsgiver}", True, (255, 255, 255)),(0,0))
        screen.blit(font.render(f"CubeAmount: {cubeAmount}", True, (255, 255, 255)),(0,15))
        screen.blit(font.render(f"Bounces: {bounces}", True, (255, 255, 255)),(0,30))
        pygame.display.flip()