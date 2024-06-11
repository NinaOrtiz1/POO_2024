"""
    Existe una estructura de ocndicion llamada "if"
    la cual evalua una condicion para encontrar el valor "True" y se cumple
    la condicion se eejecuta la linea 1 las lineas de codiog que estan dentro del bloque

    Tienes 4 tipos de variables de IF:

"""

# if simple
 
color = input("Ingrese un color: ")

if color == "rojo":
    print("El color es rojo")
 
# if else
color = input("Ingrese un color: ")

if color == "rojo":
    print("El color es rojo")
else:
    print("El color no es rojo")


# if anidado
color = input("Ingrese un color: ")

if color == "rojo":
    print("El color es rojo")
    if color != "rojo":
        print("El color no es rojo")
else:
    print("El color no es rojo")

# if y elif
color = input("Ingrese un color: ")

if color == "rojo":
    print("El color es rojo")
elif color == "azul":
    print("El color es azul")
else:
    print("El color no es rojo")



'''
Crear un programa que pida un dia de la semana 
y que imprima el dia que le corresponde
'''


dia = input("Ingrese un dia de la semana: ")
if dia == "1":
    print("Lunes")
elif dia == "2":
    print("Martes")
elif dia == "3":
    print("Miercoles")
elif dia == "4":
    print("Jueves")
elif dia == "5":
    print("Vierdes")
elif dia == "6":
    print("Sabado")
elif dia == "7":
    print("Domingo")
else: 
    print("Dia no valido")