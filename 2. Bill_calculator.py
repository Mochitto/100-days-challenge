# Bill_calculator
#
# This app helps you to calculate how much you will have to pay when eating out.

def tipcalculator(total, percentage, numberofpeople):
    if "," in total:
        total = ".".join(total.split(","))
    try:
        new_total = float(total) * (1 + int(percentage)/100)
        amout_per_person = new_total / int(numberofpeople)
        return str(round(amout_per_person, 2))
    except ValueError:  # Lets the user know the input is invalid, avoiding crashes
        raise Exception("Bad input")


if __name__ == "__main__":
    print("Welcome to Bill calculator!")
    bill_total = input("What was the total bill?\n>>>> $")
    chosen_percentage = input("What percentage would you like to tip?\n>>>> ")
    number_of_people = input("How many people to split the bill?\n>>>> ")
    try:
        pay_per_person = tipcalculator(bill_total, chosen_percentage, number_of_people)
        print(f"Each person should pay: ${pay_per_person}")
    except Exception as err:
        print(f"\nThere was an error: {err}")
