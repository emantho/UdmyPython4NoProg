# Function with one item returned
def multiplicator(num1,num2):
    mult = num1 * num2
    return mult

print(multiplicator(3,2))
result = multiplicator(7,9)
print(result)

# function returning multiple item
def prueba():
    return "Hola",45,[5,7,9]

print(prueba()) # printing all function
s,n,l = prueba() # Calling and printing item separated
print(s)
print(n)
print(l)