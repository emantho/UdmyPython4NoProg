from distutils.command.clean import clean


dictionary = {}

# show dictionry
print(dictionary)
# create
dictionary = {"Azul":"Blue", "Rojo":"Red", "Verde":"Green"}
print(dictionary)
# 
print(dictionary["Azul"])
# Add info
dictionary["amarillo"] = "yellow"
print(dictionary)
# Delete
del(dictionary["Verde"])
print(dictionary)
# Nesting dictionaries
dictionary2 = {"Eder":{"edad":35,"Hight":1.79},"Diana":[36,1.68], "Emilia":[3,1.10]}
print(dictionary2["Eder"]["edad"])# seeing item inside dictionaries
# exceptions handling
print(dictionary2.get("eder","Name without info"))
# 
print("eder" in dictionary2)
# 
print(dictionary2.keys())
#
print(dictionary2.values())
#
print(dictionary2.items())
#
print(len(dictionary2))
#
dictionary2.clear()


