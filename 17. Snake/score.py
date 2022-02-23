from turtle import Turtle

from config import UI_COLOR, GAME_SPACE


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.color(UI_COLOR)
        self.goto(0, GAME_SPACE/2 - 40)
        self.score = 0
        self.write(f"Score : {self.score}", align="center", font=("Arial", 15, "normal"))

    def get_point(self):
        """Add points to the score."""
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Arial", 15, "normal"))

    def get_score(self):
        """Write the game over message."""
        self.clear()
        self.home()
        self.goto(0, 30)
        self.write(f"Game Over!", align="center", font=("Arial", 30, "normal"))
        self.goto(0, -20)
        self.write(f"Score : {self.score}", align="center", font=("Arial", 20, "normal"))
