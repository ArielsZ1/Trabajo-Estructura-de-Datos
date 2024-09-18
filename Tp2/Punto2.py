def es_fecha_valida(dia, mes, anio):
    if anio <= 0:
        return False

    if mes < 1 or mes > 12:
        return False

    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if dia < 1 or dia > dias_por_mes[mes - 1]:
        return False

    return True

def programa():
    print("Ingrese una fecha (día, mes, año):")
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    anio = int(input("Año: "))

    if es_fecha_valida(dia, mes, anio):
        print("La fecha es válida.")
    else:
        print("La fecha no es válida.")
programa()
