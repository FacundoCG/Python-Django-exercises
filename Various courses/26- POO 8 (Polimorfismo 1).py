class Coche():

    def desplazamiento(self):
        print("Me desplazo con 4 ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo con 2 ruedas")

class Camion():

    def desplazamiento(self):
        print('Me desplazo con 6 ruedas')

def desplazarvehiculo (vehiculo): #El polimorfismo ocurre aquí, el objeto vehiculo1 se asigna a la variable de este método y llama al método universal de su clase correspondiente
    vehiculo.desplazamiento()

vehiculo1= Camion()
vehiculo2 = Coche()

desplazarvehiculo(vehiculo1)
desplazarvehiculo(vehiculo2)