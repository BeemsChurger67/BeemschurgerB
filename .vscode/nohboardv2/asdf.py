import pygame
import threading
import keyboard

pygame.init()
pygame.font.init()
font1 = pygame.font.Font(None, 30)
screen = pygame.display.set_mode((450, 200))
title = pygame.display.set_caption("nohboard")

# Define the key labels and key codes
key_labels = [
    (pygame.K_a, "A"),
    (pygame.K_s, "S"),
    (pygame.K_d, "D"),
    (pygame.K_f, "F"),
    (pygame.K_SPACE, "SPACE"),
    (pygame.K_j, "J"),
    (pygame.K_k, "K"),
    (pygame.K_l, "L"),
    (246, "Ö"),  # Unicode code point for Ö
]

key_state = {key: False for key, _ in key_labels}
button_press_counts = {key: 0 for key, _ in key_labels}

def buttonpress(x, y, sx, sy, width, keypress):
    key = pygame.key.get_pressed()

    for k, label in key_labels:
        if keypress == k:
            if key[k]:
                if not key_state[k]:
                    button_press_counts[k] += 1
                    key_state[k] = True
            else:
                key_state[k] = False
                pygame.draw.rect(screen, (0, 0, 255), (x, y, sx, sy))
            text = pygame.font.Font(None, 30).render(label, True, (0, 0, 0))
            screen.blit(text, (x + sx / 2 - 9, y + sy / 2 - 9))
            text = pygame.font.Font(None, 30).render(str(button_press_counts[k]), True, (255, 255, 255))
            screen.blit(text, (x + sx / 2 - 9, y + sy / 2 + 25))

    pygame.draw.rect(screen, (0, 0, 0), (x, y, sx, sy), width=width)

def total_presses():
    total_count = sum(button_press_counts.values())
    text = pygame.font.Font(None, 30).render(f"Total: {total_count}", True, (255,255,255))
    screen.blit(text, (200, 150))

def on_key_event(e):
    for _, label in key_labels:
        if label == e.name:
            button_press_counts[246] += 1
            break

keyboard.hook(on_key_event)

running = True

while running:
    screen.fill("dark blue")
    buttonpress(0, 0, 50, 50, 3, pygame.K_a)
    buttonpress(50, 0, 50, 50, 3, pygame.K_s)
    buttonpress(100, 0, 50, 50, 3, pygame.K_d)
    buttonpress(150, 0, 50, 50, 3, pygame.K_f)
    buttonpress(175, 75, 100, 50, 3, pygame.K_SPACE)
    buttonpress(250, 0, 50, 50, 3, pygame.K_j)
    buttonpress(300, 0, 50, 50, 3, pygame.K_k)
    buttonpress(350, 0, 50, 50, 3, pygame.K_l)
    buttonpress(400, 0, 50, 50, 3, 246)

    total_presses()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

keyboard.unhook_all()
