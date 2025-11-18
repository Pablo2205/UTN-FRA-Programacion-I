'''
Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.


'''

mi_lista = [1, -2, 3, -9, 5, 6]
def promedio_positivos(mi_lista):
    suma = 0
    cantidad_positivos = 0
    for i in range(len(mi_lista)):
        if mi_lista[i] > 0:
            suma += mi_lista[i]
            cantidad_positivos += 1
    if cantidad_positivos == 0:
        return 0
    promedio = suma / cantidad_positivos
    return promedio

print(promedio_positivos(mi_lista))
print(promedio_positivos([ -2, -3, -5]))
