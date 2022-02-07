# Make a program where user enter a phrase, give it back to the user without blanks, and 
# moreover inform how many characters are in the phrase

# Catching phrase from user
phrase = input("\nEnter a phrase to edit: ")
print(f"\nOriginal Phrase is: {phrase}")
newPhrase = ""
# Erase blank spaces
for letter in phrase:
    if letter == " ":
        continue
    else:
        newPhrase += letter
print(f"\nFinal Phrase: {newPhrase}")
print(f"\n# of Charaters: {len(newPhrase)}")

# ---------------- Shorter form
'''# Ask for phrase
phrase = input("\nEnter a phrase to edit: ")
print(f"\nOriginal Phrase is: {phrase}")
# Erasing blank spaces
new = phrase.replace(" ","")
# Printing phrase
print(f"\nFinal Phrase: {new}")
print(f"\n# of Charaters: {len(new)}")'''