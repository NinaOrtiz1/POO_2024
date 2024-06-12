# Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
#   y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

mi_lista = [1, 2, 3, 4, 5]
mi_cadena = "Hola mundo!"
mi_entero = 42
mi_booleano = True
def imprimir_mensaje(variable, nombre_variable):
    if isinstance(variable, list):
        mensaje = f"{nombre_variable} es una lista."
    elif isinstance(variable, str):
        mensaje = f"{nombre_variable} es una cadena de texto."
    elif isinstance(variable, int):
        mensaje = f"{nombre_variable} es un número entero."
    elif isinstance(variable, bool):
        mensaje = f"{nombre_variable} es un valor lógico (booleano)."
    else:
        mensaje = f"{nombre_variable} es de un tipo de dato desconocido."
    
    print(mensaje)
imprimir_mensaje(mi_lista, "mi_lista")
imprimir_mensaje(mi_cadena, "mi_cadena")
imprimir_mensaje(mi_entero, "mi_entero")
imprimir_mensaje(mi_booleano, "mi_booleano")