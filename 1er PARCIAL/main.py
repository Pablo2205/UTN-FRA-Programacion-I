# main.py
# --------- Bibliotecas ----------
from datos import*
from calculos import*
from mostrar import*
from busqueda import*

# -------- Variables principales ----------
matriz, nombres, generos, legajos, estados = crear_datos_hardcodeados()
promedios = [0] * NUM_ESTUDIANTES
cargado = True

# --------- Menu principal ----------
while True:
    print("")
    print("------- MENU PRINCIPAL -------")
    print("1 - Cargar datos (hardcode)")
    print("2 - Mostrar todos los datos")
    print("3 - Calcular promedios de cada estudiante")
    print("4 - Ordenar y mostrar por promedio (ASC o DESC)")
    print("5 - Mostrar materia(s) con mayor promedio")
    print("6 - Buscar estudiante por legajo")
    print("7 - Contar repeticiones de notas por materia")
    print("8 - Salir")
    opcion = input("Ingrese opcion (1-8): ")

    match opcion:
        case "1":   # Cargar datos
            matriz, nombres, generos, legajos, estados = crear_datos_hardcodeados()
            promedios = [0] * NUM_ESTUDIANTES
            cargado = True
            print("Datos cargados correctamente.")

        case "2":  # Mostrar todos los datos
            if cargado == True:
                mostrar_todos(matriz, nombres, generos, legajos, estados, promedios)
            else:
                print("Debe cargar los datos primero (opcion 1).")

        case "3": # Calcular promedios
            if cargado == True:
                promedios = calcular_promedios(matriz, estados)
                print("Promedios calculados.")
            else:
                print("Debe cargar los datos primero (opcion 1).")
        #
        case "4": # Ordenar y mostrar por promedio
            if cargado == True:
                orden = input("Ingrese orden (ASC o DESC): ")
                if orden == "ASC" or orden == "DESC":
                    matriz_o, nombres_o, generos_o, legajos_o, estados_o, promedios_o = \
                        ordenar_por_promedio(matriz, nombres, generos, legajos, estados, promedios, orden)
                    mostrar_ordenados(matriz_o, nombres_o, generos_o, legajos_o, estados_o, promedios_o)
                else:
                    print("Orden inválido.")
            else:
                print("Debe cargar los datos primero (opcion 1).")

        case "5":   # Mostrar materia(s) con mayor promedio
            if cargado == True:
                indices, proms = mejores_materias(matriz, estados)
                print("Promedio general por materia:")
                for j in range(NUM_MATERIAS):
                    print("  MATERIA_" + str(j + 1) + ":", round(proms[j], 2))
                print("Mejor(es) materia(s):")
                for i in range(len(indices)):
                    print("  MATERIA_" + str(indices[i] + 1))
            else:
                print("Debe cargar los datos primero (opcion 1).")

        case "6":  # Buscar y mostrar datos por legajo
            if cargado == True:
                legajo = int(input("Ingrese legajo: "))
                pos = buscar_por_legajo(legajo, legajos, estados)
                if pos != -1:
                    mostrar_uno(pos, matriz, nombres, generos, legajos, estados, promedios)
                else:
                    print("Legajo no encontrado o registro libre.")
            else:
                print("Debe cargar los datos primero (opcion 1).")

        case "7": # Contar repeticiones de notas en una materia
            if cargado == True:
                materia = int(input("Ingrese índice de materia (0-4): "))
                if materia >= 0 and materia < NUM_MATERIAS:
                    conteo = contar_notas_por_materia(matriz, materia, estados)
                    for i in range(10):
                        print("Nota", i + 1, ":", conteo[i])
                else:
                    print("Índice fuera de rango.")
            else:
                print("Debe cargar los datos primero (opcion 1).")

        case "8": # Salir
            print("Saliendo del programa.")
            break

        case _: # Opción inválida
            print("Opcion inválida.")

def mostrar_matriz_completa(matriz_notas, lista_nombres, lista_legajos):
    print("Notas de Estudiantes (nombre y legajo incluidos):\n")
    print("Estudiante\tLegajo\t", end="")
    for m in range(NUM_MATERIAS):
        print(f"M{m+1}", end="\t")
    print()

    for idx in range(NUM_ESTUDIANTES):
        print(f"{lista_nombres[idx]}\t{lista_legajos[idx]}", end="\t")
        for nota in matriz_notas[idx]:
            print(nota, end="\t")
        print()

mostrar_matriz_completa(matriz, nombres, legajos)
