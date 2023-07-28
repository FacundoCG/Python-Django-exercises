def app():
    with open('archivo.txt') as archivo: #Cuando utilizamos with open no es necesario cerrar la conexion al archivo, se hace automaticamente.
        for contenido in archivo:
            print(contenido.rstrip()) #Con rstrip se remueven los saltos de linea.

app()

#archivo_texto=open('archivo.txt',"r")

#print(archivo_texto.read()) #La funcion read lee todo el archivo desde el comienzo. Una vez que se ejecuta, el cursor pasa a estar en el final, entonces si la llamado devuelta no imprime nada

#archivo_texto.seek(0) #Con la función seek hacemos que el cursor vaya a la posición que deseemos. En este caso, con 0 se posiciona al principio

#print(archivo_texto.read(11)) #Dando un argumento le indicamos hasta donde queremos que lea

#archivo_texto.seek(len(archivo_texto.read())/2)

#print(archivo_texto.read())

archivo_texto=open('archivo.txt',"r+") #El r+ pone al archivo en modo lectura y escritura al mismo tiempo

archivo_texto.write('Modificando la primera línea') #En este modo, el cursor está en el 0. Por ende, estoy reescribiendo lo que haya al principio

lista=archivo_texto.readlines()

lista[2]="Esta línea ha sido incluida desde el exterior\n"

archivo_texto.seek(0)

archivo_texto.writelines(lista)

archivo_texto.close()
