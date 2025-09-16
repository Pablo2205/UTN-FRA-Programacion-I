mi_lista1 = [1]
mi_lista2 = mi_lista1 # ambas variables apuntan a la misma dirección de memoria

mi_lista2[0] = 2
# valores de las listas
print(mi_lista1)
print(mi_lista2)

# direcciones de memoria
print(id(mi_lista1))
print(id(mi_lista2))



