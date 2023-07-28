nombre = input('Digite su nombre: ')

print('Su nombre es: ',nombre.upper()) #El texto se pone todo en mayusculas

print('Su nombre es: ',nombre.lower()) #Devuelve todo en minusculas

print('Su nombre es: ',nombre.capitalize()) #Pone solo la primer letra en mayuscula

print('Su nombre es: ',nombre.title()) #Pone la primer letra de cada palabra en mayuscula

print(nombre.isdigit()) #Evaluacion booleano sobre el valor para saber si es un numero

edad = input('Introduce la edad: ')

while (edad.isdigit()==False): 
    print('Por favor introduzca un valor numérico')
    edad = input('Introduce la edad: ')

if (int(edad)<18):
    print('No puede pasar')

else:
    print('Puede pasar')