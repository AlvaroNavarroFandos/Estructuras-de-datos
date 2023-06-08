#Escribir un programa que no falle con código guardian para que no nos jodan y estemos de putu chill. Muestra la fecha de cada correo recibido
archivo = open('mbox-short.txt')

for linea in archivo:
    linea = linea.rstrip()
    palabras = linea.split()
    if len(palabras) < 1:   #METODO GUARDIAN: PROTEGE A LA LINEA MAS COMPLICADA
        continue
    if palabras[0] != 'From':   #LINEA MAS COMPLICADA
        continue
    print(palabras[2])