from turtle import Turtle, Screen

obj_turtle = Turtle()
obj_screen = Screen()

obj_turtle.shape("turtle")
obj_turtle.color("red")

for i in range(10):
    obj_turtle.forward(10)
    obj_turtle.pu()
    obj_turtle.forward(10)
    obj_turtle.pd()


obj_screen.exitonclick()
