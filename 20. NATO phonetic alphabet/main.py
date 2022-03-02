import pandas as pd

# Get Nato phonetic codex
df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row.letter: row.code for (index, row) in df.iterrows()}


def name_to_nato(name):
    """Return a list of NATO phonetic codes, corresponding to the letters of name."""
    try:
        return [nato_dictionary[letter] for letter in name.upper()]
    except KeyError:
        raise ValueError("Only characters of the alphabet are accepted.")


if __name__ == "__main__":
    while True:
        try:
            user_name = input("What is your name? >>> ")
            print(name_to_nato(user_name))
            break
        except ValueError as err:
            print(err)
            continue
