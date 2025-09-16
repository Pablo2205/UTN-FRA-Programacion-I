'''
Realizar una función recursiva que permita realizar la suma de los dígitos de un número:

'''

def suma_digitos(numero):
    if numero < 10:
        return numero
    else:
        return numero % 10 + suma_digitos(numero // 10)
    
num = int(input("Ingrese un número para sumar sus dígitos: "))
resultado = suma_digitos(num)
print(f"La suma de los dígitos de {num} es: {resultado}")
