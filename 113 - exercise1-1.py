# Ask user to input three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

result = (a**3 * (b**2 - (2*a*c))/(2*b))
print(f"The operation result is: {result}")