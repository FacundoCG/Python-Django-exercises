from io import *

menu = open("menu.txt",'r')

menu.write('Bebida: Coca Cola\nComida: Hamburguesa\nPostre: Helado')

comidas = menu.readlines()

menu.close()

print(comidas)