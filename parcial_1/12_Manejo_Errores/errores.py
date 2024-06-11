"""
Es la forma en la que tienen los lenguajes de programacion 
para evitar que sucedan errores en tiempo de ejecucion
"""

#Ejemplo 1 error cuando una variable no se genera 


#Try facil 
try:
    nombre = input("")
    if len(nombre) > 1:
        nombre_usuario = f"El nombre es {nombre}"
    print(nombre_usuario)
except:
    print("Es necesario introducir un nombre de usuario")

#Manejando Exception
try:
    nombre = input("")
    if len(nombre) > 1:
        nombre_usuario = f"El nombre es {nombre}"
    print(nombre_usuario)
except Exception as e:
    print(f"Ha ocurrido un error: {e}")

#Ejemplo 2 cuando se solicita un numero se introduce una letra

numero = int(input("Dame un numero: "))

if numero > 0:
    print(f"Soy un numero entero positivo: {numero}")
else:
    print(f"Soy un numero entero negativo: {numero}")


try: 
    numero = int(input("Dame un numero: "))
    if numero > 0:
        print(f"Soy un numero entero positivo: {numero}")
    else:
        print(f"Soy un numero entero negativo: {numero}")
except ValueError as e:
    print(e)

#Ejemplo 3 cuando se generan multiples excepciones

try:
    numero = int(input("Dame un numero"))

    print("El cuadrado es: "+str(numero*numero))
except ValueError:
    print("Debes de introducir un numero no se puede convertir un caracter que no sea numerico")
except TypeError:
    print("No es posible convertir el numero a entero")
else: 
    print("Finalizo correctamente")
finally: #Se ejecuta siempre
    print("Listo se termino")