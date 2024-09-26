from turtle import Screen, Turtle
import matplotlib.colors
import random

# color
colors = matplotlib.colors.CSS4_COLORS  # Get a dictionary of all named colors
colors_names = list(colors.keys())  # Print the list of color names

tom = Turtle()
obj_screen = Screen()

angles = [120, 90, 72, 60, 51.4285714286, 45, 40, 36]
sides = 3

for angle in angles:
    tom.pencolor(random.choice(colors_names))
    for _ in range(sides):
        tom.forward(100)
        tom.left(angle)
    sides += 1

obj_screen.exitonclick()
