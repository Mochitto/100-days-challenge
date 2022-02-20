# Calculator App
#
# A very basic calculator that you can use from the terminal

import os

# Art
logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


# Functions
def clear():
    """Clears the terminal, changes depending on the os of the machine"""
    os.system('cls' if os.name == 'nt' else 'clear')


def addition(a, b):
    """Adds a to b, returns their sum"""
    return a + b


def subtraction(a, b):
    """Subtracts b from a, returns the remaining value"""
    return b - a


def multiplication(a, b):
    """Multiplies a and b, returns the resulting value"""
    return a * b


def division(a, b):
    """Divides a by b, returns the resulting value"""
    return a / b


def squared(a):
    """Returns the value of a squared"""
    if a <= 0:
        return "Error"
    return a ** 0.5


def root(a, b):
    """Returns the value of the b root of a"""
    if a <= 0:
        return "Error"
    return a ** (1 / b)


def elevate(a, b):
    """Returns a^b"""
    return a ** b


def check_input_number(user_input, message="Invalid input"):
    """Raises Exception(message) if the user_input is not a number."""
    try:
        float(user_input)
    except ValueError:
        raise Exception(message)


def check_input_operation(user_input):
    if user_input not in "+$-$*$/$^$root$sqrt":
        raise Exception("Please use a valid input.")


def evaluate_operation(number1, number2, user_input):
    if user_input == "+":
        return addition(number1, number2)
    elif user_input == "-":
        return subtraction(number1, number2)
    elif user_input == "*":
        return multiplication(number1, number2)
    elif user_input == "/":
        return division(number1, number2)
    elif user_input == "^":
        return elevate(number1, number2)
    elif user_input == "root":
        return root(number1, number2)
    else:
        raise Exception("Operation not supported.")


# Main function
def main():
    # Used for consecutive calculations
    last_number = 0

    # Main loop
    while True:
        clear()

        # ASCII ART
        print(logo)

        if last_number == 0:  # Check if first number undefined
            # Define first number
            while True:
                First_number = input("What's the first number?\n>>> ")
                try:
                    check_input_number(First_number, "Please input a number.")
                except Exception as err:
                    print(err)
                    continue
                break
            First_number = float(First_number)
        else:
            First_number = last_number
            print(f"First number: {last_number}")

        print("""
Possible operations:
+ (Addition)          - (Subtraction)
* (Multiplication)    / (Division)
^ (Elevation)         root (Root)
        sqrt (Square Root)
""")

        # Defines operation
        while True:
            operation = input("Pick an operation\n>>> ").lower()
            try:
                check_input_operation(operation)
            except Exception as err:
                print(err)
                continue
            break

        # If the opertaion is square, there is no need for a second number
        if operation == "sqrt":
            result = squared(First_number)
            Second_number = ""

        else:
            # Defines second number
            while True:
                Second_number = input("\nWhat's the second number?\n>>> ")
                try:
                    check_input_number(Second_number, "Please input a number.")
                except Exception as err:
                    print(err)
                    continue
                break
            Second_number = float(Second_number)

            # Calls the right function to evaluate the result
            result = evaluate_operation(First_number, Second_number, operation)

        # Display result
        print(f"{First_number} {operation} {Second_number} = {result}")

        # Makes user choose between continuing with the result, starting over or exiting the program.
        if result == "Error":
            next_operation = input(
                f"""Type \"y\" to start a new calculation. Any other input will exit the program.""").lower()

            if next_operation == "y":
                last_number = 0
                continue
            else:
                break
        else:
            next_operation = input(
                f"""Type \"y\" to use {result} in the next operation, type \"n\" to start a new calculation. 
Any other input will exit the program.""").lower()

            if next_operation == "y":
                last_number = result
                continue
            elif next_operation == "n":
                last_number = 0
                continue
            else:
                print('\n\n' + "Thank you for using our calculator!".center(50, "*"))
                break


if __name__ == "__main__":
    main()
