import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os 

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_name = os.getenv("DB_NAME")

try:
    connec = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_pass,
        database=db_name
    )

    #Se crea un objeto de tipo cursor con un parametro que permite reutilizar el mismo objeto
    cursor = connec.cursor(buffered=True)
except Error as e:
            print("Ha ocurrido un error en la conexion de base de datos...")
            print(f"Error: {e}")
        