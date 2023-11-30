import pygame, math, random, time, os


pygame.init()
pygame.font.init()
FPS = 60
pygame.display.set_caption("Your game name here")
screen = pygame.display.set_mode((500,500))
screen.fill((0, 100, 0))

font = pygame.font.SysFont("comicsansms", 15)

directory = os.getcwd()
directory = os.path.join(directory, "Assets")
osPath = os.path.join
load = pygame.image.load
scale = pygame.transform.scale
#ExampleImage = scale(load(osPath(directory, "Example.png")),(100,100))
pSize = [25,25]
x = screen.get_size()[0] / 2 - pSize[0] / 2
y = screen.get_size()[1] / 2 - pSize[1] / 2
player = pygame.Rect(x,y,pSize[0],pSize[1])
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    screen.fill((0, 100, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen,"red",player)

    fpsgiver = int(clock.get_fps())
    screen.blit(font.render(f"FPS: {fpsgiver}", True, (255, 255, 255)),(0,0))
    pygame.display.flip()