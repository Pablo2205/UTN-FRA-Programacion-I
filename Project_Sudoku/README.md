
# ----------------- Caracteristicas -----------------

- Tres niveles de dificultad: Fácil, Medio y Difícil
- Sistema de puntuación: Gana puntos al completar zonas y pierde puntos por errores
- Validación en tiempo real: Feedback visual inmediato (verde/rojo/amarillo)
- Música y efectos de sonido: Experiencia inmersiva con audio
- Interfaz intuitiva: Fácil de usar con mouse y teclado
- Generación aleatoria: Cada partida es diferente

# ----------------- Estructura Carpetas -----------------

Project_Sudoku/
├── main.py
├── README.md
├── modulos/
│   ├── configuracion.py
│   ├── datos.py
│   ├── logica.py
│   ├── validacion.py
│   ├── interfaz.py
│   └── sonidos.py
└── assets/
    ├── imagenes/
    │   └── logo_utn.png
    └── sonidos/
        ├── musica_fondo.mp3 
        ├── inicio.wav 
        ├── reiniciar.wav 
        ├── validar.wav 
        ├── correcto.wav
        ├── error.wav 
        └── victoria.wav 

# ----------------- Controles -----------------

- Antes del juego
   - Click en un botón para seleccionar dificultad
   
- Durante el juego:
   - Click izquierdo: Seleccionar celda
   - Teclas 1-9: Colocar número
   - Backspace/Delete**: Borrar número
   - R: Nuevo tablero (misma dificultad)
   - ESC: Volver al menú principal

# ----------------- Botones -----------------

- Nuevo Juego: Vuelve al menú de selección de dificultad
- Reiniciar: Genera un nuevo tablero con la misma dificultad
- Validar: Muestra cuántos números tienes correctos, incorrectos y vacíos

# ----------------- Sistema de puntuacion -----------------


- Empiezas con 0 puntos
- +9 puntos por completar una fila, columna o región
- +81 puntos por completar todo el tablero
- -1 punto por cada número incorrecto colocado
- Los números duplicados no restan puntos

# ----------------- Códigos de colores -----------------

- Verde: Número correcto
- Rojo: Número incorrecto
- Amarillo: Número duplicado
- Azul: Celda seleccionada
- Gris: Números fijos del sistema

### Módulo: configuracion.py

**Responsabilidad**: Almacenar todas las constantes y configuraciones del juego.

**Contiene**:
- Dimensiones de la ventana
- Tamaños del tablero y celdas
- Colores RGB para todos los elementos
- Rutas de archivos (imágenes y sonidos)
- Configuración de dificultad
- Sistema de puntuación
- Volúmenes de audio

**Relación con otros módulos**: Todos los demás módulos importan sus constantes desde aquí.

### Módulo: datos.py

**Responsabilidad**: Generar y manipular los datos del Sudoku.

**Funciones principales**:
- `generar_matriz_vacia()`: Crea una matriz 9x9 con ceros
- `es_valido()`: Verifica si un número puede ir en una posición
- `resolver_sudoku()`: Resuelve un Sudoku usando backtracking
- `generar_sudoku_completo()`: Crea un Sudoku resuelto
- `generar_sudoku_jugable()`: Genera un tablero según dificultad

**Relación**: Es usado por `logica.py` para crear nuevos juegos.

### Módulo: validacion.py

**Responsabilidad**: Validar movimientos y verificar el estado del juego.

**Funciones principales**:
- `validar_numero()`: Verifica si un número cumple las reglas
- `verificar_zona_completa()`: Comprueba si una fila/columna/región está completa
- `verificar_matriz_completa()`: Verifica si todo el Sudoku está resuelto
- `validar_solucion()`: Compara el progreso del jugador con la solución

**Relación**: Es usado por `logica.py` para validar las acciones del jugador.

### Módulo: logica.py

**Responsabilidad**: Controlar el estado del juego y las acciones del jugador.

**Funciones principales**:
- `inicializar_juego()`: Crea un nuevo juego
- `seleccionar_celda()`: Marca una celda como seleccionada
- `colocar_numero()`: Coloca un número y actualiza el estado
- `borrar_numero()`: Elimina un número de una celda
- `reiniciar_juego()`: Genera un nuevo tablero

**Relación**: 
- Usa `datos.py` para generar matrices
- Usa `validacion.py` para verificar movimientos
- Es usado por `main.py` para controlar el juego

### Módulo: interfaz.py

**Responsabilidad**: Dibujar todos los elementos visuales del juego.

**Funciones principales**:
- `inicializar_pygame()`: Inicia Pygame y crea la ventana
- `dibujar_tablero()`: Dibuja el tablero con números y colores
- `dibujar_interfaz()`: Dibuja toda la interfaz del juego
- `dibujar_menu_dificultad()`: Dibuja el menú de selección
- `crear_botones()`: Crea los botones del juego
- `obtener_celda_click()`: Convierte coordenadas en posición de celda

**Relación**: Es usado por `main.py` para mostrar todo en pantalla.

### Módulo: sonidos.py

**Responsabilidad**: Gestionar música de fondo y efectos de sonido.

**Funciones principales**:
- `inicializar_sonidos()`: Inicia el sistema de audio
- `cargar_musica_fondo()`: Carga y reproduce música en loop
- `cargar_efectos_sonido()`: Carga todos los efectos
- `reproducir_sonido()`: Reproduce un efecto específico

**Relación**: Es usado por `main.py` para reproducir audio durante el juego.

### Archivo: main.py

**Responsabilidad**: Controlar el flujo principal del juego.

**Funcionalidad**:
1. Inicializa todos los sistemas (Pygame, sonidos, interfaz)
2. Controla el bucle principal del juego
3. Maneja todos los eventos del usuario (clicks, teclas)
4. Coordina todos los módulos
5. Actualiza la pantalla constantemente

**Relación**: Importa y usa TODOS los demás módulos para hacer funcionar el juego completo.

## 🔄 Flujo del programa

```
1. main.py ejecuta la función main()
   ↓
2. Inicializa Pygame, sonidos y recursos
   ↓
3. Muestra menú de dificultad (interfaz.py)
   ↓
4. Usuario selecciona dificultad
   ↓
5. logica.py genera nuevo juego usando datos.py
   ↓
6. Bucle principal:
   - Captura eventos del usuario
   - Actualiza el estado (logica.py)
   - Valida movimientos (validacion.py)
   - Dibuja todo (interfaz.py)
   - Reproduce sonidos (sonidos.py)
   ↓
7. Repite hasta que el usuario cierra el juego
```

## ⚙️ Configuración

Puedes personalizar el juego editando `modulos/configuracion.py`:

- **Colores**: Cambia los valores RGB de cualquier elemento
- **Tamaños**: Ajusta dimensiones de ventana, celdas y botones
- **Dificultad**: Modifica cuántos números aparecen por región
- **Puntuación**: Cambia los puntos ganados/perdidos
- **Audio**: Ajusta volúmenes de música y efectos

## 🎨 Archivos opcionales

El juego funciona sin problemas aunque falten los archivos de audio o la imagen del logo. Si no están presentes, simplemente se omiten esos elementos.

Para agregar estos archivos:
1. Colócalos en la carpeta `assets/` correspondiente
2. Asegúrate de que tengan el nombre correcto (ver estructura de carpetas)

## 🤝 Créditos

- **Desarrollado por**: Estudiante de UTN Avellaneda
- **Materia**: Programación I
- **Tecnología**: Python + Pygame
- **Año**: 2024

## 📝 Notas de implementación

### Estilo de código

Este proyecto sigue estándares específicos de código:

- **Sin try-except**: Todas las verificaciones son explícitas
- **Sin "if not"**: Todas las condiciones son afirmativas
- **Variables explícitas**: Todas las funciones devuelven variables, no operaciones directas
- **Documentación completa**: Cada función está documentada con su propósito, parámetros, operación y retorno
- **Nombres descriptivos**: Variables y funciones tienen nombres claros y en español

### Algoritmos principales

- **Generación de Sudoku**: Usa backtracking con números aleatorios
- **Validación**: Verifica reglas del Sudoku (filas, columnas, regiones 3x3)
- **Puntuación**: Sistema acumulativo con bonificaciones por zonas completadas


