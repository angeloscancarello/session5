name = input("What is your name?")

age2 = input (f"How old are you {name}? ")
try:
    age2 = int(age2)
    print(f"{name}, you were born in {2024-age2}")
except:
    print("please enter a valid value for age")