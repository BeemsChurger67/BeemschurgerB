import turtle,random,time,sys,pygame
pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("NOT ball platformer")
x = 0;
y = 0;
yvel = 0
block = pygame.Rect((0,325,100,25))
lava = pygame.Rect((0,375,500,500))
player = pygame.Rect((x, y, 25, 25))
win = pygame.Rect((350,0,200,500))
fps = 60
run = True
while run:
    screen.fill((175,238,238))
    pygame.draw.rect(screen,(0,0,0),block)
    pygame.draw.rect(screen,(111,111,111),player)
    pygame.draw.rect(screen,(255,0,0),lava)
    pygame.draw.rect(screen,(0,255,0),win)
    player.move_ip(0 - x,0 - y)
    key = pygame.key.get_pressed()
    if(x > 0):
        if key[pygame.K_a] == True:
            x -= 5
    if(x < 475):
        if key[pygame.K_d] == True:
            x += 5
    if(x > 350):
        print("win")
        run = False
    if(y < 300):
        yvel += 0.5
    else:
        if(x < 100):
            yvel = 0
            if key[pygame.K_w] == True:
                yvel -= 15
        else:
            yvel += 0.5
    y += yvel
    if(y > 301):
        y -= 5
    if(y > 374):
        run = False
    player.move_ip(x,y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    print("x =",x,"y =",0 - y)
    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(fps)
pygame.quit()