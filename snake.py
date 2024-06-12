from turtle import Turtle
MOVE_DISTANCE = 12
SIZE = 0.6
game_start = [True]


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for i in range(3):
            new_segment = self.add_segment("white")
            new_segment.goto(i * -MOVE_DISTANCE, 0)
        game_start[0] = False

    def up(self):
        if self.head.heading() in [0, 180]:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() in [0, 180]:
            self.head.setheading(270)

    def left(self):
        self.head.setheading(self.head.heading()+90)

    def right(self):
        self.head.setheading(self.head.heading()-90)

    def move(self):
        segm_total = len(self.snake_body)
        for segment in range(segm_total-1, 0, -1):
            new_x = self.snake_body[segment-1].xcor()
            new_y = self.snake_body[segment-1].ycor()
            self.snake_body[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, color):
        new_segment = Turtle(shape='square', visible=False)
        new_segment.speed('fastest')
        new_segment.penup()
        new_segment.setpos(320, 320)
        new_segment.shapesize(SIZE, SIZE)
        new_segment.showturtle()
        new_segment.color(color)
        self.snake_body.append(new_segment)
        if game_start[0]:
            return new_segment

    def reset(self):
        for segment in self.snake_body:
            segment.teleport(1000, 1000)
        game_start[0] = True
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]