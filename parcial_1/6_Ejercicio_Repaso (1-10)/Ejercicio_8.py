"""
8.- Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?
"""

numero = int(input("Ingresa un numero: "))
porcentaje = int(input(f"Que porcentaje del numero {numero} quieres saber?: "))

resultado = (numero * porcentaje) / 100
print(f"El {porcentaje}% de {numero} es: {resultado}")