from turtle import Turtle


def draw_square():
    mypen = Turtle()
    mypen.penup()
    mypen.setposition(-280, -278)
    mypen.pendown()
    mypen.pensize(10)
    mypen.color('white')
    for side in range(4):
        mypen.forward(555)
        mypen.left(90)
    mypen.hideturtle()