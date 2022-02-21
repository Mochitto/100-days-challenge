# Coffee machine
#
# What you need to start the day!
import sys
import time
import os

# Constants
COINS_VALUES = {
    "pennies": 0.01,
    "nickles": 0.05,
    "dimes": 0.10,
    "quarters": 0.25,
    "half-dollars": 0.50,
}

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Inventory
machine_inventory = {
    "ingredients": {
        # Liquids are in ml and coffee in grams
        "water": 1000,
        "milk": 1000,
        "coffee": 500,
    },
    "money": 0
}


# Functions
def clear():
    """Clears the terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def evaluate_input():
    """Asks for input and evaluates it.
    Can start the main function, return a str with the machine's inventory or turn off the app."""
    global machine_inventory

    pick = input("What would you like to have today?(espresso/latte/cappuccino)\n>>> ")

    if pick in ["espresso", "latte", "cappuccino"]:
        main(pick)

    # Return report and turn off the machine (for technicians only, no display)
    elif pick == "report":
        print(f"""The machine currently has in stock:
    water:{machine_inventory["ingredients"]["water"]}
    milk: {machine_inventory["ingredients"]["milk"]}
    coffee: {machine_inventory["ingredients"]["coffee"]}
    
    Money: {machine_inventory["money"]}\n"""
              )
        evaluate_input()
    elif pick == "off":
        sys.exit()
    else:
        clear()
        print("Please pick one of the beverages.")
        evaluate_input()


def translate_coins(cost) -> str:
    """Asks how many coins to insert and translates coins to money."""
    # Dictionary used for translation
    global COINS_VALUES

    coins = {
        "pennies": 0,
        "nickles": 0,
        "dimes": 0,
        "quarters": 0,
        "half-dollars": 0,
    }

    # Gets the coins, translates them and gives visual feedback.
    total_money = 0
    for coin in coins:
        while True:
            try:
                coins[coin] = int(input(f"\nHow many {coin}? "))

                total_money += COINS_VALUES[coin] * coins[coin]

                # Shows the coins so far
                total_money = "{:.2f}".format(total_money)
                print(f"Your total so far : ${total_money}")

                # Turns back str into float to continue calculating
                total_money = float(total_money)
                break

            except ValueError:
                print("Invalid Input")
                continue
        if total_money >= cost:
            break
    # User Experience
    total_money = "{:.2f}".format(total_money)
    return total_money


def enough_resources(coffee) -> (str, float):
    """Raises an Exception if the machine resources aren't enough to make the coffee. Returns the cost of the coffee"""
    global machine_inventory
    global MENU

    for ingredient in MENU[coffee]["ingredients"]:
        if machine_inventory["ingredients"][ingredient] - MENU[coffee]["ingredients"][ingredient] < 0:
            raise Exception(f"Not enough resources. {coffee.capitalize()} is out of service.")

    return f"{coffee.capitalize()} is available. The cost is ${'{:.2f}.'.format(MENU[coffee]['cost'])}", \
           MENU[coffee]['cost']


def pay(money: float, coffee: str) -> int:
    """Raises an Exception if the inputted money is not enough.
    Adds the money to the machine inventory and returns the change"""
    global MENU
    global machine_inventory

    cost = MENU[coffee]["cost"]
    change = money - cost

    # Check if enough money
    if change < 0:
        money = '{:.2f}'.format(money)
        raise Exception(f"\n${money} is not enough.\n")

    machine_inventory["money"] += cost
    return change


def change_to_coins(change) -> str:
    """Translates the change to coins. Returns a string with each coin as \n
    - n_of_coins coin """
    global COINS_VALUES
    coins = {
        "pennies": 0,
        "nickles": 0,
        "dimes": 0,
        "quarters": 0,
        "half-dollars": 0,
    }
    for coin in reversed(coins):
        coins[coin] = int(change // COINS_VALUES[coin])
        change -= COINS_VALUES[coin] * coins[coin]
        change = round(change, 2)

    change = []
    singular = {
        "pennies": "penny",
        "nickles": "nickle",
        "dimes": "dime",
        "quarters": "quarter",
        "half-dollars": "half-dollar",
    }

    for coin in coins:
        number_of_coins = coins[coin]
        if number_of_coins != 0 and number_of_coins > 1:
            change.append(f"- {number_of_coins} {coin}.")
        elif number_of_coins == 1:
            change.append(f"- {number_of_coins} {singular[coin]}.")
    change = "\n".join(change)

    return change


def make_coffee(coffee):
    """Subtracts the ingredients needed by the machine to make coffee from its inventory"""
    global MENU
    global machine_inventory
    for ingredient in machine_inventory["ingredients"]:
        try:
            machine_inventory["ingredients"][ingredient] -= MENU[coffee]["ingredients"][ingredient]
        except KeyError:
            continue


def main(choice):
    try:
        cost = enough_resources(choice)
    except Exception as err:
        print(err)
        print()
        evaluate_input()
    print(cost[0])
    cost = cost[1]
    money = translate_coins(cost)
    try:
        change = pay(float(money), choice)
    except Exception as err:
        clear()
        print(err)
        main(choice)
    if change:
        print("\nYour change will be:\n" + change_to_coins(change))
    make_coffee(choice)

    print("\nThank you for your purchase!")
    time.sleep(3)
    clear()
    evaluate_input()


if __name__ == "__main__":
    evaluate_input()
