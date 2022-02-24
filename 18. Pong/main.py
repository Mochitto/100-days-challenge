from turtle import Turtle, Screen
import time

from config import SCREEN_SIZE, BG_COLOR, TITLE, X_SCREEN_SIZE
from score import Score, Watcher, right_score, left_score
from ball import Ball
from screen import Borders
from paddle import Paddle

# Screen
screen = Screen()
screen.setup(height=SCREEN_SIZE, width=SCREEN_SIZE * 16 / 9)
screen.bgcolor(BG_COLOR)
screen.title(TITLE)
screen.colormode(255)

# Init elements
score = Score()
watcher = Watcher()
ball = Ball()
right_paddle = Paddle()
right_paddle.default("right")
left_paddle = Paddle()
left_paddle.default("left")

# Keypresses
screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)
screen.listen()

# Main loop
while True:
    screen.tracer(0)
    screen.update()
    # Bouncing
    if (right_paddle.xcor() >= ball.xcor() >= right_paddle.xcor() - SCREEN_SIZE/24
            and right_paddle.ycor() - 100 < ball.ycor() < right_paddle.ycor() + SCREEN_SIZE/7.2):
        ball.setheading(ball.towards((right_paddle.position()[0] + SCREEN_SIZE/14.5, right_paddle.position()[1])))
        ball.bounce_right()
        screen.update()
    if (left_paddle.xcor() <= ball.xcor() <= left_paddle.xcor() + SCREEN_SIZE/24
            and left_paddle.ycor() - 100 < ball.ycor() < left_paddle.ycor() + SCREEN_SIZE/7.2):
        ball.setheading(ball.towards((left_paddle.position()[0] - SCREEN_SIZE/14.5, left_paddle.position()[1])))
        ball.bounce_left()
        screen.update()
    if ball.ycor() > SCREEN_SIZE / 2 - SCREEN_SIZE / 30:
        ball.bounce_ceiling()
        screen.update()
    if ball.ycor() < -SCREEN_SIZE / 2 + SCREEN_SIZE / 30:
        ball.bounce_floor()
        screen.update()

    # Ball out of bounds
    if ball.xcor() > X_SCREEN_SIZE / 2:
        screen.tracer(1)
        score.score("left")
        ball.speed(3)
        ball.home()
        ball.speed(0)
        right_paddle.default("right")
        left_paddle.default("left")
        ball.random_start()
        time.sleep(1)
    elif ball.xcor() < -X_SCREEN_SIZE / 2:
        screen.tracer(1)
        score.score("right")
        ball.speed(3)
        ball.home()
        ball.speed(0)
        right_paddle.speed(3)
        left_paddle.speed(3)
        right_paddle.default("right")
        left_paddle.default("left")
        right_paddle.speed(0)
        left_paddle.speed(0)
        ball.random_start()
    else:
        ball.forward(SCREEN_SIZE/600)
    watcher.watch(ball)  # Ball position
    screen.update()

