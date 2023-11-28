import pygame, math, random, time, pyautogui
pygame.init()
pygame.font.init()
FPS = 60
pygame.display.set_caption("bruh")
screen = pygame.display.set_mode((750,750))
screen.fill((0, 100, 0))
font = pygame.font.SysFont("comicsansms", 15)
load = pygame.image.load
scale = pygame.transform.scale
stick = load("stick.png")
stick = scale(stick,(125,50))
clock = pygame.time.Clock()
running = True
x = 0
y = 0
player = pygame.Rect(x,y,25,25)
def swordAttack():
    mx, my = pygame.mouse.get_pos()  # Get mouse position

    # Calculate angle towards mouse cursor
    dx = mx - player.centerx
    dy = my - player.centery
    angle = math.degrees(math.atan2(dy, dx))

    # Rotate the stick and create a new rectangle to center it properly
    rotated_stick = pygame.transform.rotate(stick, -angle)
    rotated_rect = rotated_stick.get_rect(center=(player.centerx, player.centery))

    # Blit the rotated image to the screen
    screen.blit(rotated_stick, rotated_rect)

while running:
    key = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()
    mousePress = pygame.mouse.get_pressed()
    if key[pygame.K_a]:
        x -= 2
    if key[pygame.K_d]:
        x += 2
    if key[pygame.K_s]:
        y += 2
    if key[pygame.K_w]:
        y -= 2
    player = pygame.Rect(x,y,25,25)
    clock.tick(FPS)
    screen.fill((0, 100, 0))
    pygame.draw.rect(screen,(255,255,255),player)
    if mousePress[0]:
        swordAttack()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    fpsgiver = int(clock.get_fps())
    screen.blit(font.render(f"FPS: {fpsgiver}", True, (255, 255, 255)),(0,0))
    pygame.display.flip()