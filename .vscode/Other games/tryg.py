
import turtle
import random
import time
import sys
import pygame
FPS = 1000000
FramePerSec = pygame.time.Clock()
rectasize = 1;
Frames = 0;
Testnum = 0;
bgrect = turtle.Turtle()
bgrect.shape("square")
bgrect.color("green")
bgrect.shapesize(500)
def left():

    global X
    X -= 25
    print("X",X,"Y",Y)
    rect.hideturtle
    rect.penup
    rect.goto(X, Y)
    rect.shape("square")
    rect.color("red")
    rect.shapesize(rectasize)
def right():
    global X
    X += 25
    print("X",X,"Y",Y)
    rect.penup
    rect.goto(X, Y)
    rect.shape("square")
    rect.color("red")
    rect.shapesize(rectasize)
def up():
    global Y
    Y += 25
    print("X",X,"Y",Y)
    rect.penup
    rect.goto(X, Y)
    rect.shape("square")
    rect.color("red")
    rect.shapesize(rectasize)
def down():
    global Y
    Y -= 25
    print("X",X,"Y",Y)
    rect.penup
    rect.goto(X, Y)
    rect.shape("square")
    rect.color("red")
    rect.shapesize(rectasize)
def exit_program():
    turtle.bye()
    print("exit")
def sizer():
    print("sizer activated!")
    global rectasize
    bigrect1 = turtle.Turtle()
    bigrect1.shape("square")
    bigrect1.penup()
    bigrect1.goto(0,150)
    bigrect1.shapesize(10, 40)
    bigrect1.color("green")
    Text.write(rectasize, "size", align="center", font=("Courier", 19, "bold"))
    rectasize += 1
    rect.shape("square")
    rect.color("red")
    rect.shapesize(rectasize)
    print("size", rectasize)

X = 0;
Y = 0;
enemyX = 100;
enemyY = 100;
rect = turtle.Turtle()
rect.shape("square")
rect.color("red")
rect.shapesize(rectasize)
window = turtle.Screen()
window.bgcolor("green")
window.title("gameerrr")
window.setup(width=800,height=500)
Text = turtle.Turtle()
Text.pendown()
Text.speed(0)
Text.color("white")
Text.penup()
Text.hideturtle()
Text.goto(0,150)
Text.write("Welcome to wolrds bset gaem!11" , align="center", font=("Courier", 19, "bold"))
Text.goto(0,125)
Text.write("Pres t to continue idk" , align="center", font=("Courier", 19, "bold"))
def lolchicken():
    print("balls")
def commitboom():
    global rectasize
    rectasize = 1
    rect.shape("square")
    rect.color("red")
    rect.shapesize(rectasize)
    print("size", rectasize)
    bigrect1 = turtle.Turtle()
    bigrect1.shape("square")
    bigrect1.penup()
    bigrect1.goto(0,150)
    bigrect1.shapesize(10, 40)
    bigrect1.color("green")
    Text.goto(0,125)
    Text.write("Donot press backspace!!!!1111" , align="center", font=("Courier", 19, "bold"))
    Text.goto(0,150)
    Text.write("Press F with capslock" , align="center", font=("Courier", 19, "bold"))
window.onkey(exit_program, "BackSpace")
window.onkey(commitboom, "t")
window.onkey(sizer, "f")
window.onkey(left, "a")
window.onkey(up, "w")
window.onkey(right, "d")
window.onkey(down, "s")
turtle.listen()
turtle.mainloop()