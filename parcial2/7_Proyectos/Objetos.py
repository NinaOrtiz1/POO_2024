from Clases import *
estudiante1 = Estudiantes("Ana Torres Guzman", 20, "6121234567", "MECA", 2335679)
docente1 = Docentes("Daniel Fuentes Loera", 40, "6183335678", "TI", 123)

print("Estudiante:")
print(f"Nombre: {estudiante1.nombre}")
print(f"Edad: {estudiante1.edad}")
print(f"Teléfono: {estudiante1.tel}")
print(f"Carrera: {estudiante1.carrera}")
print(f"Matrícula: {estudiante1.matricula}")

print("\nDocente:")
print(f"Nombre: {docente1.nombre}")
print(f"Edad: {docente1.edad}")
print(f"Teléfono: {docente1.tel}")
print(f"Modalidad: {docente1.modalidad}")
print(f"Número de empleado: {docente1.num_empleado}")