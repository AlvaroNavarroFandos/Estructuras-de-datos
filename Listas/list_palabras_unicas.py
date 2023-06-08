#Programa que lea el archivo romeo.txt linea a linea y en cada una busque si las palabras coinciden con las que tiene y si no añadirlas. Al final 
#sacar la lista de palabras ordenada
archivo_romeo = open('romeo.txt')

palabras_unicas = []    #Crear una lista de palabras unicas
for linea in archivo_romeo: #Ir recorriendo las lineas en el archivo
    linea.rstrip()              #Eliminar los espacios de la derecha
    palabras = linea.split()    #Convertir cada linea en una lista de palabras
    for palabra in palabras:        #Ir recorriendo las palabras de la lista
        if palabra not in palabras_unicas:  #Si la palabra no está repetida guardar en la lista de palabras unicas añadiendola
            palabras_unicas.append(palabra)

palabras_unicas.sort()      #Ordenar por orden alfabetico la lista de palabras unicas e imprimir
print(palabras_unicas)