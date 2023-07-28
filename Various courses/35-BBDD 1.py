import sqlite3

miConexion = sqlite3.connect('PrimeraBase') #Creo y hago conexión con la BBDD

miCursor=miConexion.cursor() #Creo el cursor. Este me va a permitir hacer las queries

# miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR (50), PRECIO INTEGER, SECCION VARCHAR(20))") #Creo la tabla

miCursor.execute("INSERT INTO PRODUCTOS VALUES ('Balón', 15, 'Deportes')")

miConexion.commit() #Confirmo el cambio que estoy haciendo en la tabla al agregar valores.

miConexion.close() #Cierro BBDD