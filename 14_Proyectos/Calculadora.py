def suma(num1, num2):
    return num1 + num2
def resta(num1, num2):
    return num1 - num2
def multiplicacion(num1, num2):
    return num1 * num2
def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: División entre cero"
def potencia(base, exponente):
    return base ** exponente
def raiz(num):
    if num >= 0:
        return num ** 0.5
    else:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo"
def calculadora_basica():
    print(":::: CALCULADORA BASICA ::::")
    while True:
        print("\n1.- Suma")
        print("2.- Resta")
        print("3.- Multiplicación")
        print("4.- División")
        print("5.- Potencia")
        print("6.- Raíz")
        print("7.- SALIR")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = suma(num1, num2)
            print(f"El resultado de la suma es: {resultado}")
        elif opcion == "2":
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = resta(num1, num2)
            print(f"El resultado de la resta es: {resultado}")
        elif opcion == "3":
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = multiplicacion(num1, num2)
            print(f"El resultado de la multiplicación es: {resultado}")
        elif opcion == "4":
            num1 = float(input("Ingresa el dividendo: "))
            num2 = float(input("Ingresa el divisor: "))
            resultado = division(num1, num2)
            print(resultado)
        elif opcion == "5":
            base = float(input("Ingresa la base: "))
            exponente = float(input("Ingresa el exponente: "))
            resultado = potencia(base, exponente)
            print(f"El resultado de la potencia es: {resultado}")
        elif opcion == "6":
            num = float(input("Ingresa un número: "))
            resultado = raiz(num)
            print(resultado)
        elif opcion == "7":
            print("Saliendo de la calculadora...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
calculadora_basica()