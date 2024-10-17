import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("3D Cube")

# Create a turtle
cube = turtle.Turtle()
cube.color("black")

# Function to draw a square
def draw_square():
    for _ in range(4):
        cube.forward(50)
        cube.left(90)

# Draw the first square
draw_square()

# Draw the second square offset from the first
cube.penup()
cube.goto(25, 25)
cube.pendown()
draw_square()

# Connect the corners
cube.penup()
cube.goto(0, 0)
cube.pendown()
cube.goto(25, 25)

cube.penup()
cube.goto(0, 50)
cube.pendown()
cube.goto(25, 75)

cube.penup()
cube.goto(50, 50)
cube.pendown()
cube.goto(75, 75)

cube.penup()
cube.goto(50, 0)
cube.pendown()
cube.goto(75, 25)

# Hide the turtle and display the result
cube.hideturtle()
turtle.done()