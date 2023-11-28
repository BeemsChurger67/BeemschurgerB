import pygame, math, random, time, os
import Settings as S
pygame.init()
pygame.font.init()
FPS = S.Fps
pygame.display.set_caption(S.GameName)
screen = pygame.display.set_mode((S.DisplaySize))
screen.fill((0, 100, 0))
font = pygame.font.SysFont("calibri", S.FontSize)
Buyfont = pygame.font.SysFont("comicsansms", S.FontSize - 2)
WaveFont = pygame.font.SysFont("georgia", S.FontSize + 15)
BigFont = pygame.font.SysFont("georgia", S.FontSize + 30)
directory = os.getcwd()
directory = os.path.join(directory, "Assets")
load = pygame.image.load
scale = pygame.transform.scale
osPath = os.path.join
player = scale(load(osPath(directory, "player.png")),(40,40))
BasicEnemy = scale(load(osPath(directory, "basicenemy.png")),(40,40))
FastEnemy = scale(load(osPath(directory, "fastenemy.png")),(40,40))
StrongEnemy = scale(load(osPath(directory, "strongenemy.png")),(40,40))
BasicBoss = scale(load(osPath(directory, "basicboss.png")),(60,60))
SandEnemy = scale(load(osPath(directory, "sandenemy.png")),(40,40))
FastBoss = scale(load(osPath(directory, "fastboss.png")),(80,60))
BloodEnemy = scale(load(osPath(directory, "bloodenemy.png")),(40,40))
StrongBoss = scale(load(osPath(directory, "strongboss.png")),(60,60))
StormEnemy = scale(load(osPath(directory, "stormenemy.png")),(40,40))
BloodBoss = scale(load(osPath(directory, "bloodboss.png")),(60,60))
DogeBoss = scale(load(osPath(directory, "dogeboss.png")),(80,80))
Lauri = scale(load(osPath(directory, "Lauri.png")),(160,160))
clock = pygame.time.Clock()
PPosNsize = [screen.get_width() / 2 - S.playerSize[0] / 2 - 100, screen.get_height() / 2 - S.playerSize[1] / 2, S.playerSize[0],S.playerSize[1]]
Turrets = [0,0,0,0]
rng = random.randint
EnemyAmount = 0
enemies = []
bullets = []
Stats = S.StarterStats
SwordOn = False
MaxinumHP = S.StarterStats[1]
CoreMaxHP = S.StarterStats[0]
Wave = S.StarterStats[4]
CostValue = [100,25,25,200,2500,1500,0,0,0,0]
TurretDMG = [0.1,0,0,0,0,0,0,0,0,0]
EnemyTypeSpawn = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
EnemyTimesSpawn = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print("Stats",Stats)
GameStarted = False
CoreRegen = 1
class Enemy:
    def __init__(self, x, y, speed, hp, dmg, Rarity, type, boss):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.speed = speed
        self.hp = hp
        self.dmg = dmg
        self.Rarity = Rarity
        self.Type = type
        self.Boss = boss

    def draw(self, screen):
        if self.Boss:
            self.rect = pygame.Rect(self.rect.x, self.rect.y, 60,60)
        if self.Type == 1:
            screen.blit(BasicEnemy,(self.rect))
        if self.Type == 2:
            screen.blit(FastEnemy,(self.rect))
        if self.Type == 3:
            screen.blit(StrongEnemy,(self.rect))
        if self.Type == 4:
            screen.blit(BasicBoss,(self.rect))
        if self.Type == 5:
            screen.blit(SandEnemy,(self.rect))
        if self.Type == 6:
            screen.blit(FastBoss,(self.rect))
        if self.Type == 7:
            screen.blit(BloodEnemy,(self.rect))
        if self.Type == 8:
            screen.blit(StrongBoss,(self.rect))
        if self.Type == 9:
            screen.blit(StormEnemy,(self.rect))
        if self.Type == 10:
            screen.blit(BloodBoss,(self.rect))
        if self.Type == 11:
            self.rect = pygame.Rect(self.rect.x, self.rect.y, 80,80)
            screen.blit(DogeBoss,(self.rect))
        if self.Type == 12:
            self.rect = pygame.Rect(self.rect.x, self.rect.y, 160,160)
            screen.blit(Lauri,(self.rect))

    def move(self):
        if self.rect.x > 200:
            self.rect.x -= self.speed 
        else:
            Stats[0] -= self.dmg
            self.hp -= self.dmg

    def take_damage(self, damage):
        self.hp -= damage

    def is_dead(self):
        return self.hp <= 0
    @staticmethod
    def spawn(screen_width, screen_height, boss, hp2, dmg2, speed2,type2):
        Rarity = False
        x = screen_width + rng(0,125)
        y = screen_height / 2 + rng(-150,150)
        hp = hp2
        dmg = dmg2
        speed = speed2
        type = type2
        
        return Enemy(x, y, speed, hp, dmg, Rarity, type, boss)

    def handle_collision(self, bullets):
        for bullet in bullets:
            if self.rect.colliderect(bullet.rect):
                self.take_damage(bullet.dmg / len(enemies))
                bullets.remove(bullet)




class Bullet:
    def __init__(self, x, y, speed, dmg):
        self.rect = pygame.Rect(x, y, 25, 7)
        self.speed = speed
        self.dmg = dmg

    def draw(self, screen):
        pygame.draw.rect(screen, (255,0,0), self.rect)
        self.dmg = TurretDMG[0]

    def move(self):
        self.rect.x += self.speed
        if self.rect.x > screen.get_width():
            self.rect.x = 200 + rng(-50,50)
            self.rect.y = rng(0, 500)

    @staticmethod
    def spawn(screen_width, screen_height):
        x = 200
        y = rng(0, screen_height)
        dmg = 0.1
        speed = 3
        return Bullet(x, y, speed, dmg)
    

    def handle_collision(self, enemies):
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                enemy.take_damage(self.dmg / len(enemies))
SwordLength = 50
running = True
sword = pygame.draw.rect(screen,(100,100,100),(PPosNsize[0] + 25,PPosNsize[1] - 4,50,8))
EnS = 0
EnSE = 1
while running:
    key = pygame.key.get_pressed()
    screen.fill((0, 100, 0))
    mx,my = pygame.mouse.get_pos()
    Player = pygame.Rect(PPosNsize)
    if len(enemies) == 0 and GameStarted or key[pygame.K_g]:
        for I in range(len(EnemyTypeSpawn)):
            EnemyTypeSpawn[I] += 1
        Wave += 1
        for I in range(Wave):
            EnS = 0
            EnSE = 1
            if EnemyTypeSpawn[EnS] == EnS + EnSE:
                EnemyTypeSpawn[EnS] = 0
                EnemyTimesSpawn[EnS] += 1
                for I in range(EnemyTimesSpawn[EnS]):
                    new_enemy = Enemy.spawn(screen.get_width(), screen.get_height(),False,25 * (Wave * 0.1 + 1),6 * (Wave * 0.1 + 1),2,EnS + 1) # 1
                    enemies.append(new_enemy)
                    EnemyAmount += 1
            EnS += 1
            EnSE += 1
            if EnemyTypeSpawn[EnS] == EnS + EnSE:
                EnemyTypeSpawn[EnS] = 0
                EnemyTimesSpawn[EnS] += 1
                for I in range(EnemyTimesSpawn[EnS]):
                    new_enemy = Enemy.spawn(screen.get_width(), screen.get_height(),False,15 * (Wave * 0.1 + 1),3 * (Wave * 0.1 + 1),4,EnS + 1) # 2
                    enemies.append(new_enemy)
                    EnemyAmount += 1
            EnS += 1
            EnSE += 1
            if EnemyTypeSpawn[EnS] == EnS + EnSE:
                EnemyTypeSpawn[EnS] = 0
                EnemyTimesSpawn[EnS] += 1
                for I in range(EnemyTimesSpawn[EnS]):
                    new_enemy = Enemy.spawn(screen.get_width(), screen.get_height(),False,70 * (Wave * 0.1 + 1),15 * (Wave * 0.1 + 1),1,EnS + 1) # 3
                    enemies.append(new_enemy)
                    EnemyAmount += 1
            EnS += 1
            EnSE += 1
            if EnemyTypeSpawn[EnS] == EnS + EnSE:
                EnemyTypeSpawn[EnS] = 0
                EnemyTimesSpawn[EnS] += 1
                for I in range(EnemyTimesSpawn[EnS]):
                    new_enemy = Enemy.spawn(screen.get_width(), screen.get_height(),True,1000 * (Wave * 0.1 + 1),25 * (Wave * 0.1 + 1),1,EnS + 1) # 4
                    enemies.append(new_enemy)
                    EnemyAmount += 1
            EnS += 1
            EnSE += 1
            if EnemyTypeSpawn[EnS] == EnS + EnSE:
                EnemyTypeSpawn[EnS] = 0
                EnemyTimesSpawn[EnS] += 1
                for I in range(EnemyTimesSpawn[EnS]):
                    new_enemy = Enemy.spawn(screen.get_width(), screen.get_height(),False,100 * (Wave * 0.1 + 1),30 * (Wave * 0.1 + 1),2,EnS + 1) # 5
                    enemies.append(new_enemy)
                    EnemyAmount += 1
            EnS += 1
            EnSE += 1
            if EnemyTypeSpawn[EnS] == EnS + EnSE:
                EnemyTypeSpawn[EnS] = 0
                EnemyTimesSpawn[EnS] += 1
                for I in range(EnemyTimesSpawn[EnS]):
                    new_enemy = Enemy.spawn(screen.get_width(), screen.get_height(),True,600 * (Wave * 0.1 + 1),30 * (Wave * 0.1 + 1),5,EnS + 1) # 6
                    enemies.append(new_enemy)
                    EnemyAmount += 1
            EnS += 1
            EnSE += 1
            if EnemyTypeSpawn[EnS] == EnS + EnSE:
                EnemyTypeSpawn[EnS] = 0
                EnemyTimesSpawn[EnS] += 1
                for I in range(EnemyTimesSpawn[EnS]):
                    new_enemy = Enemy.spawn(screen.get_width(), screen.get_height(),False,750 * (Wave * 0.1 + 1),45 * (Wave * 0.1 + 1),2,EnS + 1) # 7
                    enemies.append(new_enemy)
                    EnemyAmount += 1
            EnS += 1
            EnSE += 1
            if EnemyTypeSpawn[EnS] == EnS + EnSE:
                EnemyTypeSpawn[EnS] = 0
                EnemyTimesSpawn[EnS] += 1
                for I in range(EnemyTimesSpawn[EnS]):
                    new_enemy = Enemy.spawn(screen.get_width(), screen.get_height(),True,5000 * (Wave * 0.1 + 1),100 * (Wave * 0.1 + 1),1,EnS + 1) # 8
                    enemies.append(new_enemy)
                    EnemyAmount += 1
            EnS += 1
            EnSE += 1
            if EnemyTypeSpawn[EnS] == EnS + EnSE:
                EnemyTypeSpawn[EnS] = 0
                EnemyTimesSpawn[EnS] += 1
                for I in range(EnemyTimesSpawn[EnS]):
                    new_enemy = Enemy.spawn(screen.get_width(), screen.get_height(),False,1000 * (Wave * 0.1 + 1),75 * (Wave * 0.1 + 1),2,EnS + 1) # 9
                    enemies.append(new_enemy)
                    EnemyAmount += 1
            EnS += 1
            EnSE += 1
            if EnemyTypeSpawn[EnS] == EnS + EnSE:
                EnemyTypeSpawn[EnS] = 0
                EnemyTimesSpawn[EnS] += 1
                for I in range(EnemyTimesSpawn[EnS]):
                    new_enemy = Enemy.spawn(screen.get_width(), screen.get_height(),True,2500 * (Wave * 0.1 + 1),75 * (Wave * 0.1 + 1),1,EnS + 1) # 10
                    enemies.append(new_enemy)
                    EnemyAmount += 1
            EnS += 1
            EnSE += 1
            if EnemyTypeSpawn[EnS] == EnS + EnSE:
                EnemyTypeSpawn[EnS] = 0
                EnemyTimesSpawn[EnS] += 1
                for I in range(EnemyTimesSpawn[EnS]):
                    new_enemy = Enemy.spawn(screen.get_width(), screen.get_height(),True,5000 * (Wave * 0.1 + 1),4000 * (Wave * 0.1 + 1),1,EnS + 1) # 11
                    enemies.append(new_enemy)
                    EnemyAmount += 1
            EnS += 1
            EnSE += 1
            if EnemyTypeSpawn[EnS] == EnS + EnSE:
                EnemyTypeSpawn[EnS] = 0
                EnemyTimesSpawn[EnS] += 1
                for I in range(EnemyTimesSpawn[EnS]):
                    new_enemy = Enemy.spawn(screen.get_width(), screen.get_height(),69,10000 * (Wave * 0.1 + 1),10000 * (Wave * 0.1 + 1),1,EnS + 1) # 12
                    enemies.append(new_enemy)
                    EnemyAmount += 1


    for bullet in bullets:
        bullet.draw(screen)
        bullet.move()
    if Stats[0] < CoreMaxHP:
        Stats[0] += CoreRegen
    if Stats[0] < 0:
        running = False
        print("WAVE", Wave)
        print("MONEY", [Stats[3]])
    if Stats[1] < 0:
        PPosNsize = [screen.get_width() / 2 - S.playerSize[0] / 2 - 100, screen.get_height() / 2 - S.playerSize[1] / 2, S.playerSize[0],S.playerSize[1]]
        Stats[1] = MaxinumHP
    for enemy in enemies:
        enemy.draw(screen)
        enemy.move()
        pygame.draw.rect(screen,(0,0,0),(enemy.rect.x, enemy.rect.y - 58,50,30))
        screen.blit(font.render(f"HP: {enemy.hp:.0f}", True, (255, 255, 255)),(enemy.rect.x, enemy.rect.y - 40))
        screen.blit(font.render(f"DMG: {enemy.dmg:.0f}", True, (255, 255, 255)),(enemy.rect.x, enemy.rect.y - 50))
        screen.blit(font.render(f"SPD: {enemy.speed:.0f}", True, (255, 255, 255)),(enemy.rect.x, enemy.rect.y - 60))
        if enemy.Boss == True:
            pygame.draw.rect(screen,(0,0,0),(enemy.rect.x, enemy.rect.y - 68,50,40))
            screen.blit(font.render("BOSS", True, (255, 0, 0)),(enemy.rect.x, enemy.rect.y - 70))
            screen.blit(font.render(f"HP: {enemy.hp:.0f}", True, (255, 255, 255)),(enemy.rect.x, enemy.rect.y - 40))
            screen.blit(font.render(f"DMG: {enemy.dmg:.0f}", True, (255, 255, 255)),(enemy.rect.x, enemy.rect.y - 50))
            screen.blit(font.render(f"SPD: {enemy.speed:.0f}", True, (255, 255, 255)),(enemy.rect.x, enemy.rect.y - 60))
        elif enemy.Boss == 69:
            pygame.draw.rect(screen,(0,0,0),(enemy.rect.x, enemy.rect.y - 68,50,40))
            screen.blit(font.render("NEO-NAZI", True, (255, 0, 0)),(enemy.rect.x, enemy.rect.y - 70))
            screen.blit(font.render(f"HP: {enemy.hp:.0f}", True, (255, 255, 255)),(enemy.rect.x, enemy.rect.y - 40))
            screen.blit(font.render(f"DMG: {enemy.dmg:.0f}", True, (255, 255, 255)),(enemy.rect.x, enemy.rect.y - 50))
            screen.blit(font.render(f"SPD: {enemy.speed:.0f}", True, (255, 255, 255)),(enemy.rect.x, enemy.rect.y - 60))
        if enemy.rect.colliderect(Player):
            Stats[1] -= enemy.dmg
        if enemy.rect.colliderect(sword) and SwordOn:
            enemy.take_damage(Stats[2])
        if enemy.is_dead():
            Stats[3] += (750 + enemy.Type * 10) * ((Wave + 1) / 2) + 1 
            enemies.remove(enemy)
        if key[pygame.K_h]:
            Stats[3] += (750 + enemy.Type * 10) * ((Wave + 1) / 2) + 1 
            enemies.remove(enemy)

        # Handle bullet-enemy collision
        for bullet in bullets:
            bullet.handle_collision(enemies)

    if key[pygame.K_a] and PPosNsize[0] > 200:
        PPosNsize[0] -= S.PlayerSpeed
    if key[pygame.K_d] and PPosNsize[0] < screen.get_width():
        PPosNsize[0] += S.PlayerSpeed
    if key[pygame.K_s] and PPosNsize[1] < screen.get_height():
        PPosNsize[1] += S.PlayerSpeed
    if key[pygame.K_w] and PPosNsize[1] > 0:
        PPosNsize[1] -= S.PlayerSpeed
    if key[pygame.K_SPACE]:
        sword = pygame.draw.rect(screen,(100,100,100),(PPosNsize[0] + 40,PPosNsize[1] + 3,SwordLength ,8))
        pygame.draw.rect(screen,(66,66,66),(PPosNsize[0] + 50,PPosNsize[1] - 8,8,30))
        SwordOn = True
    else:
        SwordOn = False
    if key[pygame.K_e]:
        GameStarted = True


    screen.blit(player,(Player[0] - 12.5,Player[1] - 12.5,Player[2],Player[3]))
    screen.blit(font.render(f"HP: {Stats[1]:.0f}", True, (255, 255, 255)),(Player[0] - 15,Player[1] - 35))
    pygame.draw.rect(screen,(66,66,66),(0,0,200,screen.get_height()))
    LaserTurretBuy = pygame.Rect(0,105,200,50)
    pygame.draw.rect(screen,(25,25,25),LaserTurretBuy)


    screen.blit(Buyfont.render(f"Laser Turret Costs: {CostValue[0]:.0f}", True, (255, 255, 255)),(0,105))
    screen.blit(Buyfont.render(f"Laser Turret amount: {Turrets[0]:.0f}", True, (255, 255, 255)),(0,105 + 15))
    if pygame.Rect(mx,my,1,1).colliderect(LaserTurretBuy):
        if key[pygame.K_e]:
            if Stats[3] > CostValue[0] - 1:
                Turrets[0] += 1
                Stats[3] -= CostValue[0]
                CostValue[0] += CostValue[0] / 25
                new_bullet = Bullet.spawn(screen.get_width(), screen.get_height())
                bullets.append(new_bullet)


    LaserTurretDMG = pygame.Rect(0,105 + 55 * 1,200,50)
    pygame.draw.rect(screen,(25,25,25),LaserTurretDMG)
    screen.blit(Buyfont.render(f"Laser Turret DMG costs: {CostValue[1]:.0f}", True, (255, 255, 255)),(0,105 + 55 * 1))
    screen.blit(Buyfont.render(f"Laser Turret DMG: {TurretDMG[0]:.1f}", True, (255, 255, 255)),(0,105 + 55 * 1 + 15))
    if pygame.Rect(mx,my,1,1).colliderect(LaserTurretDMG):
        if key[pygame.K_e]:
            if Stats[3] > CostValue[1] - 1:
                TurretDMG[0] += 0.1
                Stats[3] -= CostValue[1]
                CostValue[1] += CostValue[1] / 25


    SwordLengthBuy = pygame.Rect(0,105 + 55 * 2,200,50)
    pygame.draw.rect(screen,(25,25,25),SwordLengthBuy)
    screen.blit(Buyfont.render(f"Sword Length costs: {CostValue[2]:.0f}", True, (255, 255, 255)),(0,105 + 55 * 2))
    screen.blit(Buyfont.render(f"Sword Length: {SwordLength:.0f}", True, (255, 255, 255)),(0,105 + 55 * 2 + 15))
    if pygame.Rect(mx,my,1,1).colliderect(SwordLengthBuy):
        if key[pygame.K_e]:
            if Stats[3] > CostValue[2] - 1:
                SwordLength += 3
                Stats[3] -= CostValue[2]
                CostValue[2] += CostValue[2] / 25


    SwordDamageBuy = pygame.Rect(0,105 + 55 * 3,200,50)
    pygame.draw.rect(screen,(25,25,25),SwordDamageBuy)
    screen.blit(Buyfont.render(f"Sword Damage costs: {CostValue[3]:.0f}", True, (255, 255, 255)),(0,105 + 55 * 3))
    screen.blit(Buyfont.render(f"Sword Damage: {Stats[2]:.0f}", True, (255, 255, 255)),(0,105 + 55 * 3 + 15))
    if pygame.Rect(mx,my,1,1).colliderect(SwordDamageBuy):
        if key[pygame.K_e]:
            if Stats[3] > CostValue[3] - 1:
                Stats[2] += 1
                Stats[3] -= CostValue[3]
                CostValue[3] += CostValue[3] / 25


    CoreHpBuy = pygame.Rect(0,105 + 55 * 4,200,50)
    pygame.draw.rect(screen,(25,25,25),CoreHpBuy)
    screen.blit(Buyfont.render(f"Core HP Costs: {CostValue[4]:.0f}", True, (255, 255, 255)),(0,105 + 55 * 4))
    screen.blit(Buyfont.render(f"Core HP: {CoreMaxHP:.0f}", True, (255, 255, 255)),(0,105 + 55 * 4 + 15))
    if pygame.Rect(mx,my,1,1).colliderect(CoreHpBuy):
        if key[pygame.K_e]:
            if Stats[3] > CostValue[4] - 1:
                Stats[0] += 2500
                CoreMaxHP += 2500
                Stats[3] -= CostValue[4]
                CostValue[4] += CostValue[4] / 25


    CoreRegenBuy = pygame.Rect(0,105 + 55 * 5,200,50)
    pygame.draw.rect(screen,(25,25,25),CoreRegenBuy)
    screen.blit(Buyfont.render(f"Core Regen Costs: {CostValue[5]:.0f}", True, (255, 255, 255)),(0,105 + 55 * 5))
    screen.blit(Buyfont.render(f"Core Regen: {CoreRegen:.0f}", True, (255, 255, 255)),(0,105 + 55 * 5 + 15))
    if pygame.Rect(mx,my,1,1).colliderect(CoreRegenBuy):
        if key[pygame.K_e]:
            if Stats[3] > CostValue[5] - 1:
                CoreRegen += 1
                Stats[3] -= CostValue[5]
                CostValue[5] += CostValue[5] / 25
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    fpsgiver = int(clock.get_fps())
    pygame.draw.rect(screen,(0,0,0),(190,0,10,screen.get_height()))
    pygame.draw.rect(screen,(0,0,0),(screen.get_width() - 47,0,50,17))
    screen.blit(font.render(f"FPS: {fpsgiver:.0f}", True, (0,255,0)),(screen.get_width() - 45,0))
    screen.blit(font.render(f"CORE_HP: {Stats[0]:.0f}", True, (255, 255, 255)),(0,0))
    screen.blit(font.render(f"DMG: {Stats[2]:.0f}", True, (255, 255, 255)),(0,15))
    screen.blit(font.render(f"CASH: {Stats[3]:.0f}", True, (255, 255, 255)),(0,30))
    screen.blit(font.render(f"enemies: {len(enemies):.0f}", True, (255, 255, 255)),(0,45))
    screen.blit(WaveFont.render(f"WAVE: {Wave:.0f}", True, (255, 0, 0)),(0,60))
    screen.blit(WaveFont.render(f"WAVE: {Wave:.0f}", True, (255, 0, 0)),(1,61))
    screen.blit(WaveFont.render(f"WAVE: {Wave:.0f}", True, (0, 0, 0)),(2,62))
    screen.blit(WaveFont.render(f"WAVE: {Wave:.0f}", True, (0, 0, 0)),(3,63))
    if GameStarted == False:
        screen.blit(BigFont.render(f"Press E to start", True, (0,0,0)),(400,200))
        screen.blit(font.render(f"SPACE to attack", True, (0,0,0)),(400,190))
        screen.blit(font.render(f"E to buy items from shop", True, (0,0,0)),(400,175))
        screen.blit(font.render(f"W, A, S, D to move", True, (0,0,0)),(400,160))
    clock.tick(FPS)
    pygame.display.flip()