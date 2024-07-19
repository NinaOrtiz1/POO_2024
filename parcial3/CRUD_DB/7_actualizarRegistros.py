from conexionDB import *

try:
    micursor = conexion.cursor()
    sql = "UPDATE clientes SET direccion='Col. del UTD' where id=1"

    micursor.execute(sql)

    conexion.commit()
except:
    print(f"Ha ocurrido un error por favor intenta mas tarde...")
else:
    print(f"Se ha actualizado el registo exitosamente")
