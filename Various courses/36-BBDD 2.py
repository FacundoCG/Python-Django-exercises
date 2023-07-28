import sqlite3

miConexion = sqlite3.connect('PrimeraBase')

miCursor=miConexion.cursor()

variosProductos = [
    ("Camiseta", 10, 'Deportes'), 
    ("Jarrón", 90, "Cerámica"), 
    ("Camión", 20, "Juguetería")
]

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos) #Insertar un lote de registros.

miCursor.execute("SELECT * FROM PRODUCTOS")

listaProductos = miCursor.fetchall()

for producto in listaProductos:
    print("Nombre artículo: " + producto[0], "- Sección: "+producto[2])

miConexion.commit()
miConexion.close()