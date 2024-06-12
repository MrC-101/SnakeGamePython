from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "bold")
FONT1 = ("Arial", 20, "bold")
current_speed = [0]
SPEED_ART = (
    "⬤", "⬤⬤", "⬤⬤⬤", "⬤⬤⬤⬤", "⬤⬤⬤⬤⬤", "⯁", "⯁⯁", "⯁⯁⯁",
    "⯁⯁⯁⯁", "⯁⯁⯁⯁⯁", "✪", "✪✪", "✪✪✪", "✪✪✪✪", "✪✪✪✪✪"
)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("circle")
        self.color('white')
        self.teleport(0, 280)
        self.keep_score = 0
        with open("C:\\Users\\oldbo\\Desktop\\highscore.txt", "r") as hiscore:
            self.high_score = int(hiscore.read())
        self.score_update()
        self.snake_speed = 0

    def speed_indicator(self, speed, color):
        self.clear()
        self.teleport(0, -290)
        self.snake_speed = speed
        self.color(color)
        self.write(f"Speed: {SPEED_ART[current_speed[0]]}", move=False, align=ALIGNMENT, font=FONT)
        current_speed[0] += 1

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.keep_score}   High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.keep_score += 1
        self.score_update()

    # def game_over(self, color):
    #     self.teleport(0, 0)
    #     self.color(color)
    #     self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT1)

    def reset(self):
        if self.keep_score > self.high_score:
            self.high_score = self.keep_score
            with open("../../../highscore.txt", mode="w") as hiscore:
                hiscore.write(str(self.high_score))
        self.keep_score = 0
        current_speed[0] = 0
        self.score_update()

