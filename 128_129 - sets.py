import collections
from imp import is_frozen


#Unordered data collections

conjunto = set() # used to create empty set
conjunto = {1,2,3,"eder",5} # can't contain other collections and booleans
print(conjunto)

conjunto.add("diana")
conjunto.add("emilia") # Append is 
print(conjunto)

conjunto.discard("eder")
print(conjunto)

conjunto.clear()
print(conjunto)

print("diana" in conjunto)

a = {1,2,3}
b = {3,4,5}
# comparing
print(a == b)
# lenght
print(len(a))
# conjunction
c = a | b
print(f"result c: {c}")
# intersection
d = a & b
print(f"result d: {d}")
# asimetric diference 
e = a - b
print(f"result e: {e}")
# simetric diference
f = a ^ b
print(f"result f: {f}")

a = frozenset({1,2,3}) # make it noneditable
print(a.issubset(c))
print(c.issuperset(a))

