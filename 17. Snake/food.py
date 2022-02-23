import random
from turtle import Turtle

from config import GAME_COLOR, GAME_SPACE


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.color(GAME_COLOR)
        self.speed(0)
        self.eaten()

    def eaten(self):
        """Set food to a new random location."""
        self.goto(random.randint(-GAME_SPACE/2 + 60, GAME_SPACE/2 - 60),
                  random.randint(-GAME_SPACE/2 + 60, GAME_SPACE/2 - 60))
