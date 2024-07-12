from conexionDB import *
#Forma que enseño el profesor: 
try:
    mycursor =  conexion.cursor()
    sql = 'INSERT INTO clientes (id, nombre, direccion, telefono) VALUES (NULL, "Juan Polainas", "Col. del valle", "618-123-4567")'

    mycursor.execute(sql)
            #Es necesario ejecutar el commit para que se actualice el sql
    conexion.commit()
except Error as e:
        print(f"Ha ocurrido un error intenta mas tarde... {e}")
else:
        print("Se creo el registro con exito")
