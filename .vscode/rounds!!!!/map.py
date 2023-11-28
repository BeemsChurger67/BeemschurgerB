import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
import math
import sys

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('game')

# Load player image
player_image = pygame.image.load('Images/player.png')

# Resize player image
new_width = 50
new_height = 50
player_image = pygame.transform.scale(player_image, (new_width, new_height))

# Initialize player position
player_x = 0
player_y = 0

# Initialize bullet variables
bullets = []  # List to store bullet positions
bullet_speed = 5  # Adjust the speed as needed

# Set up the clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60  # Desired frame rate

running = True
while running:
    screen.fill((128, 128, 128))  # Use RGB tuple for gray color
    
    # Draw the player character
    screen.blit(player_image, (player_x, player_y))
    
    for bullet in bullets:
        pygame.draw.circle(screen, (255, 0, 0), (int(bullet[0]), int(bullet[1])), 5)  # Red circle for bullets

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_x, mouse_y = pygame.mouse.get_pos()
                
                # Calculate the direction vector towards the mouse cursor
                direction_x = mouse_x - player_x
                direction_y = mouse_y - player_y
                
                # Normalize the direction vector
                length = math.sqrt(direction_x ** 2 + direction_y ** 2)
                if length != 0:
                    direction_x /= length
                    direction_y /= length
                
                # Create a bullet with initial position and direction
                bullets.append([player_x, player_y, direction_x * bullet_speed, direction_y * bullet_speed])

    # Update bullet positions
    for bullet in bullets:
        bullet[0] += bullet[2]  # Update X position
        bullet[1] += bullet[3]  # Update Y position
        
        # Remove bullets that go off-screen
        if bullet[0] < 0 or bullet[0] > 400 or bullet[1] < 0 or bullet[1] > 300:
            bullets.remove(bullet)

    pygame.display.update()
    clock.tick(FPS)  # Control the frame rate

pygame.quit()
sys.exit()