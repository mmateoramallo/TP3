class Registro:

    def __init__(self, num_proyect, titulo, fecha_actualizacion, lenguaje, cant_lineas):
        self.num_proyect = num_proyect
        self.titulo = titulo
        self.fecha_actualizacion = fecha_actualizacion
        self.lenguaje = lenguaje
        self.cant_lineas = cant_lineas

    def __str__(self):
        return f"Registro: Nombre {self.titulo}, Numero :{self.num_proyect}, Fecha: {self.fecha_actualizacion}, Lenguaje:{self.lenguaje},  Lineas {self.cant_lineas}"
