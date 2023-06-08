#Escribir un programa que cuente las veces que se ha mandado un mail a una hora para saber cuantos se han mandado cada hora y los muestre en una lista
archivo = input('Ingresa el nombre de archivo: ')

try:
    n_archivo = open(archivo)
except:
    print('El archivo no se puede abrir: ',archivo)
    exit()

dicc = dict()
for linea in n_archivo:     #Solo este bucle porque solo nos interesan las lineas 'From' y luego en concreto solo importan la palabra[5] de cada linea
    linea = linea.rstrip()
    if not linea.startswith('From '):
        continue
    palabras = linea.split()    #Transformamos la linea en una lista
    horacompleta = palabras[5]          #Seleccionamos cúal es la palabra del mail                         
    horasep = horacompleta.split(':')   #Separamos la hora completa en dos por los :
    hora = horasep[0] 
    dicc[hora] = dicc.get(hora,0) + 1 #Si la hora ya estaba +1 y si es la primera vez la guardamos con un 1

tupla = list()                      #Creamos una lista de tuplas para almacenar todos los pares valor(numero de veces),clave(hora)
for hora,valor in dicc.items():     #Ordenada por el numero de veces que se repite la hora (en orden valor)
    tupla.append((hora,valor))  
    tupla = sorted(tupla)       #Ordenamos la lista de tuplas          
    
for hora,valor in tupla[0:]:
    print(hora,valor)           #Imprimimos la lista de tuplas ordenada con hora y numero de veces que se ha mandado el mail a esa hora