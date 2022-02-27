import turtle as tu
import pandas as pd

# Reading csv
df = pd.read_csv("50_states.csv")
states = df["state"]

# Turtle initiation
screen = tu.Screen()
screen.setup(width=750, height=520)
screen.title("US States Game")
screen.addshape("blank_states_img.gif")
tu.shape("blank_states_img.gif")
turtley = tu.Turtle()
turtley.penup()
turtley.speed(0)
turtley.hideturtle()

# Main loop
matches = []
for x in range(50):
    while True:
        user_answer = screen.textinput(title=f"Guess the States {x}/50",
                                       prompt="What's another state's name? (\"exit\" to give up)").title()
        if user_answer == "Exit":
            break
        if user_answer in states.values and user_answer not in matches:
            answer = df.loc[df["state"] == user_answer, ["x", "y"]]
            coordinates = answer.values

            turtley.goto(coordinates[0])
            turtley.write(user_answer)

            matches.append(user_answer)
            break

    if user_answer == "Exit":
        screen.bye()
        break

# Write a csv file with the missing states, to revise/study later
Missed_states = [state for state in states.values if state not in matches]
Missed_states = pd.DataFrame({
    "state": list(Missed_states)
})
Missed_states.to_csv("Missing_states.csv")
