
'''
colectivos_zona_sur = [373, 378, 385, 386, 388, 390, 392]
colectivos_zona_norte = [152, 153, 160, 161, 162, 163, 164]
colectivos_zona_capital = [29, 33, 34, 36, 37, 39, 64]
# Días de la semana
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

# listas de pasajeros por zona
pasajeros_sur = []
pasajeros_norte = []
pasajeros_capital = []

print("=== CARGA DE PASAJEROS ===")

# Zona Sur
print("Zona Sur")
total_sur = 0
for dia in dias:
    cantidad = int(input(f"Ingrese pasajeros del {dia}: "))
    pasajeros_sur.append(cantidad)
    total_sur = total_sur + cantidad

# Zona Norte
print("Zona Norte")
total_norte = 0
for dia in dias:
    cantidad = int(input(f"Ingrese pasajeros del {dia}: "))
    pasajeros_norte.append(cantidad)
    total_norte = total_norte + cantidad

# Zona Capital
print("Zona Capital")
total_capital = 0
for dia in dias:
    cantidad = int(input(f"Ingrese pasajeros del {dia}: "))
    pasajeros_capital.append(cantidad)
    total_capital = total_capital + cantidad

# Total general
total_general = total_sur + total_norte + total_capital

print("\n ___ INFORME SEMANAL ___")

print("\n Zona Sur:")
for i in range(7):
    print(f"{dias[i]}: {pasajeros_sur[i]} pasajeros")
print(f"Total semanal Zona Sur: {total_sur}")

print("\n Zona Norte:")
for i in range(7):
    print(f"{dias[i]}: {pasajeros_norte[i]} pasajeros")
print(f"Total semanal Zona Norte: {total_norte}")

print("\n Zona Capital:")
for i in range(7):
    print(f"{dias[i]}: {pasajeros_capital[i]} pasajeros")
print(f"Total semanal Zona Capital: {total_capital}")

print("\n _______________________________")
print(f"TOTAL GENERAL DE LAS 3 ZONAS: {total_general} pasajeros")
print(" _______________________________")

'''
# 


# Listas de líneas por zona
colectivos_zona_sur = [373, 378, 385, 386, 388, 390, 392]
colectivos_zona_norte = [152, 153, 160, 161, 162, 163, 164]
colectivos_zona_capital = [29, 33, 34, 36, 37, 39, 64]

# Días de la semana
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

# Listas para guardar pasajeros
pasajeros_sur = []
pasajeros_norte = []
pasajeros_capital = []

print("=== CARGA DE PASAJEROS ===")

# === Zona Sur ===
print("\nZona Sur")
for linea in colectivos_zona_sur:
    total_linea = 0
    print(f"\nColectivo {linea}:")
    for dia in dias:
        cantidad = int(input(f"Ingrese pasajeros del {dia}: "))
        total_linea += cantidad
    pasajeros_sur.append(total_linea)

# === Zona Norte ===
print("\nZona Norte")
for linea in colectivos_zona_norte:
    total_linea = 0
    print(f"\nColectivo {linea}:")
    for dia in dias:
        cantidad = int(input(f"Ingrese pasajeros del {dia}: "))
        total_linea += cantidad
    pasajeros_norte.append(total_linea)

# === Zona Capital ===
print("\nZona Capital")
for linea in colectivos_zona_capital:
    total_linea = 0
    print(f"\nColectivo {linea}:")
    for dia in dias:
        cantidad = int(input(f"Ingrese pasajeros del {dia}: "))
        total_linea += cantidad
    pasajeros_capital.append(total_linea)

# === Informe semanal usando ZIP ===
print("\n ___ INFORME SEMANAL ___")

print("\nZona Sur:")
for linea, total in zip(colectivos_zona_sur, pasajeros_sur):
    print(f"Línea {linea}: {total} pasajeros")

print("\nZona Norte:")
for linea, total in zip(colectivos_zona_norte, pasajeros_norte):
    print(f"Línea {linea}: {total} pasajeros")

print("\nZona Capital:")
for linea, total in zip(colectivos_zona_capital, pasajeros_capital):
    print(f"Línea {linea}: {total} pasajeros")

# === Totales generales ===
total_sur = sum(pasajeros_sur)
total_norte = sum(pasajeros_norte)
total_capital = sum(pasajeros_capital)
total_general = total_sur + total_norte + total_capital

print("\n _______________________________")
print(f"Total semanal Zona Sur: {total_sur}")
print(f"Total semanal Zona Norte: {total_norte}")
print(f"Total semanal Zona Capital: {total_capital}")
print(f"TOTAL GENERAL DE LAS 3 ZONAS: {total_general}")
print(" _______________________________")




'''
Matriz de 5 columnas y listas de lineas de colectivos


'''