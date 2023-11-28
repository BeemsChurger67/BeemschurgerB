import random, pygame.font, pygame
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((900, 500))
running = True
fps = 60  # Default FPS
PlayerPos = [0, 0]
Velocity = 0
JumpPower = 7
Speed = 0
# Font for displaying FPS
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()  # Create the Clock object outside the loop

while running:
    key = pygame.key.get_pressed()
    screen.fill((61, 61, 155))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    ground = pygame.draw.rect(screen, ((0,0,200)), (0,400, 900,100))
    player = pygame.draw.rect(screen, ((255, 255, 0)), (PlayerPos[0], PlayerPos[1], 50,50))
    pygame.draw.rect(screen, ((0,0,0)), (0,400, 900,5))
    #Ground collision
    if not player.colliderect(ground):
        # in the air
        Velocity += 0.25
        PlayerPos[1] += Velocity
    else:
        Velocity = 0
        while player.colliderect(ground):
            PlayerPos[1] -= 1
            player = pygame.draw.rect(screen, ((255, 255, 0)), (PlayerPos[0], PlayerPos[1], 50,50))
        if key[pygame.K_UP]:
            PlayerPos[1] -= 1
            Velocity -= 6

    
    elapsed_time = clock.tick(fps)
    current_fps = clock.get_fps()
    fps_text = font.render(f"FPS: {current_fps:.2f}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))

    pygame.display.update()
