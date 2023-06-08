#Programa que imprima las 10 palabras más comunes de un texto
import string
n_archivo = open('romeo-full.txt')  #Abrimos el archivo
cuenta = dict()                     #Creamos un diccionario para escribir

for linea in n_archivo:             #Recorre todo el archivo y va escribiendo todas las palabras nuevas y contando las veces que se repite cada una
    linea= linea.translate(str.maketrans('', '', string.punctuation))   #TRUCO PARA ELIMINAR TODOS LOS SIGNOS DE PUNTUACION DE UN TEXTO
    linea = linea.lower()           #Transformamos todas las palabras en minúsculas para que Romeo la cuente igual que romeo por ejemplo
    palabras = linea.split()           #Crea una lista de palabras en cada linea
    for palabra in palabras:            #Recorre palabra a palabra 
        cuenta[palabra] = cuenta.get(palabra, 0) + 1    #Realiza un historiograma para tener todas las palabras contabilizadas determinadas veces

lst = list()                    #Creamos una lista para poner todas las tuplas en orden valor,clave
for k,v in list(cuenta.items()):
    lst.append((v,k))

lst.sort(reverse = True)   #Ordenamos la lista de tuplas en orden decreciente para que al principio estén las palabras más repetidas

for v,k in lst[:10]:                #De la lista de tuplas con las palabras más repetidas, que coja las 10 más repetidas y las imprima en orden k,v
    print(k,v)



