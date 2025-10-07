# ------------------- Bibliotecas ---------------------------
from datos import*
from calculos import*
from mostrar import*
from busqueda import*

# ---------------- Variables principales -------------------
datos = crear_datos_hardcodeados()
matriz = datos[0]
nombres = datos[1]
generos = datos[2]
legajos = datos[3]
estados = [1] * NUM_ESTUDIANTES
promedios = [0] * NUM_ESTUDIANTES 
cargado = False

# ----------------- Menu principal ------------------------
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
        case "1":
            datos = crear_datos_hardcodeados()
            matriz = datos[0]
            nombres = datos[1]
            generos = datos[2]
            legajos = datos[3]

            promedios = [0] * NUM_ESTUDIANTES
            cargado = True
            print("Datos cargados correctamente.")

        case "2":
            if cargado == True:
                mostrar_todos(matriz, nombres, generos, legajos, promedios)
            else:
                print("Debe cargar los datos primero (opcion 1).")

        case "3":
            if cargado == True:
                promedios = calcular_promedios(matriz)
                print("Promedios calculados.")
            else:
                print("Debe cargar los datos primero (opcion 1).")
        
        case "4":
            if cargado == True:
                orden = input("Ingrese orden (ASC o DESC): ")
                if orden == "ASC" or orden == "DESC":
                    matriz_o, nombres_o, generos_o, legajos_o, promedios_o = \
                        ordenar_por_promedio(matriz, nombres, generos, legajos, promedios, orden)
                    mostrar_ordenados(matriz_o, nombres_o, generos_o, legajos_o, promedios_o)
                else:
                    print("Orden inválido.")
            else:
                print("Debe cargar los datos primero (opcion 1).")

        case "5":
            if cargado == True:
                indices, proms = mejores_materias(matriz)
                print("Promedio general por materia:")
                for j in range(NUM_MATERIAS):
                    print("  MATERIA_" + str(j + 1) + ":", round(proms[j], 2))
                print("Mejor(es) materia(s):")
                for i in range(len(indices)):
                    print("  MATERIA_" + str(indices[i] + 1))
            else:
                print("Debe cargar los datos primero (opcion 1).")

        case "6":
            if cargado == True:
                legajo = int(input("Ingrese legajo: "))
                pos = buscar_por_legajo(legajo, legajos)
                if pos != -1:
                    mostrar_uno(pos, matriz, nombres, generos, legajos, promedios)
                else:
                    print("Legajo no encontrado")
            else:
                print("Debe cargar los datos primero (opcion 1).")

        case "7":
            if cargado == True:
                materia = int(input("Ingrese índice de materia (0-4): "))
                if materia >= 0 and materia < NUM_MATERIAS:
                    conteo = contar_notas_por_materia(matriz, materia)
                    for i in range(10):
                        print("Nota", i + 1, ":", conteo[i])
                else:
                    print("Índice fuera de rango.")
            else:
                print("Debe cargar los datos primero (opcion 1).")

        case "8":
            print("Saliendo del programa.")
            break

        case _:
            print("Opcion inválida.")
