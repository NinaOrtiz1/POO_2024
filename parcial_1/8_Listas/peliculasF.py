from Peliculas import peliculas
import os

def agregar_pelicula():
    nombre = input("Ingresa el nombre de la pelicula: ")
    genero = input("Ingresa el genero de la pelicula: ")
    anio = int(input("Ingresa el año de la pelicula: "))
    peliculas.append([nombre, genero, anio])
    print(f"La pelicula {nombre} se agrego correctamente")

def actualizar_pelicula():
    nombre = input("Ingresa el nombre de la pelicula a actualizar: ")
    for pelicula in peliculas:
        if nombre == pelicula[0]:
            print(f"Nombre: {pelicula[0]}")
            print(f"Genero: {pelicula[1]}")
            print(f"Año: {pelicula[2]}")
            print("Ingresa los nuevos datos de la pelicula")
            nombre = input("Ingresa el nombre de la pelicula: ")
            genero = input("Ingresa el genero de la pelicula: ")
            anio = int(input("Ingresa el año de la pelicula: "))
            peliculas[peliculas.index(pelicula)] = [nombre, genero, anio]
            print(f"La pelicula {nombre} se actualizo correctamente")
            return
    print(f"La pelicula {nombre} no se encontro")

def eliminar_pelicula():
    nombre = input("Ingresa el nombre de la pelicula a eliminar: ")
    for pelicula in peliculas:
        if nombre == pelicula[0]:
            peliculas.remove(pelicula)
            print(f"La pelicula {nombre} se elimino correctamente")
            return
    print(f"La pelicula {nombre} no se encontro")

def consultar_pelicula(): 
    nombre = input("Ingresa el nombre de la pelicula a consultar: ")
    for pelicula in peliculas:
        if nombre == pelicula[0]:
            print(f"Nombre: {pelicula[0]}")
            print(f"Genero: {pelicula[1]}")
            print(f"Año: {pelicula[2]}")
            return
    print(f"La pelicula {nombre} no se encontro")

def mostrar_peliculas():
    for i in peliculas:
        if peliculas == []:
            print("No hay peliculas en la lista")
        print(f"Nombre: {i[0]}")
        print(f"Genero: {i[1]}")
        print(f"Año: {i[2]}")
        print("")

def limpiar():
    os.system("cls")

