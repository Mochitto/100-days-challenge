from turtle import Turtle

from config import GAME_COLOR, X_SCREEN_SIZE, SCREEN_SIZE


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.resizemode("user")
        self.setheading(90)
        self.shape("square")
        self.color(GAME_COLOR)
        self.shapesize(None, SCREEN_SIZE/120, None)

    def move_up(self):
        """Move up the paddle"""
        if -SCREEN_SIZE/2 < self.ycor() < SCREEN_SIZE/2:
            self.goto(self.position()[0], self.position()[1] + SCREEN_SIZE/24)

    def move_down(self):
        """Move down the paddle"""
        if -SCREEN_SIZE / 2 < self.ycor() < SCREEN_SIZE / 2:
            self.goto(self.position()[0], self.position()[1] - SCREEN_SIZE/24)

    def default(self, user="left"):
        """Brings the paddle to the default position. If user == right, move the right paddle, else left paddle"""
        if user == "right":
            self.goto(X_SCREEN_SIZE/2 - X_SCREEN_SIZE/35, 0)
        else:
            self.goto(- X_SCREEN_SIZE/2 + X_SCREEN_SIZE/35, 0)

