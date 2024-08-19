import os

clientes = []
autos = []

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def iniciar_sesion():
    correo = input("Ingrese su correo electrónico: ")
    contraseña = input("Ingrese su contraseña: ")
    if correo == "naidelynortiz@gmail.com" and contraseña == "naidelyn":
        print("Inicio de sesión exitoso.\n")
        return True
    else:
        print("Correo o contraseña incorrectos.\n")
        return False

def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    ciudad = input("Ingrese la ciudad del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    cliente = {
        "nombre": nombre,
        "direccion": direccion,
        "ciudad": ciudad,
        "telefono": telefono
    }
    clientes.append(cliente)
    print("Cliente agregado exitosamente.\n")

def leer_clientes():
    if not clientes:
        print("No hay clientes registrados.\n")
    else:
        print("Lista de Clientes:\n")
        for idx, cliente in enumerate(clientes, start=1):
            print(f"{idx}. Nombre: {cliente['nombre']}, Dirección: {cliente['direccion']}, Ciudad: {cliente['ciudad']}, Teléfono: {cliente['telefono']}")
        print()

def actualizar_cliente():
    leer_clientes()
    if clientes:
        indice = int(input("Ingrese el número del cliente a actualizar: ")) - 1
        if 0 <= indice < len(clientes):
            clientes[indice]['nombre'] = input("Ingrese el nuevo nombre: ")
            clientes[indice]['direccion'] = input("Ingrese la nueva dirección: ")
            clientes[indice]['ciudad'] = input("Ingrese la nueva ciudad: ")
            clientes[indice]['telefono'] = input("Ingrese el nuevo teléfono: ")
            print("Cliente actualizado exitosamente.\n")
        else:
            print("Índice inválido.\n")

def eliminar_cliente():
    leer_clientes()
    if clientes:
        indice = int(input("Ingrese el número del cliente a eliminar: ")) - 1
        if 0 <= indice < len(clientes):
            clientes.pop(indice)
            print("Cliente eliminado exitosamente.\n")
        else:
            print("Índice inválido.\n")

def menu():
    while True:
        limpiar_pantalla()
        print("Gestión de Clientes y Autos")
        print("1. Crear Cliente")
        print("2. Leer Clientes")
        print("3. Actualizar Cliente")
        print("4. Eliminar Cliente")
        print("5. Limpiar Pantalla")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crear_cliente()
        elif opcion == '2':
            leer_clientes()
        elif opcion == '3':
            actualizar_cliente()
        elif opcion == '4':
            eliminar_cliente()
        elif opcion == '5':
            limpiar_pantalla()
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, por favor intente de nuevo.\n")

if __name__ == "__main__":
    if iniciar_sesion():
        menu()
    else:
        print("Acceso denegado.")