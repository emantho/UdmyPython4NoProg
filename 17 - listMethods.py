from http import server


list = [1, "dos", 3]

# Search
search = 5
print( search in list)

# index
if search in list: # It's need to be used in index
    print(list.index(search))
else: print("Element does'n exist")

# Append
print(list)
list.append(10)
print(list)

# Count how many times one item appear
print(list.count(3))

# Insert
list.insert(7,"nuevo") #index of where new item will be insert is required (1,"new")
print(list)

# Extend > create a new list using iterable objects as list, tuple or string
list.extend("strings")
list.extend(("s",6,"e"))
print(list)

# pop > extract and erase
list.pop() #by default erase the last item, index must be given
print(list)

# remove
list.remove("t") # erase first coincidence
print(list)

'''for item in list:
    if "s" in list:
        list.remove("s")
        print(list)
    else: print("No more S to delete")'''

while "s" in list:
    list.remove("s")
    print(list)

# reverse
list.reverse()
print(list)