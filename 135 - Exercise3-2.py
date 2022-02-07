'''program with to list, and must do:
1- join tow list, show all elements of both list
2- Join two list, show only elements from first list
3- Join two list, show only elements from second list
4- Join two list, show elements that are repeated in both list
'''
l1 = ["Aracataca", "mz1", "Home", 2, 1, "Silver", "Black"]
l2 = ["Santa Marta", "Street", "Home", 5, 1, "Silver", "Red"]

sl1 = set(l1)
sl2 = set(l2)
lC = list(sl1 | sl2)
print(f"result of conjuction: {lC}")
lF = list(sl1 - sl2)
print(f"Result of l1 - l2: {lF}")
lS = list(sl2 - sl1)
print(f"Result of l2 -l1: {lS}")
lB = list(sl1 & sl2)
print(f"Result of intersection: {lB}")