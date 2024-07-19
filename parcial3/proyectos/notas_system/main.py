from usuarios import usuario
from notas import nota
import getpass
from funciones import *

def menu_principal():
    while True:
        borrarPantalla()
        print("""
      .::  Menu Principal ::. 
          1.- Registro
          2.- Login
          3.- Salir 
          """)
        opcion = input("\t Elige una opción: ").upper()

        if opcion == '1' or opcion=="REGISTRO":
            borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ")
            apellidos=input("\t ¿Cuales son tus apellidos?: ")
            email=input("\t Ingresa tu email: ")
            password=getpass.getpass("\t Ingresa tu contraseña: ")
            #Agregar codigo
            obj_usuario = usuario.Usuario(nombre,apellidos,email,password)
            res = obj_usuario.registrar()
            if res:
                print(f"\n\t {nombre} {apellidos} se registro correctamente, con el email: {email} 👍")
            else:
                print(f"\n\t **Por favor intentalo nuevamente, no fue posible completar registro 👎**")
            esperarTecla()
        elif opcion == '2' or opcion=="LOGIN":
            borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ")
            password=getpass.getpass("\t Ingresa tu Contraseña: ")
            #Agregar codigo   
            res = usuario.Usuario.iniciar_sesion(email,password)
            if len(res)>0:
                menu_notas(res[0], res[1], res[2])
            else:
                print(f"\n\t Email o contraseña incorrectos... Intenta nuevamente...")
        elif opcion == '3' or opcion=="SALIR":
            print("\n\t.. ¡Gracias Bye! ...")
            break
            #exit() <- otra arternativa a "brake"
        else:
            print("\t \t Opción no válida. Intenta de nuevo.")
            tiempoEspera()

def menu_notas(usuario_id,nombre,apellidos):
    while True:
        borrarPantalla()
        print(f"\n \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        print("""
                  \n
                      .::  Menu Notas ::. 
                        1.- Crear 
                        2.- Mostrar
                        3.- Cambiar
                        4.- Eliminar
                        5.- Salir 
                  """)
        opcion = input("\t\t Elige una opción: ").upper()

        if opcion == '1' or opcion=="CREAR":
            borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo=input("\tTitulo: ")
            descripcion=input("\tDescripción: ")
            #Agregar codigo
            obj_nota = nota.Nota(usuario_id, titulo, descripcion)
            res = obj_nota
            if res:
                print(f"Se ha creado la nota {titulo} correctamente 👍")
        elif opcion == '2' or opcion=="MOSTRAR":
            borrarPantalla()
            #Agregar codigo  
            reg = nota.mostrar(usuario)
            if len(reg)>0:
                print(f"\n\f {nombre} {apellidos}, tus nostas son:")
                num_notas=1
                for fila in reg:
                    print(f"Nota: {num_notas} \n ID: {fila[1]}\n Titulo: {fila[2]} \n Fecha: {fila[4]}, \n Descripcion: {fila[3]}")
                    num_notas+=1
            else:
                print(f"No existen notas para el usuario vuelve a intentarlo 📝")
        elif opcion == '3' or opcion=="CAMBIAR":
            borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::. \n")
            id = input("\t \t ID de la nota a actualizar: ")
            titulo = input("\t Nuevo título: ")
            descripcion = input("\t Nueva descripción: ")
            #Agregar codigo
        elif opcion == '4' or opcion=="ELIMINAR":
            borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
            id = input("\t \t ID de la nota a eliminar: ")
            #Agregar codigo
        elif opcion == '5' or opcion=="Salir":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

if __name__ == "__main__":
    menu_principal()