class Humano():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

class Humano2():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"{self.nombre}\n{self.edad}"

yo = Humano('Facu',17)
tu = Humano2('Facu','17')

print(yo) #Imprimiendo de esta forma, Python imprime una posición en la memoria

print(tu) #Por otro lado, al usar la función str Python la detecta e imprime los datos que ella contenga