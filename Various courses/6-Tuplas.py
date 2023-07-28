mitupla: tuple = (3,'hola',8)
mitupla[1]
#----------------------------------------------------------------------------

milista: list = list(mitupla) #Convierto una tupla a lista
milista[:]
#----------------------------------------------------------------------------

lista: list = [2,5,'hola']
tupla:tuple = tuple(lista)
tupla[:]
#----------------------------------------------------------------------------

print(7 in mitupla)
#----------------------------------------------------------------------------

mitupla.count(3) #Pone las veces que se encuentra el elemento buscado
#----------------------------------------------------------------------------

len(mitupla) #Cuenta los elementos que hay en la tupla
#----------------------------------------------------------------------------

tupla_unitaria: tuple = ('yo') #Es una tupla con un único elemento
len(tupla_unitaria) 
#----------------------------------------------------------------------------

tupla_sin_parentesis = 3,5,'chau' #Escribir una tupla sin parentesis se conoce como empaquetado de tupla.
tupla_sin_parentesis[:]
#----------------------------------------------------------------------------

tupla_ejemplo: list = ['facu', 30, 4]
nombre, día, mes = tupla_ejemplo 

"""Esto se llama desempaquetado de tupla, a cada variable se le asigna un valor de la tupla"""

print(f'''{nombre}
{día}
{mes}''')

print(tupla_ejemplo.index('facu'))