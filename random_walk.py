import turtle
from turtle import Turtle, Screen
import random

# Colors
turtle.colormode(255)


def random_color():  # color function
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


# Creating Objects
obj_turtle = Turtle()
obj_screen = Screen()

# Add attributes to objects
obj_turtle.shape()
obj_turtle.pensize(10)
obj_turtle.speed(1)
step = 30


def right(steps):
    obj_turtle.right(90)
    obj_turtle.forward(steps)


def left(steps):
    obj_turtle.left(90)
    obj_turtle.forward(steps)


def forward(steps):
    obj_turtle.forward(steps)


def backward(steps):
    obj_turtle.backward(steps)


# Adding Functions names to a List
direction = [right, left, forward, backward]

while True:
    random.choice(direction)(step)
    obj_turtle.color(random_color())  # pick a random color

obj_screen.exitonclick()
