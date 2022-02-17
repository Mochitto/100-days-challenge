# PyPassword generator - Creates a strong password!
#
# This app contains a function that lets you create a strong password of any desired length, while also deciding
# if to include letters, numbers and symbols or to exclude one or more of them.
import random


def password_generator(length, letters=1, symbols=1, numbers=1):
    # Returns a password with the desired characters groups.
    # If left unspecified, the function will return a password with at least one lowercase letter, one uppercase,
    # one symbol and one number.
    #
    # length = length of the password
    # letters, symbols, numbers: 0 = do not include, 1 = include this characters group

    # Variables that are used throughout the function
    alpha = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v',
             'w', 'x', 'y', 'z')
    ALPHA = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    numb = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    symb = list(r""" ~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/""")
    password = ""

    # Raises exception if the length is not a number
    if not length.isdigit():
        raise Exception("Length is not an intger.")
    length = int(length)

    totaltimes = length  # Lenght of the password

    groups_list = []  # Defines a list from where to take the desired character type
    groups = 0  # Makes it so that all the desired characters will be included at least once in the password.
    if letters:
        groups += 2
        groups_list.append(alpha)
        groups_list.append(ALPHA)
    if numbers:
        groups += 1
        groups_list.append(numb)
    if symbols:
        groups += 1
        groups_list.append(symb)

    # Raises Exception if the number of characters is too little to have at least one character of each group.
    if length <= groups:
        raise Exception(f"The password can't be shorter than the minimum amound of characters required: {groups + 1}")

    # Shuffles order of groups
    random.shuffle(groups_list)

    # Main algorithm
    for character_group in groups_list:
        times = 0
        for n in range(random.randint(1, round(totaltimes - groups))):
            password += random.choice(character_group)
            times += 1
        totaltimes -= times
        groups -= 1
    # Adds up characters to reach the desired length
    for n in range(totaltimes):
        password += random.choice(groups_list[random.randint(0, len(groups_list) - 1)])

    # Shuffles password to avoid the creation of patterns
    password = list(password)
    random.shuffle(password)
    password = "".join(password)
    return password


if __name__ == "__main__":
    import pyperclip

    print("Welcome to the PyPassword Generator!\n")
    user_input = input("How long should your password be? (suggested 13+)\n> ")
    while True:
        try:
            Yourpassword = password_generator(user_input)
            print("\n" + Yourpassword)
            if input("Would you like to keep use this password?(Y/N)\n> ").lower() == "y":
                pyperclip.copy(Yourpassword)
                print("\nPassword copied to your clipboard!")
                break
            else:
                continue
        except Exception as err:
            print(err)
            continue
