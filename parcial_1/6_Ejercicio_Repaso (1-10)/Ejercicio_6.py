"""
6.- Mostrar todas las tablas del 1 al 10. 
Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10
"""

for i in range(1,11):
    print("-----------------------")
    print(f"Tabla del {i}")
    print("-----------------------")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")