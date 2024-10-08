import turtle

tim = turtle.Turtle()
screen = turtle.Screen()

# add properties to the objects
tim.shape("turtle")
tim.color('red')
tim.pencolor('black')


def move_forward():
    tim.forward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def move_backward():
    tim.back(10)


def pen_up():
    tim.penup()


def pen_down():
    tim.pendown()


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


turtle.listen()
turtle.onkey(move_forward, 'w')
turtle.onkey(move_backward, 's')
turtle.onkey(turn_left, 'a')
turtle.onkey(turn_right, 'd')
turtle.onkey(pen_up, 'q')
turtle.onkey(pen_down, 'e')
turtle.onkey(clear, 'c')


screen.exitonclick()
