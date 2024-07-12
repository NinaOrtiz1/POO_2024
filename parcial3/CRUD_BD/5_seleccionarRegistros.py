from conexionDB import *


try:
    micursor = conexion.cursor()
    sql = 'SELECT * FROM clientes'
    
    micursor.execute(sql)

    resultado = micursor.fetchall()
    for fila in resultado:
        print(f"ID:{fila[0]} \nNombre: {fila[1]} \nDireccion: {fila[2]} \nTelefono: {fila[3]}")
except:
    print("Ha ocurrdio un error")
else:
    print("Registros consultados correctamente")
