# Make a program to count al vowels in a string, then show how many times each vowel appears.

# ask for string
user1 = input("Enter a word or phrase: ")
user1 = user1.lower()
aCount = user1.count("a")
eCount = user1.count("e")
iCount = user1.count("i")
oCount = user1.count("o")
uCount = user1.count("u")

'''
aCount, eCount, iCount, oCount, uCount = 0, 0, 0, 0, 0

# Searching for vowels
for i in user1:
    if i == "a":
        aCount += 1
    elif i == "e":
        eCount += 1
    elif i == "i":
        iCount += 1
    elif i == "o":
        oCount += 1
    elif i == "u":
        uCount += 1
    else:
        continue
'''
print(f"The Quantity of vowels is: a:{aCount}, e:{eCount}, i:{iCount}, o:{oCount}, u:{uCount}")
