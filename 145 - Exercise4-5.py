# Make a program to calculate factorial from any positive number entered by user

# Ask user for number
number = int(input("Enter a number to calculate it factorial: "))

# Checking input
while number < 0:
    print("Error: Number should be positive!!!")
    number = int(input("Enter a number to calculate it factorial: "))

# Calculating factorial
factorial = 1
for i in range(1, number + 1):
    factorial *= i 
print(f"\nThe factorial of {number} is: {factorial}\n")
