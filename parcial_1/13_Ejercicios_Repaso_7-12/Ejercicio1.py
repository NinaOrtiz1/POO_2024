# Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado

def lista_a_string(lista):
    string_lista = [str(elemento) for elemento in lista]
    return ', '.join(string_lista)
numeros = [5, 2, 8, 1, 9, 3, 7, 4]
print("Lista original:")
for num in numeros:
    print(num, end=" ")
print()
string_numeros = lista_a_string(numeros)
print(f"Lista en formato string: {string_numeros}")
numeros.sort()
print("Lista ordenada:")
for num in numeros:
    print(num, end=" ")
print()
longitud = len(numeros)
print(f"Longitud de la lista: {longitud}")
elemento_buscar = int(input("Ingrese el número a buscar en la lista: "))
if elemento_buscar in numeros:
    print(f"El elemento {elemento_buscar} se encuentra en la lista.")
else:
    print(f"El elemento {elemento_buscar} no se encuentra en la lista.")
