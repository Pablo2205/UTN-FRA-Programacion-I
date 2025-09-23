

estado =[0,0,1,0,0]
datos = [0,0,0,0,0]  

def carga_datos(estado: list, datos: list):
    for i in range(len(estado)):
        if estado[i] == 0:
            indice = i
            dato = int(input("ingrese un numero: "))
            datos[indice] = dato
            estado[indice] = 1
            break
    else:
        print("No hay espacio disponible")  
    
agenda = carga_datos(estado, datos)
print(agenda)



