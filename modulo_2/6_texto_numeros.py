texto_numeros = input("Introduce números separados por comas: ")

try:
    lista_numeros = [int(numero.strip()) for numero in texto_numeros.split(",")]
except ValueError:
    print("Entrada no válida. Introduce números enteros separados por comas.")
else:
    lista_numeros.sort()
    print("Números ordenados:", lista_numeros)
