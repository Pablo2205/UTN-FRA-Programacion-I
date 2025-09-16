'''
Realizar una función recursiva que calcule la suma de los primeros números naturales:

'''

def suma_numeros(n):
    if n == 1:
        return 1
    else:
        return n + suma_numeros(n - 1)


