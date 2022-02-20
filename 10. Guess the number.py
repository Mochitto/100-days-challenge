# Number Guessing Game!
#
# Try reading the computer's mind!
import random
import os


def clear():
    """Clears the terminal, changes depending on the os of the machine"""
    os.system('cls' if os.name == 'nt' else 'clear')


def game():
    """A fun game of guess the number"""
    clear()
    print(r'''
   ______                        __  __            
  / ____/_  _____  __________   / /_/ /_  ___      
 / / __/ / / / _ \/ ___/ ___/  / __/ __ \/ _ \     
/ /_/ / /_/ /  __(__  |__  )  / /_/ / / /  __/     
\____/\__,_/\___/____/____/_  \__/_/ /_/\___/      
   ____  __  ______ ___  / /_  ___  _____          
  / __ \/ / / / __ `__ \/ __ \/ _ \/ ___/          
 / / / / /_/ / / / / / / /_/ /  __/ /              
/_/ /_/\__,_/_/ /_/ /_/_.___/\___/_/               
''')
    print("Welcome to the Number Guessing Game!")

    difficulty = input("Choose a difficulty. Type \"easy\" or \"hard\".\n>>> ").lower()
    print("\nI'm thinking of a number between 1 and 100.")

    # Variables
    lives = 5 if difficulty == "hard" else 10
    secret_number = random.randint(1, 100)

    # Main loop
    while lives >= 1:
        print(f"You have {lives} attempts remaining to guess the number.")

        # Check input
        while True:
            try:
                guess = int(input("\nMake a guess: "))
                break
            except ValueError:
                print("Invalid input.")
                continue

        # Check guess
        if guess == secret_number:
            break
        elif guess > secret_number:
            print("Teasoo high.")
        else:
            print("Too low.")

        lives -= 1

    if lives == 0:
        print(f"\nYou've run out of guesses. You lose. The number was {secret_number}.")
    else:
        print(f"You guessed it! The number was {secret_number}!")

    game() if input("\nWould you like to play again?(y/n) ").lower() == "y" \
        else print('\n' + "Thanks for playing!".center(50, "-"))


if __name__ == "__main__":
    game()
