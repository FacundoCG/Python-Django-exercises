import os

CARPETA = 'contactos/' #Las mayusculas remarcan que es una constante, que no se debe modificar.
EXTENSION = '.txt' #Extension de archivos.

#Contactos.
class Contacto():
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    #Revisa si la carpeta existe o no.
    crear_directorio()

    #Muestra el menu de opciones.
    mostrar_menu()

    #Preguntar al usuario la accion a realizar.
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opcion: \r\n')
        opcion = int(opcion)

        #Ejecutar las diferentes opciones.
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opcion no valida, intente de nuevo.')

def buscar_contacto():
    nombre = input('Seleccione el contacto que desea buscar: \r\n')

    try: #Este try intenta abrir este archivo, si no existe pasa al except.
        with open (CARPETA + nombre + EXTENSION) as contacto:
            print('Informacion del contacto: \r\n')
            for linea in contacto: 
                print(linea.rstrip())
    except IOError:
        print('El archivo no existe')
        print(IOError)

    app()

def eliminar_contacto():
    nombre = input('Seleccione el contacto que desea eliminar: \r\n')
    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('Contacto eliminado correctamente')
    except:
        print('No existe ese contacto')
    
    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA) #Nos permite listar los archivos de un directorio.
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    for archivo in archivos_txt:
        with open (CARPETA + archivo) as contacto:
            for linea in contacto: 
                print(linea.rstrip()) #Imprime los contenidos.

def editar_contacto():
    print('Escribe el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea reeditar \r\n')
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

            #Resto de los campos.
            nombre_contacto = input('Agrega el nuevo nombre del contacto:\r\n')
            telefono_contacto = input('Agrega el nuevo telefono del contacto: \r\n')
            categoria_contacto = input('Agrega una nueva categoria del contacto: \r\n')

            #Instanciar.
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribir en el archivo.
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

        #Renombrar el archivo.
        os.rename (CARPETA + nombre_anterior + EXTENSION,CARPETA + nombre_contacto + EXTENSION)

        #Mostrar mensaje de exito.
        print('Contacto editado correctamente')
    
    else:
        print('Ese contacto no existe')
    
    app()

def agregar_contacto():
    print('Escribe los datos para agregar al nuevo contacto:')
    nombre_contacto = input('Nombre del contacto:\r\n')

    #Revisar si el archivo ya existe.
    existe = os.path.isfile(CARPETA + nombre_contacto + EXTENSION) #Esta funciona revisa si un archivo existe previamente.
   
    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            #Resto de los campos.
            telefono_contacto = input('Agrega el telefono del contacto: \r\n')
            categoria_contacto = input('Categoria contacto: \r\n')

            #Instanciar la clase.
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            #Mostrar un mensaje de exito.
            print('\r\n Contacto creado correctamente \r\n')
    else:
        print('Ese contacto ya existe')
    
    #Reiniciar la app
    app()

def mostrar_menu():
    print('Seleccione del menu lo que desea hacer: ')
    print('1) Agregar nuevo contacto')
    print('2) Editar contacto')
    print('3) Ver contacto')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')

def crear_directorio():
    if not os.path.exists (CARPETA): #Con este comando revisamos si la carpeta existe.
        #Crear la carpeta.
        os.makedirs(CARPETA) #Con makedirs creamos el directorio.

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app ()