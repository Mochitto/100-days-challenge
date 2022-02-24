from turtle import Turtle

from config import SCREEN_SIZE, GAME_COLOR, UI_COLOR

left_score = 0
right_score = 0


class Score(Turtle):

    def __init__(self):
        global left_score, right_score
        super().__init__()
        self.hideturtle()
        self.speed(5)
        self.penup()

        self.pensize(SCREEN_SIZE / 50)
        self.pencolor(GAME_COLOR)
        self.goto(0, -SCREEN_SIZE / 2 + SCREEN_SIZE / 12)
        self.setheading(90)
        self.pendown()

        # Draw middle lines
        for _ in range(5):
            self.forward((SCREEN_SIZE - SCREEN_SIZE / 12) / 10)
            self.penup()
            self.forward((SCREEN_SIZE - SCREEN_SIZE / 12) / 10)
            self.pendown()

        # Get to the score position
        self.penup()
        self.pencolor(UI_COLOR)
        self.setheading(270)
        self.forward(SCREEN_SIZE / 8)
        self.write(f"{left_score}      {right_score}", font=('arial', SCREEN_SIZE // 12, 'bold'), align="center")

    def score(self, user):
        global right_score, left_score
        if user == "right":
            right_score += 1
        else:
            left_score += 1
        self.undo()
        self.write(f"{left_score}      {right_score}", font=('arial', SCREEN_SIZE // 12, 'bold'), align="center")


class Watcher(Turtle):

    def __init__(self):
        super().__init__()
        self.color(UI_COLOR)
        self.shape("turtle")
        self.penup()
        self.shapesize(SCREEN_SIZE/170)
        self.goto(0, SCREEN_SIZE/2)

    def watch(self, position):
        self.setheading(self.towards(position))
        # TODO: get angle formula
