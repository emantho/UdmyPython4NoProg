# Continue will not print the number 5
for i in range(10):
    if i == 5:
        continue
    print(i)

# Break will stop the programm whe reach 5 only printing up to 4
for i in range(10):
    if i == 5:
        break
    print(i)

    