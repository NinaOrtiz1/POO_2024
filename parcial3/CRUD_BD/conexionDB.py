import mysql.connector 
from mysql.connector import Error 


#Conexion a base de datos mediante una funcion 
def conexion():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="roor",
            password="",
            database="db_python"
        )
    except Error as e:
        print(f"Ocurrio un error intenta nuevamente...")




#Mi forma
class ConnectionDB: 
    def get_conexion(): 
        try:
            conex = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='db_python',
            )
        except Error as e:
            print(f"Error: {e}")
            print(f"Tipo de error: {type(e).__name__}")
            print(f"Ocurrio un error intenta nuevamente...")