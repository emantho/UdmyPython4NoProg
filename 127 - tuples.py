from subprocess import list2cmdline


tuple = (4, "eder",True,2.5,[1,5,9],7)
print(tuple)
print(tuple[4])
print(tuple[4:7])
print(4 in tuple)
print(tuple.index("eder"))
print(tuple.count(5))
print(len(tuple))
 #tuple to list
list = list(tuple)
print(list)
#list to tuple
list = [4,"eder",True,2.5,[1,5,9],7]
tuple = tuple(list)