s = '''One Hundred Years of Solitude is a 1967 novel by Colombian author Gabriel García Márquez 
that tells the multi-generational story of the Buendía family, whose patriarch, José Arcadio 
Buendía, founded the (fictitious) town of Macondo. The novel is often cited as one of the 
supreme achievements in literature. The magical realist style and thematic substance of One 
Hundred Years of Solitude established it as an important representative novel of the literary 
Latin American Boom of the 1960s and 1970s, which was stylistically influenced by Modernism 
(European and North American) and the Cuban Vanguardia (Avant-Garde) literary movement. '''

#Print lenght or character number
print(len(s))

# Method count, how many time it appears
print(s.count("is"))
print(s.count("is",0,200)) #(x,y,z) where x=term to search, y=startposition z=endPosition

# Print all text in upper (capital)
print(s.upper())
# Print all text in lower 
print(s.lower())

# Replace search and replace a letter o word 
print(s.replace("o","x",4)) #(x,y,z) where x=item2Replace y=newItem z=repetitions 

# Split, divide string based in defined parameters
print(s.split("a"))

# Find, look for position or term serched
print(s.find("is"))
print(s.rfind("is"))

t = ("H","o","l","a")
s = ";"

# Join
print(s.join(t))