# Band name generator - 'for people that struggle with making up names'
#
# The program asks two questions and returns the name of a band based on the answers.

print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in?\n>>>> ")
pet = input("What is the name of your pet?\n>>>> ")
print("Your band name could be " + city.capitalize() + " " + pet.capitalize() + "!")
