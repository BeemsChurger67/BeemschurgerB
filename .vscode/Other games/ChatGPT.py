import turtle

# Set up the turtle window and turtle object
window = turtle.Screen()
rectangle = turtle.Turtle()

# Draw a rectangle
rectangle.penup()
rectangle.goto(-50, 0)
rectangle.pendown()
rectangle.forward(100)
rectangle.right(90)
rectangle.forward(50)
rectangle.right(90)
rectangle.forward(100)
rectangle.right(90)
rectangle.forward(50)

# Move the rectangle with the arrow keys
def move_up():
    rectangle.setheading(90)
    rectangle.forward(10)

def move_down():
    rectangle.setheading(270)
    rectangle.forward(10)

def move_left():
    rectangle.setheading(180)
    rectangle.forward(10)

def move_right():
    rectangle.setheading(0)
    rectangle.forward(10)

window.listen()  # Listen for keyboard events
window.onkeypress(move_up, "Up")  # Bind up arrow key to move_up function
window.onkeypress(move_down, "Down")  # Bind down arrow key to move_down function
window.onkeypress(move_left, "Left")  # Bind left arrow key to move_left function
window.onkeypress(move_right, "Right")  # Bind right arrow key to move_right function

window.mainloop()  # Start the turtle event loop
