
'''
1. Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.
2. Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  Crear el array con la función del punto 1.

'''

lista =[]

def crear_array(cantidad: int) -> list:
    lista = [0] * cantidad
    return lista

def ingresar_numeros(cantidad: int) -> list:
    lista = crear_array(cantidad)
    for i in range(cantidad):
        numero = int(input(f'Ingrese el numero {i+1}: '))
        lista[i] = numero
    return lista

cantidad = int(input('Ingrese la cantidad de numeros que desea ingresar: '))
print(ingresar_numeros(cantidad))


