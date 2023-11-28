import pygame
pygame.init()
pygame.font.init()

screenwidth = 700
screenheight = 700
screen = pygame.display.set_mode((screenwidth, screenheight))
running = True
blockX = []
blockY = []
block_Type = []
block_Amount = []
D = True
while running:
    mx, my = pygame.mouse.get_pos()
    screen.fill((100, 100, 100))
    for A in range(int(screenwidth / 50)):
        for B in range(int(screenwidth / 50)):
            tile_rect = pygame.Rect(A * 50, B * 50, 50, 50)
            pygame.draw.rect(screen, (0, 0, 0), tile_rect, width=2)
            if tile_rect.collidepoint(mx, my):
                pygame.draw.rect(screen, (0, 0, 0), tile_rect)
    for C in range(int(len(block_Amount))):
        pygame.draw.rect(screen,(70,0,70),(blockX[C] * 50,blockY[C] * 50,50,50))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:  # Right mouse button
                D = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3 and D:
                D = False
                del blockX[C], blockY[C], block_Type[C], block_Amount[C]
    
                

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                clicked_tile_x = mx // 50
                clicked_tile_y = my // 50
                blockX.append(clicked_tile_x)
                blockY.append(clicked_tile_y)
                block_Type.append("conveyor")
                block_Amount.append(len(block_Amount))

                

    pygame.display.flip()

pygame.quit()