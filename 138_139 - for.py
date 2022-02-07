
#using with collections
import collections


for i in [1,2,3,4,5]:
    print("Hello World")

#Collection inside for
for i in [2,10,3,4,"eder"]:
    print(f"Elemnt: {i}")

#Collection outside for
collection = [2,10,3,4,"eder"]
for i in collection:
    print(f"Elemnt: {i}")

# Can be used with Tuples and Stacks
tuple1 = (2,10,3,4,"eder")
stack1 = {2,10,3,4,"eder"}

#Using with dictionaries
dict = {"eder":35,"diana":36,"emilia":3}

# Only print the Key
for i in dict:
    print(f"Elem: {i}")
# Only print the value
for i in dict:
    print(f"Elem: {dict[i]}")
# Printing Key and Values, long form
for i in dict:
    print(f"Elem: {i} -> {dict[i]}")

# printing key and value shot form
for key,value in dict.items():
    print(f"Elem: {key} -> {value}")

# Printing strings
for i in "Manjarres":
    print(f"{i}",end=",")

# Printing Ranges
for i in range(10):
    print(i)

# using limits
for i in range(5,11):
    print(i)

# with limits and hops
for i in range(0,20,2): # (x,y,x) where: x=start y=end z=hop
    print(i)

