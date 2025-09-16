numero = 0
acumulador = 0
while numero < 10:
    print(numero)
    numero += 1
    print(numero)

if input ("Desea ver la suma acumulada? (s/n): ") == 's':
    acumulador += numero
    print(acumulador)


