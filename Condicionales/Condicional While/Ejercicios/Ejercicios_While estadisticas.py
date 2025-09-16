'''
1. Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.
'''
numero = 1
while numero < 11:
    print(numero)
    numero += 1

'''
2. Mostrar 10 repeticiones de números descendentes desde el 10 al 1.

'''
numero = 10
while numero > 0:
    print(numero)
    numero -= 1

'''
3. Mostrar la suma de los números desde el 1 hasta el 10.

'''
suma = 0
numero = 1
while numero <= 10:
    suma += numero
    numero += 1
print("La suma es:", suma)  

'''
4. Mostrar la suma de los números pares desde el 1 hasta el 10.
'''
suma_pares = 0
numero = 1
while numero <= 10:
    if numero % 2 == 0:
        suma_pares += numero
    numero += 1
print("La suma de los números pares es:", suma_pares)

'''
5. Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.
'''

suma = 0
contador = 0
while contador < 5:
    numero = float(input("Ingrese un número: "))
    suma += numero
    contador += 1
promedio = suma / 5
print("La suma es:", suma)
print("El promedio es:", promedio)

'''
6. Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.

'''

suma = 0
contador = 0
while True:
    numero = input("Ingrese un número (o 'salir' para terminar): ")
    if numero.lower() == 'salir':
        break
    suma += float(numero)
    contador += 1
'''
7. Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.

'''

suma_positivos = 0
producto_negativos = 1  
contador_negativos = 0
while True:
    numero = input("Ingrese un número (o 'salir' para terminar): ")
    if numero.lower() == 'salir':
        break
    numero = float(numero)
    if numero > 0:
        suma_positivos += numero
    elif numero < 0:
        producto_negativos *= numero
        contador_negativos += 1
if contador_negativos == 0:
    producto_negativos = 0
print("La suma de los números positivos es:", suma_positivos)
print("El producto de los números negativos es:", producto_negativos)

'''
8. Ingresar 10 números enteros. Determinar el máximo y el mínimo.

'''

max_num = float('-inf')
min_num = float('inf')
contador = 0
while contador < 10:
    num = int(input("Ingrese un número entero: "))
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
    contador += 1
print("El número máximo es:", max_num)
print("El número mínimo es:", min_num)


'''
9. Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.

'''

suma = 0
contador = 0
while contador < 5:
    numero = float(input("Ingrese un número: "))
    suma += numero
    contador += 1
promedio = suma / contador
print("La suma es:", suma)
print("El promedio es:", promedio)


'''
10. Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.

'''


suma = 0
contador = 0
while contador < 5:
    numero = float(input("Ingrese un número: "))
    suma += numero
    contador += 1
while contador < 10:
    opcion = input("¿Desea ingresar otro número? (s/n): ")
    if opcion.lower() == 's':
        numero = float(input("Ingrese un número: "))
        suma += numero
        contador += 1
    else:
        break

promedio = suma / contador
print("La suma es:", suma)  
print("El promedio es:", promedio)



