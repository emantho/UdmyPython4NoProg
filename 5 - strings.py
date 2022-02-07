# Comillas simples
stringSimple = 'Texto en comillas simples'

#Comillas dobles
stringDoble = "Texto en comillas dobles"

#Comillas triples
strgingMultiLinea = """ 
Texto 
en
linea
Multiple
"""

#Caracteres de escape
conTabulacion = "Texto \t tabulado"
conSalto = "Texto \n con salto"
saltoMasTabulacion = "Texto \n con salto \t y tabulado"

print(stringSimple)
print(stringDoble)
print(strgingMultiLinea)
print(conTabulacion)
print(conSalto)
print(saltoMasTabulacion)

#Repetir o duplicar strings
string1 = "Eder" * 3
print(string1)

# Concatenar strings
string2 = " Manjarres"
print(string1 + string2)


# Booleans
'''
AND 
True = Both are True, else are False
False = Both are False, else are True

#OR
True = When both are not False
False = When both are False

#NOT
Invert AND or OR
'''

bAnd1 = True and False
bAnd2 = True and True
bAnd3 = False and False

bOr1 = True or True
bOr2 = False or False
bOr3 = True or False

print(bAnd1)
print(bAnd2)
print(bAnd3)

print(bOr1)
print(bOr2)
print(bOr3)
