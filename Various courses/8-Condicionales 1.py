def nota (a):
    valoración='Aprobado'
    if a<6:
        valoración="Suspendido"
    return valoración

print(nota(4))
#----------------------------------------------------------------------------

print('Programa de evaluación')
note = int(input())

def app(n1):
    valoración='Aprobado'
    if n1<6:
        valoración="Suspendido"
    return valoración

print(app(note))
print('Su nota es', app(note))
#----------------------------------------------------------------------------

prueba = int(input('Introduzca su nota: '))

if prueba<6 and prueba>0:
    print('Reprobaste')
elif prueba>=6 and prueba<=10:
    print('Aprobaste')
else:
    print('Digitaste cualquier cosa')


