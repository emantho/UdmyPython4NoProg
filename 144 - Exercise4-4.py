# Make a program to add to even numbers inside a range

userRange = int(input("Enter a number to set a range: "))
addition = 0
for i in range(userRange + 1):
    if i % 2 == 0 and i > 0:
        addition += i
    
print(f"\nThe result of adding all even numbers is: {addition}")

    