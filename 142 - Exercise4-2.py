# Fill a list with numbers from 1 to 10, then change the elements multipliying this for a 
# number entered by user

### Resolution #1
#----------------
'''from wsgiref.validate import validator


listNew = []
list10 = list(range(1,11)) # Creating List with 10 items 

# User modification
print(f"This is the initial list: {list10}")
userModification = int(input("Please anter a number to multiply for each item: "))

for item in list10:
    nuevo = item * userModification
    listNew.append(nuevo)
list10 = list(listNew)    
print(f"This is the resulting list: {list10}")'''

### Resolution #2
#----------------
'''list10 = list(range(1,11)) # Creating List with 10 items 

# User modification
print(f"This is the initial list: {list10}")
userModification = int(input("Please anter a number to multiply for each item: "))
index = 0
for i in list10:
    list10[index] *= userModification
    index += 1
print(f"This is the resulting list: {list10}") 
'''
### Resolution #3
#----------------
list10 = list(range(1,11)) # Creating List with 10 items 
# User modification
print(f"This is the initial list: {list10}")
userModification = int(input("Please anter a number to multiply for each item: "))

for index,i in enumerate(list10):
    list10[index] *= userModification

print(f"This is the resulting list: {list10}") 