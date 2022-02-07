from subprocess import list2cmdline


list = ["monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday","sunday",1,2.5,[1,2,3],False]
print(list) # print all list
print(list[0]) # print one index ascendent order
print(list[-3]) # print one index descendent order
print(list[0:3]) # [start:end]
print(list[9][1]) # Print index of list inside list

# lengh of list
print(len(list))

list = [1,2,3,4,5]

# append
list.append(6)
print(list)
# insert
list.insert(3,9) #(index, data)
print(list)
#extend
list.extend([6,7,8])
print(list)
# operation with list
list2 = [10,11,12]
list3 = list + list2
print(list3)
# Search in list
print(3 in list)
# Index in list
print(list.index(9))
# Count item in list
print(list.count(6))
# extract
print(list.pop(3)) #by default pop() erase the last item
# remove > erase item not index
print(list.remove(5))
print(list)
# clear list
list.clear()
# invert item in list
list = [1,2,3,4,5]
list.reverse()
print(list)
# sort list
list.sort() # sort(reverse=True) 
print(list)
