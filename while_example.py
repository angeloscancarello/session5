from random import randint

lives = 3
while lives > 0:
    roll = randint(1,6)
    if roll == 6:
        print("You rolled a 6! You win!")
        break #this exists the while eben if lives still > 0
    else:
        print(f"You rolled a {roll}! You lose a life.")
        lives -= 1
        print(f"Lives left: {lives}")
else:
    print("You lost!")
