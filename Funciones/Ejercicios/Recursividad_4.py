'''
Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir el siguiente prototipo:

Nota general: en cada ejercicio al ingresar un número, se tendrá que utilizar la función get_int del módulo Input

'''

def fibonacci(numero: int) -> int:
    if numero <= 0:
        return 0
    elif numero == 1:
        return 1
    else:
        #f(n) = f(n-1) + f(n-2)
        return fibonacci(numero - 1) + fibonacci(numero - 2)
    
num = int(input("Ingrese un número para calcular su Fibonacci: "))
resultado = fibonacci(num)
print(f"El número de Fibonacci de {num} es: {resultado}")

