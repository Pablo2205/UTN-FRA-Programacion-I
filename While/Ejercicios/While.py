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
    cantiddad += 1     