"""
Módulo de funciones para gestión de estudiantes
Autor: Pablo
Fecha: 2024
Descripción: Funciones modulares para cargar nombres, notas, calcular promedios y buscar por promedio
"""

from typing import List, Tuple, Dict, Any
from vectores_matrices import crear_vector, crear_matriz, mostrar_vector, mostrar_matriz


# ==================== FUNCIONES DE CARGA DE NOMBRES ====================

def cargar_nombres(estados: List[int], nombres: List[str], legajos: List[int], 
                  cantidad_maxima: int = 100) -> int:
    """
    Carga los nombres y legajos de los estudiantes.
    
    Args:
        estados (List[int]): Vector de estados (0=vacío, 1=ocupado)
        nombres (List[str]): Vector de nombres
        legajos (List[int]): Vector de legajos
        cantidad_maxima (int): Cantidad máxima de estudiantes (default: 100)
    
    Returns:
        int: Número de estudiantes registrados
    """
    print("\n--- CARGA DE NOMBRES ---")
    print("Ingrese los datos de los estudiantes (0 para terminar):")
    
    contador = 0
    while contador < cantidad_maxima:
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
    return contador


def cargar_nombres_automatico(estados: List[int], nombres: List[str], legajos: List[int],
                             datos_estudiantes: List[Tuple[str, int]]) -> int:
    """
    Carga nombres y legajos de forma automática desde una lista de datos.
    
    Args:
        estados (List[int]): Vector de estados
        nombres (List[str]): Vector de nombres
        legajos (List[int]): Vector de legajos
        datos_estudiantes (List[Tuple[str, int]]): Lista de tuplas (nombre, legajo)
    
    Returns:
        int: Número de estudiantes registrados
    """
    contador = 0
    for nombre, legajo in datos_estudiantes:
        if contador >= len(estados):
            break
            
        if legajo in legajos:
            print(f"Legajo {legajo} ya existe, saltando...")
            continue
            
        estados[contador] = 1
        nombres[contador] = nombre
        legajos[contador] = legajo
        contador += 1
        print(f"✓ {nombre} (Legajo: {legajo}) registrado automáticamente.")
    
    return contador


# ==================== FUNCIONES DE CARGA DE NOTAS ====================

def cargar_notas(estados: List[int], nombres: List[str], legajos: List[int], 
                notas: List[List[int]], materias: int = 3) -> int:
    """
    Carga las notas de los estudiantes en la matriz.
    
    Args:
        estados (List[int]): Vector de estados
        nombres (List[str]): Vector de nombres
        legajos (List[int]): Vector de legajos
        notas (List[List[int]]): Matriz de notas
        materias (int): Número de materias (default: 3)
    
    Returns:
        int: Número de estudiantes con notas cargadas
    """
    print("\n--- CARGA DE NOTAS ---")
    
    # Mostrar estudiantes registrados
    estudiantes_registrados = []
    for i in range(len(estados)):
        if estados[i] == 1:
            estudiantes_registrados.append((i, nombres[i], legajos[i]))
    
    if not estudiantes_registrados:
        print("No hay estudiantes registrados. Use cargar_nombres() primero.")
        return 0
    
    print("Estudiantes registrados:")
    for i, (idx, nombre, legajo) in enumerate(estudiantes_registrados):
        print(f"{i+1}. {nombre} (Legajo: {legajo})")
    
    estudiantes_con_notas = 0
    
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
        
        # Cargar las notas
        for materia in range(materias):
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
        estudiantes_con_notas += 1
    
    return estudiantes_con_notas


def cargar_notas_automatico(estados: List[int], nombres: List[str], legajos: List[int],
                           notas: List[List[int]], datos_notas: Dict[int, List[int]]) -> int:
    """
    Carga notas de forma automática desde un diccionario.
    
    Args:
        estados (List[int]): Vector de estados
        nombres (List[str]): Vector de nombres
        legajos (List[int]): Vector de legajos
        notas (List[List[int]]): Matriz de notas
        datos_notas (Dict[int, List[int]]): Diccionario {legajo: [nota1, nota2, nota3]}
    
    Returns:
        int: Número de estudiantes con notas cargadas
    """
    estudiantes_con_notas = 0
    
    for i in range(len(estados)):
        if estados[i] == 1 and legajos[i] in datos_notas:
            notas_estudiante = datos_notas[legajos[i]]
            if len(notas_estudiante) == len(notas[i]):
                notas[i] = notas_estudiante.copy()
                print(f"✓ Notas cargadas para {nombres[i]}: {notas[i]}")
                estudiantes_con_notas += 1
    
    return estudiantes_con_notas


# ==================== FUNCIONES DE CÁLCULO DE PROMEDIOS ====================

def calcular_promedios(estados: List[int], nombres: List[str], notas: List[List[int]], 
                      promedios: List[float], materias: int = 3) -> int:
    """
    Calcula y pobla los promedios de los estudiantes.
    
    Args:
        estados (List[int]): Vector de estados
        nombres (List[str]): Vector de nombres
        notas (List[List[int]]): Matriz de notas
        promedios (List[float]): Vector de promedios
        materias (int): Número de materias (default: 3)
    
    Returns:
        int: Número de promedios calculados
    """
    print("\n--- CÁLCULO DE PROMEDIOS ---")
    
    promedios_calculados = 0
    for i in range(len(estados)):
        if estados[i] == 1:  # Si el estudiante está registrado
            suma = sum(notas[i])
            promedio = suma / materias
            promedios[i] = round(promedio, 2)
            promedios_calculados += 1
            print(f"{nombres[i]}: {notas[i]} → Promedio: {promedios[i]}")
    
    print(f"\n✓ Se calcularon {promedios_calculados} promedios.")
    return promedios_calculados


def calcular_promedio_individual(notas: List[int]) -> float:
    """
    Calcula el promedio de un estudiante individual.
    
    Args:
        notas (List[int]): Lista de notas del estudiante
    
    Returns:
        float: Promedio calculado
    """
    if not notas:
        return 0.0
    return round(sum(notas) / len(notas), 2)


def calcular_promedios_silencioso(estados: List[int], notas: List[List[int]], 
                                 promedios: List[float], materias: int = 3) -> int:
    """
    Calcula promedios sin mostrar mensajes (versión silenciosa).
    
    Args:
        estados (List[int]): Vector de estados
        notas (List[List[int]]): Matriz de notas
        promedios (List[float]): Vector de promedios
        materias (int): Número de materias (default: 3)
    
    Returns:
        int: Número de promedios calculados
    """
    promedios_calculados = 0
    for i in range(len(estados)):
        if estados[i] == 1:
            suma = sum(notas[i])
            promedio = suma / materias
            promedios[i] = round(promedio, 2)
            promedios_calculados += 1
    
    return promedios_calculados


# ==================== FUNCIONES DE BÚSQUEDA ====================

def buscar_por_promedio(estados: List[int], nombres: List[str], legajos: List[int], 
                       promedios: List[float], notas: List[List[int]], 
                       promedio_minimo: float) -> List[Tuple[str, int, float, List[int]]]:
    """
    Busca estudiantes con promedio mayor o igual al especificado.
    
    Args:
        estados (List[int]): Vector de estados
        nombres (List[str]): Vector de nombres
        legajos (List[int]): Vector de legajos
        promedios (List[float]): Vector de promedios
        notas (List[List[int]]): Matriz de notas
        promedio_minimo (float): Promedio mínimo a buscar
    
    Returns:
        List[Tuple[str, int, float, List[int]]]: Lista de estudiantes encontrados
    """
    estudiantes_encontrados = []
    
    for i in range(len(estados)):
        if estados[i] == 1 and promedios[i] >= promedio_minimo:
            estudiantes_encontrados.append((nombres[i], legajos[i], promedios[i], notas[i]))
    
    return estudiantes_encontrados


def buscar_por_promedio_interactivo(estados: List[int], nombres: List[str], legajos: List[int], 
                                   promedios: List[float], notas: List[List[int]]) -> None:
    """
    Busca estudiantes por promedio de forma interactiva.
    
    Args:
        estados (List[int]): Vector de estados
        nombres (List[str]): Vector de nombres
        legajos (List[int]): Vector de legajos
        promedios (List[float]): Vector de promedios
        notas (List[List[int]]): Matriz de notas
    """
    print("\n--- BÚSQUEDA POR PROMEDIO ---")
    
    if not any(estados):
        print("No hay estudiantes registrados.")
        return
    
    try:
        promedio_buscar = float(input("Ingrese el promedio mínimo a buscar: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return
    
    estudiantes_encontrados = buscar_por_promedio(estados, nombres, legajos, promedios, notas, promedio_buscar)
    
    if not estudiantes_encontrados:
        print(f"\nNo se encontraron estudiantes con promedio >= {promedio_buscar}")
    else:
        print(f"\nEstudiantes con promedio >= {promedio_buscar}:")
        print("-" * 80)
        print(f"{'Nombre':<20} {'Legajo':<10} {'Promedio':<10} {'Notas':<20}")
        print("-" * 80)
        for nombre, legajo, promedio, notas_est in estudiantes_encontrados:
            print(f"{nombre:<20} {legajo:<10} {promedio:<10} {str(notas_est):<20}")


def buscar_por_nombre(estados: List[int], nombres: List[str], legajos: List[int], 
                     promedios: List[float], notas: List[List[int]], 
                     nombre_buscar: str) -> List[Tuple[str, int, float, List[int]]]:
    """
    Busca estudiantes por nombre (búsqueda parcial).
    
    Args:
        estados (List[int]): Vector de estados
        nombres (List[str]): Vector de nombres
        legajos (List[int]): Vector de legajos
        promedios (List[float]): Vector de promedios
        notas (List[List[int]]): Matriz de notas
        nombre_buscar (str): Nombre o parte del nombre a buscar
    
    Returns:
        List[Tuple[str, int, float, List[int]]]: Lista de estudiantes encontrados
    """
    estudiantes_encontrados = []
    nombre_buscar_lower = nombre_buscar.lower()
    
    for i in range(len(estados)):
        if estados[i] == 1 and nombre_buscar_lower in nombres[i].lower():
            estudiantes_encontrados.append((nombres[i], legajos[i], promedios[i], notas[i]))
    
    return estudiantes_encontrados


def buscar_por_legajo(estados: List[int], nombres: List[str], legajos: List[int], 
                     promedios: List[float], notas: List[List[int]], 
                     legajo_buscar: int) -> Tuple[str, int, float, List[int]]:
    """
    Busca un estudiante por legajo.
    
    Args:
        estados (List[int]): Vector de estados
        nombres (List[str]): Vector de nombres
        legajos (List[int]): Vector de legajos
        promedios (List[float]): Vector de promedios
        notas (List[List[int]]): Matriz de notas
        legajo_buscar (int): Legajo a buscar
    
    Returns:
        Tuple[str, int, float, List[int]]: Datos del estudiante encontrado o None
    """
    for i in range(len(estados)):
        if estados[i] == 1 and legajos[i] == legajo_buscar:
            return (nombres[i], legajos[i], promedios[i], notas[i])
    
    return None


# ==================== FUNCIONES DE UTILIDAD ====================

def mostrar_estudiantes(estados: List[int], nombres: List[str], legajos: List[int], 
                       promedios: List[float] = None, notas: List[List[int]] = None) -> None:
    """
    Muestra todos los estudiantes registrados.
    
    Args:
        estados (List[int]): Vector de estados
        nombres (List[str]): Vector de nombres
        legajos (List[int]): Vector de legajos
        promedios (List[float], optional): Vector de promedios
        notas (List[List[int]], optional): Matriz de notas
    """
    print("\n--- LISTADO DE ESTUDIANTES ---")
    
    estudiantes_registrados = []
    for i in range(len(estados)):
        if estados[i] == 1:
            estudiantes_registrados.append((i, nombres[i], legajos[i]))
    
    if not estudiantes_registrados:
        print("No hay estudiantes registrados.")
        return
    
    print(f"{'#':<3} {'Nombre':<20} {'Legajo':<10}", end="")
    if promedios:
        print(f" {'Promedio':<10}", end="")
    if notas:
        print(f" {'Notas':<20}")
    else:
        print()
    
    print("-" * 80)
    
    for i, (idx, nombre, legajo) in enumerate(estudiantes_registrados):
        print(f"{i+1:<3} {nombre:<20} {legajo:<10}", end="")
        if promedios:
            print(f" {promedios[idx]:<10}", end="")
        if notas:
            print(f" {str(notas[idx]):<20}")
        else:
            print()


def obtener_estadisticas(estados: List[int], promedios: List[float]) -> Dict[str, Any]:
    """
    Obtiene estadísticas de los estudiantes.
    
    Args:
        estados (List[int]): Vector de estados
        promedios (List[float]): Vector de promedios
    
    Returns:
        Dict[str, Any]: Diccionario con estadísticas
    """
    estudiantes_activos = [promedios[i] for i in range(len(estados)) if estados[i] == 1]
    
    if not estudiantes_activos:
        return {
            'total_estudiantes': 0,
            'promedio_general': 0,
            'promedio_maximo': 0,
            'promedio_minimo': 0,
            'estudiantes_aprobados': 0,
            'estudiantes_desaprobados': 0
        }
    
    promedio_general = sum(estudiantes_activos) / len(estudiantes_activos)
    estudiantes_aprobados = sum(1 for p in estudiantes_activos if p >= 60)
    
    return {
        'total_estudiantes': len(estudiantes_activos),
        'promedio_general': round(promedio_general, 2),
        'promedio_maximo': max(estudiantes_activos),
        'promedio_minimo': min(estudiantes_activos),
        'estudiantes_aprobados': estudiantes_aprobados,
        'estudiantes_desaprobados': len(estudiantes_activos) - estudiantes_aprobados
    }


# ==================== FUNCIÓN DE INICIALIZACIÓN COMPLETA ====================

def inicializar_sistema_estudiantes(cantidad: int = 100, materias: int = 3) -> Dict[str, List]:
    """
    Inicializa todo el sistema de gestión de estudiantes.
    
    Args:
        cantidad (int): Cantidad máxima de estudiantes (default: 100)
        materias (int): Número de materias (default: 3)
    
    Returns:
        Dict[str, List]: Diccionario con todas las estructuras inicializadas
    """
    sistema = {
        'estados': crear_vector(cantidad, 0),
        'nombres': crear_vector(cantidad, ""),
        'legajos': crear_vector(cantidad, 0),
        'notas': crear_matriz(cantidad, materias, 0),
        'promedios': crear_vector(cantidad, 0.0),
        'cantidad_maxima': cantidad,
        'materias': materias
    }
    
    print("✓ Sistema de gestión de estudiantes inicializado:")
    print(f"  - Capacidad: {cantidad} estudiantes")
    print(f"  - Materias: {materias}")
    print(f"  - Estructuras: estados, nombres, legajos, notas, promedios")
    
    return sistema


# ==================== EJEMPLO DE USO ====================

if __name__ == "__main__":
    # Ejemplo de uso de las funciones modulares
    
    print("=== EJEMPLO DE USO DE FUNCIONES MODULARES ===\n")
    
    # Inicializar el sistema
    sistema = inicializar_sistema_estudiantes(5, 3)  # Solo 5 estudiantes para el ejemplo
    
    # Cargar algunos estudiantes de forma automática
    datos_estudiantes = [
        ("Juan Pérez", 1001),
        ("María García", 1002),
        ("Carlos López", 1003)
    ]
    
    cargados = cargar_nombres_automatico(
        sistema['estados'], 
        sistema['nombres'], 
        sistema['legajos'], 
        datos_estudiantes
    )
    
    # Cargar notas automáticamente
    datos_notas = {
        1001: [85, 90, 78],
        1002: [92, 88, 95],
        1003: [76, 82, 80]
    }
    
    cargar_notas_automatico(
        sistema['estados'],
        sistema['nombres'],
        sistema['legajos'],
        sistema['notas'],
        datos_notas
    )
    
    # Calcular promedios
    calcular_promedios(
        sistema['estados'],
        sistema['nombres'],
        sistema['notas'],
        sistema['promedios']
    )
    
    # Mostrar estudiantes
    mostrar_estudiantes(
        sistema['estados'],
        sistema['nombres'],
        sistema['legajos'],
        sistema['promedios'],
        sistema['notas']
    )
    
    # Buscar por promedio
    estudiantes_encontrados = buscar_por_promedio(
        sistema['estados'],
        sistema['nombres'],
        sistema['legajos'],
        sistema['promedios'],
        sistema['notas'],
        80.0
    )
    
    print(f"\nEstudiantes con promedio >= 80: {len(estudiantes_encontrados)}")
    
    # Mostrar estadísticas
    stats = obtener_estadisticas(sistema['estados'], sistema['promedios'])
    print(f"\nEstadísticas: {stats}")
