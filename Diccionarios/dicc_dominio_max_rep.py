# Programa que leyendo de un archivo de texto, cuenta cuantos correos han llegado de cada  dominio (final del mail)
# Para esto, buscar las líneas que empiezan con 'From', después la segunda palabra de cada línea es el email, y en esa palabra lo de detras del @
# Al final hay que imprimir quien tiene la mayoria de mensajes y su dominio mail
archivo = input("Ingresa el nombre de archivo: ")

try:
    n_archivo = open(archivo)
except:
    print("El archivo no se puede abrir: ", archivo)
    exit()

dicc = dict()
for (
    linea
) in (
    n_archivo
):  # Solo este bucle porque solo nos interesan las lineas 'From' y luego en concreto solo importan la palabra[2] de cada linea
    linea = linea.rstrip()
    if not linea.startswith("From "):
        continue
    palabras = linea.split()  # Transformamos la linea en una lista
    mail = palabras[1]  # Seleccionamos cúal es la palabra del mail
    sep_mail = mail.split("@")  # Separamos el mail en dos por la @
    # for partes in sep_mail:
    dominio = sep_mail[1]
    dicc[dominio] = (
        dicc.get(dominio, 0) + 1
    )  # Si la fecha ya estaba +1 y si es la primera vez la guardamos con un 1

dominio_mas_rep = None
n_veces_rep = None
for mail, valor in dicc.items():
    if n_veces_rep is None or valor > n_veces_rep:
        dominio_mas_rep = mail
        n_veces_rep = valor

print(dicc)
print(dominio_mas_rep, n_veces_rep)
