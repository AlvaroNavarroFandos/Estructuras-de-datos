# cuenta las veces que se repite cada palabra en un archivo de texto y las imprime las que se repiten mas de una vez
archivo = input("Ingresa el nombre de archivo: ")

try:
    n_archivo = open(archivo)
except:
    print("El archivo no se puede abrir: ", archivo)
    exit()

d = dict()
for linea in n_archivo:
    palabras = linea.split()
    for palabra in palabras:
        d[palabra] = d.get(palabra, 0) + 1  # MUY CLAVE

nmax_veces = None  # Inicializamos a None tanto la clave como el valor
pal_mas_rep = None
for (
    palabra,
    valor,
) in d.items():  # Recorremos todo el diccionario, tanto claves como valores
    if (
        nmax_veces is None or valor > nmax_veces
    ):  # La primera sentencia del if es para el primer valor del diccionario, y luego ya buscar el max
        pal_mas_rep = palabra  # Guarda la clave y el valor
        nmax_veces = valor

print(pal_mas_rep, nmax_veces)  # Imprime las dos cosas

# Si quisieramos imprimir en orden alfabético: haríamos una lista lst= list(d.palabra()) y la ordenariamos con lst.sort()
