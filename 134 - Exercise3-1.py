'''# remove repeated items in list
l = []
l = input("enter 10 items separated by comma: ")
print(f"These are your entered items: {l}")
l2 = set(l)
l = list(l2)
l.sort()
print(f"These are your item without those not repited: {l}")'''

# shorter 

l = input("enter 10 items separated by comma: ")
l = list(set(l))
l.sort()
print(l)