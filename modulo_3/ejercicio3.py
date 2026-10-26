frutas = ["manzana", "pera", "plátano", "naranja", "uva"]

print(f"Primera fruta: {frutas[0]}")
print(f"Última fruta: {frutas[-1]}")
print(f"Cantidad de frutas: {len(frutas)}")

frutas.append("kiwi")
print (*frutas, sep=", ")