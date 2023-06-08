# Programa para ver la utilidad del uso del split que divide cadenas y las pasa a listas **QUEREMOS SOLO LA DIRECCION DE EMAIL
nombre_archivo = input("Ingresa un nombre de archivo: ")
cont = 0
try:  # Con esto, si el archivo no existe salimos del programa para que no se vuelva loco
    archivo = open(nombre_archivo)
except:
    print("No se puede abrir el archivo:", nombre_archivo)
    quit()

for line in archivo:
    line = line.rstrip()  # Quitamos los espacios de la derecha en las lineas
    if not line.startswith("From "):
        continue  # Si la linea no empieza como interesa, la descartamos y empezamos bucle otra vez
    words = line.split()  # Convertimos la cadena de cada linea en una lista de palabras
    print(words[1])  # Imprimimos la palabra de la lista que nos interesa en cada linea
    cont = cont + 1

print(
    "Hay", cont, "lineas en el archivo con la palabra From al inicio"
)  # Imprimimos el numero de lineas que empiezan con From que hay
