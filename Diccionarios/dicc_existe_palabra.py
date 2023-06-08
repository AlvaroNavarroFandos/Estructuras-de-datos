#Abrir el archivo de texto y leer las palabras
archivo = open('words.txt')
palabras = archivo.read().split()
#Crear un diccionario con las palabras guardadas como claves
diccionario = {}
for palabra in palabras:
    diccionario[palabra] = None
#Utilizar in para buscar palabras
if 'hola' in diccionario:
    print('La palabra ''hola'' está en el diccionario')
else:
    print('La palabra ''hola'' no está en el diccionario')
print(diccionario)
