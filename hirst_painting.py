# # This code will not work in repl.it as there is no access to the colorgram package here.
# # We talk about this in the video tutorials
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:  # <colorgram.py Color: Rgb(r=245, g=243, b=238), 64.68350168350169%>
#     r = color.rgb.r  # color.rgb :-  Rgb(r=245, g=243, b=238)
#     g = color.rgb.g  # 245
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)

# Creating Objects
obj_Screen = Screen()
tim = Turtle()

# Set to starting position
tim.penup()
x = -300
y = -200
tim.setposition(x, y)  # Set turtle position


# Color list
Color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]


def print_a_line():
    global y  # Declare that we are modifying the global variable
    for _ in range(0, 10):
        tim.dot(20, random.choice(Color_list))  # Printing dots
        tim.forward(50)
    y += 40
    tim.setposition(x, y)


for _ in range(0, 10):
    print_a_line()


obj_Screen.exitonclick()
