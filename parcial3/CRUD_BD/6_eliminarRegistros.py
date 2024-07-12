from conexionDB import *


try:
        micursor = conexion.cursor()
        sql = "DELETE FROM clientes WHERE id = 1"

        micursor.execute(sql)

        conexion.commit()
except:
        print(f"Ha ocurrido un error por favor intenta mas tarde...")
else:
        print(f"Se ha eliminado el registo exitosamente")