import sqlite3

miConexion = sqlite3.connect('db.sqlite3')

miCursor = miConexion.cursor()

#miCursor.execute("""
#    CREATE TABLE CURSOS (
#        CURSO VARCHAR (30) PRIMARY KEY,
#       INTEGRANTES INTEGER
#    )
#""")

#cursos = [("Django", 25), ("HTML", 10), ("JavaScript", 30)]

#miCursor.executemany("INSERT INTO CURSOS VALUES (?,?)", cursos)

miConexion.commit()

miConexion.close()

