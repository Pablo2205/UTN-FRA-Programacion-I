'''
Hacer una funcion que carge de manera secuencial 10 elementos numericos, y otra que los cargue de manera aleatoria.

'''
lista = [0] * 10

def cargar_secuencial()-> list:
    for i in range(len(lista)):
        numero = int(input(f'Ingrese el elemento {i+1}: '))
        lista[i] = numero
    return lista

def cargar_aleatorio()-> list:
    import random
    for i in range(len(lista)):
        numero = random.randint(1, 100)
        lista[i] = numero
    return lista

valores_lista_secuencial = cargar_secuencial()
print(valores_lista_secuencial)

valores_lista_aleatoria = cargar_aleatorio()
print(valores_lista_secuencial)


