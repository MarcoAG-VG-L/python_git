palabra = input("Introduce una palabra: ")
vocales = "aeiouáéíóúü"

cantidad_vocales = sum(1 for letra in palabra.lower() if letra in vocales)
print("Cantidad de vocales:", cantidad_vocales)
