#Ahora vamos a dejar que el usuario introduzca el nombre del archivo
nombre_archivo = input('Introduzca el nombre del archivo: ')
#Con el try y except vamos a salir del programa si el archivo introducido es incorrecto
try:
    archivo = open(nombre_archivo)
except:
    print('Nombre de archivo incorrecto, no se puede abrir:',nombre_archivo)
    quit()  #Así se sale del programa

cont = 0    #Ahora ejecutamos el bucle
for linea in archivo:
    if linea.startswith('Subject:'):#Contamos las lineas que contienen Subject: en el archivo introducido
        cont = cont + 1
print('Hay',cont,'lineas que contienen Subject en el archivo',nombre_archivo)