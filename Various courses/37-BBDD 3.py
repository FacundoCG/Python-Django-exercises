import sqlite3

miConexion = sqlite3.connect('GestionProductos')

miCursor=miConexion.cursor()

miCursor.execute("""
    CREATE TABLE PRODUCTOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTÍCULO VARCHAR(50),
        PRECIO INTEGER,
        SECCIÓN VARCHAR(20)
    )
""")


productos = [
    ("Pelota", 20, "Juguetería"),
    ("Pantalón", 15, "Ropa"),
    ("Destornillador", 25, "Ferretería"),
    ("Jarrón", 45, "Cerámica")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

miConexion.commit()
miConexion.close()