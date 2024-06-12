from turtle import Turtle
import random
FOOD_AREA = [-264, 264, 12]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("circle")
        self.color("red")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.refresh()

    def refresh(self):
        x_coord = random.choice(range(*FOOD_AREA))
        y_coord = random.choice(range(*FOOD_AREA))
        self.teleport(x_coord, y_coord)
        self.showturtle()
