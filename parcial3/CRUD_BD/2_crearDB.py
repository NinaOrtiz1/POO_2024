import mysql.connector 
from mysql.connector import Error 

#Forma que enseño el profesor

#Conexion a base de datos mediante una funcion 
def conexion():
    try:
        conexion = mysql.connector.connect(
            host ='localhost',
            user= 'root',
            password='',
            database=''
        )

        #Crear un objeto de tipo cursor para ejecutar SQL
        cursor = conexion.cursor()
        db_name = input("Ingresa el nombre de la BD: ")
        sql = f'CREATE DATABASE {db_name}'
        cursor.execute(sql)
    

    except Error as e:
        print(f"Error: {e}")
        print(f"Tipo de error: {type(e).__name__}")
        print(f"Ocurrio un error intenta nuevamente...")
    else:
        print("Se creo la base de datos exitosamente")
        sql = "SHOW DATABASES"
        cursor.execute(sql)
        for x in cursor:
            print(x)
    finally:
        cursor.close()
        conexion.close()

conexion()


#Mi forma 
class ConexionDB: 
    def get_conexion(): 
        try:
            conex = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='',
            )

            if conex.is_connected():
                print("Se ha conectado correctamente a MYSQL")
                return conex
        except Error as e:
            print(f"Ha ocurrido un error: {e}")


class CrearTabla:
    def crearDB():
        try:
            nombre = input("Que nombre le quieres dar a la DB: ")
            sql = f"CREATE DATABASE {nombre}"
            conex = ConexionDB.get_conexion()
            if conex:
                cursor = conex.cursor()
                cursor.execute(sql)
                print(f"La BD {nombre} ha sido creada correctamente")
        except Error as e:
            print(f"Ha ocurrido un error: {e}")
        finally:
            cursor.close()
            conex.close()