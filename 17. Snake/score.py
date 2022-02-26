from turtle import Turtle

from config import UI_COLOR, GAME_SPACE
from highscore import read_hs, write_hs

# Import high score
try:
    high_score = int(read_hs())
except (TypeError, FileNotFoundError):
    high_score = 0
    write_hs("0")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.color(UI_COLOR)
        self.goto(0, GAME_SPACE/2 - 40)
        self.score = 0
        self.write(f"Score : {self.score} - High score: {high_score}", align="center", font=("Arial", 15, "normal"))

    def get_point(self):
        """Add points to the score."""
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score} - High score: {high_score}", align="center", font=("Arial", 15, "normal"))

    def get_score(self):
        """Write the game over message."""
        global high_score
        if self.score > high_score:
            high_score = self.score
            write_hs(str(high_score))
        self.clear()
        self.home()
        self.goto(0, 30)
        self.write(f"Game Over!", align="center", font=("Arial", 30, "normal"))
        self.goto(0, -20)
        self.write(f"Score : {self.score} - High score: {high_score}", align="center", font=("Arial", 20, "normal"))
