#Programa que solicita el nombre de archivo, lee el archivo y busca las lineas que contienen 'X-DSPAM-Confidence:', en esas líneas rescata el numero
#decimal que hay en esa línea y cuando acaba de leer el archivo imprime el promedio de todos esos valores.
nombre_archivo = input('Ingresa un nombre de archivo: ')
#Si el nombre de archivo no es valido, sale del programa
try:
    archivo = open(nombre_archivo)
except:
    print('Nombre de archivo incorrecto, no se puede abrir:',nombre_archivo)
    quit()
#Ahora creamos el bucle para calcular el promedio de todos los spam confidences.
cont = 0
total = 0
for linea in archivo:
    if not 'X-DSPAM-Confidence:' in linea:  #Descartamos las lineas que no incluyen lo que buscamos
        continue
    else:                                   #En estas lineas extraemos el numero y calculamos el promedio
        pos_dos_puntos = linea.find(':')
        num = linea[pos_dos_puntos+1:]
        fnum = float(num)
        total = total + fnum
        cont = cont + 1
print('Promedio spam confidence:',total/cont)   #Mostramos el resultado por pantalla