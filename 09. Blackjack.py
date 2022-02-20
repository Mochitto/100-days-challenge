# Blackjack
#
# A fun game that some people like so much, they spend all of their money into!
import random
import os

# Art
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

# Deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Functions
def clear():
    """Clears the terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def draw(person):
    """Function to draw a card from the deck. Person is a list of cards."""
    global cards
    card = random.choice(cards)
    person.append(card)


def check_overflow(person):
    """Check if the total of the cards is over 21. If so, check if there are Aces and turns them into 1."""
    if sum(person) > 21:
        if 11 in person:
            person[person.index(11)] = 1
            return
    if sum(person) >= 21:
        return True


def check_winner(person1, person2):
    """Check who is the winner and returns a string. User is person1. person1 and person2 are lists of cards"""
    if (sum(person1) == sum(person2)) or (sum(person1) > 21 and sum(person2) > 21):
        return "It's a draw!".center(50, "*")
    elif sum(person1) > 21:
        return "You lose.".center(50, "*")
    elif sum(person2) > 21:
        return "You win.".center(50, "*")
    else:
        return "You win!".center(50, "*") if sum(person1) > sum(person2) else "You lose.".center(30, "*")


def main():
    """A game of Blackjack"""
    clear()
    print(logo)
    User_cards = []
    CPU_cards = []

    # Beginning draws
    for _ in range(2):
        draw(User_cards)
        draw(CPU_cards)
    print(f"\n    Your cards: {User_cards}")
    print(f"    Computer's first card: {CPU_cards}")

    while sum(CPU_cards) < 21 and sum(User_cards) < 21:
        pass_or_continue = input("Type \"y\" to get another card, type \"n\" to pass: ").lower()
        # Draw more cards
        if pass_or_continue == "y":
            draw(User_cards)

            if sum(CPU_cards) < 17:
                draw(CPU_cards)

            if check_overflow(User_cards):
                break
            if check_overflow(CPU_cards):
                break

            print(f"\n    Your cards: {User_cards}")
            print(f"    Computer's cards: {CPU_cards}")
            continue

        else:
            break

    while sum(CPU_cards) < 17:
        draw(CPU_cards)
        check_overflow(CPU_cards)
    print(f"\n    Your final cards: {User_cards}")
    print(f"    Computer's final cards: {CPU_cards}")
    print(check_winner(User_cards, CPU_cards))

    main() if input("\nDo you want to play again?(y/n)\n>>> ").lower() == "y" else print("\nThanks for playing!")


if __name__ == "__main__":
    main()
