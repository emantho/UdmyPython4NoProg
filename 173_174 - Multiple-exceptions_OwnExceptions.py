

## Multiple exceptions example
'''------------------------------'''
# def divide():
#     while True:
#         try: 
#             num1 = float(input("Enter a number: "))
#             num2 = float(input("Enter a number: "))
#             result = num1 / num2
#             print(f"the result is {result:.2f}")

#         except ZeroDivisionError: 
#             print("ERROR >> Zero division is not allowed")

#         except ValueError:
#             print("ERROR >> Must enter a number not a word or letter")

#         else: break
# divide()

## Launching our owns exceptions
'''------------------------------'''

def ageVerification(age):
    if age < 0:
        raise ValueError ("Age can't be negative")
    elif age < 18:
        print("You're to young")
    elif age < 30:
        print("You're young")
    elif age < 50:
        print("You're Mature")
    
age = int(input("Enter your age: "))

# exception appears in two places, but try / except must be write on the action where error ocurre
try:
    ageVerification(age)
except ValueError as NegativeAge:
    print(NegativeAge)


print("Program terminated")
