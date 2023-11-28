import pygame, random
pygame.init()
pygame.font.init()
fps = 60
screen = pygame.display.set_mode((900, 600))
playerx = 0
playery = 0
player = pygame.Rect(playerx, playery, 25, 25)
yvel = 0
blockx = 0
blocky = 500
on_ground = False  # Flag to indicate if the player is on the ground
running = True

while running:
    screen.fill((50, 50, 140))
    for bx in range(3):
        for by in range(2):
            by = random.randint(-1,2)
            square = pygame.Rect(blockx + bx * 25, blocky + by * 25, 25, 25)
            pygame.draw.rect(screen, (111, 255, 111), square, 20)
            if player.colliderect(square):
                yvel = 0
                on_ground = True  # Set on_ground to True when player touches the square
    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        playerx += 5
    if key[pygame.K_a]:
        playerx -= 5
    if player.colliderect(square):
        playery -=1
    player = pygame.Rect(playerx, playery, 25, 25)
    
    if on_ground:
        if key[pygame.K_w]:
            yvel = -5
            on_ground = False
    else:
        yvel += 0.5  # Apply gravity when in the air
    
    playery += yvel
    pygame.draw.rect(screen, (111, 111, 111), player, 20)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    print("x =", playerx, "y =", playery)
    
    pygame.display.update()
    pygame.time.Clock().tick(fps)