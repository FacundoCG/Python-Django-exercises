import pickle

lista = ["Facu","Gabriel","Juan"]

fichero_binario = open('archivob',"wb") #El wb indica que queremos escritura binaria

pickle.dump(lista, fichero_binario) #La función dump nos permite volcar la información en el fichero. El primer argumento es la información que queremos insertar, y el segundo es el nombre del fichero en la memoria Python

fichero_binario.close()

del(fichero_binario) #La función del lo borra de la memoria

fichero=open('archivob','rb') #Indico para leer en binario

mensaje=pickle.load(fichero) #La información que está en el fichero debemos cargarla en alguna variable para luego poder imprimirla

fichero.close()

print(mensaje)