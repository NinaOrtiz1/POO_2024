"""
7.- Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

"""
n1 = int(input("Ingresa el primer numero: "))
n2 = int(input("Ingresa el segundo numero: "))

if n1 < n2:
    for i in range(n1, n2):
        if i % 2 != 0:
            print(i)
elif n1 > n2:
    for i in range(n2, n1):
        if i % 2 != 0:
            print(i)