import random
import turtle
from turtle import Turtle, Screen

aurora = Turtle()
john = Turtle()
alex = Turtle()
angela = Turtle()

turtles = [aurora, john, alex, angela]

screen = Screen()
turtle.colormode(255)
screen.delay(10)


def random_walk_race(turtle_obj_list: list):
    """Takes a list of turtle objects and makes them create a random pattern on a black screen."""
    for turtley in turtle_obj_list:
        screen.bgcolor("black")
        turtley.shape("turtle")
        turtley.pensize(4)
        turtley.speed(0)
        turtley.resizemode("auto")
        turtley.color(random.randint(100, 255), random.randint(30, 155), random.randint(100, 150))
    for _ in range(400):
        for turtley in turtle_obj_list:
            turtley.forward(random.choice([-20, 20]))
            turtley.right(random.choice([90, -90, 45, 180, 270, -270, 0, 0, 0, 0]))


if __name__ == "__main__":
    random_walk_race(turtles)
    screen.exitonclick()
