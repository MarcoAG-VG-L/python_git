try:
    with open("archivo_inexistente.txt", "r", encoding="utf-8") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print("Error: no se encontró el archivo.")

try:
    resultado = 10 / 0
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero.")
