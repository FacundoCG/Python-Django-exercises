import re

nombres = ['Facu','Gabriel','Juan','Valentín','Mateo']

for i in nombres:
    if re.findall('[o-t]',i): #El - me permite establecer un rango. En este caso, indica que devuelva los elementos que tenga un caracter entre la o y la t
        print(i)

ciudades = ['Ma1','Se1','Ma2','Ba1','Ma3','Va1','Va2','Ma4','MaA','MA5','MaB','MaC']

for i in ciudades:
    #if re.findall('Ma[^0-3]',i): El ^ indica la negación del rango
    if re.findall('Ma[0-3 A-B]',i): #Estoy estableciendo dos rangos.
        print(i)