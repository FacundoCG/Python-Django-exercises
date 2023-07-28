
area_triangulo=lambda base,altura: (base*altura)/2

print(area_triangulo(5,7))

cubo = lambda numero: numero**3 #Una forma

cubo2 = lambda numero: pow(numero,3)

print(cubo2(3))

destacar = lambda comision: "¡{}! $".format(comision)

print(destacar(1900))