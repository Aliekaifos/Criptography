import numpy as np
# TAREA 10
# OBTIENE TODAS LAS RAICES PRIMITIVOS DE Z(subindice)x

#PARA Z29

#LISTA DE Z*29
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
         21,22,23,24,25,26,27,28]
modulo = 29

# CANTIDAD DE NUMEROS UNICOS QUE DEBEN HABER
cant_unicos = 28

lista3 = []
for i in lista:
    lista2 = []
    prim = i
    x = 1
    while x < modulo:
        multiplicacion = ((prim)**(x))%(modulo)
        print(prim, '**', x, '=', multiplicacion)
        x += 1
        lista2.append(multiplicacion)
    unicos = len(np.unique(lista2))
    if unicos == cant_unicos:
        lista3.append(prim)
    input('stop: ')

#LISTA DE LOS QUE SI SON PRIMITIVOS
print(lista3)