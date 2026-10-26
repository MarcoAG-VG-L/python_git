def leer_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Introduce un número.")


def calcular_media(primer_valor, segundo_valor):
    return (primer_valor + segundo_valor) / 2


valor1 = leer_numero("Introduce el primer número: ")
valor2 = leer_numero("Introduce el segundo número: ")
print(f"La media aritmética es: {calcular_media(valor1, valor2)}")
