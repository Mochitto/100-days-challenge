import turtle as t
import colorgram
import random

colors = colorgram.extract("YourImage.jpg", 10)

alex = t.Turtle()
alex.hideturtle()

screen = t.Screen()
t.colormode(255)
alex.speed(0)
alex.penup()
screen.bgcolor("black")


def make_dotted_painting(turtley, rows):
    """Draws a square made of random colour dots."""
    global colors
    screen.setup(rows * 35, rows * 35)
    turtley.setposition(-rows * 14.5 * 0.5 * 1.41421356237, -rows * 14.5 * 0.5 * 1.41421356237)

    for row in range(rows + 1):
        for dot in range(rows):
            turtley.dot(15, random.choice(colors).rgb)
            turtley.forward(20)
        turtley.dot(15, colors[0].rgb)
        turtley.setheading(90)
        turtley.forward(20)
        if row % 2 == 1:
            turtley.right(90)
        else:
            turtley.left(90)
    screen.exitonclick()

if __name__ == "__main__":
    make_dotted_painting(alex, 10)


