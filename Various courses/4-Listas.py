milista: list = ['A','B','C']

print(milista[:])

print(milista[2])

print(milista[-3])

print(milista[0:2])

print(milista[:2])

print(milista[1:])

milista.append('D') #Agrega el elemento al final

milista.insert(0, 'Z') #Yo elijo donde agregar al elemento

milista.extend(['E','F','G']) #Agrego varios elementos a la lista

del milista[1] #Borro el elemento que está en el indice 1 

milista

print(milista.index('F')) #Me da el indice del elemento que busco

print('J' in milista) #La función in nos dice si el elemento se encuentra en la lista.

milista.remove('Z') #Elimina el elemento Z

milista.pop() #Elimina el último elemento de la lista

print(milista[:]) 

lista1: list = ['FACU','YO', 5]
lista2: list = ['TÚ', 3]

lista3: list = lista1 + lista2 #Se concatenan las listas
print(lista3[:])
#----------------------------------------------------------------------------

lista3: list = lista3*3 #El asterico repite la lista.
print(lista3[:]) #[:] imprimo toda la lista

lista4: list = [1,2,3,4]
print(lista4[2:]) #Imprimo la lista a partir del tercer elemento
print(lista4[:3]) #Imprimo la lista hasta el tercer elemento
#----------------------------------------------------------------------------

lista4: list = [lista1, lista2, lista3] #Anido las listas
print(lista4[:])
print(lista4[1])

#----------------------------------------------------------------------------
lis: list = [3,11,9,7,5]
lis.sort() #Con la función sort se ordena los elementos de una lista
print(lis) 