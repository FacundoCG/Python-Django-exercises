class vehiculos():                     
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

class Furgoneta(vehiculos):
    def carga (self, carga):
        self.cargado= carga
        if (self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"

class Moto (vehiculos):
    hcaballito=""
    def caballito (self):
        self.hcaballito="Voy haciendo el caballito"
    
    def estado (self): 
        print("Marca: ",self.marca, "\nModelo: ",self.modelo,"\nEn marcha: ",self.enmarcha,
        "\nAcelera: ",self.acelera,"\nFrena: ",self.frena, "\n",self.hcaballito) 

class VElectricos (vehiculos):
    def __init__ (self,marca,modelo):
        super().__init__(marca,modelo) #Con la funcion super llamo al constructor de la clase padre y lo ejecuto
        self.autonomia  = 100
    
    def energia (self):
        self.cargando = True

class BiciElectrica (VElectricos, vehiculos): 
    pass

moto1=Moto("Honda","CBR")

moto1.caballito()

moto1.estado()  

furgoneta1 = Furgoneta("Ford", "Kangoo")

furgoneta1.carga(True)

furgoneta1.arrancar()

furgoneta1.estado()

bicicleta1 = BiciElectrica("Honda","CB500") 

bicicleta1.estado()