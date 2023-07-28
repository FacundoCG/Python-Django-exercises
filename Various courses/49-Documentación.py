class area:
    '''Clase en la que se calculan áreas de figuras geométricas'''
    def area_cuadrado (lado):

        """Calcula el área de un cuadrado. El único argumento requerido es el lado"""

        return "El área del cuadrado es: " + str(lado*lado)


print(area.area_cuadrado(5))
print(area.area_cuadrado.__doc__) #Funcion.__doc__ devuelve la documentación de f

#help(area.area_cuadrado) #La ayuda de Python nos ofrece una ayuda más específica de la función
help(area)
