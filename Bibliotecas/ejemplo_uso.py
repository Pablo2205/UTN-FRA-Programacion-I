"""
Ejemplo de cómo importar y usar las funciones de vectores y matrices
"""

# Importar todas las funciones
from vectores_matrices import *

# O importar funciones específicas
# from vectores_matrices import crear_vector, crear_matriz, mostrar_vector, mostrar_matriz

def main():
    print("=== EJEMPLO DE USO DE LAS FUNCIONES ===\n")
    
    # 1. Crear un vector de 10 elementos con valor inicial 0
    mi_vector = crear_vector(10, 0)
    mostrar_vector(mi_vector, "Vector de 10 ceros")
    
    # 2. Crear un vector con números del 0 al 9
    vector_numeros = crear_vector_numeros(10)
    mostrar_vector(vector_numeros, "Vector con números del 0 al 9")
    
    # 3. Crear una matriz de 4x5 con valor inicial -1
    mi_matriz = crear_matriz(4, 5, -1)
    mostrar_matriz(mi_matriz, "Matriz 4x5 con -1")
    
    # 4. Crear una matriz y cargarla con valores aleatorios
    matriz_aleatoria = crear_matriz(3, 3, 0)
    matriz_aleatoria = cargar_matriz_aleatoria(matriz_aleatoria, 1, 20)
    mostrar_matriz(matriz_aleatoria, "Matriz 3x3 aleatoria (1-20)")
    
    # 5. Buscar un valor en la matriz
    valor_buscar = 15
    posicion = buscar_valor_matriz(matriz_aleatoria, valor_buscar)
    if posicion != (-1, -1):
        print(f"Valor {valor_buscar} encontrado en posición: {posicion}")
    else:
        print(f"Valor {valor_buscar} no encontrado en la matriz")
    
    # 6. Obtener dimensiones de la matriz
    filas, columnas = obtener_dimensiones_matriz(matriz_aleatoria)
    print(f"Dimensiones de la matriz: {filas} filas x {columnas} columnas")
    
    # 7. Inicializar estructuras para gestión de estudiantes
    print("\n=== ESTRUCTURAS PARA ESTUDIANTES ===")
    estructuras = inicializar_estructuras_estudiantes(3)  # Solo 3 para el ejemplo
    
    # Mostrar las estructuras creadas
    mostrar_vector(estructuras['estados'], "Estados")
    mostrar_vector(estructuras['nombres'], "Nombres")
    mostrar_vector(estructuras['legajos'], "Legajos")
    mostrar_matriz(estructuras['notas'], "Notas")
    mostrar_vector(estructuras['promedios'], "Promedios")

if __name__ == "__main__":
    main()
