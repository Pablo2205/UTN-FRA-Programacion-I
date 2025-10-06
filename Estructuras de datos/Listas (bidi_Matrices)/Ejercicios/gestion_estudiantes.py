'''
Programa de Gestión de Estudiantes
Autor: Pablo Coria
Descripción: Sistema para gestionar datos de estudiantes con vectores y matrices
'''

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n" + "-"*50)
    print("        SISTEMA DE GESTIÓN DE ESTUDIANTES")
    print("-"*50)
    print("1 - Generar e inicializar los vectores y la matriz")
    print("2 - Cargar los datos: nombre")
    print("3 - Cargar las notas en la matriz")
    print("4 - Calcular y poblar los promedios")
    print("5 - Buscar por promedio mayor o igual que el dato a buscar")
    print("6 - Salir")
    print("-"*50)

def inicializar_estructuras():
    """Inicializa los vectores y la matriz"""
    global estados, nombres, legajos, notas, promedios
    
    # Vectores de 100 elementos
    estados = [0] * 100  # 0 = vacío, 1 = ocupado
    nombres = [""] * 100
    legajos = [0] * 100
    
    # Matriz de 100x3 para las notas
    notas = [[0 for _ in range(3)] for _ in range(100)]
    
    # Vector de promedios
    promedios = [0.0] * 100
    
    print("✓ Estructuras inicializadas correctamente:")
    print("  - Vector estados: 100 elementos")
    print("  - Vector nombres: 100 elementos")
    print("  - Vector legajos: 100 elementos")
    print("  - Matriz notas: 100x3 elementos")
    print("  - Vector promedios: 100 elementos")

def cargar_nombres():
    """Carga los nombres de los estudiantes"""
    global estados, nombres, legajos
    
    print("\n--- CARGA DE NOMBRES ---")
    print("Ingrese los datos de los estudiantes (0 para terminar):")
    
    contador = 0
    while contador < 100:
        print(f"\nEstudiante {contador + 1}:")
        nombre = input("Nombre: ").strip()
        
        if nombre == "0":
            break
            
        if nombre == "":
            print("El nombre no puede estar vacío. Intente nuevamente.")
            continue
            
        legajo = input("Legajo: ").strip()
        
        if legajo == "0":
            break
            
        try:
            legajo_num = int(legajo)
            if legajo_num <= 0:
                print("El legajo debe ser un número positivo.")
                continue
        except ValueError:
            print("El legajo debe ser un número entero.")
            continue
        
        # Verificar si el legajo ya existe
        if legajo_num in legajos:
            print("Este legajo ya está registrado. Intente con otro.")
            continue
        
        # Guardar los datos
        estados[contador] = 1
        nombres[contador] = nombre
        legajos[contador] = legajo_num
        contador += 1
        
        print(f"✓ Estudiante {nombre} (Legajo: {legajo_num}) registrado correctamente.")
    
    print(f"\n✓ Se registraron {contador} estudiantes.")

def cargar_notas():
    """Carga las notas en la matriz"""
    global estados, nombres, legajos, notas
    
    print("\n--- CARGA DE NOTAS ---")
    
    # Mostrar estudiantes registrados
    estudiantes_registrados = []
    for i in range(100):
        if estados[i] == 1:
            estudiantes_registrados.append((i, nombres[i], legajos[i]))
    
    if not estudiantes_registrados:
        print("No hay estudiantes registrados. Use la opción 2 primero.")
        return
    
    print("Estudiantes registrados:")
    for i, (idx, nombre, legajo) in enumerate(estudiantes_registrados):
        print(f"{i+1}. {nombre} (Legajo: {legajo})")
    
    while True:
        try:
            opcion = int(input(f"\nSeleccione estudiante (1-{len(estudiantes_registrados)}) o 0 para terminar: "))
            if opcion == 0:
                break
            if opcion < 1 or opcion > len(estudiantes_registrados):
                print("Opción inválida. Intente nuevamente.")
                continue
        except ValueError:
            print("Debe ingresar un número válido.")
            continue
        
        # Obtener el índice real del estudiante
        idx_real = estudiantes_registrados[opcion-1][0]
        nombre = nombres[idx_real]
        
        print(f"\nCargando notas para: {nombre}")
        
        # Cargar las 3 notas
        for materia in range(3):
            while True:
                try:
                    nota = int(input(f"Nota {materia + 1} (0-100): "))
                    if nota < 0 or nota > 100:
                        print("La nota debe estar entre 0 y 100.")
                        continue
                    notas[idx_real][materia] = nota
                    break
                except ValueError:
                    print("Debe ingresar un número entero.")
        
        print(f"✓ Notas cargadas para {nombre}: {notas[idx_real]}")

def calcular_promedios():
    """Calcula y pobla los promedios"""
    global estados, notas, promedios
    
    print("\n--- CÁLCULO DE PROMEDIOS ---")
    
    promedios_calculados = 0
    for i in range(100):
        if estados[i] == 1:  # Si el estudiante está registrado
            suma = sum(notas[i])
            promedio = suma / 3.0
            promedios[i] = round(promedio, 2)
            promedios_calculados += 1
            print(f"{nombres[i]}: {notas[i]} → Promedio: {promedios[i]}")
    
    print(f"\n✓ Se calcularon {promedios_calculados} promedios.")

def buscar_por_promedio():
    """Busca estudiantes con promedio mayor o igual al especificado"""
    global estados, nombres, legajos, promedios
    
    print("\n--- BÚSQUEDA POR PROMEDIO ---")
    
    if not any(estados):
        print("No hay estudiantes registrados.")
        return
    
    try:
        promedio_buscar = float(input("Ingrese el promedio mínimo a buscar: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return
    
    estudiantes_encontrados = []
    for i in range(100):
        if estados[i] == 1 and promedios[i] >= promedio_buscar:
            estudiantes_encontrados.append((nombres[i], legajos[i], promedios[i], notas[i]))
    
    if not estudiantes_encontrados:
        print(f"\nNo se encontraron estudiantes con promedio >= {promedio_buscar}")
    else:
        print(f"\nEstudiantes con promedio >= {promedio_buscar}:")
        print("-" * 80)
        print(f"{'Nombre':<20} {'Legajo':<10} {'Promedio':<10} {'Notas':<20}")
        print("-" * 80)
        for nombre, legajo, promedio, notas_est in estudiantes_encontrados:
            print(f"{nombre:<20} {legajo:<10} {promedio:<10} {str(notas_est):<20}")

def main():
    """Función principal del programa"""
    global estados, nombres, legajos, notas, promedios
    
    # Inicializar variables globales
    estados = []
    nombres = []
    legajos = []
    notas = []
    promedios = []
    
    print("Bienvenido al Sistema de Gestión de Estudiantes")
    print("Curso de Ingreso - UTN FRA")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("\nSeleccione una opción: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue
        
        if opcion == 1:
            inicializar_estructuras()
        elif opcion == 2:
            if not estados:
                print("Primero debe inicializar las estructuras (opción 1).")
            else:
                cargar_nombres()
        elif opcion == 3:
            if not estados:
                print("Primero debe inicializar las estructuras (opción 1).")
            else:
                cargar_notas()
        elif opcion == 4:
            if not estados:
                print("Primero debe inicializar las estructuras (opción 1).")
            else:
                calcular_promedios()
        elif opcion == 5:
            if not estados:
                print("Primero debe inicializar las estructuras (opción 1).")
            else:
                buscar_por_promedio()
        elif opcion == 6:
            print("\n¡Gracias por usar el Sistema de Gestión de Estudiantes!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
