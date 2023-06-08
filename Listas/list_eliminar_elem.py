lista = ['patatas', 'carne', 'lasaña', 'macarrones','pollo']

#Crear una funcion llamada medio que al introducir una lista, devuelva la misma lista sin el primer ni el ultimo elemento
def medio(lista):
    return lista[1:-1]


#Crear una funcion llamada recortar que al introducir una lista, elimine el primer y el ultimo elemento y regrese None
def recortar(lista):
    del lista[0]
    del lista[-1]
    print(lista)
    return None
    

lista_medio = medio(lista)
print(lista_medio)

lista_recortada = recortar(lista)
print(lista_recortada)