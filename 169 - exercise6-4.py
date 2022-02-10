'''
Make a program to calculate number factorial using recursive functions
'''

def uFactorial(num):
    if num > 0:
        isFacto = num * (uFactorial(num-1))
    else:
        isFacto = 1

    return isFacto

print(uFactorial(5))