mi_tupla = ("Juan", 25, "Argentina")
nombre, edad, pais = mi_tupla
print(nombre)
print(edad)
print(pais)

print(mi_tupla)


mi_lista = tuple(["Rojo", "Verde", "Azul"])
print(mi_lista)

mi_lista[2] = "Amarillo"  # Esto dará un error porque las tuplas son inmutables
