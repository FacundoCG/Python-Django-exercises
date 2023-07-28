class Empleado:
    def __init__ (self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    
    def __str__(self) -> str:
        return "{} que trabaja como {} tiene un salario de ${}".format(self.nombre,self.cargo,self.salario)

listaEmpleados=[
    Empleado("Juan", "Conserje",6000),
    Empleado("Ana", "Presidenta",100000),
    Empleado("Pedro", "Gerente",10000)
]

def calculo_comision(empleado):

    if(empleado.salario<= 6000):
        empleado.salario=empleado.salario*1.03

    return empleado

listaEmpleadosComision=map(calculo_comision, listaEmpleados)

for i in listaEmpleadosComision:
    print(i)