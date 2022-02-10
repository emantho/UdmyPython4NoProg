'''
Make a program to add all digits from a number, using recursive functions
'''
def numbersAddition(num):
    if num == 0: 
        result = 0
    else:
        result = numbersAddition(int(num/10)) + (num%10)
    
    return result

value = numbersAddition(123)
print(value)