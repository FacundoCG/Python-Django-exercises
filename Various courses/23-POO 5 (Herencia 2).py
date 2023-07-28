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
        "\nAcelera: ",self.acelera,"\nFrena: ",self.frena) #No tiene sentido agregar acá a self.caballito, ya que esa propiedad es exclusiva del objeto moto, quien tiene una clase propia. No todos los vehículos pueden hacer tal acción

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
    
    def estado (self): #Se sobreescribe el método heredado. Se llama a este método y no el de la clase padre, ya que el nuevo método heredado invalida al primigenio 
        print("Marca: ",self.marca, "\nModelo: ",self.modelo,"\nEn marcha: ",self.enmarcha,
        "\nAcelera: ",self.acelera,"\nFrena: ",self.frena, "\n",self.hcaballito) 

class VElectricos ():
    def __init__ (self):
        self.autonomia  = 100
    
    def energia (self):
        self.cargando = True

class BiciElectrica (VElectricos, vehiculos): #Herencia multiple. La primera clase escrita en los parentesis va a tener preferencia ante la segunda, si hay dos constructores, el primero será tomado en cuenta. 
    pass

moto1=Moto("Honda","CBR")

moto1.caballito()

moto1.estado()  

furgoneta1 = Furgoneta("Ford", "Kangoo")

furgoneta1.carga(True)

furgoneta1.arrancar()

furgoneta1.estado()

bicicleta1 = BiciElectrica() 

bicicleta1.estado() #Ocurre un error, ya que no le puedo asignar al método los argumentos requeridos. 