# Ask for numbers and store it in a list, exit and print when user insert 0

print('''This program will create a list with the numbers you enter, to exit enter Zero (0)''')
numberUser = float(input("Enter number: "))
listUser = []
while numberUser != 0:
    listUser.append(numberUser)
    numberUser = float(input("Enter number: "))

listUser.sort()
print(f"The list of number you've enter is: {listUser}")