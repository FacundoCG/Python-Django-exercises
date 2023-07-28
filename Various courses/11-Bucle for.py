for i in [1,2,3]: #Lo que hace el bucle en su primer vuelta es igualar i al primer elemento, y luego repite lo mismo hasta que ya no puede asignarle a la variable i valores.
    print('Hola')
#----------------------------------------------------------------------------

for i in "juan":
    print(i)
#----------------------------------------------------------------------------

for i in ['primavera','hola','chau','facu']:
    print(i) 
#----------------------------------------------------------------------------

for i in [1,2,3]: 
    print('Hola', end=" ") #El argumento end impide que haya salto de linea.
#----------------------------------------------------------------------------

for i in 'facu': #Se imprime la palabra i según que tantos caracteres tenga la palabra.
    print(i)
#----------------------------------------------------------------------------

email = False
miemail=input('Introduzca su mail: ')

for a in miemail:
    if a=="@":
        email = True
    else:
        email = False

if email==True:
    print('El email es correcto')

else:
    print('El email es incorrecto')
#----------------------------------------------------------------------------

mail = input('Deposite el mail: ')
contador=0
for c in mail:
    if c=="@" or c==".":
        contador=contador+1
    else:
        contador+=0

if contador>=2:
    print('El email es correcto')

else:
    print('El email es incorrecto')
#----------------------------------------------------------------------------

for i in range(5): 
    print(i)
#----------------------------------------------------------------------------

for i in range(4): 
    print(f'Valor de la variable {i}') #Concateno el valor de la variable
#----------------------------------------------------------------------------

for i in range(1, 21, 2):
    print(f'El valor de la variable es {i}')
#----------------------------------------------------------------------------
validar = False
hotmail = input('Digite el mail: ')

for i in range(len(hotmail)):
    if hotmail[i] =="@":
        validar = True

if validar == True:
    print('Bien')
else:
    print('Mal')