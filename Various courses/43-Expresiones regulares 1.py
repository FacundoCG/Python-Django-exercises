from cgitb import text
import re

cadena = "Zack Baloo Mascotas"

print(re.search("Baloo",cadena)) #Devuelve un objeto. Si no lo encuentro, regresa un none

frase = "Java PHP C Python"
textoBuscar="Python"

#if re.search(textoBuscar, frase) is not None:
    #print('He encontrado el texto')

#else:
    #print('No he encontrado el texto')

textoEncontrado = re.search(textoBuscar, frase)

print(textoEncontrado.start()) #Indica a partir de que caracter de la frase original empieza el texto

print(textoEncontrado.end()) #Indica a partir de que caracter de la frase original termina el texto

print(textoEncontrado.span()) #Devuelve los valores del método start y end en una tupla

frase2= "Python es un lenguaje multiparadigma. Asimismo, Python es de sintaxis sencilla."

print(len(re.findall(textoBuscar, frase2))) #Findall devuelve todas las veces que aparece una x palabra.