max_num =float('inf')
min_num =float('-inf')
cantiddad = 0
print(max_num, min_num)
condicion = True

while condicion == True:
    num = input("Ingrese un numero o 'fin' para terminar: ")
    num = float(num)
    if num == 'fin':
        condicion = False
    elif num > max_num:
        max_num = num
    elif num < min_num:
        min_num = num


print("El numero maximo es: ", max_num)
print("El numero minimo es: ", min_num)
print("La cantidad de numeros ingresados es: ", cantiddad)

'''
clave_correcta = "python123"
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    clave_ingresada = input("Ingrese la clave: ")
    if clave_ingresada == clave_correcta:
        print("Clave correcta. Acceso concedido.")
        break
    else:
        intentos += 1
        print(f"Clave incorrecta. Te quedan {max_intentos - intentos} intentos.")


'''