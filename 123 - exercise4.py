#Build a basic calculator

num1 = float(input("Enter a number: "))
num2 = float(input("Enter other number: "))
oper = input("Enter operation using first letter: ").lower()

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
#div = num1 / num2

if oper == "a" or oper == "s" or oper == "m" or oper == "d":
    if oper == "a":
        print(f"Result of addition is: {add}")
    elif oper == "s":
        print(f"Result of substraction is: {sub}")
    elif oper == "m":
        print(f"Result of Multiplication is: {mul}")
    elif oper == "d":
        if num2 != 0:
            div = num1 / num2
            print(f"Result of Division is: {div}")
        else: print(f"Division by Zero is not allowed") 
    
else: print(f"Wrong insertion, please check and retry")    
