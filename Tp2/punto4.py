def calcular_precio_final(cantidad, tipo_moneda):
    precio_por_zapallo = 1000
    descuentos = {
        "dolares": 0.05,  # 5% de descuento
        "yenes": 0.15,    # 15% de descuento
        "guaranies": 0.20,  # 20% de descuento
        "pesos": 0.10     # 10% de descuento
    }

    # Calcular el descuento o incremento según el tipo de moneda
    if tipo_moneda in descuentos:
        descuento = descuentos[tipo_moneda]
        precio_final = precio_por_zapallo * cantidad * (1 - descuento)
        mensaje_descuento = f"Descuento aplicado: {int(descuento * 100)}%"
    else:
        # Si es otra moneda, se aplica un incremento del 10%
        incremento = 0.10
        precio_final = precio_por_zapallo * cantidad * (1 + incremento)
        mensaje_descuento = "Incremento aplicado: 10% por moneda no reconocida"

    return precio_final, mensaje_descuento


def generar_recibo(nombre_comprador, nombre_empresa, tipo_moneda, cantidad, precio_final, mensaje_descuento):
    recibo = f"""
    Recibo de compra
    --------------------
    Nombre del comprador: {nombre_comprador}
    Nombre de la empresa: {nombre_empresa}
    Producto: Zapallo
    Cantidad: {cantidad}
    Moneda: {tipo_moneda.capitalize()}
    {mensaje_descuento}
    Precio total a pagar: ${precio_final:.2f} pesos
    --------------------
    ¡Gracias por su compra!
    """
    return recibo


# Programa principal
def programa():
    nombre_empresa = "Zapallos S.A."
    nombre_comprador = input("Ingrese el nombre del comprador: ")
    cantidad = int(input("Ingrese la cantidad de zapallos que desea comprar: "))
    tipo_moneda = input("Ingrese el tipo de moneda con la que pagará (dolares, yenes, guaranies, pesos, otra): ").lower()

    # Calcular precio final y obtener el mensaje de descuento o incremento
    precio_final, mensaje_descuento = calcular_precio_final(cantidad, tipo_moneda)

    # Generar y mostrar el recibo
    recibo = generar_recibo(nombre_comprador, nombre_empresa, tipo_moneda, cantidad, precio_final, mensaje_descuento)
    print(recibo)

# Invocar el programa
programa()
