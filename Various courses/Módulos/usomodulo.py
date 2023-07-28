#import fmates #Importando el módulo entero, tengo que poner su nombre adelante de la función que quiera usar de él

#fmates.suma(7,5)
#fmates.resta(7,5)
#fmates.mult(7,5)

#from fmates import suma #Con esta sintaxis, solo importo la función que necesito
#suma(7,5)

from fmates import * #Con el * indico que quiero importar absolutamente todo lo que haya en el módulo
suma(5,5)
resta(7,3)