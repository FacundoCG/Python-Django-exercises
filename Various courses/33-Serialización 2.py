import pickle
 
class vehiculos():                     #Clase padre
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
    
    def arrancar (self):
        self.enmarcha=True

    def acelerar (self):
        self.acelera = True

    def frenar (self):
        self.frena = True

    def estado (self):
        print("Marca: ",self.marca, "\nModelo: ",self.modelo,"\nEn marcha: ",self.enmarcha,
        "\nAcelera: ",self.acelera,"\nFrena: ",self.frena)

coche1 = vehiculos('Ford','Ecosport')
coche2= vehiculos('Fiat','200')
coche3 = vehiculos('Renault','Megane')

coches = [coche1,coche2,coche3]

fichero = open('Coches','wb')

pickle.dump(coches, fichero)

fichero.close()

del(fichero)

