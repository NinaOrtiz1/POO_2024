#Crear una lista con valores numericos enteros e imprimir la lista

numeros = [23, 34]
print(numeros)

#Recorer lista con for
for numero in numeros:
    print(numero)

#Recorer lista con while
    #Forma 1
i = 0
while i < len(numeros):
    print(numeros[i])
    i += 1
    #Forma 2
while numeros:
    print(numeros.pop())

#Ejemplo 2 Crar una lista de palabras, posteriormente ingresar una palabra para buscar la coincidencia en la e indicar si aparece la palabra y en que posicion en caso de contrario indicar solo una vez si la encontro

palabras = ["hola", "2024", "10.23", "True", "hola", "hola", "Falso"]

palabra = input("Ingresa una palabra: ")

noencontro = True
#FOR
for i in palabras: 
    if palabra == i:
        print(f"Encontre al palabra {palabra}, en la posicion {palabras.index(i)}")
        noencontro = False

if noencontro: 
    print(f"La palabra {palabra} no se encontro en la lista")

#WHILE
while(True):
    palabras = ["hola", "2024", "10.23", "True", "hola", "hola", "Falso"]

    palabra = input("Ingresa una palabra: ")
    
    if palabra in palabras:
        print(f"La palabra {palabra} se encontro {palabras.count(palabra)} vez(ces) en la lista") #count para saber cuantas veces se repite la palabra
        for i in range(len(palabras)): #este ciclo sirve para recorrer posiciones [0-6]

            if palabras[i] == palabra: #if para saber si la palabra se encuentra en la lista

                print(f"Se encuentra en la posicion {i}")  #i para saber en que posicion se encuentra la palabra
        opcion = input("Deseas buscar otra captura (SI/NO)?").upper()
        if opcion == "NO":
            break
    else:
        print(f"No se encontro la palabra '{palabra}', vuelve a intentarlo...")


#Ejemplo 3 Crear una lista multidimensionar AKA matriz para crear una agenda telefonica

agenda = [
    ["Gerardo", 6771135160],
    ["Jorgw", 6181003960],
    ["Maria", 6771133090],
    ["Angel", 6185420110],
]

for i in agenda:
    print(f"{agenda.index(i)+1} {agenda}")

"""
Ejemplo 4 Crear un programa que permita Gestionar (administrar) peliculas, colocar un menu de opciones para agregar, remover, consultar peliculas.
Notas:
Utilizar Funciones y madnar llamar desde otro archivo
2 utilizar liztas para almacenar los nombres de peliculas
"""


