#Programa que leyendo de un archivo de texto, cuenta cuantos correos han llegado de cada email
#Para esto, buscar las líneas que empiezan con 'From', después la segunda palabra de cada línea es el email, hacer un cont y print
#Al final hay que imprimir quien tiene la mayoria de mensajes y su direccion email
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
    mail = palabras[1]         #Cogemos la palabra del mail completo
    dicc[mail] = dicc.get(mail,0) + 1 #Si el mail ya estaba +1 y si es la primera vez la guardamos con un 1

mail_mas_rep = None
n_veces_rep = None
for mail,valor in dicc.items():
    if n_veces_rep is None or valor > n_veces_rep:
        mail_mas_rep = mail
        n_veces_rep = valor

print (mail_mas_rep,n_veces_rep)