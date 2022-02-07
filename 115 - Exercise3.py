a = 10
b = 5

c = a
d = b

a = d
b = c

print(f"{c} and {d} Original value, now is {a} and {b}")

#easiest form

a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

print(f"original value of a:{a} and b:{b}")
a , b = b , a

print(f"New value of a:{a} and b:{b}")
