#A veces es mejor saltarse las lineas que no nos interesa leer con el continue en el bucle
archivo = open('mbox-short.txt')
for linea in archivo:
    linea = linea.rstrip()
    #Ignorar las lineas que no nos interesan
    if not linea.startswith('From: '):
        continue
    #Procesar la linea que nos interesa
    print(linea)