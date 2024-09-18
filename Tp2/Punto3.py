def calcular_vuelto(total_compra, dinero_recibido):
    if dinero_recibido < total_compra:
        return "Error: El dinero recibido es insuficiente para gestionar la compra."

    vuelto = dinero_recibido - total_compra

    billetes = [500, 100, 50, 20, 10, 5, 1]

    cantidad_billetes = {}

    for billete in billetes:
        cantidad_billetes[billete] = vuelto // billete
        vuelto = vuelto % billete 

    return cantidad_billetes

def programa():
    total_compra = int(input("Ingrese el total de la compra: "))
    dinero_recibido = int(input("Ingrese el dinero recibido: "))

    resultado = calcular_vuelto(total_compra, dinero_recibido)

    if isinstance(resultado, str):
        print(resultado)
    else:
        print("Vuelto: ")
        for billete, cantidad in resultado.items():
            if cantidad > 0:
                print(f"{cantidad} billete(s) de ${billete}")
programa()
