print("===== Organización de Aulas - Universidad Privada =====\n")

dia = int(input("Ingrese el número de día (1 = lunes, 6 = sábado): "))

if 1 <= dia <= 6:
    if dia % 2 == 0:
        aula = "A-300"
    else:
        aula = "A-315"
    print(f"Los alumnos de primer año cursan en el aula {aula}.")
else:
    print("Número de día inválido. Por favor ingrese un valor entre 1 y 6.")

print("===== Organización de Aulas - Universidad Privada =====\n")

dia = int(input("Ingrese el número de día (1 = lunes, 6 = sábado): "))

if 1 <= dia <= 6:
    if dia % 2 == 0:
        aula = "A-300"
    else:
        aula = "A-315"
    print(f"Los alumnos de primer año cursan en el aula {aula}.")
else:
    print("Número de día inválido. Por favor ingrese un valor entre 1 y 6.")

print("\n===== Asignación de Costo de Estacionamiento =====\n")

vehiculo = input("¿Viene en auto, moto o bicicleta?: ").lower()

if vehiculo == "auto" or vehiculo == "moto":
    costo_estacionamiento = 300
elif vehiculo == "bicicleta":
    costo_estacionamiento = 50
else:
    costo_estacionamiento = 0
    print("Tipo de vehículo no reconocido. No se asigna costo de estacionamiento.")

if costo_estacionamiento > 0:
    print(f"El costo diario de estacionamiento es: ${costo_estacionamiento}")
