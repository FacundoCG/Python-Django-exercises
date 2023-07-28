import re

nombre1 = "Sandra López"
nombre2= "Antonio Gómez"
nombre3 = "sandra López"
nombre4 = "Lara López"
nombre5 = "Jara López"

cadena1="54565654"
cadena2="a54565654"

code1 = "jkajksdsajdksajdjak64sakdasjk"
code2 = "sdajldaldad64jasjkdas"

'''if re.match("Sandra", nombre3, re.IGNORECASE): #El parámetro ignorehace hace que la función no distinga entre mayusculas y minusculas
    print('Hemos encontrando el nombre') #La función match siempre busca al inicio de la palabra
else:
        print('No hemos encontrando el nombre')'''

'''if re.match(".ara", nombre5, re.IGNORECASE): #El carácter . indica que en ese lugar puede ir una letra cualquiera
    print('Hemos encontrando el nombre')
else:
        print('No hemos encontrando el nombre')'''

'''if re.match("\d", cadena1): #El \d busca si la cadena empieza o no con un número
    print('Hemos encontrando el número')
else:
    print('No hemos encontrando el número')'''

if re.search("López", nombre3): #La función search busca al patrón de busqueda en la totalidad del texto
    print('Hemos encontrado el nombre')
else:
    print('No hemos encontrado el nombre')

if re.search("64", code2): 
    print('Hemos encontrado el número')
else:
    print('No hemos encontrado el número')