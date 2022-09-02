class Registro:

    def __init__(self, num_proyect, titulo, fecha_actualizacion, lenguaje, cant_lineas):
        self.num_proyect = num_proyect
        self.titulo = titulo
        self.fecha_actualizacion = fecha_actualizacion
        self.lenguaje = lenguaje
        self.cant_lineas = cant_lineas

    def __str__(self):
        return 'Proyecto Numero: ', self.num_proyect, ' Titulo:', self.titulo, 'Fecha de Actualizacion:', self.fecha_actualizacion, 'tiene una cantidad de lineas de:', self.cant_lineas, 'lineas', 'y se desarrollo en el lenguaje:', self.lenguaje
    # return f"Registro: Nombre {self.titulo}, Numero :{self.num_proyect}, Fecha: {self.fecha_actualizacion}, Lenguaje:{self.lenguaje},  Lineas {self.cant_lineas}"

    def mostrar_descripcion(self):
        descr = ''
        descr += '{:}'.format('Nombre Proyecto:' + (self.titulo))
        descr += '{:}'.format('ID del Proyecto:' + (self.num_proyect))
        descr += '{:}'.format('Fecha De Actualizacion del Proyecto:' + (self.fecha_actualizacion))
        descr += '{:}'.format('Cantidad de Lineas del Proyecto:' +str(self.cant_lineas))
        descr += '{:}'.format('Lenguaje:' +(self.lenguaje))
        return descr