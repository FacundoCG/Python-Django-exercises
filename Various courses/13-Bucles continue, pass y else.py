for letra in "Python":
    if letra=="h":
        continue #Cuando se cumple dicha instrucción, el continue ignora las lineas restantes del bucle, y lo reinicia empezando en la siguiente vuelta
    print('Viendo la letra: ' + letra)
#----------------------------------------------------------------------------

nombre="Facundo Coronel"
c=0

for i in nombre:
    if i==" ":
        continue
    c+=1

print('La cantidad de letras en '+nombre+" son: "+str(c))
#----------------------------------------------------------------------------

class Miclase:
    pass   #Para implementar más tarde, la función pass da un valor nulo. Se usa cuando se requisiera una declaración, pero no queremos ejecutar código

#----------------------------------------------------------------------------

email=input('Introduce un email: ')
for i in email:
    if i=="@":
        arroba=True
        break

else:               #Si no se cumple la condición del bucle, se pasa directamente al else, ya que este forma parte del bucle for
    arroba=False

print(arroba)
#----------------------------------------------------------------------------

