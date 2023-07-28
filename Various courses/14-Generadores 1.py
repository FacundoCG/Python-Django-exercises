def Generapares (limite):
    n=1

    while n<limite:
        yield n*2    
        n+=1
        
dp = Generapares(8)

print(next(dp))

print('Espacio') #Entre llamada y llamada el objeto generado entra en un estado de suspensión

print(next(dp))

print('Espacio')

print(next(dp))

print('Espacio')