entrada = input("Introduce un número: ")

try:
    numero = float(entrada)
    print("Has introducido el número", numero)
except ValueError:
    print("La entrada no es un número válido.")
