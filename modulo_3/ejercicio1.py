nombre = str(input("Introduce tu nombre: "))
edad = int(input("Introduce tu edad: "))
estudiante = input("¿Eres estudiante? (si/no)")
if estudiante.lower() == "si":
    estudiante = True
    print(f"Tu nombre es: {nombre.title()}, tu edad es: {edad} y eres estudiante")
else:
    estudiante = False
    print(f"Tu nombre es: {nombre.title()}, tu edad es: {edad} y no eres estudiante")
