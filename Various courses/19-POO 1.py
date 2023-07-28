class Coche():              #Defino la clase
    largoChasis=250             
    anchoChasis=120          #Propiedades de la clase. Son 4 en total
    ruedas=4
    enmarcha=False

    def arrancar (self):      #Comportamiento de la clase, se determina mediante un método. Self hace referencia al objeto de la clase
        self.enmarcha = True    #Para cambiar el comportamiento hay que utilizar adelante de la propiedad el self.
    
    def detener (self):
        self.enmarcha = False 
    
    def estado (self):              #La clase en total tiene 2 comportamientos
        if (self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está detenido"

coche1 = Coche()     #Instanciar una clase/Ejemplarizar la clase

print("El largo del coche es: ",coche1.largoChasis) #Veo la propiedad del objeto
print("El ancho del coche es: ",coche1.anchoChasis)
print("El coche tiene: ",coche1.ruedas," ruedas")

coche1.arrancar()  #El método arrancar lo enciende

print(coche1.estado()) #El método estado nos indica cual es su situación


