# Rock, Paper, Scissors!
#
# A simple game of Rock, Paper, Scissors, with ASCII art
import random
import time

Player_score = 0
CPU_score = 0


def valid_move(move):  # Raises an Exception if the move is invalid
    if move.lower() not in ["rock", "paper", "scissors"]:
        raise Exception


def win_or_lose():  # Checks who wins and who loses, returns a message and uppers the score
    global CPU_move
    global CPU_score
    global Player_move
    global Player_score
    if Player_move.lower() == CPU_move:
        print("It's a Tie!")
    elif Player_move.lower() == "rock":
        if CPU_move == "paper":
            CPU_score += 1
            print("You lose!")
        else:
            Player_score += 1
            print("You Win!")
    elif Player_move.lower() == "paper":
        if CPU_move == "scissors":
            CPU_score += 1
            print("You lose!")
        else:
            Player_score += 1
            print("You Win!")
    elif Player_move == "scissors":
        if CPU_move == "rock":
            CPU_score += 1
            print("You lose!")
        else:
            Player_score += 1
            print("You Win!")


def display_moves():  # Adds ASCII art to the game
    moves = [Player_move, CPU_move]

    Art = ["""        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)    """, """         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)    """, """        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)    """]
    print(" MATCH START! ".center(30, "-") + "\n")

    for move in moves:
        if move.lower() == "rock":
            print(Art[0])
        elif move.lower() == "paper":
            print(Art[1])
        else:
            print(Art[2])
        time.sleep(1)
        print()
    print()
    print("".center(30, "-"))


# Welcome message
print("Welcome to Rock, Paper, Scissors!\nEnter \"Q\" to end the game.")

# Game loop
while True:
    print("\n" + f" SCORE [{Player_score}-{CPU_score}] ".center(30, "*"))
    Player_move = input("What's your move?\n>>>> ")

    if Player_move.lower() in "quit":
        break

    try:
        valid_move(Player_move)
    except:
        print("Invalid move.")
        continue

    CPU_move = random.choice(["rock", "paper", "scissors"])

    display_moves()
    win_or_lose()

# End message
print("\n" + f" FINAL SCORE [{Player_score}-{CPU_score}] ".center(30, "*"))
print("\nThanks for playing!".center(30))
