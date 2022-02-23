# Snake
#
# For the people that miss the Nokia 3310
from turtle import Screen
import time

from snake import Snake
from food import Food
from score import Score
from borders import Border
from config import GAME_SPACE, SPEED, BG_COLOR


def game_over():
    """End the game

    Make the snake and the food disappear, move Turtle and get game over message."""
    snake.vanish()
    food.hideturtle()
    border.end_game()
    screen.update()
    score.get_score()


def game():
    game_is_on = True
    while game_is_on:
        screen.tracer(0)
        time.sleep(SPEED)
        snake.follow()  # Make the snake move
        screen.update()

        # Eat food and grow
        if snake.head.distance(food) < 15:
            screen.tracer(0)
            score.get_point()
            food.eaten()
            snake.create_body()
            screen.update()

        # Check for collisons with the snake body
        for body_part in snake.body:
            if snake.head.distance(body_part) < 10:
                game_is_on = False
                game_over()

        # Check for collisons with the walls body
        if (not -GAME_SPACE / 2 + 50 < snake.head.xcor() < GAME_SPACE / 2 - 50
                or not -GAME_SPACE / 2 + 50 < snake.head.ycor() < GAME_SPACE / 2 - 50):
            game_is_on = False
            game_over()


# Screen settings
screen = Screen()
screen.setup(GAME_SPACE, GAME_SPACE)
screen.bgcolor(BG_COLOR)
screen.title("Snake")
screen.colormode(255)

time.sleep(1)
# Game objects
score = Score()
border = Border()
snake = Snake()
food = Food()
screen.listen()

# Game keys
screen.onkeypress(key="Up", fun=snake.move_up)
screen.onkeypress(key="Right", fun=snake.move_right)
screen.onkeypress(key="Down", fun=snake.move_down)
screen.onkeypress(key="Left", fun=snake.move_left)

# Main loop
game()
screen.exitonclick()
