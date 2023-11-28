import pygame

pygame.init()

# Set up the display
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("ASCII Art")

# Load the font
font = pygame.font.Font(None, 36)

# Load the image and convert it to ASCII
image = pygame.image.load("C:/Users/toivo/Downloads/thunahgbma.png")  # Replace with your image path
ascii_art = pygame.transform.scale(image, (80, 40))
ascii_characters = "@B%8WM#*oahkbdwmZO0QCJYXzcvnxrjft/\|()1{}[]-_+~<>i!lI;:,\"^`'. "
ascii_art_width, ascii_art_height = ascii_art.get_size()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the ASCII art
    screen.blit(ascii_art, ((window_size[0] - ascii_art_width) // 2, (window_size[1] - ascii_art_height) // 2))

    # Update the display
    pygame.display.flip()

pygame.quit()