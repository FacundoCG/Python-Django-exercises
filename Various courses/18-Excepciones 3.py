import math

def edad(n):

    if n<0:
        raise TypeError ('La edad digitada es incorrecta.') #Con raise uno puede lanzar excepciones
    elif n<20:
        return 'Eres muy joven'
    
    elif n<40: 
        return "Eres joven"

    elif n<55: 
        return "Eres un adulto"

    elif n<100: 
        return "Cuidate"

edad(96)

def mate (n1):
    if n1<0: 
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(n1)

op = int(input('Introducir un número: '))

try:            #Hay que capturar la excepción que se levantó en la función porque si no, no se corren las últimas lineas.
    mate(op)
except ValueError as ErrorNegativo:
    print(ErrorNegativo)

print('Programa terminado')