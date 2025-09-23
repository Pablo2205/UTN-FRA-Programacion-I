def lista_cant_establecida (cant_elementos: int):
    mi_lista_numeros = [0] * cant_elementos
    for i in range(len(mi_lista_numeros)):
        mi_lista_numeros[i] = i
        #print(mi_lista_numeros[i])
    return mi_lista_numeros