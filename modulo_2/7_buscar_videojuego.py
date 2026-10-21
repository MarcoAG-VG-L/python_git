videojuegos = ["Minecraft", "The Legend of Zelda", "Mario Bros", "Pokemon", "League of Legends"]
busqueda = input("Que videojuego quieres buscar? ").strip().lower()

encontrado = False
for videojuego in videojuegos:
    if videojuego.lower() == busqueda:
        encontrado = True
        break

if encontrado:
    print("\nEl videojuego SI esta en la lista.")
else:
    print("\nEl videojuego NO esta en la lista.")
