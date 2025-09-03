'''

Ejemplo de paso de parámetros por referencia y por valor en Python.

- Los tipos de datos mutables (como listas y diccionarios) se pasan por referencia, 
lo que significa que si se modifica el objeto dentro de la función, 
el cambio se reflejará fuera de la función. 

- Los tipos de datos inmutables (como números, cadenas y tuplas) se pasan por valor, 
lo que significa que cualquier modificación dentro de la función no afectará al objeto original fuera de la función.

'''
def doblar(referencia, valor):
    referencia *= 2
    valor *= 2
    print ("DURANTE LA FUNCION", referencia, valor)

estructura = ["a", "b", "c"]
primitiva = "x"

print ("ANTES DE LA FUNCION", estructura, primitiva)
doblar(estructura, primitiva)
print ("DESPUES DE LA FUNCION", estructura, primitiva)

