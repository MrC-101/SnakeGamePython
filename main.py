import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake

speed = 0.1
snake_color_index = 0
SNAKE_COLORS = (
    "white", "khaki", "yellow", "gold", "orange", "darkorange", "orangered",
    "red", "crimson", "mediumvioletred", "darkorchid", "darkmagenta", "purple"
)

snake = Snake()
food = Food()
score = Scoreboard()
speed_label = Scoreboard()
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Το φιδάκι ο Διαμαντής")
screen.tracer(0)
speed_label.speed_indicator(speed, SNAKE_COLORS[snake_color_index])

screen.listen()
screen.onkeypress(key='Left', fun=snake.left)
screen.onkeypress(key='Right', fun=snake.right)
screen.update()


def reset():
    global snake_color_index, speed
    speed = 0.1
    snake_color_index = 0
    score.reset()
    snake.reset()
    speed_label.speed_indicator(speed, "white")


game_is_on = True
while game_is_on:
    print(speed)
    screen.update()
    time.sleep(speed)
    snake.move()

    # Detect collision with food and increase speed every 5 points of score
    # and changes snake color accordingly to alert user
    if snake.head.distance(food) < 11:
        food.refresh()
        score.add_point()
        snake.add_segment(SNAKE_COLORS[snake_color_index])
        if score.keep_score % 2 == 0:
            snake_color_index += 1
            speed -= 0.01
            speed_label.speed_indicator(speed, SNAKE_COLORS[snake_color_index])
            for segment in snake.snake_body:
                segment.color(SNAKE_COLORS[snake_color_index])

    # Detect collision with walls
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() <= -290:
        reset()

    # Detect collision with snake body
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            reset()


screen.exitonclick()
