def mayor_estricto(a, b, c):
    mayor = max(a, b, c)

    contador_mayor = (a == mayor) + (b == mayor) + (c == mayor)

    if contador_mayor == 1:
        return mayor
    else:
        return None

def programa():
    print("Por favor ingrese tres números positivos: ")
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    c = float(input("Número 3: "))

    resultado = mayor_estricto(a, b, c)

    if resultado is None:
        print("No existe un numero mayor, todos son iguales.")
    else:
        print(f"El numero mayor es: {resultado}")

programa()
