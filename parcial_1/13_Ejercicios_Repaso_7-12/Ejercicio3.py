# Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
#  palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
#  el contenido de la lista en mayusculas

def esta_vacia(lista):
    return len(lista) == 0
def imprimir_lista_mayusculas(lista):
    for elemento in lista:
        print(elemento.upper())
mi_lista = []
if esta_vacia(mi_lista):
    print("La lista está vacía. Vamos a llenarla.")
    continuar = True
    while continuar:
        elemento = input("Ingrese una palabra o frase (o 'salir' para terminar): ")
        if elemento.lower() == "salir":
            continuar = False
        else:
            mi_lista.append(elemento)
else:
    print("La lista ya contiene elementos.")
print("\nContenido de la lista en mayúsculas:")
imprimir_lista_mayusculas(mi_lista)