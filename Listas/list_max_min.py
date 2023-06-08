#Programa que crea una lista de números enteros hasta que se introduce 'hecho', al final devuelve el max y el min de los numeros de esa lista
numlist = list()    #Creamos una variable que tiene una lista vacia
#Bucle para ir añadiendo numeros a la lista
while True:
    inp = input('Ingresa un número: ')
    if inp == 'hecho':
        break   #Si se introduce 'fin' ya no pide mas numeros y salta a calcular
    fnum = float(inp)
    numlist.append(fnum)

nmaximo = max(numlist)
nminimo = min(numlist)
print('Máximo:',nmaximo)
print('Mínimo:',nminimo)