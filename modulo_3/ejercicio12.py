def leer_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Introduce un número.")


def calcular_media(*valores):
    if len(valores) < 2:
        raise ValueError("Se necesitan al menos dos valores.")
    return sum(valores) / len(valores)


valores = []
while True:
    entrada = input(
        "Introduce un número (o pulsa Enter para terminar): "
    )
    if entrada == "":
        if len(valores) >= 2:
            break
        print("Introduce al menos dos números.")
        continue

    try:
        valores.append(float(entrada))
    except ValueError:
        print("Entrada no válida. Introduce un número.")

print(f"La media aritmética es: {calcular_media(*valores)}")
