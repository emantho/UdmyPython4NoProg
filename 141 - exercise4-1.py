# Create a list with number from 1 to 50, then print this in the form 1-2-3...-50 using for 

# Appending items from 1 to 50 in list
list50 = []
for i in range(1,51):
    list50.append(i)

# Using range converted a list 
list50 = list(range(1,51))

# Printing list items separated by comma
for i in list50:
    print(f"{i}",end="-")
        


    


