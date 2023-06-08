#Programa que pide que se introduzca el nombre del archivo, y si es el correcto transforma el texto a mayusculas línea a línea
nombre_archivo = input('Ingresa un nombre de archivo: ')
try:
    archivo = open(nombre_archivo)
except:
    print('No se puede abrir el archivo:',nombre_archivo)
    quit()
for linea in archivo:
    linea = linea.rstrip()
    print(linea.upper())