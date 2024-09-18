print("===== Inscripción de Alumnos - Universidad Privada =====\n")
nombre = input("Ingrese su nombre completo: ")
edad = int(input("Ingrese su edad: "))
fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/yyyy): ")

posee_titulo_secundario = True

monto_matricula = float(input("Ingrese el monto de la matrícula: $"))

cuota = monto_matricula + 1000

arancel_python = 12000 

costo_mensual = (cuota + arancel_python) / 4

pago_efectivo = input("¿Paga en efectivo? (si/no): ").lower()

if pago_efectivo == "si":
    costo_mensual_con_descuento = costo_mensual * 0.85
    print(f"\nDescuento aplicado. El costo mensual con descuento es: ${costo_mensual_con_descuento:.2f}")
else:
    print(f"\nEl costo mensual es: ${costo_mensual:.2f}")

print("\n===== Resumen de Inscripción =====")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Fecha de Nacimiento: {fecha_nacimiento}")
print(f"Posee Título Secundario: {'Sí' if posee_titulo_secundario else 'No'}")
print(f"Monto de Matrícula: ${monto_matricula:.2f}")
print(f"Cuota (incluyendo $1000): ${cuota:.2f}")
print(f"Arancel de 'Python I': ${arancel_python}")
print(f"Costo Mensual {'con' if pago_efectivo == 'si' else 'sin'} Descuento: ${costo_mensual_con_descuento:.2f}")