import math


numero = int(input("Introduce un número entero no negativo: "))
if numero < 0:
    raise ValueError("El factorial solo está definido para enteros no negativos.")

print(f"{numero}! = {math.factorial(numero)}")
