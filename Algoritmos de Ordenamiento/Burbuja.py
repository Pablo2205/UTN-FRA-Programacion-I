'''
Crear una función llamada ordenar_array que reciba como parámetro un array de números enteros y lo ordene de forma ascendente. La función debe implementar como algoritmo de ordenamiento el método de la burbuja. Además, como parámetro opcional debe recibir un booleano (que por default está en False), que en caso de ser True ordena el vector en forma descendente.



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
