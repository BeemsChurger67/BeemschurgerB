import turtle
import random
import time
import sys
import pygame

pygame.init

print("importables done")

#Movement speed + Player health

speed = 15;
HP = 15;

print("players speed and health done")

#XY's

X = 0;
Y = 0;

print("players x and y done")

#direction

direction = 2;

weirdx = random.randint(-300, 300);
weirdy = random.randint(-300, 300);

enemyx = 100 #random.randint(-300, 300);
enemyy = 100 #random.randint(-300, 300);

print("random values done and values and dir")

#turtle

enemy1 = turtle.Turtle()
enemy2 = turtle.Turtle()

print("first turtles done")

enemy1.goto(enemyx - X,enemyy - Y),enemy2.goto(enemyx - X,enemyy - Y)

enemy1.shapesize(2)
enemy1.color("black")
enemy1.shape("circle")
enemy1.penup
enemy1.hideturtle


enemy2.shapesize(1.7)
enemy2.color("red")
enemy2.shape("circle")
enemy2.penup
enemy2.hideturtle

print("Enemy sprite done")
print("shapes and sizes done")

#random block in the middle of nowhere :skull:

block1 = turtle.Turtle()
block1.shapesize(1)
block1.color("black")
block1.shape("square")
block1.goto(weirdx - X, weirdy - Y)
block1.penup
block1.hideturtle


print("block done")

#background update

bg = turtle.Turtle()
bg.goto(0,0)
bg.shapesize(30)
bg.color("green")
bg.shape("square")
bg.penup
bg.hideturtle

print("bg done")

#window

window = turtle.Screen()
window.bgcolor("white")
window.title("wolrds bset gaem!11")
window.setup(width=600,height=600)

print("window done")

#borders

topwall = turtle.Turtle()
bottomwall = turtle.Turtle()
leftwall = turtle.Turtle()
rightwall = turtle.Turtle()

print("wall turtles done")

#border XY, shape and size

topwall.goto(0 - X, 300 - Y),bottomwall.goto(0 - X, -300 - Y),rightwall.goto(300 - X, 0 - Y),leftwall.goto(-300 - X, 0 - Y)
topwall.shape("square")
bottomwall.shape("square")
rightwall.shape("square")
leftwall.shape("square")

topwall.shapesize(1,100)
bottomwall.shapesize(1,100)
rightwall.shapesize(100,1)
leftwall.shapesize(100,1)

topwall.hideturtle
bottomwall.hideturtle
rightwall.hideturtle
leftwall.hideturtle

topwall.penup
bottomwall.penup
rightwall.penup
leftwall.penup

print("walls finished")

#Point amount
score = 0;
points = turtle.Turtle()
points.speed(0)
points.color("white")
points.penup()
points.hideturtle()
points.goto(0,150)
points.write("Points = {}".format(score), align="center", font=("Courier", 24, "bold"))
points.goto(0,125)
points.write("Health = {}".format(HP), align="center", font=("Courier", 24, "bold"))

print("points amount done")

#powerups
speedpowerup = 0;

speedpux = random.randint(-280, 280)
speedpuy = random.randint(-280, 280)
speedpu = turtle.Turtle()
speedpu.shape("circle")
speedpu.shapesize(1.2)
speedpu.color("red")
speedpu.goto(speedpux - X, speedpux - Y)

print("powerups done")

#show + player pos deco

p1 = turtle.Turtle()
p2 = turtle.Turtle()
p3 = turtle.Turtle()
p4 = turtle.Turtle()

print("all turtles done")

p1.goto(0,0)
p2.goto(0,0)
p3.goto(7,8)
p4.goto(-7,8)

p1.penup
p2.penup
p3.penup
p4.penup

p1.hideturtle
p2.hideturtle
p3.hideturtle
p4.hideturtle

p1.shapesize(2)
p1.color("black")
p1.shape("circle")

p2.shapesize(1.75)
p2.color("white")
p2.shape("circle")

p3.shapesize(0.3)
p3.color("black")
p3.shape("circle")

p4.shapesize(0.3)
p4.color("black")
p4.shape("circle")

print("shapes and sizes done")

#powerup time

def power():
    global speed, score
    speed += 5
    score += 1

print("powerup definity done")

#cheats

enemytog = 1

def infspeed():
    global speed, score
    speed += random.randint(10000,1000000)
    score += random.randint(10000,1000000)

def cheat():
    global enemytog
    if(enemytog == 1):
        enemytog -= 1
    else:
        enemytog += 1

#movement + updating
print("GAME DONE LOADING")
while True:
    block1.penup
    topwall.penup
    bottomwall.penup
    leftwall.penup
    rightwall.penup
    points.penup
    enemy1.penup
    enemy2.penup
    speedpu.penup
    block1.goto(weirdx - X, weirdy - Y), topwall.goto(0 - X, 300 - Y), bottomwall.goto(0 - X, -300 - Y), rightwall.goto(300 - X, 0 - Y), leftwall.goto(-300 - X, 0 - Y),turtle.penup, turtle.hideturtle, turtle.clearstamps
    enemy1.goto(enemyx - X,enemyy - Y),enemy2.goto(enemyx - X,enemyy - Y)
    points.goto(0,150)
    points.write("Points = {}".format(score), align="center", font=("Courier", 24, "bold"))
    points.goto(0,125)
    points.write("Health = {}".format(HP), align="center", font=("Courier", 24, "bold"))
    speedpu.goto(speedpux - X, speedpux - Y)
    window.update
    def left():
        global X, direction
        if(X > -270):
            X -= speed
        direction = 1
        bg.goto(0,0),p1.goto(0,0),p2.goto(0,0),p3.goto(-8,-7),p4.goto(-7,8),turtle.penup,turtle.hideturtle

    def right():
        global X, direction
        if(X < 270):
            X += speed
        direction = 3
        bg.goto(0,0),p1.goto(0,0),p2.goto(0,0),p3.goto(8,7),p4.goto(7,-8),turtle.penup,turtle.hideturtle

    def up():
        global Y, direction
        if(Y < 270):
            Y += speed
        direction = 2
        bg.goto(0,0),p1.goto(0,0),p2.goto(0,0),p3.goto(7,8),p4.goto(-7,8),turtle.penup,turtle.hideturtle

    def down():
        global Y, direction
        if(Y > -270):
            Y -= speed
        direction = 4
        bg.goto(0,0),p1.goto(0,0),p2.goto(0,0),p3.goto(-7,-8), p4.goto(7,-8),turtle.penup,turtle.hideturtle

    def end():
        turtle.bye
        print("end")
    turtle.onkey(left, "a")
    turtle.onkey(right, "d")
    turtle.onkey(up, "w")
    turtle.onkey(down, "s") 
    turtle.onkey(end, "BackSpace")
    turtle.onkey(infspeed, "f")
    turtle.onkey(cheat, "1" and "2")
    turtle.listen()
    if(enemytog == 1):
        if(enemyx < X):
            enemyx += 5 + score + score + score

        if(enemyx > X):
            enemyx -= 5 + score + score + score

        if(enemyy < Y):
            enemyy += 5 + score + score + score

        if(enemyy > Y):
            enemyy -= 5 + score + score + score

        if enemy1.distance(p1) < 40:
            p2.color("red")
            HP -= 1
            time.sleep(0.05)
            p2.color("white")
    
    if speedpu.distance(p1) < 30 + speed:
        speedpowerup = 1
        speedpux = random.randint(-280, 280)
        speedpuy = random.randint(-280, 280)
        power()


    print("enemy toggle",enemytog)
    print("X =",X, "Y =",Y)
    print("Enemy X =",enemyx, "Enemy Y =",enemyy)
    print("health",HP)
    print("dir",direction)
    print("speed",speed)
    if(HP < 1):
        print("you daead!!1111")
        turtle.bye()
