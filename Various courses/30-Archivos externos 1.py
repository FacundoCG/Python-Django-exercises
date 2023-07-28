from io import open

def app():
    #Crear el archivo.
    archivo = open('archivo.txt', 'w') # W es escritura, si no existe lo creara.

    #Generar numeros en un archivo.
    for i in range (0, 20):
        archivo.write('Esta es la linea ' + str(i) + '\r\n') #Write es el comando para escribir en un archivo.
    
    #Cerrar el archivo.
    archivo.close()
    
app()

archivo_texto=open("archivo.txt","w") #El archivo con open se puede abrir en modo lectura, escritura, o para agregarle información si ya tiene contenido
#Si no existe el archivo, Python lo crea

frase="Estupendo dia para estudiar Python\nEl lunes"

archivo_texto.write(frase)

archivo_texto.close() #Con cerrar hace referencia a cerrar el archivo que hemos abierto en memoria desde Python

archivo_texto=open("archivo.txt","r") #Abro el archivo para leerlo

leer = archivo_texto.read() #Almaceno el contenido del archivo en una variable para posteriormente leerlo

archivo_texto.close()

print(leer)

archivo_texto=open("archivo.txt","r")

lineas = archivo_texto.readlines() #Guarda la información en una lista que almacena las lineas de texto

archivo_texto.close()

print(lineas)

print(lineas[0])

archivo_texto=open("archivo.txt","a") #La a establece al archivo en modo extensión

archivo_texto.write("\nSiempre es una buena ocasion para estudiar python")

archivo_texto.close()