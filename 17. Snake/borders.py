from turtle import Turtle

from config import UI_COLOR, GAME_SPACE, TURTLE_COLOR


class Border(Turtle):

    def __init__(self):
        super().__init__()
        # Turtle settings
        self.shape("turtle")
        self.shapesize(2)
        self.speed(5)
        self.pensize(3)
        self.color(UI_COLOR)
        self.penup()

        # Draw the borders
        self.goto(GAME_SPACE/2 - 50, GAME_SPACE/2 - 50)  # Goto top right of the canvas
        self.pendown()
        self.setheading(180)

        for _ in range(4):
            self.forward(GAME_SPACE-100)
            self.left(90)
        # Sit in the top right corner
        self.setheading(-135)
        self.color(TURTLE_COLOR)

    def end_game(self):
        """Go to the middle of the screen and increase in size."""
        self.penup()
        self.setheading(90)
        self.goto(0, -320)
        self.shapesize(17)
