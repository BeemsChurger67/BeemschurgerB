import pygame, math, random, time, os
pygame.init()
pygame.font.init()
FPS = 60
pygame.display.set_caption("walking simulator")
screen = pygame.display.set_mode((600,300))
screen.fill((0, 100, 0))
font = pygame.font.SysFont("comicsansms", 15)
logfont = pygame.font.SysFont("comicsansms", 10)
directory = os.getcwd()
directory = os.path.join(directory, "Assets")
osPath = os.path.join
load = pygame.image.load
scale = pygame.transform.scale
wall = scale(load(osPath(directory, "brickblock.png")),(600,50))
wallofflesh = scale(load(osPath(directory, "wallofflesh.png")),(100,200))
falppybrid = scale(load(osPath(directory, "falppybird.png")),(25,25))
catinvasion = scale(load(osPath(directory, "cat.png")),(75,75))
clock = pygame.time.Clock()
rng = random.randint
x = screen.get_size()[0] / 2 - 12.5
y = screen.get_size()[1] / 2 - 12.5
bgx = 0
bgVal = 0
health = 50
maxHealth = 100
defense = 0
orgspeed = 5
speed = 0
player = pygame.Rect(x,y, 25, 25)
EventSequense = 0
textDisplay = []
WoFstats = [bgx,False]
WofX = bgx
plusSpeed = [0]
plusSpeedList = []
plusSpeedDelTickAmount = 100
plusSpeedDelTick = 0
catinvasiontick = 0
catinvasiontickamount = 500
catinvasionON = False
textTimeTick = 0
flapOn = False
running = True
while running:
    clock.tick(FPS)
    if EventSequense == 1:
        screen.fill((rng(0,50),rng(0,50),rng(0,50)))
    else:
        screen.fill((0, 100, 0))
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player = pygame.Rect(x, y, 25, 25)
    pygame.draw.rect(screen,(255,255,255),player)
    screen.blit(font.render(f"HP: {health:.1f}/{maxHealth:.0f}", True, (255, 255, 255)),(x - 10,y - 35))
    screen.blit(font.render(f"DEF: {defense:.1f}", True, (255, 255, 255)),(x - 10,y - 20))
    plusSpeedList = 0
    plusSpeedDelTick
    for I in range(len(plusSpeed)):
        plusSpeedList += plusSpeed[I]
    if EventSequense == 2:
        speed = orgspeed + plusSpeedList * 2
    else:
        speed = orgspeed + plusSpeedList
    if key[pygame.K_a]:
        if x < 0:
            if not bgx == 0:
                bgx -= speed
                bgVal -= speed
        else:
            x -= speed
            
    if key[pygame.K_d]:
        if x > screen.get_size()[0] / 2:
            bgx += speed
            bgVal += speed
        else:
            x += speed
    if key[pygame.K_w] and y > 50:
        y -= speed
    if key[pygame.K_s] and y < 225:
        y += speed
    for i in range(int(bgx / 600 + 2)):
        screen.blit(wall,(-bgx + i * 600,0))
        screen.blit(wall,(-bgx + i * 600,250))
    if bgVal > 600:
        bgVal = 0
        EventSequense = rng(1,9)
        
        if bgx / 600 > 11:
            WoFstats = [bgx,True]
        if rng(1,100) == 1:
            textDisplay.append(f"you won a 1/100 chance and got the number {rng(0,1000)}/1000 be aware lmoasdmfasomdf joasd o nodf osdaf adoadsf omasdmoasdf omasd")
        if rng(1,100) == 1:
            textDisplay.append(f"(1/100) CAT INVASION CAT INVASION CAT INVASION CAT INVASION CAT INVASION CAT INVASION CAT INVASION CAT INVASION CAT INVASION CAT INVASION")
            catinvasionON = True
        if rng(1,100) == 1:
            textDisplay.append(f"(1/100) SUPERSONIC!!!!!!!!!!!!!!!")
            plusSpeed.append(1000)

        if EventSequense == 1:
            textDisplay.append("epilepsy")
        if EventSequense == 2:
            textDisplay.append("DOUBLE SPEED NO WAY")
        if EventSequense == 3:
            textDisplay.append("Oh no you take damage !!!!!")
            health /= 1.5
            health *= defense + 1 / 1.5
        if EventSequense == 4:
            textDisplay.append(f"Very sigma you get {health * 2:.1f} health!!!!! and {maxHealth * 1.1:.0f} more max hp")
            health *= 2
            maxHealth *= 1.1
        if EventSequense == 5:
            textDisplay.append("Very sigma you get defense +1 !!!!!")
            defense += 1
        if EventSequense == 6:
            textDisplay.append("Very sigma you get speed +3 !!!!!")
            if len(plusSpeed) > 0:
                plusSpeed[0] += 3
            else:
                plusSpeed.append(0)
        if EventSequense == 7:
            textDisplay.append("cool you are flapy bird :skull:")
            if len(plusSpeed) > 0:
                plusSpeed[0] += 3
            else:
                plusSpeed.append(0)
        if EventSequense == 8:
            textDisplay.append("Very sigma you get speed !!!!!")
            if len(plusSpeed) > 0:
                plusSpeed[0] += 3
            else:
                plusSpeed.append(rng(0,100))
        if EventSequense == 9:
            textDisplay.append("UHH YOU GET A LOT OF SPEED????????????????")
            plusSpeed.append(rng(0,100))
        if EventSequense == 10:
            textDisplay.append("rip speed ): ): ): 9:")
            plusSpeed.append(-rng(0,10))
            
        if EventSequense == 7:
            flapOn = True
    if flapOn == True:
        screen.blit(falppybrid,(x,y))
    if WoFstats[1] == True:
        WofX += bgx / 300
        screen.blit(wallofflesh,(WofX - bgx,50))
    if WofX > bgx + x:
        health -= 2 * maxHealth / 10



    if health > maxHealth:
        health = maxHealth
    for i in range(len(textDisplay)):
        screen.blit(logfont.render(f"{textDisplay[i]}", True, (0,0,0)),(175,50 + 10 * i))
    if len(textDisplay) > 10:
        del textDisplay[0]
    if len(plusSpeed) > 0:
        plusSpeedDelTick += 1
        if plusSpeedDelTick > plusSpeedDelTickAmount:
            plusSpeedDelTick = 0
            del plusSpeed[0]
    if catinvasionON:
        catinvasiontick += 1
        if catinvasiontick > catinvasiontickamount:
            catinvasionON = False
            catinvasiontick = 0
        for i in range(4):
            screen.blit(catinvasion,(rng(0,screen.get_width()),rng(0,screen.get_height())))
    if health < 0:
        running = False
        print(f"STATS: (Mile = {bgx / 600}),(Defense = {defense}),(max health = {maxHealth})")
        running2 = True
        while running2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running2 = False
            screen.fill((111,111,111))
            screen.blit(font.render("Stats:", True, (255, 255, 255)),(50,50))
            screen.blit(font.render(f"Mile = {bgx / 600:.1f}/10000.0", True, (255, 255, 255)),(50,65))
            screen.blit(font.render(f"Defense = {defense}", True, (255, 255, 255)),(50,80))
            screen.blit(font.render(f"max health = {maxHealth}", True, (255, 255, 255)),(50,95))
            screen.blit(font.render(f"speed = {speed}", True, (255, 255, 255)),(50,110))
            pygame.display.flip()
    if bgx / 600 > 10000:
        running = False
        print(f"STATS: (Mile = {bgx / 600}),(Defense = {defense}),(max health = {maxHealth})")
        running3 = True
        while running3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running3 = False
            screen.fill((111,111,111))
            screen.blit(font.render("YOU WIN NO WAY WTF HOW YOUR SO GOOD WTFFFFFFF??????????????????????????????????????????????????", True, (255, 255, 255)),(50,50))
            screen.blit(font.render("Stats:", True, (255, 255, 255)),(50,65))
            screen.blit(font.render(f"Mile = {bgx / 600}", True, (255, 255, 255)),(50,80))
            screen.blit(font.render(f"Defense = {defense}", True, (255, 255, 255)),(50,95))
            screen.blit(font.render(f"max health = {maxHealth}", True, (255, 255, 255)),(50,110))
            screen.blit(font.render(f"speed = {speed}", True, (255, 255, 255)),(50,125))
            screen.blit(font.render(f"How many miles the WoF was away from you: {bgx / 600 - WofX / 600:.1f}", True, (255, 255, 255)),(50,140))
            pygame.display.flip()
            
    fpsgiver = int(clock.get_fps())
    screen.blit(font.render(f"FPS: {fpsgiver}/{FPS}", True, (255, 255, 255)),(0,50))
    screen.blit(font.render(f"Mile: {bgx / 600:.1f}", True, (255, 255, 255)),(0,65))
    screen.blit(font.render(f"bgval: {bgVal}", True, (255, 255, 255)),(0,80))
    screen.blit(font.render(f"event: {EventSequense}", True, (255, 255, 255)),(0,95))
    screen.blit(font.render(f"speed {speed}", True, (255, 255, 255)),(0,110))
    screen.blit(font.render(f"Speed amount {len(plusSpeed)}", True, (255, 255, 255)),(0,125))
    screen.blit(font.render(f"WoF distance {bgx / 600 - WofX / 600:.1f} miles", True, (255, 255, 255)),(0,140))
    screen.blit(font.render(f"WoF speed {7 + bgx / 450:.0f}", True, (255, 255, 255)),(0,165))
    screen.blit(font.render("please dont play this game lmao", True, (255, 255, 255)),(-bgx + 50,200))
    screen.blit(font.render("good luck", True, (255, 255, 255)),(-bgx + 50,215))
    pygame.display.flip()