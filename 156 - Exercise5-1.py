# Make a program to compare two string, printing who's the larger and how many characters have, in caso of tie inform that and tha number of characters

string1 = input("\nEnter a word or phrase: ")
string2 = input("\nEnter second word o phrase: ")

if len(string1) == len(string2):
    print(f"\nBoth words o phrases are same lenght: {len(string1)} ")
elif len(string1) > len(string2):
    print(f"\nThe firts word or phrase is larger and have {len(string1)} characters.")
elif len(string1) < len(string2):
    print(f"\nThe second word or phrase is larger and have {len(string2)} characters.")
