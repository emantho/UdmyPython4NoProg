# Make a program to define the greatest of three numbers

number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))
number3 = float(input("Enter another number: "))

if number1 >= number2 and number1 >= number3:
    print(f"The greatest number is {number1}")
elif number2 >= number3 and number2 >= number1:
    print(f"The greatest number is {number2}")
elif number3 >= number2 and number3 >= number1:
    print(f"the greatest number is {number3}")