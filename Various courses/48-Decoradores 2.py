from random import expovariate


def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args, **kwargs): #El *args significa que la función va a recibir un número indeterminado de parámetros

        print('Por realizar un cálculo ...')

        funcion_parametro(*args, **kwargs) #El **kwargs toma (exclusivamente) argumentos clave-valor

        print('Cálculo realizado')
    
    return funcion_interior

@funcion_decoradora
def suma(n1,n2,n3):
    print(n1+n2+n3)

def resta(n1,n2):
    print(n1-n2)

@funcion_decoradora
def potencia(base,exponente):
    print(pow(base,exponente))

#suma(10,9,1)
potencia(base=5, exponente=3) #Los parámetros estan en formato clave-valor. En este caso, las claves son base y exponentes, y los valores 5 y 3