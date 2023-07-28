"""def numero_par(num):
    if num%2 ==0:
        return True

numeros=[10,9,4,6,5,7]
print(list(filter(numero_par, numeros)))"""

numeros=[10,9,4,6,5,7]
print(list(filter(lambda numero_par: numero_par%2==0, numeros)))

class Empleado:
    def __init__ (self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    
    def __str__(self) -> str:
        return "{} que trabaja como {} tiene un salario de ${}".format(self.nombre,self.cargo,self.salario)

listaEmpleados=[
    Empleado("Juan", "Conserje",10000),
    Empleado("Ana", "Presidenta",1000000),
    Empleado("Pedro", "Gerente",100000)
]

salarios_altos=filter(lambda empleado: empleado.salario>=100000, listaEmpleados)

for empleado_salario in salarios_altos:
    print(empleado_salario)