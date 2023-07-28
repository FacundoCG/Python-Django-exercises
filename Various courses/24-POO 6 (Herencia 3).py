class Persona ():
    def __init__ (self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar = lugar_residencia

    def descripcion (self):
        print("Nombre:",self.nombre, "\nEdad:",self.edad, "\nLugar:",self.lugar)

class Empleado (Persona):

    def __init__ (self,salario, antiguedad,nombre_e,edad_e,lugar_e):
        super().__init__(nombre_e,edad_e,lugar_e) #La función super llama al método de la clase padre, ni bien lo llama va a ejecutarlo y asignarle los valores correspondientes a las variables
        self.salario=salario
        self.antiguedad=antiguedad

    def descripcion (self):
        super().descripcion() #Se llama a la función de la clase padre para que se ejecute
        print('Salario: ',self.salario,
        "\nAntiguedad:",self.antiguedad)

Facu=Empleado(50000,1, "Facundo", 17, "Argentina")

Facu.descripcion()

print(isinstance(Facu, Persona)) #Esta función comprueba si una instancia pertenece a tal clase.

