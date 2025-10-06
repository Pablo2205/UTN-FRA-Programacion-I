# Indexacion [0]
# Slicing [0:2] [2:] [:3] [:-1]
# Las cadenas son inmutables
# ORD: Devuelve el codigo ASCII de un caracter
# CHR: Devuelve el caracter de un codigo ASCII

def pasar_a_mayusculas(cadena: str) -> str:
    resultado = ""
    for i in cadena:
        codigo_ascii = ord(i)
        if codigo_ascii >= 97 and codigo_ascii <= 122:
            codigo_ascii -= 32
            resultado += chr(codigo_ascii)
        else:
            resultado += i
    return resultado

cadena = input("Ingrese una cadena de caracteres: ")
resultado_may = pasar_a_mayusculas(cadena)
print(resultado_may)


#----------------
'''
def pasar_a_minusculas(cadena: str) -> str:
    resultado = ""
    for i in cadena:
        codigo_ascii = ord(i)
        if codigo_ascii >= 65 and codigo_ascii <= 90:
            codigo_ascii += 32
        resultado += chr(codigo_ascii)
        
    else:
        resultado += i
    return resultado

resultado_min = pasar_a_minusculas(cadena)
print(resultado_min)




'''










