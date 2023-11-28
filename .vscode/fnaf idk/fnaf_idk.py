import pygame, random
pygame.init()
pygame.font.init()
font1 = pygame.font.Font(None, 30)  # Create a font object (thanks chatGPT)
screen = pygame.display.set_mode((900,700))
print(pygame.ver)
FPS = 60
ingame = 0
Mouse = pygame.mouse.get_pos()
MouseRect = pygame.Rect((0,0,1,1))
clock = pygame.time.Clock()
scrollx = 0
closed = [0,0,0,0]
load = pygame.image.load
scale = pygame.transform.scale
fnafroomidk = load("images/fnafroomidk.png")
fnafroomidk = scale(fnafroomidk, (1300,700))

running = True
while running:
    Mouse = pygame.mouse.get_pos()
    screen.fill((75,75,75))
    if ingame == 0:
        if MouseRect.colliderect(pygame.draw.rect(screen,(0,255,0),(700,550,200,75))):
            if (event.type == pygame.MOUSEBUTTONDOWN) == True:
                ingame = 1
        pygame.draw.rect(screen,(110,110,110),(700,0,200,700))
        pygame.draw.rect(screen,(0,255,0),(700,550,200,75))
        pygame.draw.rect(screen,(0,0,0),(700,0,10,700))
    if ingame == 1:
        screen.blit(fnafroomidk,(scrollx,0))
        if scrollx > -400:
            if Mouse[0] > 600:
                scrollx -= 8
        if scrollx < 0:
            if Mouse[0] < 100:
                scrollx += 8
    
    pygame.draw.rect(screen,(0,0,0),MouseRect)
    MouseRect.x = Mouse[0]
    MouseRect.y = Mouse[1]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(FPS)
    print("closed =",closed," scrollx =",scrollx)
pygame.quit()