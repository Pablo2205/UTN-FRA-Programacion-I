# modulo_busqueda_orden.py

def buscar_por_legajo(legajo, legajos, estados):
    for i in range(len(legajos)):
        if legajos[i] == legajo and estados[i] == 1:
            return i
    return -1

def ordenar_por_promedio(matriz, nombres, generos, legajos, estados, promedios, orden):
    indices = []
    for i in range(len(estados)):
        if estados[i] == 1:
            indices = indices + [i]

    n = len(indices)
    for i in range(n - 1):
        pos = i
        for j in range(i + 1, n):
            if orden == "DESC":
                if promedios[indices[j]] > promedios[indices[pos]]:
                    pos = j
            else:
                if promedios[indices[j]] < promedios[indices[pos]]:
                    pos = j
        if pos != i:
            aux = indices[i]
            indices[i] = indices[pos]
            indices[pos] = aux

    matriz_o = []
    nombres_o = []
    generos_o = []
    legajos_o = []
    estados_o = []
    promedios_o = []

    for k in range(n):
        idx = indices[k]
        matriz_o = matriz_o + [matriz[idx]]
        nombres_o = nombres_o + [nombres[idx]]
        generos_o = generos_o + [generos[idx]]
        legajos_o = legajos_o + [legajos[idx]]
        estados_o = estados_o + [estados[idx]]
        promedios_o = promedios_o + [promedios[idx]]

    return matriz_o, nombres_o, generos_o, legajos_o, estados_o, promedios_o
