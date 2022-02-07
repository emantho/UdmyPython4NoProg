dictionary = {
    "socialNetworks":["Twitter","Facebook","Linkedin"],3:"tres","Hola":"Mundo"
}

# checking and printing items existences
print(dictionary.items())

# # checking and printing keys existences
print(dictionary.keys())

# checking and printing items existences
print(dictionary.values())

# POP, exporting and deleting items
print(dictionary.pop("Hola"))
print(dictionary)
print(dictionary.pop("Hola", "toPrint"))
print(dictionary)

# Delete only one element
del dictionary["socialNetworks"]
print(dictionary)

# Clining or wiping the dictionary
dictionary.clear()
print(dictionary)

# Add new item to dictionary
dictionary["newItem"] = "Diana"
print(dictionary)

# copy
dictionary2 = dictionary.copy()
print(dictionary2)