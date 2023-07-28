def dev (*ciudad): #El asterisco significa que a la función se le pueden asignar varios parametros
    for elementos in ciudad:
        for subelementos in elementos:
            yield subelementos  #Utilizo for anidados
v=dev('Barcelona', 'Madrid','Bs.As')
print(next(v))
print(next(v))
#----------------------------------------------------------------------------
def dv (*city): 
    for i in city:
        yield from i

a=dv('Barcelona',"Madrid","Bs.As")
print(next(a))
print(next(a))
