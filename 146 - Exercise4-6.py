# Make a program that ask for a number, store it multiplication table until number 10

number = int(input("\nEnter a number to get it multiplication table: "))
result = 0
tableM = []
for i in range(1,11):
    result = number * i
    tableM.append(f"{number} * {i} = {result}")
print(f"\nThe result is: \n{tableM}")
