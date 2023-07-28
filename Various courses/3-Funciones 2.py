def suma(n1,n2):
    print(n1+n2)

suma(3,4)

suma(3.5,7)

suma('hola','chau')
#----------------------------------------------------------------------------
def resta (n1: int,n2:int = 0)->int: #Si no ingresan nada en el segundo parametro, se toma a 0 como default
    resultado:int = n1-n2

    return resultado



