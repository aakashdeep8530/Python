import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle named "pen"
pen = turtle.Turtle()
pen.speed(0)  # Fastest speed

# Function to draw a colorful square
def draw_square(size):
    for _ in range(4):
        pen.forward(size)
        pen.right(90)

# Draw a colorful spiral of squares
for i in range(100):
    pen.color(random.random(), random.random(), random.random())  # Random color
    draw_square(100)
    pen.right(10)  # Rotate slightly to create a spiral effect
    pen.forward(5)  # Move forward to create space between squares

# Hide the turtle and finish
pen.hideturtle()
turtle.done()