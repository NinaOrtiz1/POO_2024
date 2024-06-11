'''
Calculadora
'''
#-------------------------eJERCICIO REALIZADO CON IF-------------------------
# print("Que operacion deseas realizar:")
# operacion = input("1.- Suma (+) \n2.- Resta (-)\n3.- Multiplicaion (*)\n4.- Division (/)\n5.- Salir \n").upper()

# if operacion == '+' | operacion == 'SUMA' | operacion == '1' | operacion == '-' | operacion == 'RESTA' | operacion == '2' | operacion == '*' | operacion == 'MULTIPLICACION' | operacion == '3' | operacion == '/' | operacion == 'DIVISION' | operacion == '4':
#     n1 = int(input("Ingresa un numero:"))
#     n2 = int(input("Ingresa un numero:"))

# if operacion == '+' or operacion == 'SUMA' or operacion == '1':
#     print(f"{n1}+{n2} = {n1+n2}")
# elif operacion == '-' or operacion == 'RESTA' or operacion == '2':
#     print(f"{n1}-{n2} = {n1-n2}")
# elif operacion == '*' or operacion == 'MULTIPLICACION' or operacion == '3':
#     print(f"{n1}*{n2} = {n1*n2}")
# elif operacion == '/' or operacion == 'DIVISION' or operacion == '4':
#     print(f"{n1}/{n2} = {n1/n2}")
# else:
#     print("TERMINASTE GRACIAS POR UTILIZAR EL SISTEMA")









'''
#-------------------------eJERCICIO REALIZADO CON MATCH-------------------------
print("Que operacion deseas realizar:")
operacion = input("1.- Suma (+) \n2.- Resta (-)\n3.- Multiplicaion (*)\n4.- Division (/)\n5.- Salir \n").upper()


"""
    Explicacion:
    el if {variable} in [bloque codigo]
    sirve para comparar si lo ingresado en la variable se encuentra dentro de las opciones
    preestablesidas en el codigo.
    Se compara si lo ingresado por el usuario se encuentra en la lista de opciones:
    ['+','SUMA','1','-','RESTA','2','*','MULTIPLICACION','3','/','DIVISION','4']
    en caso de que se encuentre se ejecutara el codigo que se encuentra dentro del if
    si no no entrara dentro de esa concicion y seguira su flujo normal
    
"""
if operacion in ['+','SUMA','1','-','RESTA','2','*','MULTIPLICACION','3','/','DIVISION','4']:
    n1= int(input("Ingresa un numero:"))
    n2= int(input("Ingresa un numero:"))

match operacion: 
    case "+" | "SUMA" | "1":
        print(f"{n1}+{n2} = {n1+n2}")
    case "-" | "RESTA" | "2":
        print(f"{n1}-{n2} = {n1-n2}")
    case "*" | "MULTIPLICACION" | "3":
        print(f"{n1}*{n2} = {n1*n2}")
    case "/" | "DIVISION" | "4":
        print(f"{n1}/{n2} = {n1/n2}")
    case _:
        print("TERMINASTE GRACIAS POR UTILIZAR EL SISTEMA")

'''

#-------------------------EJERCICIO REALIZADO CON FUNCIONES-------------------
from variasfunciones import * 

while True:
    limpiar()
    print("Que operacion deseas realizar:")
    opcion = input("1.- Suma (+) \n2.- Resta (-)\n3.- Multiplicaion (*)\n4.- Division (/)\n5.- Salir \n").upper()
    if opcion != "5" :
        n1,n2 = solicitarNum()
        print(calculadora(n1, n2, opcion))
    else: 
        print("TERMINASTE GRACIAS POR UTILIZAR EL SISTEMA")
        break
