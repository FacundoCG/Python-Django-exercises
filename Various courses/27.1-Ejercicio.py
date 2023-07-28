mail = input('Introduzca una dirección de mail: ') #Solución propia

while (mail.isdigit()==True):
    print('Introduzca un mail con valores alfanumericos')
    mail = input('Introduzca una dirección de mail: ')

contador=0
for i in mail:
    if i == "@":
        contador+=1
    else:
        continue

if mail.endswith("@"):
    contador=0

elif (mail.find("@")==0):
    contador=0

if contador==1:
    print('Su dirección de correo es correcta')

else: 
    print('Su dirección de correo no es valida')

#Solución del video

usuariom = input('Introduzca su mail: ')
arroba=usuariom.count("@")

if (arroba!=1 or usuariom.rfind("@")==(len(usuariom) - 1) or usuariom.find("@")==0) :
    print('El mail es incorrecto')

else:
    print('El mail es correcto')