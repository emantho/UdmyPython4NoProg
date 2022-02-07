# Make a program which ask for 2 numbers and define which is even or if both are even

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))

if number1 != str and number2 != str: 
    if number1 % 2 == 0 and number2 % 2 == 0:
       print(f"Both numbers {number1} and {number2} are even")
    elif number1 % 2 != 0 and number2 % 2 != 0:
        print(f"None number is even")
    elif number1 % 2 == 0:
        print(f"number {number1}, is even")
    else: print(f"number {number2}, is even")

else: print(f"the data entered is not a number!")

