import sqlite3

miConexion = sqlite3.connect('GestionProductos2')

miCursor=miConexion.cursor()

#Unique hace que dicho campo no admita información repetida.
'''
miCursor.execute("""
    CREATE TABLE PRODUCTOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTÍCULO VARCHAR (50) UNIQUE, 
        PRECIO INTEGER,
        SECCIÓN VARCHAR(20)
    )
""")
'''

productos = [
    ("Pelota", 20, "Juguetería"),
    ("Pantalón", 15, "Ropa"),
    ("Destornillador", 25, "Ferretería"),
    ("Jarrón", 45, "Cerámica"),
    ("Pantalones", 25, "Ropa")
]

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

#miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCIÓN = 'Ropa' ")

miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTÍCULO='Pelota' ")

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5 ")

informacion = miCursor.fetchall()

for item in informacion:
    print(item)

miConexion.commit()
miConexion.close()