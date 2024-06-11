"""
4.- Solicitar 2 numeros al usuario
 y realizar todas las operaciones
 basicas de una calculadora (+,-,*,/)
 y mostrar por pantalla el resultado
"""

n1 = input("Ingresa el primer numero: ")
n2 = input("Ingresa el segundo numero: ")

suma = int(n1) + int(n2)
resta = int(n1) - int(n2)
multi = int(n1) * int(n2)
division = int(n1) / int(n2)


print(f"La suma de los dos numeros es de: {suma}")
print(f"La resta de los dos numeros es de: {resta}")
print(f"La multiplicacion de los dos numeros es de: {multi}")
print(f"La division de los dos numeros es de: {division}")