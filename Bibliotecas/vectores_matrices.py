"""
Biblioteca de funciones para inicializar vectores y matrices
Autor: Pablo
Fecha: 2024
"""

import random
from typing import List, Any, Union


# ==================== FUNCIONES PARA VECTORES ====================

def crear_vector(cantidad: int, valor_inicial: Any = 0) -> List[Any]:
    """
    Crea un vector (lista) con la cantidad de elementos especificada.
    
    Args:
        cantidad (int): Número de elementos del vector
        valor_inicial (Any): Valor inicial para todos los elementos (default: 0)
    
    Returns:
        List[Any]: Vector inicializado
    """
    return [valor_inicial] * cantidad


def crear_vector_numeros(cantidad: int) -> List[int]:
    """
    Crea un vector de números del 0 al cantidad-1.
    
    Args:
        cantidad (int): Número de elementos del vector
    
    Returns:
        List[int]: Vector con números del 0 al cantidad-1
    """
    return [i for i in range(cantidad)]


def cargar_vector_secuencial(cantidad: int) -> List[int]:
    """
    Carga un vector de manera secuencial pidiendo valores al usuario.
    
    Args:
        cantidad (int): Número de elementos a cargar
    
    Returns:
        List[int]: Vector con los valores ingresados
    """
    vector = crear_vector(cantidad)
    for i in range(cantidad):
        vector[i] = int(input(f'Ingrese el elemento {i+1}: '))
    return vector


def cargar_vector_aleatorio(cantidad: int, min_val: int = 1, max_val: int = 100) -> List[int]:
    """
    Carga un vector con valores aleatorios.
    
    Args:
        cantidad (int): Número de elementos del vector
        min_val (int): Valor mínimo para los números aleatorios (default: 1)
        max_val (int): Valor máximo para los números aleatorios (default: 100)
    
    Returns:
        List[int]: Vector con valores aleatorios
    """
    vector = crear_vector(cantidad)
    for i in range(cantidad):
        vector[i] = random.randint(min_val, max_val)
    return vector


def cargar_vector_paralelo(estado: List[int], datos: List[Any], valor_estado: int = 1) -> bool:
    """
    Carga datos en un vector paralelo verificando espacio disponible.
    
    Args:
        estado (List[int]): Vector de estados (0=vacío, 1=ocupado)
        datos (List[Any]): Vector de datos
        valor_estado (int): Valor que indica ocupado (default: 1)
    
    Returns:
        bool: True si se pudo cargar, False si no hay espacio
    """
    for i in range(len(estado)):
        if estado[i] == 0:  # Posición vacía
            estado[i] = valor_estado
            datos[i] = input(f"Ingrese el dato para la posición {i}: ")
            return True
    print("No hay espacio disponible")
    return False


# ==================== FUNCIONES PARA MATRICES ====================

def crear_matriz(filas: int, columnas: int, valor_inicial: Any = 0) -> List[List[Any]]:
    """
    Crea una matriz con las dimensiones especificadas.
    
    Args:
        filas (int): Número de filas
        columnas (int): Número de columnas
        valor_inicial (Any): Valor inicial para todos los elementos (default: 0)
    
    Returns:
        List[List[Any]]: Matriz inicializada
    """
    return [[valor_inicial for _ in range(columnas)] for _ in range(filas)]


def inicializar_matriz(filas: int, columnas: int, valor_inicial: Any = 0) -> List[List[Any]]:
    """
    Función alternativa para inicializar matrices (compatible con código existente).
    
    Args:
        filas (int): Número de filas
        columnas (int): Número de columnas
        valor_inicial (Any): Valor inicial para todos los elementos (default: 0)
    
    Returns:
        List[List[Any]]: Matriz inicializada
    """
    matriz = []
    for i in range(filas):
        fila = [valor_inicial] * columnas
        matriz.append(fila)
    return matriz


def cargar_matriz_secuencial(matriz: List[List[int]]) -> List[List[int]]:
    """
    Carga una matriz de manera secuencial pidiendo valores al usuario.
    
    Args:
        matriz (List[List[int]]): Matriz a cargar
    
    Returns:
        List[List[int]]: Matriz cargada
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input(f'Ingrese el elemento fila {i+1} columna {j+1}: '))
    return matriz


def cargar_matriz_aleatoria(matriz: List[List[int]], min_val: int = 1, max_val: int = 100) -> List[List[int]]:
    """
    Carga una matriz con valores aleatorios.
    
    Args:
        matriz (List[List[int]]): Matriz a cargar
        min_val (int): Valor mínimo para los números aleatorios (default: 1)
        max_val (int): Valor máximo para los números aleatorios (default: 100)
    
    Returns:
        List[List[int]]: Matriz cargada con valores aleatorios
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = random.randint(min_val, max_val)
    return matriz


def cargar_matriz_interactiva(matriz: List[List[int]]) -> List[List[int]]:
    """
    Carga una matriz de manera interactiva, permitiendo al usuario elegir posición.
    
    Args:
        matriz (List[List[int]]): Matriz a cargar
    
    Returns:
        List[List[int]]: Matriz cargada
    """
    seguir = "S"
    while seguir.upper() == "S":
        fila = int(input(f"Ingrese la fila donde quiere cargar el dato (0-{len(matriz)-1}): "))
        columna = int(input(f"Ingrese la columna donde quiere cargar el dato (0-{len(matriz[0])-1}): "))
        dato = int(input("Ingrese el dato que quiere cargar: "))
        matriz[fila][columna] = dato
        seguir = input("Desea seguir cargando datos? S/N: ")
    return matriz


# ==================== FUNCIONES DE UTILIDAD ====================

def mostrar_vector(vector: List[Any], titulo: str = "Vector") -> None:
    """
    Muestra un vector de forma legible.
    
    Args:
        vector (List[Any]): Vector a mostrar
        titulo (str): Título para el vector (default: "Vector")
    """
    print(f"\n{titulo}:")
    print("[" + ", ".join(map(str, vector)) + "]")


def mostrar_matriz(matriz: List[List[Any]], titulo: str = "Matriz") -> None:
    """
    Muestra una matriz de forma legible.
    
    Args:
        matriz (List[List[Any]]): Matriz a mostrar
        titulo (str): Título para la matriz (default: "Matriz")
    """
    print(f"\n{titulo}:")
    for fila in matriz:
        for elemento in fila:
            print(f"{elemento:4}", end=" ")
        print()


def buscar_valor_matriz(matriz: List[List[Any]], valor: Any) -> tuple:
    """
    Busca un valor en una matriz y retorna su posición.
    
    Args:
        matriz (List[List[Any]]): Matriz donde buscar
        valor (Any): Valor a buscar
    
    Returns:
        tuple: (fila, columna) si encuentra el valor, (-1, -1) si no lo encuentra
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)
    return (-1, -1)


def obtener_dimensiones_matriz(matriz: List[List[Any]]) -> tuple:
    """
    Obtiene las dimensiones de una matriz.
    
    Args:
        matriz (List[List[Any]]): Matriz a analizar
    
    Returns:
        tuple: (filas, columnas)
    """
    if not matriz:
        return (0, 0)
    return (len(matriz), len(matriz[0]))


# ==================== FUNCIONES DE INICIALIZACIÓN RÁPIDA ====================

def inicializar_estructuras_estudiantes(cantidad: int = 100) -> dict:
    """
    Inicializa las estructuras necesarias para gestión de estudiantes.
    
    Args:
        cantidad (int): Número de estudiantes (default: 100)
    
    Returns:
        dict: Diccionario con todas las estructuras inicializadas
    """
    estructuras = {
        'estados': crear_vector(cantidad, 0),  # 0 = vacío, 1 = ocupado
        'nombres': crear_vector(cantidad, ""),
        'legajos': crear_vector(cantidad, 0),
        'notas': crear_matriz(cantidad, 3, 0),  # 100x3 para las notas
        'promedios': crear_vector(cantidad, 0.0)
    }
    
    print("✓ Estructuras inicializadas correctamente:")
    print(f"  - Vector estados: {cantidad} elementos")
    print(f"  - Vector nombres: {cantidad} elementos")
    print(f"  - Vector legajos: {cantidad} elementos")
    print(f"  - Matriz notas: {cantidad}x3 elementos")
    print(f"  - Vector promedios: {cantidad} elementos")
    
    return estructuras


# ==================== EJEMPLOS DE USO ====================

if __name__ == "__main__":
    # Ejemplos de uso de las funciones
    
    print("=== EJEMPLOS DE USO ===\n")
    
    # Crear vector básico
    vector1 = crear_vector(5, 0)
    mostrar_vector(vector1, "Vector básico")
    
    # Crear vector con números
    vector2 = crear_vector_numeros(5)
    mostrar_vector(vector2, "Vector con números")
    
    # Crear matriz básica
    matriz1 = crear_matriz(3, 4, 0)
    mostrar_matriz(matriz1, "Matriz básica")
    
    # Crear matriz con valores aleatorios
    matriz2 = crear_matriz(3, 3, 0)
    matriz2 = cargar_matriz_aleatoria(matriz2, 1, 10)
    mostrar_matriz(matriz2, "Matriz aleatoria")
    
    # Buscar valor en matriz
    posicion = buscar_valor_matriz(matriz2, 5)
    if posicion != (-1, -1):
        print(f"Valor 5 encontrado en posición: {posicion}")
    else:
        print("Valor 5 no encontrado")
    
    # Inicializar estructuras de estudiantes
    print("\n=== ESTRUCTURAS DE ESTUDIANTES ===")
    estructuras = inicializar_estructuras_estudiantes(5)  # Solo 5 para el ejemplo
