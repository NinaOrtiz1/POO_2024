class Personas:
    def __init__(self, nombre, edad, tel):
        self.nombre = nombre
        self.edad = edad
        self.tel = tel
    def info_persona(self):
        pass
class Estudiantes(Personas):
    def __init__(self, nombre, edad, tel, carrera, matricula):
        super().__init__(nombre, edad, tel)
        self.carrera = carrera
        self.matricula = matricula
    def informar_carrera(self):
        pass
class Docentes(Personas):
    def __init__(self, nombre, edad, tel, modalidad, num_empleado):
        super().__init__(nombre, edad, tel)
        self.modalidad = modalidad
        self.num_empleado = num_empleado
    def informar_modalidad(self):
        pass