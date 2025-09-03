'''
# 1. Mostrar los números ascendentes desde el 1 al 10
for numero in range (1, 11):
    print(numero)

'''

'''
# 2. Mostrar los números descendentes desde el 10 al 1

for numero in range (10, 0, -1):
    print(numero)
'''

'''
# 3. Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.

numero = int(input("Ingrese un número: "))
for i in range (0, numero + 1):
    print(i)

'''

'''
# 4. Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5

numero = int(input("Ingrese un número: "))
for i in range (0, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

'''

'''
# 5. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.
summa = 0
promedio = 0
contador = 0


for i in range (10):
    numero = int(input("Ingrese un número (0 para finalizar): "))
    if numero == 0:
        break
    summa += numero
    contador += 1

'''

'''
# 6. Imprimir los números múltiplos de 3 entre el 1 y el 10.

for numero in range (1, 11):
    if numero % 3 == 0:
        print(numero)

'''

'''
# 7. Mostrar los números pares que hay desde la unidad hasta el número 50.

for numero in range (1, 51):
    if numero % 2 == 0:
        print(numero)
'''

'''
# 8. Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:

numero = int(input("Ingrese un número: "))
for i in range (1, numero + 1):
    for j in range (1, i + 1):
        print(j, end="")
    print("")   

'''

'''
# 9. Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.

contador = 0
numero = int(input("Ingrese un número: "))

for i in range (1, numero + 1):
    if numero % i == 0:
        print(i)
        contador += 1
print(f"Cantidad de divisores encontrados: {contador}")

'''

'''
# 10. Ingresar un número. Determinar si el número es primo o no.
es_primo = True
numero = int(input("Ingrese un número: "))

for i in range (2, numero):
    if numero % i == 0:
        es_primo = False
        break
'''


# 11. Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.

contador_primos = 0
numero = int(input("Ingrese un número: "))
for i in range (2, numero + 1):
    es_primo = True
    for j in range (2, i):
        if i % j == 0:
            es_primo = False
            break
    if es_primo:
        print(i)
        contador_primos += 1
print(f"Cantidad de números primos encontrados: {contador_primos}")

