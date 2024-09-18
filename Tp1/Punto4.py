print("===== Listado de Aulas por Día =====")
print("Día   Aula")

for dia in range(1, 7):
    if dia % 2 == 0:
        aula = "A-300"
    else:
        aula = "A-315"
    print(f"{dia}     {aula}")

print("\n===== Validación de Edades =====")

errores = 0

while True:
    try:
        edad = int(input("Ingrese una edad válida (mayores de 18 años): "))
        if edad >= 18:
            print(f"Edad ingresada: {edad}")
            break
        else:
            print("Error: La edad debe ser 18 o más.")
            errores += 1
    except ValueError:
        print("Error: Ingrese un valor numérico.")
        errores += 1

print(f"Cantidad de cargas erróneas: {errores}")

print("\n===== Promedio de Notas =====")

suma_notas = 0

for i in range(5): 
    nota = float(input(f"Ingrese la nota del alumno {i + 1}: "))
    suma_notas += nota

promedio = suma_notas / 5
print(f"El promedio de las notas es: {promedio:.2f}")

print("\n===== Promedio de Notas =====")

suma_notas = 0

for i in range(5): 
    nota = float(input(f"Ingrese la nota del alumno {i + 1}: "))
    suma_notas += nota

promedio = suma_notas / 5
print(f"El promedio de las notas es: {promedio:.2f}")

for i in range(1, 6): 
    nota = float(input(f"Ingrese la nota del alumno {i}: "))
    suma_notas += nota

print("\n===== Costo del Comedor =====")

cuota_diaria = 1250

for dias in range(1, 7):
    costo_total = dias * cuota_diaria
    print(f"{dias} días cuestan ${costo_total}")
