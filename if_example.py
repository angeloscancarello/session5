from random import choice

drinks = ["whiskey", "rum", "tequila", "gin", "sake", "wine", "beer", "vodka"]
mixers = ["fanta", "fanta limon", "redbull", "tonic", "cola", "soda"]

print("I am the virtual bartender, welcome to my humble bar")
name = input("How should I call you?")

try:
    age = input("How old are you?")
    age = int(age) #this is where we can have problems if the number is expressed with characters
    legal = None
    country = input("Where are you from? ")
    if age < 14:
        legal = False
    elif age < 16:
        if country == "Austria":
            legal = True
        else:
            legal = False
    elif age < 18:
        if country == "Austria" or country == "Luxembourg":
            legal = True
        else:
            legal = False
    elif age < 21:
        if country == "USA" or country == "UAE":
            legal = False
        else:
            legal = True
    else:
        legal = True
    if legal:
        print(f"Here is a {choice(drinks)} {choice(mixers)}")
    else:
        print (f"I can only serve you {choice(mixers)}")
except ValueError:
    print("I don't have time for your games! Get Out")