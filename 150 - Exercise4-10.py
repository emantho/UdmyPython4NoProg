# Ask for a string, the store each character in a list without repetitions

## --- Using SETs -----
user = input("\nEnter a phrase or word: ") # user enter the string
user = user.replace(" ","") # deleting blanks

word = []

for l in user: 
    word.append(l)

user = list(set(word)) # Converting list in set and then in list again to delete words repeated
print(f"\nList without repeated characters: \n\t{user}")

## --- Usingn IN ----
'''# Asking user
user = input("\nEnter a phrase or word: ")
user = user.replace(" ","")
word = []

for l in user:
    if l not in word:
        word.append(l)

print(f"\nResult without repeated words: {word}")
'''