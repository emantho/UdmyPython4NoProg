# Make a program to ask one letter and say it is vowel or not

char = str(input("Enter a letter: ")).lower() #convert to lower to capital letter 
#letra = char.lower()

if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
    print(f"letter {char} is vowel")
else: print(f"letter {char} is not a vowel")

