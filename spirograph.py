import turtle
from turtle import Turtle, Screen
import random

# Colors
turtle.colormode(255)


def random_color():  # color function
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


# Creating Objects
obj_turtle = Turtle()
obj_screen = Screen()

# Add attributes to objects
obj_turtle.shape()
obj_turtle.pensize(1)
obj_turtle.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        obj_turtle.color(random_color())
        obj_turtle.circle(100)
        obj_turtle.setheading(obj_turtle.heading() + size_of_gap)


draw_spirograph(4)

obj_screen.exitonclick()
