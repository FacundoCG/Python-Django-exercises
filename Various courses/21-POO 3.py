class Coche():              
    
    def __init__(self):
        self.__largoChasis=250             
        self.__anchoChasis=120          
        self.__ruedas=4
        self.__enmarcha=False

    def arrancar (self,arrancamos):      
        self.__enmarcha = arrancamos
        if (self.__enmarcha):
            prueba=self.__chequeo()
        
        if (self.__enmarcha and prueba): 
            return "El coche está en marcha. Chequeo exitoso."
        elif (self.__enmarcha and prueba == False):
            return "Problemas en el chequeo."
        else:
            return "El coche está detenido."
    
    def estado (self):           
        print("El coche tiene ",self.__ruedas," ruedas \nUn ancho de ",self.__anchoChasis," y un largo de ",self.__largoChasis)

    def __chequeo (self):   #Encapsulamiento de método. De esta forma, desde el exterior de la clase no se puede llamarlo
        print("Realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False
    
coche1 = Coche()     

coche1.gasolina="mal" #Al estar encapsulado el método donde se guarda dicha variable, no se puede alterar el valor de esta desde fuera

print(coche1.arrancar(True))  

coche1.estado()

print("---------Creando el segundo objeto-----------")

coche2 = Coche()

print(coche2.arrancar(False))

coche2.estado()