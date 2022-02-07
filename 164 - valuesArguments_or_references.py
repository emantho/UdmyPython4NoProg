
# value arguments = all items not collections
def double(number):
    number *= 2
    print(number)
# original valur of n, is never alterated
n = 5
print(n)
double(n)

# Reference Arguments = used in collections
def double_values(numbers):
    for i,n in enumerate(numbers):
        numbers[i] *= 2

n = [5,10,15,20]
double_values(n)
print(n)

# to send a copy of list and not alterate this, send it sliced
def double_values1(numbers):
    for i,m in enumerate(numbers):
        numbers[i] *= 2
m = [5,10,15,20]
double_values1(m[:])
print(m)



