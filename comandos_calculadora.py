from TEMA_1.TAREAS.CALCULADORA_PYTHON.calculadora import suma, resta, multiplicacion, potencia, división, division_entera, resto_modulo

nombre = input("Indique su nombre a continuación: ").strip().upper()
apellido = input("Indique su apellido a continuación: ").strip().upper()
edad = int(input("Indique su edad a continuación: "))

if edad < 18:
    print("No tienes la edad necesaria para acceder")
else:
    print(f"¡Hola {nombre} {apellido}, tienes {edad} años, bienvenido a la calculadora!")

    num1 = int(input("Indique el primer número: "))
    num2 = int(input("Indique el segundo número: "))
    accion = input("Indique la operación a realizar: + , -, *, **, /, //, %: ").strip()

    if accion == "+":
        print(f"La suma de {num1} y {num2} es: {suma(num1, num2)}")
    elif accion == "-":
        print(f"La resta de {num1} y {num2} es: {resta(num1, num2)}")
    elif accion == "*":
        print(f"La multiplicación de {num1} y {num2} es: {multiplicacion(num1, num2)}")
    elif accion == "**":
        print(f"La potencia de {num1} y {num2} es: {potencia(num1, num2)}")
    elif accion == "/":
        print(f"La división de {num1} y {num2} es: {división(num1, num2)}")
    elif accion == "//":
        print(f"La división entera de {num1} y {num2} es: {division_entera(num1, num2)}")
    elif accion == "%":
        print(f"El resto módulo de {num1} y {num2} es: {resto_modulo(num1, num2)}")
    else:
        print("Valor inválido")