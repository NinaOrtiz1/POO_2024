peliculas = []
def agregar_pelicula():
    nombre = input("Ingresa el nombre de la película: ")
    peliculas.append(nombre)
    print(f"La película '{nombre}' ha sido agregada correctamente.")
def eliminar_pelicula():
    nombre = input("Ingresa el nombre de la película a eliminar: ")
    if nombre in peliculas:
        peliculas.remove(nombre)
        print(f"La película '{nombre}' ha sido eliminada correctamente.")
    else:
        print(f"La película '{nombre}' no se encuentra en la lista.")
def actualizar_pelicula():
    nombre_actual = input("Ingresa el nombre de la película a actualizar: ")
    if nombre_actual in peliculas:
        nuevo_nombre = input("Ingresa el nuevo nombre de la película: ")
        indice = peliculas.index(nombre_actual)
        peliculas[indice] = nuevo_nombre
        print(f"La película '{nombre_actual}' ha sido actualizada a '{nuevo_nombre}'.")
    else:
        print(f"La película '{nombre_actual}' no se encuentra en la lista.")
def consultar_peliculas():
    if peliculas:
        print("Lista de películas:")
        for pelicula in peliculas:
            print("- " + pelicula)
    else:
        print("No hay películas en la lista.")
def buscar_pelicula():
    nombre = input("Ingresa el nombre de la película a buscar: ")
    if nombre in peliculas:
        print(f"La película '{nombre}' se encuentra en la lista.")
    else:
        print(f"La película '{nombre}' no se encuentra en la lista.")
def vaciar_lista():
    peliculas.clear()
    print("La lista de películas ha sido vaciada.")
def menu():
    while True:
        print("\n:::: CINEPOLIS CLON ::::")
        print(":::: Sistema de Gestión de Películas ::::")
        print("1.- Agregar")
        print("2.- Eliminar")
        print("3.- Actualizar")
        print("4.- Consultar")
        print("5.- Buscar")
        print("6.- Vaciar")
        print("7.- SALIR")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            agregar_pelicula()
        elif opcion == "2":
            eliminar_pelicula()
        elif opcion == "3":
            actualizar_pelicula()
        elif opcion == "4":
            consultar_peliculas()
        elif opcion == "5":
            buscar_pelicula()
        elif opcion == "6":
            vaciar_lista()
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
menu() 