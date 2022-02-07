# Ask user for a phrase, then replace all blanks for an asterics, also (moreover) all words must be capitalized

user1 = input("\nEnter a phrase: ")
user1 = user1.replace(" ","*")
user1 = user1.title()

print(f"The phrase resulting is: {user1}")