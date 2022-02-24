from turtle import Turtle
import random

from config import GAME_COLOR, SCREEN_SIZE


class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__()
        self.penup()
        self.speed(8)
        self.shape("circle")
        self.shapesize(SCREEN_SIZE / 300)
        self.color(GAME_COLOR)

    def random_start(self):
        """Start the ball with a random angle."""
        self.speed(0)
        self.setheading(random.choice([random.randint(-15, 15), random.randint(170, 190)]))

    def bounce_ceiling(self):
        """Bounce off the ceiling with the opposite angle."""
        if 90 < self.heading() < 180:
            self.setheading(self.heading() + (180 - self.heading()) * 2)
        elif 0 < self.heading() < 90:
            self.setheading(-self.heading())

    def bounce_right(self):
        """Bounce off the right wall/paddle with the opposite angle."""
        if 0 < self.heading() < 90:
            self.setheading(self.heading() + (90 - self.heading()) * 2)
        elif 270 < self.heading() < 360:
            self.setheading(self.heading() - (self.heading() - 270) * 2)

    def bounce_floor(self):
        """Bounce off the floor with the opposite angle."""
        if 180 < self.heading() < 270:
            self.setheading(self.heading() - (self.heading() - 180) * 2)
        elif 270 < self.heading() < 360:
            self.setheading(self.heading() + (360 - self.heading()) * 2)

    def bounce_left(self):
        """Bounce off the left wall/paddle with the opposite angle."""
        if 90 < self.heading() < 180:
            self.setheading(self.heading() - (self.heading() - 90) * 2)
        elif 180 < self.heading() < 270:
            self.setheading(self.heading() + (270 - self.heading()) * 2)
