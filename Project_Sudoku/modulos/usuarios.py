"""
================================================================================
MÓDULO: usuarios.py
DESCRIPCIÓN: Gestiona usuarios y puntajes del juego
             Guarda y carga datos desde archivo JSON
AUTOR: UTN Avellaneda - Tecnicatura en Programación
================================================================================
"""

# -------------------- IMPORTS --------------------
import json
import os
from datetime import datetime


# -------------------- CONFIGURACIÓN --------------------
RUTA_DATOS = "datos_usuarios.json"


# -------------------- FUNCIONES --------------------
def cargar_datos():
    """
    Carga los datos de usuarios desde el archivo JSON
    
    Operación:
        1. Verifica si existe el archivo
        2. Si existe, lo carga
        3. Si no existe, devuelve estructura vacía
    
    Retorna:
        dict: Diccionario con usuarios y sus puntajes
    """
    archivo_existe = os.path.exists(RUTA_DATOS)
    
    if archivo_existe == False:
        datos_vacios = {
            'usuarios': [],
            'partidas': []
        }
        return datos_vacios
    
    with open(RUTA_DATOS, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
    
    return datos


def guardar_datos(datos):
    """
    Guarda los datos de usuarios en el archivo JSON
    
    Parámetros:
        datos (dict): Diccionario con usuarios y partidas
    
    Operación:
        - Escribe los datos en formato JSON
    """
    with open(RUTA_DATOS, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def crear_usuario(nombre):
    """
    Crea un nuevo usuario en el sistema
    
    Parámetros:
        nombre (str): Nombre del usuario (nick)
    
    Operación:
        1. Carga datos existentes
        2. Verifica que el nombre no exista
        3. Agrega el nuevo usuario
        4. Guarda los datos
    
    Retorna:
        dict: {'exito': bool, 'mensaje': str}
    """
    datos = cargar_datos()
    
    # Verificar que el nombre no esté vacío
    nombre_limpio = nombre.strip()
    nombre_vacio = len(nombre_limpio) == 0
    
    if nombre_vacio:
        resultado = {
            'exito': False,
            'mensaje': 'El nombre no puede estar vacío'
        }
        return resultado
    
    # Verificar que el usuario no exista
    for usuario in datos['usuarios']:
        if usuario['nombre'].lower() == nombre_limpio.lower():
            resultado = {
                'exito': False,
                'mensaje': 'El usuario ya existe'
            }
            return resultado
    
    # Crear nuevo usuario
    usuario_nuevo = {
        'nombre': nombre_limpio,
        'fecha_creacion': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'partidas_jugadas': 0,
        'mejor_puntaje': 0
    }
    
    datos['usuarios'].append(usuario_nuevo)
    guardar_datos(datos)
    
    resultado = {
        'exito': True,
        'mensaje': 'Usuario creado exitosamente'
    }
    return resultado


def obtener_usuarios():
    """
    Obtiene la lista de todos los usuarios
    
    Retorna:
        list: Lista de nombres de usuarios
    """
    datos = cargar_datos()
    nombres = []
    
    for usuario in datos['usuarios']:
        nombre = usuario['nombre']
        nombres.append(nombre)
    
    return nombres


def usuario_existe(nombre):
    """
    Verifica si un usuario existe en el sistema
    
    Parámetros:
        nombre (str): Nombre del usuario
    
    Retorna:
        bool: True si existe, False si no
    """
    usuarios = obtener_usuarios()
    
    for usuario in usuarios:
        if usuario.lower() == nombre.lower():
            return True
    
    return False


def guardar_partida(nombre, puntaje, dificultad, tiempo_segundos):
    """
    Guarda el resultado de una partida
    
    Parámetros:
        nombre (str): Nombre del usuario
        puntaje (int): Puntaje obtenido
        dificultad (str): Nivel de dificultad
        tiempo_segundos (int): Tiempo que tardó en jugar
    
    Operación:
        1. Carga datos
        2. Agrega la partida al historial
        3. Actualiza estadísticas del usuario
        4. Guarda todo
    """
    datos = cargar_datos()
    
    # Crear registro de partida
    partida = {
        'nombre': nombre,
        'puntaje': puntaje,
        'dificultad': dificultad,
        'fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'tiempo_segundos': tiempo_segundos
    }
    
    datos['partidas'].append(partida)
    
    # Actualizar estadísticas del usuario
    for usuario in datos['usuarios']:
        if usuario['nombre'].lower() == nombre.lower():
            usuario['partidas_jugadas'] = usuario['partidas_jugadas'] + 1
            
            # Actualizar mejor puntaje
            puntaje_actual = usuario['mejor_puntaje']
            if puntaje > puntaje_actual:
                usuario['mejor_puntaje'] = puntaje
            
            break
    
    guardar_datos(datos)


def obtener_top_puntajes(cantidad=5):
    """
    Obtiene los mejores puntajes ordenados
    
    Parámetros:
        cantidad (int): Cantidad de puntajes a devolver (default: 5)
    
    Operación:
        1. Carga todas las partidas
        2. Las ordena por puntaje (mayor a menor)
        3. Devuelve las primeras 'cantidad'
    
    Retorna:
        list: Lista de diccionarios con puntajes
    """
    datos = cargar_datos()
    partidas = datos['partidas']
    
    # Ordenar por puntaje (mayor a menor)
    partidas_ordenadas = sorted(partidas, key=lambda x: x['puntaje'], reverse=True)
    
    # Tomar solo la cantidad solicitada
    top_partidas = partidas_ordenadas[:cantidad]
    
    return top_partidas


def obtener_estadisticas_usuario(nombre):
    """
    Obtiene las estadísticas de un usuario específico
    
    Parámetros:
        nombre (str): Nombre del usuario
    
    Retorna:
        dict: Estadísticas del usuario o None si no existe
    """
    datos = cargar_datos()
    
    for usuario in datos['usuarios']:
        if usuario['nombre'].lower() == nombre.lower():
            return usuario
    
    return None


def exportar_puntajes_txt(ruta="puntajes.txt"):
    """
    Exporta los puntajes a un archivo de texto
    
    Parámetros:
        ruta (str): Ruta donde guardar el archivo
    
    Operación:
        - Crea un archivo de texto formateado con los puntajes
    """
    top = obtener_top_puntajes(100)  # Todos los puntajes
    
    with open(ruta, 'w', encoding='utf-8') as archivo:
        archivo.write("=" * 70 + "\n")
        archivo.write("RANKING DE PUNTAJES - SUDOKU UTN AVELLANEDA\n")
        archivo.write("=" * 70 + "\n\n")
        
        archivo.write(f"{'POS':<5} {'NOMBRE':<20} {'PUNTAJE':<10} {'DIFICULTAD':<12} {'FECHA':<20}\n")
        archivo.write("-" * 70 + "\n")
        
        for i in range(len(top)):
            partida = top[i]
            posicion = i + 1
            nombre = partida['nombre']
            puntaje = partida['puntaje']
            dificultad = partida['dificultad'].capitalize()
            fecha = partida['fecha']
            
            linea = f"{posicion:<5} {nombre:<20} {puntaje:<10} {dificultad:<12} {fecha:<20}\n"
            archivo.write(linea)
        
        archivo.write("\n" + "=" * 70 + "\n")


def exportar_puntajes_csv(ruta="puntajes.csv"):
    """
    Exporta los puntajes a un archivo CSV
    
    Parámetros:
        ruta (str): Ruta donde guardar el archivo
    
    Operación:
        - Crea un archivo CSV con los puntajes
    """
    top = obtener_top_puntajes(100)
    
    with open(ruta, 'w', encoding='utf-8') as archivo:
        # Encabezados
        archivo.write("Posicion,Nombre,Puntaje,Dificultad,Fecha,Tiempo(seg)\n")
        
        # Datos
        for i in range(len(top)):
            partida = top[i]
            posicion = i + 1
            nombre = partida['nombre']
            puntaje = partida['puntaje']
            dificultad = partida['dificultad']
            fecha = partida['fecha']
            tiempo = partida.get('tiempo_segundos', 0)
            
            linea = f"{posicion},{nombre},{puntaje},{dificultad},{fecha},{tiempo}\n"
            archivo.write(linea)


def limpiar_datos():
    """
    Elimina todos los datos guardados (para testing)
    
    Operación:
        - Elimina el archivo de datos si existe
    """
    archivo_existe = os.path.exists(RUTA_DATOS)
    
    if archivo_existe:
        os.remove(RUTA_DATOS)