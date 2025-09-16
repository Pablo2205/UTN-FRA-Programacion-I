'''
1. Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.
'''
clave_correcta = "python123"
clave_ingresada = input("Ingrese la clave: ")
while clave_ingresada != clave_correcta:
    print("Clave incorrecta. Intente nuevamente.")
print("Clave correcta. Acceso concedido.")

'''
2. Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.

'''

clave_correcta = "python123"
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    clave_ingresada = input("Ingrese la clave: ")
    if clave_ingresada == clave_correcta:
        print("Clave correcta. Acceso concedido.")
        break
    else:
        intentos += 1
        print(f"Clave incorrecta. Te quedan {max_intentos - intentos} intentos.")

'''
3. Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.

'''

nota = float(input("Ingrese una nota entre 1 y 10: "))
while nota < 1 or nota > 10:
    print("Nota inválida. Intente nuevamente.")
    nota = float(input("Ingrese una nota entre 1 y 10: "))
print("Nota válida:", nota)

'''
4. Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul.

'''

color = input("Ingrese un color (Rojo, Verde o Azul): ")
while color not in ["Rojo", "Verde", "Azul"]:
    print("Color inválido. Intente nuevamente.")
    color = input("Ingrese un color (Rojo, Verde o Azul): ")
print("Color válido:", color)


'''
Integrador Validaciones
Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
 
Los datos requeridos son:
Apellido
Edad, entre 18 y 90 años inclusive.
Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

Una vez ingresados y validados los datos, mostrarlos por pantalla.

'''

apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad (entre 18 y 90 años): "))
while edad < 18 or edad > 90:
    print("Edad inválida. Intente nuevamente.")
    edad = int(input("Ingrese su edad (entre 18 y 90 años): "))
estado_civil = input("Ingrese su estado civil (Soltero/a, Casado/a, Divorciado/a o Viudo/a): ")
while estado_civil not in ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]:
    print("Estado civil inválido. Intente nuevamente.")
    estado_civil = input("Ingrese su estado civil (Soltero/a, Casado/a, Divorciado/a o Viudo/a): ")
numero_legajo = input("Ingrese su número de legajo (4 cifras, sin ceros a la izquierda): ")
while not (numero_legajo.isdigit() and len(numero_legajo) == 4 and numero_legajo[0] != '0'):
    print("Número de legajo inválido. Intente nuevamente.")
    numero_legajo = input("Ingrese su número de legajo (4 cifras, sin ceros a la izquierda): ")
print("Datos ingresados:")
print("Apellido:", apellido)
print("Edad:", edad)    
print("Estado civil:", estado_civil)
print("Número de legajo:", numero_legajo)
