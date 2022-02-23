from turtle import Turtle

from config import GAME_COLOR


class Snake:

    def __init__(self):
        """Create head and the first parts of the body."""
        self.head = Turtle("square")
        self.head.color(GAME_COLOR)
        self.head.penup()
        self.head.speed(0)
        self.head.shapesize(0.8)
        self.body = []
        for _ in range(2):
            self.create_body()

    def create_body(self):
        """Add parts to the snake body."""
        body = Turtle("square")
        body.penup()
        body.speed(0)
        body.shapesize(0.8)
        body.color(GAME_COLOR)

        if not self.body:  # First body part
            body.goto(self.head.position()[0] - 20, self.head.position()[1])
        else:
            body.goto(self.body[len(self.body) - 1].position())

        self.body.append(body)

    def follow(self):
        """Make the snake move, making the body follow the head."""
        for number in range(len(self.body) - 1, -1, -1):
            if number == 0:
                self.body[number].goto(self.head.position())
            else:
                self.body[number].goto(self.body[number - 1].position())
        self.head.forward(20)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def vanish(self):
        """Make the snake disappear."""
        self.head.hideturtle()
        for body in self.body:
            body.hideturtle()
