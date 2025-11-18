# Sudoku - UTN Avellaneda

## Descripción

Juego de Sudoku desarrollado en Python con interfaz gráfica usando Pygame. Incluye sistema de usuarios, múltiples niveles de dificultad, sistema de puntuación y ranking de mejores puntajes.

**Institución:** UTN Avellaneda - Tecnicatura Universitaria en Programación  
**Año:** 2025
**Materia:** Programacion I
**Alumno:** Pablo Cria

---
## Características principales

- Tres niveles de dificultad (Fácil, Medio y Difícil)
- Sistema de usuarios con persistencia de datos
- Ranking de mejores puntajes
- Interfaz gráfica intuitiva
- Efectos de sonido y música de fondo
- Sistema de validación con retroalimentación visual
- Exportación de puntajes en formato TXT y CSV
- Generación aleatoria de tableros

---
### Estructura de carpetas

```
sudoku-utn/
│
├── main.py
├── modulos/
│   ├── configuracion.py
│   ├── datos.py
│   ├── interfaz.py
│   ├── logica.py
│   ├── sonidos.py
│   ├── usuarios.py
│   └── validacion.py
│
├── assets/
│   ├── imagenes/
│   │   └── logo_utn.png
│   └── sonidos/
│       ├── musica_fondo.mp3
│       ├── inicio.wav
│       ├── reiniciar.wav
│       ├── validar.wav
│       ├── correcto.wav
│       ├── error.wav
│       ├── victoria.wav
│       └── click.wav
│
└── README.md
```

**Nota:** Los archivos de sonido e imágenes son opcionales. El juego funcionará sin ellos pero sin audio ni logo.

---

### Controles

- **Seleccionar celda:** Click izquierdo
- **Colocar número:** Teclas 1-9
- **Borrar número:** Backspace o Delete
- **Nuevo tablero:** Tecla R
- **Validar solución:** Botón "Validar"
- **Volver al menú:** ESC

### Flujo del juego

1. Seleccionar dificultad en el menú principal
2. Crear usuario o seleccionar uno existente
3. Completar el Sudoku colocando números del 1 al 9
4. Presionar "Validar" para verificar la solución y obtener puntaje
5. Consultar el ranking de mejores puntajes

---

## Sistema de puntuación

### Cálculo de puntos

- **Zona completa** (fila, columna o región 3x3): +9 puntos
- **Tablero completo:** +81 puntos bonus
- **Error:** -1 punto por cada número incorrecto

### Niveles de dificultad

| Nivel | Números iniciales por región 3x3 |
|-----------|-------------|
| Fácil     |   5 números |
| Medio     |   4 números |
| Difícil   |   3 números |

---

## Estructura del proyecto y documentación

### main.py

**Responsabilidad:** Programa principal que ejecuta el bucle del juego y maneja todos los eventos del usuario.

**Función principal:**
- `main()`: Bucle principal que controla estados del juego, procesa eventos (clicks, teclas) y actualiza la pantalla.

**Estados del juego:**
- `ESTADO_MENU`: Menú principal
- `ESTADO_DIFICULTAD`: Selector de nivel
- `ESTADO_USUARIOS`: Pantalla de selección de usuario
- `ESTADO_CREAR_USUARIO`: Input para crear nuevo usuario
- `ESTADO_JUGANDO`: Partida en curso
- `ESTADO_PUNTAJES`: Visualización de ranking

**Relación:** Importa y coordina todos los demás módulos. Es el punto de entrada del programa.

---

### modulos/configuracion.py

**Responsabilidad:** Contiene todas las constantes y configuraciones del juego.

**Configuraciones incluidas:**
- Dimensiones de ventana y tablero
- Colores RGB para todos los elementos visuales
- Rutas de archivos (imágenes, sonidos)
- Configuración de dificultad
- Sistema de puntuación
- Configuración de audio

**Constantes principales:**
```python
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
TAMANO_TABLERO = 9
TAMANO_CELDA = 50
FPS = 30
```

**Relación:** Importado por todos los módulos para acceder a constantes globales.

---

### modulos/datos.py

**Responsabilidad:** Gestiona la generación y manipulación de datos del Sudoku. Genera matrices, valida números y resuelve el Sudoku mediante backtracking.

**Funciones principales:**
- `generar_matriz_vacia()`: Crea matriz 9x9 inicializada en ceros
- `es_valido(matriz, fila, col, num)`: Verifica si un número puede colocarse en una posición
- `resolver_sudoku(matriz)`: Resuelve Sudoku usando algoritmo de backtracking
- `generar_sudoku_completo()`: Genera un Sudoku completamente resuelto y válido
- `generar_sudoku_jugable(dificultad)`: Genera Sudoku con números iniciales según dificultad
- `obtener_region(fila, col)`: Calcula el número de región (0-8) para una celda

**Retorno de generar_sudoku_jugable:**
```python
(matriz_juego, matriz_solucion, matriz_fijos)
```

**Relación:** Usado por `logica.py` para inicializar nuevos juegos.

---

### modulos/interfaz.py

**Responsabilidad:** Maneja toda la interfaz gráfica del juego con Pygame. Dibuja el tablero, botones, menús y mensajes.

**Funciones principales:**
- `inicializar_pygame()`: Inicializa Pygame y crea la ventana del juego
- `cargar_imagen_fondo()`: Carga logo UTN con opacidad configurada
- `dibujar_tablero(pantalla, estado, imagen_fondo)`: Dibuja tablero completo con números y colores
- `dibujar_interfaz(pantalla, estado, botones, imagen_fondo)`: Dibuja interfaz completa durante el juego
- `dibujar_boton(pantalla, boton)`: Dibuja un botón con hover effect
- `dibujar_menu_principal(pantalla, imagen_fondo)`: Dibuja menú principal con opciones
- `dibujar_menu_dificultad(pantalla, imagen_fondo)`: Dibuja selector de dificultad
- `dibujar_pantalla_usuarios(pantalla, usuarios, imagen_fondo)`: Dibuja pantalla de gestión de usuarios
- `dibujar_input_nombre(pantalla, texto_actual, activo, imagen_fondo)`: Dibuja campo de texto para crear usuario
- `dibujar_pantalla_puntajes(pantalla, puntajes, imagen_fondo)`: Dibuja tabla de mejores puntajes
- `obtener_celda_click(pos)`: Convierte coordenadas de mouse en posición de celda
- `actualizar_hover_botones(botones, pos_mouse)`: Actualiza estado hover de botones
- `obtener_boton_clickeado(botones, pos)`: Determina qué botón fue clickeado
- `crear_botones()`: Crea botones de la interfaz del juego
- `dibujar_mensaje_victoria(pantalla, estado)`: Dibuja mensaje cuando se completa el Sudoku

**Relación:** Usado por `main.py` para renderizar todas las pantallas del juego.

---

### modulos/logica.py

**Responsabilidad:** Maneja toda la lógica del juego (estado, acciones, puntuación). Controla las acciones del jugador y actualiza el estado.

**Funciones principales:**
- `inicializar_juego(dificultad, nombre_jugador)`: Inicializa nuevo juego con dificultad elegida
- `seleccionar_celda(estado, fila, col)`: Selecciona una celda del tablero para editar
- `colocar_numero(estado, numero)`: Coloca número en celda seleccionada (valida duplicados)
- `borrar_numero(estado)`: Borra el número de la celda seleccionada
- `reiniciar_juego(estado)`: Reinicia el juego manteniendo la misma dificultad
- `validar_y_calcular_puntaje(estado)`: Valida matriz completa, aplica colores y calcula puntaje

**Estructura del estado del juego:**
```python
estado = {
    'matriz_juego': [...],
    'matriz_solucion': [...],
    'matriz_fijos': [...],
    'celda_seleccionada': (fila, col) o None,
    'puntaje': int,
    'errores': int,
    'juego_terminado': bool,
    'dificultad': str,
    'zonas_completadas': set(),
    'estados_celdas': {},
    'nombre_jugador': str
}
```

**Relación:** Usado por `main.py` para gestionar todas las acciones del jugador.

---

### modulos/validacion.py

**Responsabilidad:** Valida números, verifica zonas completas y calcula puntuación. Comprueba si el jugador está colocando números correctamente.

**Funciones principales:**
- `validar_numero(matriz, fila, col, num)`: Verifica si un número cumple las reglas del Sudoku
- `verificar_zona_completa(matriz, fila, col)`: Verifica si fila/columna/región está completa y correcta
- `verificar_matriz_completa(matriz)`: Verifica si todo el Sudoku está completo y correcto
- `validar_solucion(estado)`: Valida solución comparándola con la solución correcta
- `calcular_puntos_zona(zonas_completas)`: Calcula puntos obtenidos por completar zonas

**Retorno de validar_solucion:**
```python
{
    'correcta': bool,
    'celdas_incorrectas': [(fila, col), ...],
    'celdas_correctas': [(fila, col), ...],
    'total_incorrectas': int,
    'total_correctas': int,
    'total_vacias': int
}
```

**Relación:** Usado por `logica.py` para validar números y calcular puntuaciones.

---

### modulos/sonidos.py

**Responsabilidad:** Gestiona la música de fondo y los efectos de sonido del juego. Carga, reproduce y controla todos los sonidos.

**Funciones principales:**
- `inicializar_sonidos()`: Inicializa el sistema de sonido de Pygame
- `cargar_musica_fondo()`: Carga y reproduce música en loop infinito
- `detener_musica()`: Detiene la música de fondo completamente
- `pausar_musica()`: Pausa la música de fondo
- `reanudar_musica()`: Reanuda la música pausada
- `cargar_efectos_sonido()`: Carga todos los efectos de sonido del juego
- `reproducir_sonido(efectos, nombre)`: Reproduce un efecto de sonido específico
- `ajustar_volumen_musica(volumen)`: Ajusta volumen de la música (0.0 a 1.0)
- `ajustar_volumen_efectos(efectos, volumen)`: Ajusta volumen de efectos (0.0 a 1.0)

**Efectos disponibles:**
- `inicio`: Al comenzar nueva partida
- `reiniciar`: Al generar nuevo tablero
- `validar`: Al presionar validar
- `correcto`: Número correcto
- `error`: Número incorrecto
- `victoria`: Al completar el Sudoku
- `click`: Clicks en botones

**Relación:** Usado por `main.py` para reproducir sonidos en eventos específicos.

---

### modulos/usuarios.py

**Responsabilidad:** Gestiona usuarios y puntajes (persistencia en JSON).

**Funciones principales:**
- `cargar_datos()`: Carga datos de usuarios desde archivo JSON
- `guardar_datos(datos)`: Guarda datos en archivo JSON
- `crear_usuario(nombre)`: Registra nuevo jugador en el sistema
- `obtener_usuarios()`: Devuelve lista de nombres de usuarios registrados
- `usuario_existe(nombre)`: Verifica si un usuario ya existe
- `guardar_partida(nombre, puntaje, dificultad, tiempo_segundos)`: Guarda resultado de partida
- `obtener_top_puntajes(cantidad)`: Devuelve Top N puntajes ordenados
- `obtener_estadisticas_usuario(nombre)`: Obtiene estadísticas de un usuario específico
- `exportar_puntajes_txt(ruta)`: Exporta ranking a archivo de texto
- `exportar_puntajes_csv(ruta)`: Exporta ranking a CSV (Excel)
- `limpiar_datos()`: Elimina todos los datos guardados (para testing)

**Archivo generado:** `datos_usuarios.json` (se crea automáticamente)

**Estructura del JSON:**
```json
{
    "usuarios": [
        {
            "nombre": "Juan",
            "fecha_creacion": "2024-11-18 10:30:00",
            "partidas_jugadas": 5,
            "mejor_puntaje": 95
        }
    ],
    "partidas": [
        {
            "nombre": "Juan",
            "puntaje": 95,
            "dificultad": "medio",
            "fecha": "2024-11-18 10:35:00",
            "tiempo_segundos": 480
        }
    ]
}
```

**Relación:** Usado por `main.py` para gestionar usuarios antes y después de jugar.

---

## Personalización

### Modificar colores

Edita `modulos/configuracion.py`:

```python
COLOR_CELDA_SELECCIONADA = (200, 220, 255)  # RGB
COLOR_NUMERO_USUARIO = (0, 100, 200)
```

### Ajustar dificultad

Cambia la cantidad de números iniciales por región:

```python
DIFICULTAD = {
    'facil': 5,
    'medio': 4,
    'dificil': 3
}
```

### Modificar puntuación

```python
PUNTOS_ZONA_COMPLETA = 9
PUNTOS_COMPLETAR_TABLERO = 81
DESCUENTO_POR_ERROR = 1
```

---

---

## Exportación de puntajes

Desde la pantalla de puntajes, puedes descargar:

- **TXT:** Formato de texto legible y formateado
- **CSV:** Para importar en Excel o Google Sheets

Los archivos se guardan en el directorio raíz del proyecto.

---

## Algoritmo de generación

El juego utiliza el algoritmo de **backtracking** para generar Sudokus válidos:

1. Genera una matriz vacía 9x9
2. Coloca números aleatorios respetando las reglas del Sudoku
3. Si encuentra conflicto, retrocede y prueba otro número
4. Una vez completo, oculta números según la dificultad seleccionada
5. Garantiza que cada región 3x3 tenga la cantidad correcta de números visibles

---

## Conceptos aplicados

Este proyecto implementa:

- Estructuras de datos (listas, diccionarios, conjuntos)
- Algoritmos de backtracking y recursión
- Programación orientada a eventos
- Manejo de archivos JSON
- Interfaz gráfica con Pygame
- Modularización y organización de código
- Persistencia de datos

