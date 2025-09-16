'''
Hacer una funcion que reciba como parametros un vector y un dato a buscar (int), y la misma retorne el indice del elemento encontrado.
En caso de no encontrarse, retornar el valor -1
'''

def buscar_elemento(vector, dato):
    for i in range(len(vector)):
        if vector[i] == dato:
            return i
    return -1

vector = [10, 20, 30, 40, 50]
dato_a_buscar = 30
indice = buscar_elemento(vector, dato_a_buscar)
print(f'El indice del elemento {dato_a_buscar} es: {indice}')

