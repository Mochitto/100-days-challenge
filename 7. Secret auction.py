# Secret auction
#
# Bid against your friends!
import os


# Functions
def clear():
    # Clears the terminal, changes depending on the os of the machine
    os.system('cls' if os.name == 'nt' else 'clear')


def highest_bid(dictionary):
    # Finds the highest bidder from a dictionary {"person" : float} and returns ("winner", winning_bid)
    winner = ""
    winning_value = 0
    for bidder in dictionary:
        money = dictionary[person]
        if money > winning_value:
            winning_value = money
            winner = bidder
    return winner, winning_value


# ASCII Art
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

# Variables used throughout the program
bidders = {}

# Main
print(logo)
print("Welcome to the secret auction program.")

# Main loop
while True:
    # Inputs
    person = input("What's your name?\n>>> ").capitalize()
    try:
        value = round(float(input("How much would you like to bid?\n>>> $")), 2)
    except ValueError:
        print("Invalid format.")
        clear()
        continue
    bidders[person] = value

    # Get winner or keep on adding people to the bid
    if input("Are there other people that want to bid?(Y/N)\n>>> ").lower() == "y":
        clear()
        continue
    else:
        clear()
        break

# Winner evaluation
bidding_winner = highest_bid(bidders)
print(f"The winner is {bidding_winner[0]}, with a bid of ${bidding_winner[1]}.")
