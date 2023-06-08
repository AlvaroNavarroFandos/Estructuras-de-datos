# Programa para ver la utilidad del uso del split que divide cadenas y las pasa a listas **QUEREMOS SOLO LO QUE VA DETRAS DEL @ EN EL MAIL
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()  # Quitamos los espacios de la derecha en las lineas
    if not line.startswith("From "):
        continue  # Si la linea no empieza como interesa, la descartamos y empezamos bucle otra vez
    words = line.split()  # Convertimos la cadena de cada linea en una lista de palabras
    mail = words[1]
    pieces = mail.split("@")
    print(pieces[1])  # Imprimimos la palabra de la lista que nos interesa en cada linea
