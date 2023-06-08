#Cuenta el número de veces que está una letra en un string gracias a una funcion

def cuenta (texto,letrita):
    cont = 0
    for letra in texto:
        if letra == letrita:
            cont = cont +1
    print(cont)

texto = input ('Introduzca el texto que quieras: ')
letrita = input ('Introduce la letra que quieres ver cuánto se repite: ')
cuenta(texto,letrita)