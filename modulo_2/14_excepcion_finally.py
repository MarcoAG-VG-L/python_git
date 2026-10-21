try:
    with open("archivo_inexistente.txt", "r", encoding="utf-8") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print("Error: no se encontró el archivo.")
finally:
    print("El bloque finally se ejecuta siempre.")
