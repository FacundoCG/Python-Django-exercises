class Coche():              
    
    def __init__(self): #Este método es un constructor que define el estado inicial de los objetos de la clase
        self.__largoChasis=250             
        self.__anchoChasis=120          #Con los dos guiones bajos encapsulo la propiedad para que no sea accedible del exterior de la clase
        self.__ruedas=4
        self.__enmarcha=False

    def arrancar (self,arrancamos):      
        self.__enmarcha = arrancamos
        if (self.__enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está detenido"
    
    def estado (self):           
        print("El coche tiene ",self.__ruedas," ruedas \nUn ancho de ",self.__anchoChasis," y un largo de ",self.__largoChasis)
        
coche1 = Coche()     

print(coche1.arrancar(True))  

coche1.estado()

print("---------Creando el segundo objeto-----------")

coche2 = Coche()

print(coche2.arrancar(False))

coche2.__ruedas=5 #Estoy modificando la propiedad del objeto, alterando su valor inicial. Ahora que la propiedad fue encapsulada, este comando no puede alterar el valor de la variable

coche2.estado()
