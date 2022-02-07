lista1 = [2, "tres", 2.5, [1.5, "casa"]]
#indices [0]   [1]    [2]       [3]
#indNeg  [-4]  [-3]   [-2]      [-1]
print(lista1)

#Imprimir item de lista
print(lista1[2])
#Crear una nueva lista
lista2 = lista1[1]
print(lista2)
# Indices negativos inician desde el último item con -1
print(lista1[-3])
#acceder a una lista dentro de una lista, se usa doble cuadrado con los indices requeridos
lista3 = lista1[3][1]
print(lista3)
#Modificar lista
lista1[0]="uno"
print(lista1)
lista1[0:2]=[4,3]
print(lista1)
#Extraer items
lista5 = lista1[0:3] #donde 0 = indiceInicio : 3 = cantidadItems
print(lista5)
lista6a = lista1[0:3:1] #donde 0 = indiceInicio : 3 = cantidadItemsDesdeInicio : 2 = saltoxItemDesdePrimer
lista6b = lista1[0:3:2] #donde 0 = indiceInicio : 3 = cantidadItemsDesdeInicio : 2 = saltoxItemDesdePrimer
lista6c = lista1[0:3:3] #donde 0 = indiceInicio : 3 = cantidadItemsDesdeInicio : 2 = saltoxItemDesdePrimer
print(lista6a)
print(lista6b)
print(lista6c)
