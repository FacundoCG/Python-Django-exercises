from cgitb import text
from tkinter import *
from tkinter import messagebox
import sqlite3
from tokenize import String

from pyparsing import col

#Funcionalidades barra menú
def conexionBBDD():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    try:
        miCursor.execute("""
            CREATE TABLE DATOSUSUARIOS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_USUARIO VARCHAR (35),
                APELLIDO VARCHAR (35),
                PASSWORD VARCHAR (50),
                DIRECCIÓN VARCHAR (50),
                COMENTARIOS VARCHAR (100)
            )
        """)

        messagebox.showinfo("BBDD", "Base de datos creada con éxito.")
    
    except:
        messagebox.showwarning("¡Atención!", "La base de datos ya existe.")

def salir():
    valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicación")

    if valor == "yes":
        root.destroy()

def borrarCampos():
    miId.set("")
    miNombre.set("")
    miApellido.set("")
    miPass.set("")
    miDireccion.set("")
    textoComentario.delete(1.0, END)

def crearCRUD():
    miConexion=sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    datos=miNombre.get(), miApellido.get(), miPass.get(), miDireccion.get(), textoComentario.get("1.0",END)

    """miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,  '" + miNombre.get() + "', '" + miApellido.get() + "', '" + miPass.get() + "',  '" + miDireccion.get() + "','" + textoComentario.get("1.0",END) + "')")"""

    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL, ?,?,?,?,?)", (datos))

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro ingresado con éxito")

def leerCRUD():
    miConexion=sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miId.get())

    elUsuario = miCursor.fetchall()

    for usuario in elUsuario:
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miApellido.set(usuario[2])
        miPass.set(usuario[3])
        miDireccion.set(usuario[4])
        textoComentario.insert(1.0, usuario[5])

    miConexion.commit()

def actualizarCRUD():
    miConexion=sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    datos=miNombre.get(), miApellido.get(), miPass.get(), miDireccion.get(), textoComentario.get("1.0",END)

    """miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() + "', APELLIDO='" + miApellido.get() + "', PASSWORD='" + miPass.get() + "', DIRECCIÓN='" + miDireccion.get() + "', COMENTARIOS = '" + textoComentario.get("1.0", END) + "' WHERE ID = " + miId.get())"""

    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO = ?, APELLIDO=?, PASSWORD=?, DIRECCIÓN=?, COMENTARIOS=?" + "WHERE ID="+ miId.get(), (datos))
    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro actualizado con éxito")

def borrarCRUD():
    miConexion=sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miId.get())

    miConexion.commit()

    messagebox.showinfo("BBDD","Registro borrado con éxito.")

#Inicio app
root=Tk()

#Barra menú
barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salir)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=borrarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crearCRUD)
crudMenu.add_command(label="Leer", command=leerCRUD)
crudMenu.add_command(label="Actualizar", command=actualizarCRUD)
crudMenu.add_command(label="Borrar", command=borrarCRUD)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de ...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)



#Inputs Campos 
miFrame=Frame(root)
miFrame.pack()

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

cuadroID=Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroPass=Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=3, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario= Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

#Labels campos
idLabel = Label(miFrame, text="Id: ")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

passLabel = Label(miFrame, text="Contraseña: ")
passLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel = Label(miFrame, text="Dirección: ")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentarioLabel = Label(miFrame, text="Comentario: ")
comentarioLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#Botones inferiores
miFrame2=Frame(root)
miFrame2.pack()

botonCrear= Button(miFrame2, text="Crear", command=crearCRUD)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer= Button(miFrame2, text="Leer", command=leerCRUD)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar= Button(miFrame2, text="Actualizar", command=actualizarCRUD)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar= Button(miFrame2, text="Borrar", command=borrarCRUD)
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)


#Cierre app
root.mainloop()