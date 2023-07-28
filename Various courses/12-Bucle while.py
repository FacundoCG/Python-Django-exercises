import math
print('Programa de cálculo de raíz cuadrada')
n = int(input('Introduce un número por favor: '))
intento=0

while n<0:
    print('No se puede hallar la raíz de un número negativo')
    
    if intento==2:
        print('Demasiados intentos')
        break

    n=int(input('Introdce un número por favor: '))
    if n<0:
        intento+=1

if intento<2:
    r=math.sqrt(n)
    print(f'La raíz cuadrada de {n} es: {r}')
#----------------------------------------------------------------------------

i=1

while i<=10:
    print(f'El valor de i es {i}')
    i+=1

print('El programa ha finalizado')
#----------------------------------------------------------------------------

edad=int(input('Digite su edad: '))

while edad<0 or edad>125:
    print('Ha digitado una edad incorrecta')
    edad=int(input('Digite su edad: '))

print('Gracias por haber digitado su edad')
print('Su edad es: '+str(edad))