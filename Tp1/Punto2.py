print("===== Registro de Notas - Universidad Privada =====\n")
nota_parcial1 = float(input("Ingrese la nota del primer examen: "))
nota_parcial2 = float(input("Ingrese la nota del segundo examen: "))

prom = (nota_parcial1 + nota_parcial2) / 2

if nota_parcial2 >= 7:
    print("Aprobó el segundo examen.")
else:
    print("Desaprobó el segundo examen.")

if nota_parcial2 > nota_parcial1:
    print("Mejoró su desempeño en el segundo examen.")
elif nota_parcial2 == nota_parcial1:
    print("Mantuvo la nota entre ambos exámenes.")
else:
    print("Empeoró su desempeño en el segundo examen.")

if prom >= 7:
    print(f"\nPromedio: {prom:.2f} - El alumno promocionó la materia.")
elif prom >= 4:
    print(f"\nPromedio: {prom:.2f} - El alumno debe rendir el examen final.")
else:
    print(f"\nPromedio: {prom:.2f} - El alumno debe recursar la materia.")