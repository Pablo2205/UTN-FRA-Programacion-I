'''
Crear una función que reciba como parámetro un vector de números enteros. La función debe mostrar los números negativos de forma decreciente y luego los positivos de forma creciente. 
Nota: solo se puede usar un vector, y se debe utilizar la menor cantidad de estructuras repetitivas.

ordenarlos con el método de la burbuja.


'''
def ordenar_array(arr, descendente=False):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if (descendente and arr[j] < arr[j+1]) or (not descendente and arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Ejemplo de uso:
array_asc = [64, 34, 25, 12, 22,

                11, 90, 45, 46]
array_desc = [64, 34, 25, 12, 22,
                11, 90, 45, 46]
print("Array ordenado ascendente:")
print(ordenar_array(array_asc))
print("Array ordenado descendente:")
print(ordenar_array(array_desc, True))

#Salida:
#Array ordenado ascendente:

        