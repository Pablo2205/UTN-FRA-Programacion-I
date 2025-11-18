'''
Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.

'''
mi_lista = [1, 2, 3]

def producto_lista(mi_lista):
    producto = 1
    for i in range(len(mi_lista)):
        producto *= mi_lista[i]
    return producto

print(producto_lista(mi_lista))
