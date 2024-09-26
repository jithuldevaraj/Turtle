import turtle

obj_turtle = turtle.Turtle()
obj_screen = turtle.Screen()

obj_turtle.shape("turtle")
obj_turtle.color("red")


def make_a_square(side):
    for i in range(4):
        obj_turtle.forward(side)
        obj_turtle.left(90)


make_a_square(100)
obj_screen.exitonclick()
