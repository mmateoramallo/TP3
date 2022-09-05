class Registro:

    def __init__(self, num_proyect, titulo, fecha_actualizacion, lenguaje, cant_lineas):
        self.num_proyect = num_proyect
        self.titulo = titulo
        self.fecha_actualizacion = fecha_actualizacion
        self.lenguaje = lenguaje
        self.cant_lineas = cant_lineas
    
    def __str__(self) -> str:
        return f"Numero De Proyecto {self.num_proyect}, Titulo: {self.titulo}, Fecha De Actualiazcion: {self.fecha_actualizacion}, Lenguaje: {self.lenguaje}, Cantidad de lineas: {self.cant_lineas}"



    def mostrar_descripcion(registro):
        descr = ''
        descr += '{:>30}'.format('Nombre Proyecto:' + (registro.titulo))
        descr += '{:>30}'.format('ID del Proyecto:' + (registro.num_proyect))
        descr += '{:>30}'.format('Fecha De Actualizacion del Proyecto:' + (registro.fecha_actualizacion))
        descr += '{:>30}'.format('Cantidad de Lineas del Proyecto:' + str(registro.cant_lineas))
        descr += '{:>30}'.format('Lenguaje:' + (registro.lenguaje))
        return descr
