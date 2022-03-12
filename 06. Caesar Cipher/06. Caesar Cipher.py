# Caesar Cipher
#
# A low level security encription app, that you can impress some of your friends with
import string
import math
import pyperclip
import os

# Constants
alpha = list(string.ascii_lowercase)
ALPHA = list(string.ascii_uppercase)


def encode(message, shift):
    # Encodes your message by shifting it right (in the alphabet) by the desired amount
    returning_message = []

    message = list(message)
    for letter in message:
        # Checks for special characters
        if letter in (string.punctuation + string.whitespace + string.digits):
            returning_message.append(letter)
            continue

        letter_index = alpha.index(letter.lower())

        # Checks the index to avoid crashes
        if letter_index + shift > 25:
            letter_index = letter_index - 26 * (math.floor((letter_index + shift) / 26))

        if letter in alpha:
            returning_message.append(alpha[letter_index + shift])
        if letter in ALPHA:
            returning_message.append(ALPHA[letter_index + shift])

        # Gives back the real shift, if shift was bigger than 26
    if shift > 26:
        print(f"\n!!!The real shift is {shift%26} !!!")

    return "".join(returning_message)


def decode(message, shift):
    # Decodes your message by shifting it left (in the alphabet) by the desired amount
    returning_message = []

    message = list(message)
    for letter in message:
        # Checks for special characters
        if letter in string.punctuation + string.whitespace + string.digits:
            returning_message.append(letter)
            continue
        letter_index = alpha.index(letter.lower())
        if letter_index - shift < 0:
            letter_index = letter_index + 26
        if letter in alpha:
            returning_message.append(alpha[letter_index - shift])
        if letter in ALPHA:
            returning_message.append(ALPHA[letter_index - shift])
    return "".join(returning_message)


# Main Loop
while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    # Art
    print("""           
     ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
    a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
    8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
    "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
     `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   


               88             88                                 
               ""             88                                 
                              88                                 
     ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
    8b         88 88       d8 88       88 8PP""""""" 88          
    "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
     `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                  88                                             
                  88           
    """)

    encode_or_decode = input("Do you wish to encode (\"0\") your secret message or to decode one (\"1\")?\n>>> ")

    # Encoding
    if encode_or_decode == "0":
        user_message = input("\nWhat is your secret message?\n>>> ")
        while True:

            # Checks for bad input
            try:
                user_shift = int(input("What's the shift number?\n>>> "))
            except (TypeError, ValueError):
                print("Bad input.")
                continue

            encoded_message = encode(user_message, user_shift)
            print("\nThis will be your message: " + encoded_message)

            choice = input("\nDo you want to change the shift?(Y/N)\n>>> ").lower()
            if choice == "n":
                break

        choice = input("Would you like to save this message to your clipboard?(Y/N)\n>>> ").lower()
        if choice == "y":
            pyperclip.copy(encoded_message)
            print("Messaged copied!")

    # Decoding
    elif encode_or_decode == "1":
        user_message = input("\nWhat is your secret message?\n>>> ")
        while True:
            # Checks for bad input
            try:
                user_shift = int(input("What's the shift number?\n>>> "))
            except (TypeError, ValueError):
                print("Bad input.")
                continue

            try:
                print("\n This is your message: " + decode(user_message, user_shift))
            except IndexError:
                print('Please use the "real shift" number (<=26).')
                continue
            break

    else:
        print("Wrong input.")
        continue

    # Restarts program
    choice = input("Would you like to encode/decode another message?(Y/N)\n>>> ")
    if choice == "n":
        break
