edad=int(input('Introducir edad: '))

if 0<edad<100:
    print('Edad correcta')
else:
    print('Edad incorrecta')
#----------------------------------------------------------------------------

salario = int(input('Salario presidente: '))
salario2 = int(input('Salario ejecutivo: '))
salario3 = int(input('Salario conserje: '))

print('El salario del presidente es: ' + str(salario)) #Con la función str convierto el dato int en letras.
print('El salario del presidente es: ', salario)
#----------------------------------------------------------------------------

if salario3<salario2<salario:
    print('La empresa funciona bien')
else:
    print('Algo anda mal')




