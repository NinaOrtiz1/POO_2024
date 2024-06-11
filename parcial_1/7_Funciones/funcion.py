'''
    Una funciones es un conjunto de instrucciones agrupadas bajo un nombre en particular
    como un programa mas pequeño que cumple una funcion especifica. la funcion puede 
    reutilizar con el simple hecho de invocarla es decir mandarla a llamar.

    SINTAXIS:
    def nombre_funcion(parametros):
        instrucciones
    
    nombre_funcion(parametros)

    Las funciones pueden ser de 4 tipos
    1. Funcion que no recibe parametros y no regreas valor
    2. Funcion que no recibe parametros y regresa valor
    3. Funcion que recibe parametros y no regresa valor
    4. Funcion que recibe parametros y regresa valor

'''
#|---------------------------NO RECIBEN VALOR--------------------------------------|#
# Funcion que no recibe parametros y no regresa valor
def sumaNumeros():
    n1 = int(input("Ingrese el primer numero: "))
    n2 = int(input("Ingrese el segundo numero: "))
    suma = n1 + n2
    print(f"{n1}+{n2}={suma}")

sumaNumeros()

# Funcion que recibe parametros y no regresa valor
def multiplicacion(n1, n2):
    multiplicacion = n1*n2
    print(f"{n1} * {n2} = {multiplicacion}")

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
multiplicacion(n1, n2)

#|---------------------------RECIBEN VALOR--------------------------------------|#

# Funcion que no recibe parametros y regresa valor
def restaNumeros():
    n1 = int(input("Ingrese el primer numero: "))
    n2 = int(input("Ingrese el segundo numero: "))
    resta = n1 - n2
    return f"{n1}-{n2}={resta}"

print(restaNumeros())
# Funcion que recibe parametros y regresa valor
def divisionNumeros(n1, n2):
    division = n1 / n2 
    return f"{n1}/{n2}={division}"

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
print(divisionNumeros(n1, n2))

'''
Ejemplo 6 Crear un programa que solicite a traves de una funcion la siguiente informacion:
    - Nombre del paciente
    - Edad
    - Estatura
    - Tipo de sabre
Utilizar los 4 tipos de funciones.
'''

def paciente():
    name = input("Ingresa el nombre del paciente: ")
    age = int(input("Ingresa la edad: "))
    lg = float(input("Ingresa su altura en METROS: "))
    ts = input("Ingresa el tipo de sangre: ")
    print(f"Nombre: {name}\nEdad: {age}\nAltura: {lg}\nTipo de sabgre: {ts}")
paciente()