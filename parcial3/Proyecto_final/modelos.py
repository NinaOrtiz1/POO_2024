from ConexionBd import ConexionBd

class Proveedores:
    def __init__(self, nombre_compania, nombre, correo, telefono, ciudad, id=None):
        self.id = id
        self.nombre_compania = nombre_compania
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.ciudad = ciudad

    @staticmethod
    def obtener_todos():
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM proveedores")
        proveedores = cursor.fetchall()
        cursor.close()
        conexion.close()
        return proveedores

    @staticmethod
    def obtener_por_id(id_proveedor):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM proveedores WHERE id = %s", (id_proveedor,))
        proveedor = cursor.fetchone()
        cursor.close()
        conexion.close()
        return proveedor

    def crear(self):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        query = """
            INSERT INTO proveedores (nombre_compania, nombre, correo, telefono, ciudad)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (self.nombre_compania, self.nombre, self.correo, self.telefono, self.ciudad)
        cursor.execute(query, values)
        conexion.commit()
        self.id = cursor.lastrowid
        cursor.close()
        conexion.close()
        return self.id is not None

    def actualizar(self, id_proveedor):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        try:
            query = """
                UPDATE proveedores
                SET nombre_compania = %s, nombre = %s, correo = %s, telefono = %s, ciudad = %s
                WHERE id = %s
            """
            values = (self.nombre_compania, self.nombre, self.correo, self.telefono, self.ciudad, id_proveedor)
            cursor.execute(query, values)
            conexion.commit()
            if cursor.rowcount == 0:
                print("No se encontró el registro con el ID proporcionado.")
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def eliminar(id_proveedor):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        try:
            query = "DELETE FROM proveedores WHERE id = %s"
            cursor.execute(query, (id_proveedor,))
            conexion.commit()
            if cursor.rowcount == 0:
                print("No se encontró el registro con el ID proporcionado.")
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar: {e}")
            return False
        finally:
            cursor.close()
            conexion.close()

class Productos:
    def __init__(self, nombre, precio, categoria, id=None):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    @staticmethod
    def obtener_bebidaspreparadas():
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos WHERE categoria_id = 4")
        productos = cursor.fetchall()
        cursor.close()
        conexion.close()
        return productos
    
    @staticmethod
    def obtener_botanas():
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos WHERE categoria_id = 2")
        productos = cursor.fetchall()
        cursor.close()
        conexion.close()
        return productos
    
    @staticmethod
    def obtener_cervezas():
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos WHERE categoria_id = 1 ")
        productos = cursor.fetchall()
        cursor.close()
        conexion.close()
        return productos

    @staticmethod
    def obtener_servicios():
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos WHERE categoria_id = 3")
        productos = cursor.fetchall()
        cursor.close()
        conexion.close()
        return productos

    def crear(self):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        query = """
            INSERT INTO productos (nombre, precio, categoria_id)
            VALUES (%s, %s, %s)
        """
        values = (self.nombre, self.precio, self.categoria)
        cursor.execute(query, values)
        conexion.commit()
        cursor.close()
        conexion.close()
        return True

    def actualizar(self, id_producto):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        try:
            query = """
                UPDATE productos
                SET nombre = %s, precio = %s
                WHERE id = %s
            """
            values = (self.nombre, self.precio, id_producto)
            cursor.execute(query, values)
            conexion.commit()
            if cursor.rowcount == 0:
                print("No se encontró el registro con el ID proporcionado.")
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def eliminar(id_producto):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        try:
            query = "DELETE FROM productos WHERE id = %s"
            cursor.execute(query, (id_producto,))
            conexion.commit()
            if cursor.rowcount == 0:
                print("No se encontró el registro con el ID proporcionado.")
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar: {e}")
            return False
        finally:
            cursor.close()
            conexion.close()
            
class Ventas:
    def __init__(self, fecha, id_cliente, total, id=None):
        self.id = id
        self.fecha = fecha
        self.id_cliente = id_cliente
        self.total = total

    @staticmethod
    def obtener_todos():
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ventas")
        ventas = cursor.fetchall()
        cursor.close()
        conexion.close()
        return ventas

    def crear(self):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        query = """
            INSERT INTO ventas (fecha, id_cliente, total)
            VALUES (%s, %s, %s)
        """
        values = (self.fecha, self.id_cliente, self.total)
        cursor.execute(query, values)
        conexion.commit()
        self.id = cursor.lastrowid
        cursor.close()
        conexion.close()
        return self.id is not None

    def actualizar(self, id_venta):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        try:
            query = """
                UPDATE ventas
                SET fecha = %s, id_cliente = %s, total = %s
                WHERE id = %s
            """
            values = (self.fecha, self.id_cliente, self.total, id_venta)
            cursor.execute(query, values)
            conexion.commit()
            if cursor.rowcount == 0:
                print("No se encontró el registro con el ID proporcionado.")
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False
        finally:
            cursor.close()
            conexion.close()
          