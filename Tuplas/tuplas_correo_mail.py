#Programa que leyendo de un archivo de texto, cuenta cuantos correos han llegado de cada persona
#Para esto, buscar las líneas que empiezan con 'From', después la segunda palabra de cada línea es el email, 
#Al final hay que imprimir quien tiene la mayoria de mensajes y su mail
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
    mail = palabras[1]          #Seleccionamos cúal es la palabra del mail                         
    dicc[mail] = dicc.get(mail,0) + 1 #Si el mail ya estaba +1 y si es la primera vez la guardamos con un 1

tupla = list()                      #Creamos una lista de tuplas para almacenar todos los pares valor(numero de veces),clave(mail persona)
for mail,valor in dicc.items():     #Ordenada por el numero de veces que se repite el mail (en orden valor)
    tupla.append((valor,mail))

tupla = sorted(tupla, reverse=True)     #Ordenamos la lista para que los más repetidos esten al principio

for valor,mail in tupla[:1]:            #Seleccionamos el primer par valor,clave de la lista y lo imprimimos
    print(mail,valor)
