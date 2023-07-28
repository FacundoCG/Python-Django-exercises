distancia =int(input('Kilometros para la escuela: '))
hermanos = int(input('Hermanos para la escuela: '))
salario = int(input('Salario para la escuela: '))

if distancia>60 and hermanos>3 or salario<10000:
    print('Cumples los requisitos para la beca')
else:
    print('No cumples los requisitos')
#----------------------------------------------------------------------------

print('Asignaturas 2021: Catequesis - Física - Biología')
asignatura = input('Introduzca su asignatura: ')
#----------------------------------------------------------------------------

option = asignatura.lower() #Esta función pasa a minusculas la palabra introducida
#----------------------------------------------------------------------------

option2 = asignatura.upper() #Esta función pasa a mayusculas la palabra introducida
#----------------------------------------------------------------------------

if option in ('catequesis', 'física', 'biología'): #Python diferencia entre mayusculas y minusculas (case sensitive).
    print('La asignatura elegida es: ',option)
else:
    print('La asignatura elegida no está disponible')

