'''
Make a game, guess a number between 0 and 100 randomly generated, the tell user
"is greater" o "is minor" depending of which options is. The game's over when user 
guess the number, the try number must be show with the hide number
'''
import random

# Create the hide number
numbers = list(range(101))
hideNumber = random.choice(numbers)
# hideNumber = random.randint(0,100) is a shorter way

# Contruction of game
game = True
tries = 0

while game:
    user = int(input("\nEnter a number between 0-100: "))
    tries += 1
    if user > hideNumber:
        print("\tIs not the mumber, enter a lower.")
        #tries += 1
    elif user < hideNumber:
        print("\tIs not the numner, enter a highger.")
        #tries += 1
    elif user == hideNumber:
        print(f"\nYou won!!! The hide number is: {hideNumber}")
        game = False
print(f"\nYou made {tries} tries")


