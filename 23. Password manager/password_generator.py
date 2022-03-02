import random
import string
import math

import pyperclip


def generator(length: int, **kwargs: int) -> str:
    """Generate a secure password. Suggested: length >= 16

    Accepts kw: A=(Uppercase), a=(lowercase), num=(numbers), symb=(symbols).
    length = length of the password.
    If kw are left untouched, it defaults to 1/4 of length to alfa, with remainder evenly distributed between symbols
    and numbers (the first being preferred for extra remainder).
    """
    # Exceptions handling
    if not str(length).isdigit() or length < 0:
        raise ValueError("Length must be a positive integer.")
    for value in kwargs.values():
        if not str(value).isdigit() or value < 0:
            raise ValueError("KeyWord argument must be a positive integer.")

    # CONSTANT
    CHARACTERS = {
        "A": string.ascii_uppercase,
        "a": string.ascii_lowercase,
        "num": string.digits,
        "symb": string.punctuation,
    }

    # Variables
    password = ""
    remaining = ["symb", "num", "A", "a"]  # In order of priority, the first getting the most remainder

    # MAIN
    characters_numbers = {}  # Used to construct how many characters per group

    # Get kwargs
    if kwargs:
        characters_numbers = characters_numbers | kwargs

        for key in kwargs:
            remaining.remove(key)

        for value in kwargs.values():
            length -= value

    # Add groups that aren't in kw to the dictionary
    try:
        first_number = math.floor(length / len(remaining))
        second_number = math.floor(length % len(remaining) // 2)
        third_number = length % len(remaining) % 2

        for index, key in enumerate(remaining):
            if index == 0:
                characters_numbers[key] = first_number + second_number + third_number  # Highest priority group (=symb)
            elif index == 1:
                characters_numbers[key] = first_number + second_number  # Medium priority group (=num)
            else:
                characters_numbers[key] = first_number  # Low priority group (=Alfa)
    except ZeroDivisionError:
        pass  # Avoid crash if all kw have been used

    # Password generation
    for key, value in characters_numbers.items():
        for _ in range(value):
            password += random.choice(CHARACTERS[key])

    # Shuffle
    password = list(password)
    random.shuffle(password)
    password = "".join(password)

    pyperclip.copy(password)
    return password


if __name__ == "__main__":
    print(generator("ciao", a=3, A=2))