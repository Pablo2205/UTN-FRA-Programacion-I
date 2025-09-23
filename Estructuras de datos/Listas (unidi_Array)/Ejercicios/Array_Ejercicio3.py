'''
Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números. 


'''
mi_lista = [1, 2, 3, 9, 5, 6]

def promedio_lista(mi_lista):
    suma = 0
    for i in range(len(mi_lista)):
        suma += mi_lista[i]
    promedio = suma / len(mi_lista)
    return promedio

print(promedio_lista(mi_lista))
