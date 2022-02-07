#WHILE
age = 0
while age <= 20:
    
    #Avoid print 15
    if age == 15:
        age = age + 1
        continue
        #instead "continue", can be use "break" to stop program when this condition be reached
    
    print ("You're: " + str(age))
    age = age + 1

#FOR IN
list = ["element1", "element2", "element3"]

for element in list:
    print(element)

for letter in "Elements":
    print(letter)
