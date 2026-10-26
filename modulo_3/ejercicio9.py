palabra = input("Introduce una palabra: ")
cantidad_letras = 0

for letra in palabra:
    if letra.isalpha():
        cantidad_letras += 1

print(f"La palabra tiene {cantidad_letras} letras.")
