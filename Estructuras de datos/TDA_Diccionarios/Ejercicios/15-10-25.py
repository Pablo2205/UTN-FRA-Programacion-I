'''
Crear una lista llamada estudiantes, donde cada elemento sea un diccionario con las siguientes claves:
"nombre", "edad", "nota"

1 - Cargar manualmemte 5 estudiantes
2 - Mostrar el promedio de notas general
3 - Listar los nombres de los estudiantes cuya nota sea mayor o igual a 6

4 - Listar el o los nombre/s del o los estudiante/s con la nota mas alta

'''

# 1 - Cargar manualmemte 5 estudiantes
'''
estudiantes = [
    {"nombre": "Ana", "edad": 20, "nota": 8},
    {"nombre": "Luis", "edad": 22, "nota": 5},
    {"nombre": "Marta", "edad": 21, "nota": 9},
    {"nombre": "Carlos", "edad": 23, "nota": 6},
    {"nombre": "Sofia", "edad": 20, "nota": 4}
]
'''

estudiantes = []
for i in range(4):
    estudiantes.append({
        "nombre": input("Ingrese el nombre del estudiante: "),
        "edad": int(input("Ingrese la edad del estudiante: ")),
        "nota": float(input("Ingrese la nota del estudiante: "))
    })
print(estudiantes)
# 2 - Mostrar el promedio de notas general
def mostrar_promedios(estudiantes: list) -> float:
    suma_notas = 0
    for estudiante in estudiantes:
        suma_notas += estudiante["nota"]
    promedio_notas = suma_notas / len(estudiantes)
    print("Promedio de notas general:", promedio_notas)
    return promedio_notas
mostrar_promedios(estudiantes)
print()

# 3 - Listar los nombres de los estudiantes cuya nota sea mayor o igual a 6
def mostrar_estudiantes_aprobados(estudiantes: list) -> float:
    print(f"Estudiantes con nota mayor o igual a {nota_minima}:")
    nota_minima = 6
    for estudiante in estudiantes:
        if estudiante["nota"] >= nota_minima:
            print(estudiante["nombre"])
    return None

mostrar_estudiantes_aprobados(estudiantes)
print()

# 4 - Listar el o los nombre/s del o los estudiante/s con la nota mas alta
def mostrar_estudiantes_nota_alta(estudiantes: list) -> float:
    nota_maxima = max(estudiante["nota"] for estudiante in estudiantes)
    print("Estudiante/s con la nota más alta:")
    for estudiante in estudiantes:
        if estudiante["nota"] == nota_maxima:
            print(estudiante["nombre"])
        return nota_maxima
    
mostrar_estudiantes_nota_alta(estudiantes)