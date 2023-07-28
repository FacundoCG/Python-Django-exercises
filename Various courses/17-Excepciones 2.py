def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
    try:		            #Con el try se indica que hacer en caso de que ocurra una excepción en la función del programa
        return num1/num2
    except:
        print('No se puede dividir por 0')
        return "Operación errónea"

while True:                 #Con este bucle infinito, le informo al usuario que está ingresando un tipo de dato incorrecto, y le doy la oportunidad de que los reingrese
    try:
        op1=(int(input("Introduce el primer número: ")))

        op2=(int(input("Introduce el segundo número: ")))

        break
    except ValueError:		
        print('Los datos ingresados son incorrectos. Intente de nuevo.')

operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")

print("Operación ejecutada. Continuación de ejecución del programa")
#----------------------------------------------------------------------------
def dividir ():
    try:
        n1 = float(input('Digite un número: '))
        n2 = float(input('Digite un número: '))
        
        print('La división es: '+ str(n1/n2))
    except ValueError:              #También se pueden calcular excepciones en general sin poner un argumento al lado del except. Da igual cual excepción sea, ya que el programa la va a agarrar
        print('El valor introducido es erróneo')
    except ZeroDivisionError:
        print('No se puede dividir por cero')
    
    finally:            #Con finally se ejecutará el código siempre, sin importar que ocurran excepciones. Para introducirlo debe haber si o si un try previamente
        print('Cálculo finalizado')



