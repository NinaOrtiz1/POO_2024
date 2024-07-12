from conexionDB import *

#Forma que enseño el profesor: 

try:
    mycursor = conexion.cursor()
    sql = 'CREATE TABLE clientes(id INT PRIMARY KEY AUTO_INCREMENT, nombre VARCHAR(60), Direccion VARCHAR(120), telefono VARCHAR (12))'
    mycursor.execute(sql)
except:
    print("Ha ocurrido un error intenta mas tarde...")
else:
    print("Se creo la tabla con exito")
finally:
    mycursor.close()










#Mi forma 

class CrearTabla():

    def obteneratributos():
        while True:
            atributos = []
            nombre = input("Ingresa el nombre del atributo (enter para terminar): ")
            if nombre == "":
                break
            tipo = input(f"Ingresa el tipo para {nombre}: ")
            pk = input(f"¿Es una PRIMARY KEY? (s/n)").lower() == 's'
            fk = input(f"¿Es una FOREIGN KEY? (s/n)").lower() == 's'

            atributo_def = f"{nombre} {tipo}"
            if pk:
                atributo_def += " PRIMARY KEY"
            atributos.append(atributo_def)
            if fk:
                referencia = input("Ingresa la referencia tabla(atributo): ")
                atributos.append(f"FOREIGN KEY ({nombre}) REFERENCES {referencia}")
        print(atributos)
        return ', '.join(atributos)
            

    def creartabla(atributos):
        try:
            tb_name = input("Que nombre quieres darle a la tabla: ")
            sql = f"CREATE TABLE {tb_name} ({atributos})"
            conex = ConnectionDB.get_conexion()
            if conex:
                cursor = conex.cursor()
                cursor.execute(sql)
                print(f"Se ha creado la tabla {tb_name} CORRECTAMENTE")
        except Error as e:
            print(f"Ha ocurrido un error: {e}")

    atributos = obteneratributos()
    creartabla(atributos)