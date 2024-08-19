import tkinter as tk
from tkinter import messagebox,ttk
from modelos import Productos, Ventas
from usuarios import Usuarios
class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("The Pub")
        self.geometry("1920x1080")
        self.mostrar_menu_inicio()

    def mostrar_menu_inicio(self):
        self.limpiar_pantalla()
        tk.Label(self, text="..::THE PUB::..", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Registrarse", command=self.mostrar_registro).pack(pady=10)
        tk.Button(self, text="Iniciar sesión", command=self.mostrar_login).pack(pady=10)
        tk.Button(self, text="Salir del sistema", command=self.quit).pack(pady=10)

    def mostrar_login(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Inicio de sesión", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="Correo:").pack()
        self.correo_entry = tk.Entry(self)
        self.correo_entry.pack(pady=5)
        tk.Label(self, text="Contraseña:").pack()
        self.contrasena_entry = tk.Entry(self, show='*')
        self.contrasena_entry.pack(pady=5)
        tk.Button(self, text="Iniciar sesión", command=self.login).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_inicio).pack(pady=10)

    def login(self):
        correo = self.correo_entry.get()
        contrasena = self.contrasena_entry.get()
        usuario = Usuarios.verificar_credenciales(correo, contrasena)
        if usuario:
                self.mostrar_menu_empleado()
        else:
            messagebox.showerror("Error", "Credenciales inválidas.")

    def mostrar_registro(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Registro de Usuario", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=5)
        tk.Label(self, text="Correo:").pack()
        self.correo_entry = tk.Entry(self)
        self.correo_entry.pack(pady=5)
        tk.Label(self, text="Contraseña:").pack()
        self.contrasena_entry = tk.Entry(self, show='*')
        self.contrasena_entry.pack(pady=5)
        tk.Button(self, text="Registrar", command=self.registrar_usuario).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_inicio).pack(pady=10)

    def registrar_usuario(self):
        nombre = self.nombre_entry.get()
        correo = self.correo_entry.get()
        contrasena = self.contrasena_entry.get()
        nuevo_usuario = Usuarios(nombre, correo, contrasena )
        if nuevo_usuario.crear():
            messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
            self.mostrar_menu_inicio()
        else:
            messagebox.showerror("Error", "No se pudo registrar el usuario.")

    def mostrar_menu_empleado(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Menú Empleado", font=("Arial", 14)).pack(pady=20)
        tk.Button(self, text="Gestión de Productos", command=self.mostrar_menu_productos).pack(pady=10)
        tk.Button(self, text="Gestión de Ventas", command=self.mostrar_menu_ventas).pack(pady=10)
        tk.Button(self, text="Cerrar sesión", command=self.mostrar_menu_inicio).pack(pady=10)

    def mostrar_menu_productos(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Gestión de Productos", font=("Arial", 14)).pack(pady=20)
        tk.Button(self, text="Ver Bebidas", command=self.ver_bebidas).pack(pady=10)
        tk.Button(self, text="Ver Botanas", command=self.ver_botanas).pack(pady=10)
        tk.Button(self, text="Ver Cervezas", command=self.ver_cervezas).pack(pady=10)
        tk.Button(self, text="Ver Servicios", command=self.ver_servecios).pack(pady=10)
        tk.Button(self, text="Añadir Producto", command=self.anadir_producto).pack(pady=10)
        tk.Button(self, text="Actualizar Producto", command=self.actualizar_producto).pack(pady=10)
        tk.Button(self, text="Eliminar Producto", command=self.eliminar_producto).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_empleado).pack(pady=10)

    def mostrar_menu_ventas(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Gestión de Ventas", font=("Arial", 14)).pack(pady=20)
        tk.Button(self, text="Ver Ventas", command=self.ver_ventas).pack(pady=10)
        tk.Button(self, text="Añadir Venta", command=self.anadir_venta).pack(pady=10)
        tk.Button(self, text="Actualizar Venta", command=self.actualizar_venta).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_empleado).pack(pady=10)

    def ver_bebidas(self):
        self.limpiar_pantalla()
        productos = Productos.obtener_bebidaspreparadas()
        tk.Label(self, text="Bebidas", font=("Arial", 14)).pack(pady=20)
        tree = ttk.Treeview(self, columns=("ID", "Nombre", "Precio"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Precio", text="Precio")
        tree.pack(expand=True, fill='both')
        for producto in productos:
            tree.insert("", tk.END, values=(producto["id"], producto["nombre"], producto["precio"]))
        tk.Button(self, text="Regresar", command=self.mostrar_menu_productos).pack(pady=10)

    def ver_botanas(self):
        self.limpiar_pantalla()
        productos = Productos.obtener_botanas()
        tk.Label(self, text="Botanas", font=("Arial", 14)).pack(pady=20)
        tree = ttk.Treeview(self, columns=("ID", "Nombre", "Precio"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Precio", text="Precio")
        tree.pack(expand=True, fill='both')
        for producto in productos:
            tree.insert("", tk.END, values=(producto["id"], producto["nombre"], producto["precio"]))
        tk.Button(self, text="Regresar", command=self.mostrar_menu_productos).pack(pady=10)

    def ver_cervezas(self):
        self.limpiar_pantalla()
        productos = Productos.obtener_cervezas()
        tk.Label(self, text="Cervezas", font=("Arial", 14)).pack(pady=20)
        tree = ttk.Treeview(self, columns=("ID", "Nombre", "Precio"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Precio", text="Precio")
        tree.pack(expand=True, fill='both')
        for producto in productos:
            tree.insert("", tk.END, values=(producto["id"], producto["nombre"], producto["precio"]))
        tk.Button(self, text="Regresar", command=self.mostrar_menu_productos).pack(pady=10)

    def ver_servecios(self):
        self.limpiar_pantalla()
        productos = Productos.obtener_servicios()
        tk.Label(self, text="Servicios", font=("Arial", 14)).pack(pady=20)
        tree = ttk.Treeview(self, columns=("ID", "Nombre", "Precio"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Precio", text="Precio")
        tree.pack(expand=True, fill='both')
        for producto in productos:
            tree.insert("", tk.END, values=(producto["id"], producto["nombre"], producto["precio"]))
        tk.Button(self, text="Regresar", command=self.mostrar_menu_productos).pack(pady=10)

    def ver_ventas(self):
        self.limpiar_pantalla()
        ventas = Ventas.obtener_todos()
        tk.Label(self, text="Ventas", font=("Arial", 14)).pack(pady=20)
        tree = ttk.Treeview(self, columns=("ID", "Fecha", "ID Cliente", "Total"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Fecha", text="Fecha")
        tree.heading("ID Cliente", text="ID Cliente")
        tree.heading("Total", text="Total")
        tree.pack(expand=True, fill='both')
        for venta in ventas:
            tree.insert("", tk.END, values=(venta["id"], venta["fecha"], venta["id_cliente"], venta["total"]))
        tk.Button(self, text="Regresar", command=self.mostrar_menu_empleado).pack(pady=10)

    def anadir_producto(self):
        self.limpiar_pantalla()
        menu_bar = tk.Menu()
        tk.Label(self, text="Añadir Producto", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=5)
        tk.Label(self, text="Precio:").pack()
        self.precio_entry = tk.Entry(self)
        self.precio_entry.pack(pady=5)
        tk.Label(self, text="Categoria:").pack()
        self.categoria_entry = tk.Entry(self)
        self.categoria_entry.pack(pady=5)
        tk.Button(self, text="Añadir", command=self.crear_producto).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_productos).pack(pady=10)

    def crear_producto(self):
        nombre = self.nombre_entry.get()
        precio = float(self.precio_entry.get())
        categoria = self.categoria_entry.get()
        producto = Productos(nombre, precio, categoria)
        if producto.crear():
            messagebox.showinfo("Éxito", "Producto añadido correctamente.")
            self.mostrar_menu_productos()
        else:
            messagebox.showerror("Error", "No se pudo añadir el producto.")

    def anadir_venta(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Añadir Venta", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="Fecha:").pack()
        self.fecha_entry = tk.Entry(self)
        self.fecha_entry.pack(pady=5)
        tk.Label(self, text="ID Cliente:").pack()
        self.id_cliente_entry = tk.Entry(self)
        self.id_cliente_entry.pack(pady=5)
        tk.Label(self, text="Total:").pack()
        self.total_entry = tk.Entry(self)
        self.total_entry.pack(pady=5)
        tk.Button(self, text="Añadir", command=self.crear_venta).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_ventas).pack(pady=10)

    def crear_venta(self):
        fecha = self.fecha_entry.get()
        id_cliente = int(self.id_cliente_entry.get())
        total = float(self.total_entry.get())
        venta = Ventas(fecha, id_cliente, total)
        if venta.crear():
            messagebox.showinfo("Éxito", "Venta añadida correctamente.")
            self.mostrar_menu_ventas()
        else:
            messagebox.showerror("Error", "No se pudo añadir la venta.")


    def actualizar_producto(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Actualizar Producto", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="ID Producto:").pack()
        self.id_producto_entry = tk.Entry(self)
        self.id_producto_entry.pack(pady=5)
        tk.Label(self, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=5)
        tk.Label(self, text="Precio:").pack()
        self.precio_entry = tk.Entry(self)
        self.precio_entry.pack(pady=5)
        tk.Button(self, text="Actualizar", command=self.actualizar_producto_db).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_productos).pack(pady=10)

    def actualizar_producto_db(self):
        id_producto = int(self.id_producto_entry.get())
        nombre = self.nombre_entry.get()
        precio = float(self.precio_entry.get())
        categoria = ""
        producto = Productos(nombre, precio,categoria)
        if producto.actualizar(id_producto):
            messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
            self.mostrar_menu_productos()
        else:
            messagebox.showerror("Error", "No se pudo actualizar el producto.")

    def actualizar_venta(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Actualizar Venta", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="ID Venta:").pack()
        self.id_venta_entry = tk.Entry(self)
        self.id_venta_entry.pack(pady=5)
        tk.Label(self, text="Fecha:").pack()
        self.fecha_entry = tk.Entry(self)
        self.fecha_entry.pack(pady=5)
        tk.Label(self, text="ID Cliente:").pack()
        self.id_cliente_entry = tk.Entry(self)
        self.id_cliente_entry.pack(pady=5)
        tk.Label(self, text="Total:").pack()
        self.total_entry = tk.Entry(self)
        self.total_entry.pack(pady=5)
        tk.Button(self, text="Actualizar", command=self.actualizar_venta_db).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_ventas).pack(pady=10)

    def actualizar_venta_db(self):
        id_venta = int(self.id_venta_entry.get())
        fecha = self.fecha_entry.get()
        id_cliente = int(self.id_cliente_entry.get())
        total = float(self.total_entry.get())
        venta = Ventas(fecha, id_cliente, total)
        if venta.actualizar(id_venta):
            messagebox.showinfo("Éxito", "Venta actualizada correctamente.")
            self.mostrar_menu_ventas()
        else:
            messagebox.showinfo("Éxito", "Venta actualizada correctamente.")

    def eliminar_producto(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Eliminar Producto", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="ID Producto:").pack()
        self.id_producto_entry = tk.Entry(self)
        self.id_producto_entry.pack(pady=5)
        tk.Button(self, text="Eliminar", command=self.eliminar_producto_db).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_productos).pack(pady=10)

    def eliminar_producto_db(self):
        id_producto = int(self.id_producto_entry.get())
        if Productos.eliminar(id_producto):
            messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
            self.mostrar_menu_productos()
        else:
            messagebox.showerror("Error", "No se pudo eliminar el producto.")

    def limpiar_pantalla(self):
        for widget in self.winfo_children():
            widget.destroy()

# Ejecución de la aplicación
if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
