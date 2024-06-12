# Escribir un programa  que añada valores a una lista mientras que su longitud 
#  sea menor a 120, y luego mostrar la lista: Usar un while y for

mi_lista = []
print("Ingrese valores para agregar a la lista (longitud máxima: 120)")
while len(mi_lista) < 120:
    valor = input("Ingrese un valor (o 'salir' para terminar): ")
    if valor.lower() == "salir":
        break
    mi_lista.append(valor)
print("\nLista final:")
for elemento in mi_lista:
    print(elemento)