''' Write a program which contains the following characters: 
Name:   Aragorn             Gandalf     Legolas
Clase:  Guerrero            Mago        Arquero
Raza:   Dúnadan del norte   Istar       Elfo Sindar      
'''
from subprocess import list2cmdline

characters = []
character1 = {"Name":"Aragorn","Class":"Warrior","Race":"North Dunadan"}
character2 = {"Name":"Gandalf","Class":"Magician","Race":"Istar"}
character3 = {"Name":"Legolas","Class":"Archer","Race":"Sindar Elf"}

characters.append(character1)
characters.append(character2)
characters.append(character3)
print(characters)