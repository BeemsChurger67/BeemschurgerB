import pygame, random, math
pygame.init()
pygame.font.init(
)
font1 = pygame.font.SysFont("calibri", 16)
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Rounds made on py")
running = True
Player1 = [0,0,50,100,125,10,1,0]# X,Y,DMG,HP,SPD,JPOWER,ATKSPD,DEFENSE
MaxHp1 = Player1[3]
FPS = 60
CardAm = 7
rng = random.randint
EveryCard = [
    "Test card",[2,2,2,2],
]
EveryCardTesting = [
    "Bad RNG card",rng(5,15),rng(0,5),
    "RNG card",rng(15,50),rng(0,5),
    "Good RNG card",rng(25,100),rng(0,5),
    "alright bro",rng(-50,50),rng(0,5),
    "Tank",100,1,
    "Heroin",500,2,
    "Damage",7,0,
    "Damage++",25,0,
    "Cocaine",125,2,
    "Damage+",15,0,
    "good luck card",250,rng(0,5),
    "Defender",5,5,
]
def Shoot(Mx,My):
    pass
StatsNam = ["x","y","Damage","Health","Speed","Jumppower","Fire speed","Defense"]
CardStatsNam = ["Damage","Health","Speed","Jumppower","Fire speed","Defense"]
cardD = []
cardR = []
cardS = 0
GameStarted = False
keypressed = False
delay = 0
for I in range(CardAm):
    cardD.append(0)
    cardR.append(random.randint(0,len(EveryCard) / 3 - 2))
print(cardR)
while running:
    key = pygame.key.get_pressed()
    if GameStarted == True:
        if key[pygame.K_SPACE]:
            if key[pygame.K_a]:
                Player1[0] -= Player1[4] / 100
            if key[pygame.K_d]:
                Player1[0] += Player1[4] / 100
        else:
            cardR.clear()
            cardD.clear()
            cardS = 0
            GameStarted = False
            keypressed = False
            delay = 0
            for I in range(CardAm):
                cardD.append(0)
                cardR.append(random.randint(0,len(EveryCard) / 3 - 2))
    else:
        if keypressed == False:
            if key[pygame.K_a] and cardS > 0 and delay == 0:
                cardS -= 1
                delay = 7
            if key[pygame.K_d] and cardS < CardAm - 1 and delay == 0:
                cardS += 1
                delay = 7
            if key[pygame.K_SPACE]:
                Player1[EveryCard[cardR[cardS] * 3 + 2] + 2] += EveryCard[cardR[cardS] * 3 + 1]

                MaxHp1 = Player1[3]
                GameStarted = True
    if delay > 0:
        delay -= 1
    screen.fill((100,100,100))
    for Length in range(len(Player1)):
        screen.blit(font1.render(f"{StatsNam[Length]}: ({Player1[Length]:.0f})", True, (255, 255, 255)),(0,Length * -font1.get_height() / 1.2 + 800 - font1.get_height()))
    screen.blit(font1.render(f"{cardS}", True, (255, 255, 255)),(0,25))
    pygame.draw.rect(screen,(0,0,0),(Player1[0],Player1[1],25,25))
    if GameStarted == False:
        for cardX in range(CardAm):
            pygame.draw.rect(screen,(0,0,0),(18 + cardX * 110,300,100,180))
            screen.blit(font1.render(f"{EveryCard[cardR[cardX] * 2]}", True, (255, 255, 255)),(cardX * 110 + 18,300))
            screen.blit(font1.render(f"{CardStatsNam[EveryCard[cardR[cardX] * 2]]} {EveryCard[cardR[cardX] * 2]}", True, (255, 255, 255)),(cardX * 110 + 18,320))
            pygame.draw.rect(screen,(0,0,0),(50 + cardS * 110,100,30,60))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.Clock().tick(FPS)
    pygame.display.flip()