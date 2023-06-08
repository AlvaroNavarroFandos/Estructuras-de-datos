#Programa que leyendo de un archivo de texto, clasifica cada mensaje de correo dependiendo del día que se ha recibido
#Para esto, buscar las líneas que empiezan con 'From', después la tercera palabra de cada línea es el día de la semana, hacer un cont y print
archivo = input('Ingresa el nombre de archivo: ')

try:
    n_archivo = open(archivo)
except:
    print('El archivo no se puede abrir: ',archivo)
    exit()

dicc = dict()
for linea in n_archivo:     #Solo este bucle porque solo nos interesan las lineas 'From' y luego en concreto solo importan la palabra[2] de cada linea
    linea = linea.rstrip()
    if not linea.startswith('From '):
        continue
    palabras = linea.split()    #Transformamos la linea en una lista
    fecha = palabras[2]         #Cogemos la palabra de la fecha
    dicc[fecha] = dicc.get(fecha,0) + 1 #Si la fecha ya estaba +1 y si es la primera vez la guardamos con un 1

print (dicc)
