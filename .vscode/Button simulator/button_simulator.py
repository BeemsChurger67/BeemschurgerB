# special thanks to chatGPT
print("game has opened")
import pygame
import time
import random
import sys
import pickle
import os
import math
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((700,700))
chicken = pygame.display
pygame.display.set_caption("Button Simulator")
screen.fill("gray")
mouse = pygame.mouse.get_pos()
print("pygame version =", pygame.ver)
gens_bought  = [0,0,0,0,0,0,0,0,0]
poupgradepower = [1,1,1,1,1,1,1,1]
presup = [1,0,0,0,0]
clock = pygame.time.Clock()
quests = [0,0,0,0,0,0,0,0,0,1]
TickSpeed = 200
activegen = 0
points = [0,0,0,0,0,0,0,0,0,0,0,0]
#points = [1000000,1000000,1000000,1000000,1000000] #CHEATS ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
big_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
achievementson = 0
achievementsget = [0,0,0,0,0,0,0,0,0,0,0,0]
upgtree = [0,0]
page = 0
stats = [0,0,0,0,0,0]
crash = 0
crashtime = 0
key = pygame.key.get_pressed()
font0 = pygame.font.Font(None, 70)  # Create a font object (thanks chatGPT)
font1 = pygame.font.Font(None, 30)  # Create a font object (thanks chatGPT)
font2 = pygame.font.Font(None, 25)  # Create a font object (thanks chatGPT)
font3 = pygame.font.Font(None, 20)  # Create a font object (thanks chatGPT)
#Points[0] are points req: free
#Points[1] are prestige points req: 500 points
#Points[2] are chicken points req: 1M points
#Points[3] are quest points req: complete a quest
#Points[4] are mega points req 
#Points[5] are flame points
def gencollision():
    global points, activegen, gens_bought, mouse, presup, page, key, TickSpeed, stats, achievementson
    mx,my = pygame.mouse.get_pos()
    key = pygame.key.get_pressed()
    # arrow buttons
    # left arrow button
    if pygame.Rect(0, 0, 50, 50).collidepoint(mx, my):
        if activegen == 0 and achievementson == 0:
            if event.type == pygame.MOUSEBUTTONDOWN or key[pygame.K_e] == True:
                if pygame.MOUSEBUTTONDOWN:
                    activegen = 1
                    stats[0] += 1
                if page > -4:
                    page -= 1
                print("pointup:",poupgradepower,"tickspeed:",TickSpeed,"points:",points,"gens:",gens_bought,"page:",page)
    # right arrow button
    if pygame.Rect(650, 0, 50,50).collidepoint(mx, my):
        if activegen == 0 and achievementson == 0:
            if event.type == pygame.MOUSEBUTTONDOWN or key[pygame.K_e] == True:
                if pygame.MOUSEBUTTONDOWN:
                    activegen = 1
                    stats[0] += 1
                if page < 4:
                    page += 1 #69th line of code (or used to be)
                print("pointup:",poupgradepower,"tickspeed:",TickSpeed,"points:",points,"gens:",gens_bought,"page:",page)
    # point generator 
    global pointamount
    pointamount = poupgradepower[0] * poupgradepower[1] * poupgradepower[2] * poupgradepower[3] * poupgradepower[4] * poupgradepower[5] 
    if gens_bought[0] == 1:
        points[0] += pointamount
        stats[1] += pointamount
        if quests[2] < quests[1]:
            quests[2] += pointamount
    if(page == 0):
        if gens_bought[0] == 0:
            if pygame.Rect(250, 575, 200, 75).collidepoint(mx, my):
                if activegen == 0 and achievementson == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN or key[pygame.K_e] == True:
                        if pygame.MOUSEBUTTONDOWN:
                            activegen = 1
                            stats[0] += 1
                        gens_bought[0] = 1
                        print("pointup:",poupgradepower,"tickspeed:",TickSpeed,"points:",points,"gens:",gens_bought,"page:",page)
        # point upgrader
        if(points[0] < (25 * (poupgradepower[0] * (poupgradepower[0]) * ((poupgradepower[0]) * 10)))) - 1:
            if pygame.Rect(50, 450, 200, 75).collidepoint(mx, my):
                if activegen == 0 and achievementson == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN or key[pygame.K_e] == True:
                        if pygame.MOUSEBUTTONDOWN:
                            activegen = 1
                            stats[0] += 1
                        points[0] -= (25 * (poupgradepower[0] * (poupgradepower[0]) * ((poupgradepower[0]) * 10)))
                        poupgradepower[0] += 1
                        print("pointup:",poupgradepower,"tickspeed:",TickSpeed,"points:",points,"gens:",gens_bought,"page:",page)
                            
    if (page == 1):     
        # prestige giver
        if((points[0] > (500 / presup[0]))):
            if pygame.Rect(250, 575, 200, 75).collidepoint(mx, my):
                if activegen == 0 and achievementson == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN or key[pygame.K_e] == True:
                        if pygame.MOUSEBUTTONDOWN:
                            activegen = 1
                            stats[0] += 1
                        points[1] += points[0] / (500 / presup[0] + 1)
                        stats[2] += points[0] / (500 / presup[0] + 1)
                        gens_bought[0] = 0
                        poupgradepower[0] = 1
                        if quests[0] == 1:
                            quests[4] += points[0] / (500 / presup[0])
                        points[0] = 0
                        print("pointup:",poupgradepower,"tickspeed:",TickSpeed,"points:",points,"gens:",gens_bought,"page:",page)
        # prestige upgrader
        if presup[0] <= 15:
            if points[1] > ((5 * (presup[0] * presup[0] * presup[0])) - 1):
                if pygame.Rect(500, 545, 200, 75).collidepoint(mx, my):
                    if activegen == 0 and achievementson == 0:
                        if event.type == pygame.MOUSEBUTTONDOWN or key[pygame.K_e] == True:
                            if pygame.MOUSEBUTTONDOWN:
                                activegen = 1
                                stats[0] += 1
                            points[1] -= (5 * (presup[0] * presup[0] * presup[0]))
                            presup[0] += 1
                            print("pointup:",poupgradepower,"tickspeed:",TickSpeed,"points:",points,"gens:",gens_bought,"page:",page)
        # prestige point upgrader
        if(points[1] > ((25 * (poupgradepower[1] * (poupgradepower[1]) * (poupgradepower[1])))) - 1):
            if pygame.Rect(500, 465, 200, 75).collidepoint(mx, my):
                if activegen == 0 and achievementson == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN or key[pygame.K_e] == True:
                        if pygame.MOUSEBUTTONDOWN:
                            activegen = 1
                            stats[0] += 1
                        points[1] -= (25 * (poupgradepower[1] * (poupgradepower[1]) * (poupgradepower[1])))
                        poupgradepower[1] += 1
                        print("pointup:",poupgradepower,"tickspeed:",TickSpeed,"points:",points,"gens:",gens_bought,"page:",page)
    if(page == 2):
        # chicken point giver
        if(points[0] > 999999):
            if pygame.Rect(250, 575, 200, 75).collidepoint(mx, my):
                if activegen == 0 and achievementson == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN or key[pygame.K_e] == True:
                        if pygame.MOUSEBUTTONDOWN:
                            activegen = 1
                            stats[0] += 1
                        points[2] += points[0] / 1000000
                        stats[3] += points[0] / 1000000
                        points[0] = 0
                        gens_bought[0] = 0
                        poupgradepower[0] = 1
                        print("pointup:",poupgradepower,"tickspeed:",TickSpeed,"points:",points,"gens:",gens_bought,"page:",page)
        # chicken tickspeed giver
        if(points[2] > (2 * (TickSpeed - 199) - 1)):
            if pygame.Rect(250, 495, 200, 75).collidepoint(mx, my):
                if activegen == 0 and achievementson == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN or key[pygame.K_e] == True:
                        if pygame.MOUSEBUTTONDOWN: 
                            activegen = 1
                            stats[0] += 1
                        points[2] -= 2 * (TickSpeed - 199)
                        TickSpeed += 3
                        print("pointup:",poupgradepower,"tickspeed:",TickSpeed,"points:",points,"gens:",gens_bought,"page:",page)
    # Mega point giver
    if page == 3:
        if points[1] > 9999:
            if pygame.Rect(250, 575, 200, 75).collidepoint(mx, my):
                if activegen == 0 and achievementson == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN or key[pygame.K_e] == True:
                        if pygame.MOUSEBUTTONDOWN:
                            activegen = 1
                            stats[0] += 1
                        points[4] += points[1] / 9999
                        stats[5] += points[1] / 9999
                        presup[0] = 1
                        gens_bought[0] = 0
                        poupgradepower[0] = 1
                        poupgradepower[1] = 1
                        points[1] = 0
                        points[0] = 0
                        print("pointup:",poupgradepower,"tickspeed:",TickSpeed,"points:",points,"gens:",gens_bought,"page:",page)
    # Mega point multiplier
    if page == 3:
        if points[4] > 99:
            if pygame.Rect(250, 490, 200, 75).collidepoint(mx, my):
                if activegen == 0 and achievementson == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN or key[pygame.K_e] == True:
                        if pygame.MOUSEBUTTONDOWN:
                            activegen = 1
                            stats[0] += 1
                        points[4] -= 100
                        poupgradepower[3] += 15
                        print("pointup:",poupgradepower,"tickspeed:",TickSpeed,"points:",points,"gens:",gens_bought,"page:",page)
    # Flame point giver
    if page == 4:
        if points[4] > 50000000 - 1:
            if pygame.Rect(250, 575, 200, 75).collidepoint(mx, my):
                if activegen == 0 and achievementson == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN or key[pygame.K_e] == True:
                        if pygame.MOUSEBUTTONDOWN:
                            activegen = 1
                            stats[0] += 1
                        points[5] += points[4] / 50000000
                        stats[5] += points[4] / 50000000
                        presup[0] = 1
                        gens_bought[0] = 0
                        poupgradepower[0] = 1
                        poupgradepower[1] = 1
                        poupgradepower[3] = 1
                        points[4] = 0
                        points[1] = 0
                        points[0] = 0
                        print("pointup:",poupgradepower,"tickspeed:",TickSpeed,"points:",points,"gens:",gens_bought,"page:",page)
        # Flame point point multiplier
        if points[5] > 100000 * poupgradepower[4] * poupgradepower[4]:
            if pygame.Rect(250, 490, 200, 75).collidepoint(mx, my):
                if activegen == 0 and achievementson == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN or key[pygame.K_e] == True:
                        if pygame.MOUSEBUTTONDOWN:
                            activegen = 1
                            stats[0] += 1
                        points[4] -= 100000 * poupgradepower[4] * poupgradepower[4]
                        poupgradepower[4] += 1
                        print("pointup:",poupgradepower,"tickspeed:",TickSpeed,"points:",points,"gens:",gens_bought,"page:",page)
    # quests and achievements
    if page == -1:
        if quests[0] == 0:
            if pygame.Rect(0, 50, 200, 75).collidepoint(mx, my):
                if activegen == 0 and achievementson == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN or key[pygame.K_e] == True:
                        if pygame.MOUSEBUTTONDOWN:
                            activegen = 1
                            stats[0] += 1
                        quests[0] = 1
                        quests[1] = random.randint(1000 * quests[9] * quests[9] * (quests[9] * quests[9] * quests[9]),1000000 * quests[9] * quests[9] * (quests[9] * quests[9] * quests[9]))
                        quests[3] = random.randint(10 * quests[9] * quests[9] * (quests[9] * quests[9] * quests[9]),100 * quests[9] * quests[9] * (quests[9] * quests[9] * quests[9]))
                        print("pointup:",poupgradepower,"tickspeed:",TickSpeed,"points:",points,"gens:",gens_bought,"page:",page)
    if page == -1 or achievementson == 1:
        # achievements
        if pygame.Rect(250, 575, 200, 75).collidepoint(mx, my):
            if activegen == 0:
                if event.type == pygame.MOUSEBUTTONDOWN or key[pygame.K_e] == True:
                    if pygame.MOUSEBUTTONDOWN:
                        activegen = 1
                        stats[0] += 1
                    if achievementson == 1:
                        achievementson = 0
                    else:
                        achievementson = 1
                    print("pointup:",poupgradepower,"tickspeed:",TickSpeed,"points:",points,"gens:",gens_bought,"page:",page)
    # quest completion
    if quests[0] == 1:
        if (quests[2] > quests[1] - 1) and (quests[4] > quests[3] - 1):
            points[3] += (quests[1] + quests[3]) / 200
            stats[4] += (quests[1] + quests[3]) / 200
            quests[0] = 0
            quests[1] = 0
            quests[2] = 0
            quests[3] = 0 
            quests[4] = 0
            quests[9] += 1
            print(f"Quest {quests[9]} Complete!")
            print("pointup:",poupgradepower,"tickspeed:",TickSpeed,"points:",points,"gens:",gens_bought,"page:",page)
    # quest upgrades
    if page == -2:
        if pygame.Rect(0, 625, 200, 75).collidepoint(mx, my):
            if points[3] > (200 * poupgradepower[2] * poupgradepower[2]) - 1:
                if activegen == 0 and achievementson == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN or key[pygame.K_e] == True:
                        if pygame.MOUSEBUTTONDOWN:
                            stats[0] += 1
                            activegen = 1
                        points[3] -= 200 * poupgradepower[2] * poupgradepower[2]
                        poupgradepower[2] += 3
                        print("pointup:",poupgradepower,"tickspeed:",TickSpeed,"points:",points,"gens:",gens_bought,"page:",page)
def achievementcomplete(achtext,reward,pointtype,howmuch):
    screen.blit(font1.render(f"ACHIEVEMENT COMPLETE", True, (0,255,0)),(200,30))
    screen.blit(font1.render(f"{achtext}", True, (0,255,0)),(200,50))
    screen.blit(font1.render(f"Reward: {reward}", True, (0,255,0)),(200,70))
    points[pointtype] += howmuch / 1000
    stats[pointtype + 1] += howmuch / 1000
load = pygame.image.load
scale = pygame.transform.scale
directory = os.getcwd()
converted_path = directory.replace('\\', '/')
print(converted_path)
# Get the absolute path of the script directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the absolute path to the images directory
images_directory = os.path.join(script_directory, "images")
achievements_directory = os.path.join(images_directory, "achievements")

# Load the images using the absolute path
leftarrow = load(os.path.join(images_directory, "leftpage.png"))
leftarrow = scale(leftarrow, (50, 50))
rightarrow = load(os.path.join(images_directory, "rightpage.png"))
rightarrow = scale(rightarrow, (50, 50))
pointgenerator = load(os.path.join(images_directory, "Pointgen.png"))
pointgenerator = scale(pointgenerator, (200, 75))
pointupg = load(os.path.join(images_directory,"Point multiplier.png"))
pointupg = scale(pointupg, (200, 75))
prestige = load(os.path.join(images_directory,"Prestige button.png"))
prestige = scale(prestige, (200, 75))
prestigeupg = load(os.path.join(images_directory,"prestige upgrader.png"))
prestigeupg = scale(prestigeupg, (200, 75))
prestigepointupg = load(os.path.join(images_directory,"prestige point upgrader.png"))
prestigepointupg = scale(prestigepointupg, (200, 75))
megapoint = load(os.path.join(images_directory,"Mega points.png"))
megapoint = scale(megapoint, (200, 75))
chickenpoint = load(os.path.join(images_directory,"chicken point.png"))
chickenpoint = scale(chickenpoint, (200, 75))
chickentickspeedupg = load(os.path.join(images_directory,"chicken tickspeed upgrade.png"))
chickentickspeedupg = scale(chickentickspeedupg, (200, 75))
easyquests = load(os.path.join(images_directory,"easyquests.png"))
easyquests = scale(easyquests, (200, 700))
randomquest = load(os.path.join(images_directory,"getquest.png"))
randomquest = scale(randomquest, (200, 75))
questpointmulti = load(os.path.join(images_directory,"Questpointmulti.png"))
questpointmulti = scale(questpointmulti, (200, 75))
megapointpointmulti = load(os.path.join(images_directory,"Mega point point multi.png"))
megapointpointmulti = scale(megapointpointmulti, (200, 75))
flamepointgiver = load(os.path.join(images_directory,"Flamepointgiver.png"))
flamepointgiver = scale(flamepointgiver, (200, 75))
flamepointpointmulti = load(os.path.join(images_directory,"Flamepointpointmulti.png"))
flamepointpointmulti = scale(flamepointpointmulti, (200, 75))
bg = load(os.path.join(images_directory,"coolcolorbg.png"))
bg = scale(bg, (screen.get_width(), screen.get_height()))
#achievements
achievements = load(os.path.join(achievements_directory,"showachievements.png"))
achievements = scale(achievements, (200, 75))
achievementslist = load(os.path.join(achievements_directory,"Achievementslist.png"))
achievementslist = scale(achievementslist, (600,screen.get_height()))
button1000times = load(os.path.join(achievements_directory,"button1000press.png"))
button1000times = scale(button1000times, (75,75))
onehundredkpoints = load(os.path.join(achievements_directory,"get100kpoints.png"))
onehundredkpoints = scale(onehundredkpoints, (75,75))
onehundredmpoints = load(os.path.join(achievements_directory,"get100mpoints.png"))
onehundredmpoints = scale(onehundredmpoints, (75,75))
onehundredbpoints = load(os.path.join(achievements_directory,"get100bpoints.png"))
onehundredbpoints = scale(onehundredbpoints, (75,75))
onehundredtpoints = load(os.path.join(achievements_directory,"get100tpoints.png"))
onehundredtpoints = scale(onehundredtpoints, (75,75))
onehundredquintilpoints = load(os.path.join(achievements_directory,"get100Quintil.png"))
onehundredquintilpoints = scale(onehundredquintilpoints, (75,75))
# Initialize variables
start_time = 0
elapsed_time = 0
def save_game():
    global start_time, elapsed_time,screen
    print("SAVED GAME")
    print(directory)
    current_time = time.time()
    elapsed_time = current_time - start_time  # Update elapsed time
    with open("SaveFile", "wb") as file:
        pickle.dump((points, gens_bought, poupgradepower, presup, page, stats, quests, TickSpeed, elapsed_time,achievementsget), file)

def load_game():
    global points, gens_bought, poupgradepower, presup, page, stats, quests, TickSpeed, elapsed_time, start_time,achievementsget
    try:
        with open("SaveFile", "rb") as file:
            points, gens_bought, poupgradepower, presup, page, stats, quests, TickSpeed, elapsed_time,achievementsget = pickle.load(file)
            start_time = time.time() - elapsed_time  # Calculate start time based on elapsed time
    except FileNotFoundError:
        print("No saved game found.")

load_game()
for bruh in range(100):
    achievementsget.append(0)

folder_path = os.getcwd()
convertfolderpath = os.getcwd()
files = os.listdir(folder_path)
num_files = len(files)
print(num_files)
for file_name in os.listdir(folder_path):
    print(file_name)
    break
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        if file_name.endswith(".py"):
            os.system(f'python "{file_path}"')
            if ModuleNotFoundError == True or ImportError == True:
                break
if ModuleNotFoundError == True:
    crash = 1
    crashtime = 0
    print(f"mods folder had an issue experiencing an error. {ModuleNotFoundError}")
if ImportError == True:
    crash = 2
    crashtime = 0
    print(f"mods folder had an issue experiencing an error. {ImportError}")
mods_path = os.path.join(os.path.dirname(__file__), 'mods')
sys.path.append(mods_path)
if any(file.endswith('.py') for file in files):
    pass
    #from mods import mod as c
    # PLACE THE MODS FUNCTIONS BELOW
    #c.pointgive()
print("pointup:",poupgradepower,"tickspeed:",TickSpeed,"points:",points,"gens:",gens_bought,"page:",page)
fps = int(clock.get_fps())
frametimer = 0
pointspersecond = font1.render(f"Points/second: {poupgradepower[0] * poupgradepower[1] * poupgradepower[2] * poupgradepower[3] * fps}", True, (0,0,0))
scroll_direction = -50
savetimer = 0
# WHILE RUNNING LOOP -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
running = True
while running:
    current_time = time.time()
    if start_time == 0:
        start_time = current_time - elapsed_time  # Calculate start time if it's the first run
    elapsed_time = current_time - start_time  # Update elapsed time
    elapsed_seconds = int(elapsed_time)
    screen.fill("gray")
    screen.blit(bg,(0,0))
    if page == -1:
        screen.blit(easyquests,(0,0))
        screen.blit(randomquest,(0,50))
        screen.blit(achievements,(250, 575))
    if page == -1:
        page_text = font1.render(f"Quests", True, (0,0,0))
        screen.blit(page_text, (325,0))
    elif page == -2:
        page_text = font1.render(f"Quest upgrades", True, (0,0,0))
        screen.blit(page_text, (290,0))    
    elif page == -3:
        page_text = font1.render(f"Battle", True, (0,0,0))
        screen.blit(page_text, (325,0))    
    elif page == -4:
        page_text = font1.render(f"Statistics", True, (0,0,0))
        screen.blit(page_text, (325,0))
    else:
        page_text = font1.render(f"Page {page + 1}", True, (0,0,0))
        screen.blit(page_text, (325,0))
    #420th line of code (or used to be)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            current_saved_time = current_time
            save_game()
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll up
                if scroll_direction > -50:
                    scroll_direction -= 10
            elif event.button == 5:  # Scroll down
                if scroll_direction < 50:
                    scroll_direction += 10

    mouse = pygame.mouse.get_pos()
    if not page == -3:
        screen.blit(leftarrow, (0, 0))
    if not page == 4:
        screen.blit(rightarrow, (650, 0))
    if(page == 0):
        if(points[0] > 0):
            pygame.draw.line(screen,(0,0,0),(300,620),(150,500), width=55)
            pygame.draw.line(screen,(155,155,255),(300,620),(150,500), width=35)
            screen.blit(pointupg, (50, 450))
        screen.blit(pointgenerator, (250, 575))
    if(page == 1):
        screen.blit(prestige, (250, 575))
        if(points[1] > 0):
            screen.blit(prestigeupg, (500, 545))
            screen.blit(prestigepointupg, (500, 465))
    if(page == 2):
        screen.blit(chickenpoint, (250, 575))
        if points[2] > 1:
            screen.blit(chickentickspeedupg,(250,495))
    if(page == 3):
        screen.blit(megapoint, (250, 575))
        if points[4] > 0:
            screen.blit(megapointpointmulti, (250, 490))
    if page == 4:
        screen.blit(flamepointgiver,(250,575))
        if points[5] > 0:
            screen.blit(flamepointpointmulti,(250,490))
        
    if page == -2:
        screen.blit(questpointmulti, (0, 625))
    if event.type == pygame.MOUSEBUTTONUP:
        activegen = 0
    gencollision()
    # Calculate the FPS (thanks chatgpt)
    fps = int(clock.get_fps())
    # Update the window's caption with the FPS value (thanks chatgpt)
    pygame.display.set_caption(f"Button Simulator | FPS: {fps:.2f}")
    # Render variable values on the screen (thanks chatGPT)
    points_text = font1.render(f"Points: {points[0]:.2f}", True, (0,0,0))
    prestige_text = font1.render(f"Prestige points: {points[1]:.2f}", True, (0,0,0))
    questpoints_text = font1.render(f"Quest points: {points[3]:.2f}", True, (0,0,0))
    flamepoints_text = font1.render(f"Flame points: {points[5]:.2f}", True, (0,0,0))
    questfortext = font1.render(f": {points[3]:.2f}", True, (0,0,0))
    tickspeed_text = font1.render(f"Tickspeed: {TickSpeed:.2f}", True, (0,0,0))
    chicken_text = font1.render(f"Chicken points: {points[2]:.2f}", True, (0,0,0))
    megaptext = font1.render(f"Mega points: {points[4]:.2f}", True, (0,0,0))
    if presup[0] == 16:
        prestigemulti_text = font2.render(f"MAXED OUT", True, (0,0,0))
    else:
        prestigemulti_text = font2.render(f"req: {((5 * (presup[0] * presup[0] * presup[0])) - 1):.2f}prestige points", True, (0,0,0))
    clickstext = font1.render(f"button clicks: {stats[0]:.2f}", True, (0,0,0))
    allpointstext = font1.render(f"all points: {stats[1]:.2f}", True, (0,0,0))
    allpptext = font1.render(f"all prestige points: {stats[2]:.2f}", True, (0,0,0))
    allchickenp = font1.render(f"all chicken points: {stats[3]:.2f}", True, (0,0,0))
    allquestp = font1.render(f"all quest points: {stats[4]:.2f}", True, (0,0,0))
    allmegap = font1.render(f"all mega points: {stats[5]:.2f}", True, (0,0,0))
    pointquest_text = font1.render(f"Quest point amount: {quests[2]:.2f}/{quests[1]:.2f}", True, (0,0,0))
    prestigequest_text = font1.render(f"Quest prestige amount: {quests[4]:.2f}/{quests[3]:.2f}", True, (0,0,0))
    questsdone_text = font1.render(f"Quests done: {quests[9] - 1:.2f}", True, (0,0,0))
    extra_text1 = font1.render(f"Point upgrades: {poupgradepower}", True, (0,0,0))
    extra_text2 = font1.render(f"Prestige upgrades: {presup}", True, (0,0,0))
    pointsperframetext = font1.render(f"Points/frame: {poupgradepower[0] * poupgradepower[1] * poupgradepower[2] * poupgradepower[3]:.2f}", True, (0,0,0))
    frametimer += 1
    if frametimer == 100:
        pointspersecond = font1.render(f"Points/second: {poupgradepower[0] * poupgradepower[1] * poupgradepower[2] * poupgradepower[3] * fps:.2f}", True, (0,0,0))
        frametimer = 0
    megapointpointmultitext = font1.render(f" {pointamount -1}", True, (0,0,0))
    secondtimer_text = font1.render("played: {} seconds".format(elapsed_seconds), True, (0,0,0))
    minutetimer_text = font1.render("played: {} minutes".format(round((elapsed_seconds / 60) - 0.5)), True, (0,0,0))
    hourtimer_text = font1.render("played: {} hours".format(round((elapsed_seconds / 3600) - 0.5)), True, (0,0,0))
    if crashtime < 2500:
        crashtime += 1
        if ModuleNotFoundError == True:
            screen.blit(pygame.font.Font(None, 25).render(F"{ModuleNotFoundError}", True, (0,0,0)),(0,300))
        if ImportError == True:
            screen.blit(pygame.font.Font(None, 25).render(F"{ImportError}", True, (0,0,0)),(0,320))
        if FileNotFoundError == True:
            screen.blit(pygame.font.Font(None, 25).render(F"{FileNotFoundError}", True, (0,0,0)),(0,340))
    if page == -1:
        screen.blit(questpoints_text,(5,125))
        screen.blit(questsdone_text,(5,145))
        if quests[0] == 1:
            screen.blit(pointquest_text,(210,25))
            screen.blit(prestigequest_text,(210,45))
    if page > -1:
        screen.blit(points_text, (1,50))
        screen.blit(prestige_text, (1,70))
        screen.blit(questpoints_text, (1,90))
        screen.blit(chicken_text, (1,110))
        screen.blit(megaptext, (1,130))
        screen.blit(flamepoints_text, (1,150))
        screen.blit(tickspeed_text, (1,170))
    if page == -2:
        screen.blit(points_text, (1,50))
        screen.blit(prestige_text, (1,70))
        screen.blit(questpoints_text, (1,90))
        screen.blit(chicken_text, (1,110))
        screen.blit(megaptext, (1,130)) 
        screen.blit(flamepoints_text, (1,150))
        screen.blit(tickspeed_text, (1,170))
    if page == -4:
        screen.blit(points_text, (1,1))
        screen.blit(prestige_text, (1,21))
        screen.blit(questpoints_text, (1,41))
        screen.blit(chicken_text, (1,61))
        screen.blit(flamepoints_text, (1,81))
        screen.blit(tickspeed_text, (1,101))
        screen.blit(clickstext,(1,121))
        screen.blit(allpointstext,(1,141))
        screen.blit(allpptext,(1,161))
        screen.blit(allchickenp,(1,181))
        screen.blit(allquestp,(1,201))
        screen.blit(allmegap,(1,221))
        screen.blit(pointsperframetext,(1,241))
        screen.blit(pointspersecond,(1,261))
        screen.blit(extra_text1,(1,281))
        screen.blit(extra_text2,(1,301))
        screen.blit(secondtimer_text, (1,321))
        screen.blit(minutetimer_text, (1,341))
        screen.blit(hourtimer_text, (1,361))

    if page == 0:
        pointreqtext = font1.render(f"Req: {(25 * (poupgradepower[0] * (poupgradepower[0]) * ((poupgradepower[0]) * 10)))} points", True, (0,0,0))
        if(points[0] > 0):
            screen.blit(pointreqtext, (75, 490))
    if page == -2:
        questfortext = font2.render(f"Req: {200 * poupgradepower[2] * poupgradepower[2]} quest points", True, (0,0,0))
        screen.blit(questfortext,(10, 675))
    if(page == 1):
        if(points[1] > ((5 * presup[0]) - 1)):
            screen.blit(prestigemulti_text,(510,555))
            prestigepointtext = font2.render(f"req: {25 * (poupgradepower[1] * poupgradepower[1] * poupgradepower[1])} prestige points", True, (0,0,0))
            screen.blit(prestigepointtext, (510,475))
        if(points[0] > 499 / presup[0]):
            prestigefor_text = font1.render(f"for {(points[0] / (500 / presup[0])) + 1}", True, (0,0,0))
            screen.blit(prestigefor_text, (275,615))
        else:
            prestigefor_text = font1.render(f"req {500 / presup[0]} points", True, (0,0,0))
            screen.blit(prestigefor_text, (275,615))
    if(page == 2):
        if points[0] > 999999:
            chicken_text = font2.render(f"{points[0] / 1000000}points", True, ("white"))
            screen.blit(chicken_text, (250, 575))
        else:
            chicken_text = font2.render(f"req: {1000000}points", True, ("white"))
            screen.blit(chicken_text, (250, 575))
        if points[2] > 0:
            if points[2] > (2 * (TickSpeed - 199)):
                chicken_ticktext = font2.render(f"req: {2 * (TickSpeed - 199):.2f} chicken points", True, ("white"))
                screen.blit(chicken_ticktext, (250, 495))
    if page == 3:
        if points[1] > 4999:
            megafor_text = font3.render(f"{points[1] / 9999:.2f} mega points", True, ("white"))
            screen.blit(megafor_text, (275,615))
        else:
            megafor_text = font3.render(f"req: {10000} prestige points", True, ("white"))
            screen.blit(megafor_text, (260,615))
    if page == 4:
        if points[4] > 50000000 - 1:
            megafor_text = font3.render(f"{points[4] / 50000000:.2f} mega points", True, ("white"))
            screen.blit(megafor_text, (275,615))
        else:
            megafor_text = font3.render(f"req: 5e+8 mega points", True, ("white"))
            screen.blit(megafor_text, (260,615))
        if points[5] > 0:
            if points[5] < 100000 * poupgradepower[4] * poupgradepower[4]:
                screen.blit(font3.render(f"req: {100000 * poupgradepower[4] * poupgradepower[4]} flame points", True, (0,0,0)),(260,515))
            else:
                screen.blit(font3.render(f"{points[5] / 100000 * poupgradepower[4] * poupgradepower[4]}", True, (0,0,0)),(260,515))

    if savetimer > 10000:
        savetimer = 0
        save_game()
        print("game saved")
    else:
        savetimer += 1
    if achievementson == 1:
        screen.blit(achievementslist,(50,0))
        screen.blit(achievements,(250, 575))
        screen.blit(button1000times,(60,60 + -scroll_direction - 100))
        screen.blit(onehundredkpoints,(60,60 + 80 * 1 + -scroll_direction - 100))
        screen.blit(onehundredmpoints,(60,60 + 80 * 2 + -scroll_direction - 100))
        screen.blit(onehundredbpoints,(60,60 + 80 * 3 + -scroll_direction - 100))
        screen.blit(onehundredtpoints,(60,60 + 80 * 4 + -scroll_direction - 100))
        screen.blit(onehundredquintilpoints,(60,60 + 80 * 5 + -scroll_direction - 100))
        pygame.draw.rect(screen,(200,200,200),(600,70 + scroll_direction * 6 + 250,25,50))

        # page clicker
        if not stats[0] > 999:
            pygame.draw.rect(screen,(255,0,0),(140,70 + -scroll_direction - 100,440,60))
            pygame.draw.rect(screen,(0,255,0),(140,70 + -scroll_direction - 100,stats[0] / 1000 * 440,60))
            screen.blit(font1.render(f"Press the page change button", True, (0,0,0)),(140,90 + -scroll_direction - 100))
            screen.blit(font1.render(f"{stats[0]}/1000", True, (0,0,0)),(140,110 + -scroll_direction - 100))
        else:
            pygame.draw.rect(screen,(0,255,0),(140,70 + -scroll_direction - 100,440,60))
            screen.blit(font1.render(f"Completed!", True, (0,0,0)),(140,90 + -scroll_direction - 100))

        # 100k points
        if not stats[1] > 99999:
            pygame.draw.rect(screen,(255,0,0),(140,70 + 80 * 1 + -scroll_direction - 100,440,60))
            pygame.draw.rect(screen,(0,255,0),(140,70 + 80 * 1 + -scroll_direction - 100,stats[1] / 100000 * 440,60))
            screen.blit(font1.render(f"Get 100,000 points", True, (0,0,0)),(140,90 + 80 * 1 + -scroll_direction - 100))
            screen.blit(font1.render(f"{stats[1]}/100000", True, (0,0,0)),(140,110 + 80 * 1 + -scroll_direction - 100))
        else:
            pygame.draw.rect(screen,(0,255,0),(140,70 + 80 * 1 + -scroll_direction - 100,440,60))
            screen.blit(font1.render(f"Completed!", True, (0,0,0)),(140,90 + 80 * 1 + -scroll_direction - 100))

        # 100m points
        if not stats[1] > 99999999:
            pygame.draw.rect(screen,(255,0,0),(140,70 + 80 * 2 + -scroll_direction - 100,440,60))
            pygame.draw.rect(screen,(0,255,0),(140,70 + 80 * 2 + -scroll_direction - 100,stats[1] / 100000000 * 440,60))
            screen.blit(font1.render(f"Get 100,000,000 points", True, (0,0,0)),(140,90 + 80 * 2 + -scroll_direction - 100))
            screen.blit(font1.render(f"{stats[1]}/100000000", True, (0,0,0)),(140,110 + 80 * 2 + -scroll_direction - 100))
        else:
            pygame.draw.rect(screen,(0,255,0),(140,70 + 80 * 2 + -scroll_direction - 100,440,60))
            screen.blit(font1.render(f"Completed!", True, (0,0,0)),(140,90 + 80 * 2 + -scroll_direction - 100))

        # 100b points
        if not stats[1] > 99999999999:
            pygame.draw.rect(screen,(255,0,0),(140,70 + 80 * 3 + -scroll_direction - 100,440,60))
            pygame.draw.rect(screen,(0,255,0),(140,70 + 80 * 3 + -scroll_direction - 100,stats[1] / 100000000000 * 440,60))
            screen.blit(font1.render(f"Get 100,000,000,000 points", True, (0,0,0)),(140,90 + 80 * 3 + -scroll_direction - 100))
            screen.blit(font1.render(f"{stats[1]}/100000000000", True, (0,0,0)),(140,110 + 80 * 3 + -scroll_direction - 100))
        else:
            pygame.draw.rect(screen,(0,255,0),(140,70 + 80 * 3 + -scroll_direction - 100,440,60))
            screen.blit(font1.render(f"Completed!", True, (0,0,0)),(140,90 + 80 * 3 + -scroll_direction - 100))

        # 100t points
        if not stats[1] > 99999999999999:
            pygame.draw.rect(screen,(255,0,0),(140,70 + 80 * 4 + -scroll_direction - 100,440,60))
            pygame.draw.rect(screen,(0,255,0),(140,70 + 80 * 4 + -scroll_direction - 100,stats[1] / 100000000000000 * 440,60))
            screen.blit(font1.render(f"Get 100,000,000,000,000 points", True, (0,0,0)),(140,90 + 80 * 4 + -scroll_direction - 100))
            screen.blit(font1.render(f"{stats[1]}/100000000000000", True, (0,0,0)),(140,110 + 80 * 4 + -scroll_direction - 100))
        else:
            pygame.draw.rect(screen,(0,255,0),(140,70 + 80 * 4 + -scroll_direction - 100,440,60))
            screen.blit(font1.render(f"Completed!", True, (0,0,0)),(140,90 + 80 * 4 + -scroll_direction - 100))

        # 100quintil points
        if not stats[1] > 99999999999999999999:
            pygame.draw.rect(screen,(255,0,0),(140,70 + 80 * 5 + -scroll_direction - 100,440,60))
            pygame.draw.rect(screen,(0,255,0),(140,70 + 80 * 5 + -scroll_direction - 100,stats[1] / 100000000000000000000 * 440,60))
            screen.blit(font1.render(f"Get 100,000,000,000,000,000,000 points", True, (0,0,0)),(140,90 + 80 * 5 + -scroll_direction - 100))
            screen.blit(font1.render(f"{stats[1]}/100000000000000000000", True, (0,0,0)),(140,110 + 80 * 5 + -scroll_direction - 100))
        else:
            pygame.draw.rect(screen,(0,255,0),(140,70 + 80 * 5 + -scroll_direction - 100,440,60))
            screen.blit(font1.render(f"Completed!", True, (0,0,0)),(140,90 + 80 * 5 + -scroll_direction - 100))
        
    if stats[0] > 999 and achievementsget[0] < 1000:
        achievementcomplete("Press the page button 1000 times", "25,000 points",0,25000)
        achievementsget[0] += 1
    if stats[1] > 99999 and achievementsget[1] < 1000:
        achievementcomplete("Get 100000 points", "1500 prestige points",1,1500)
        achievementsget[1] += 1
    if stats[1] > 99999999 and achievementsget[2] < 1000:
        achievementcomplete("Get 100000000 points", "100 mega points",4,100)
        achievementsget[2] += 1
    if stats[1] > 99999999999 and achievementsget[3] < 1000:
        achievementcomplete("Get 100000000000 points", "100,000,000 quest points",3,100000000)
        achievementsget[3] += 1
    if stats[1] > 99999999999999 and achievementsget[4] < 1000:
        achievementcomplete("Get 100000000000000 points", "100,000,000,000 quest points",3,100000000000)
        achievementsget[4] += 1
    if stats[1] > 99999999999999999999 and achievementsget[5] < 1000:
        achievementcomplete("Get 100000000000000 points", "100,000,000,000,000 quest points",3,100000000000000)
        achievementsget[5] += 1    
    # print("pointup:",poupgradepower,"tickspeed:",TickSpeed,"points:",points,"gens:",gens_bought,"page:",page)
    pygame.display.flip()
    clock.tick(TickSpeed)