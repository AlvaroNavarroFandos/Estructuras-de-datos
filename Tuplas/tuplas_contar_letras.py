import string

def contar_letras(archivo):
    # Diccionario para almacenar la frecuencia de las letras
    frecuencia = {}

    # Abrir el archivo en modo lectura
    with open(archivo, 'r') as file:
        # Leer el contenido del archivo
        contenido = file.read()

        # Convertir todas las letras a minúsculas
        contenido = contenido.lower()

        # Iterar sobre cada carácter del contenido
        for caracter in contenido:
            # Verificar si el carácter es una letra a-z
            if caracter.isalpha():
                # Verificar si la letra ya está en el diccionario
                if caracter in frecuencia:
                    # Incrementar la frecuencia de la letra
                    frecuencia[caracter] += 1
                else:
                    # Agregar la letra al diccionario con frecuencia 1
                    frecuencia[caracter] = 1

    # Ordenar el diccionario por frecuencia en orden descendente
    frecuencia_ordenada = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)

    # Imprimir las letras en orden decreciente de frecuencia
    for letra, frecuencia in frecuencia_ordenada:
        print(letra, frecuencia)

# Nombre del archivo de texto a procesar
nombre_archivo = 'clown.txt'

# Llamar a la función para contar las letras
contar_letras(nombre_archivo)

