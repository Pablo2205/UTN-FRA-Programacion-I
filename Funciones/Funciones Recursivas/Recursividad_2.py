'''
Realizar una función recursiva que calcule la potencia de un número:


'''

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es: {resultado}")  
