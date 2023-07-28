import pickle

class Persona():
    def __init__(self,nombre,edad,genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        print('Se ha creado una persona con el nombre de: ',nombre)

    def __str__(self): #El método str convierte en cadenas de texto la información de un objeto
        return 