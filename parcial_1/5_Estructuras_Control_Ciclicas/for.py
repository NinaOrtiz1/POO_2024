'''
    Ciclo For estructura interativa que se ejecuta X veces

    Sintaxis:
        for variable in range(inicio, fin, incremento):
            bloque de codigo
'''

#Ejemplo 1 Crear que imprima en pantalla 5 veces el @

for i in range(5):
    print('@')

#Ejemplo 2 Crear un programa que imprima los numeros del 1 al 5 y los sume al final debe imprimir la suma

suma = 0
for i in range(1, 6):
    print(i)
    suma += i
print(f"La suma es: {suma}")

#Ejemplo 3 Crear un programa que imprima la tabla de multiplicar que el usuario desee

tabla = int(input("Ingrese la tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{tabla} x {i} = {tabla * i}")

    
    