'''
4. Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 

'''
def area_rectangulo(base,altura):
    area_rec = base * altura
    return area_rec
base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))

area_calculada = area_rectangulo(base, altura)

print(area_calculada)

'''
5. Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

'''
'''
def area_circulo (radio):
    pi = 3.1416
    area = pi * radio**2
    return area

radio = float(input("Ingrese el Area del Circulo: "))

area_calculada = area_circulo(radio)

print(f"El area del circulo con radio {radio} es: {area_calculada}")
'''
