from Registro import *
import random


def cargar_proyectos():
    print('-' * 25, 'Cargar Proyectos', '-' * 25)


def mostrar_menu():
    vector_menu = [
        print('-' * 25, '> Gestión de Proyectos de Software'),
        print('1. Cargar Proyectos'),
        print('2. Listar Proyectos'),
        print('3. Actualizar Proyectos'),
        print('4. Resumen por Lenguaje'),
        print('5. Resumen por Año'),
        print('6. Filtrar Lenguaje'),
        print('7. Productividad'),
        print('8. Salir')
    ]


def convert_tuple_str(tuple):
    tuple_str = ''
    for i in tuple:
        tuple_str = tuple_str + i
    return tuple_str


def crear_registros(id, titulo, fecha_actualizacion, lenguaje, lineas_codigo):
    pass


def validar_fecha(fecha):
    year = fecha[6], fecha[7], fecha[8], fecha[9]
    # Convertir tupla a string
    year_str = convert_tuple_str(year)
    # Convertir de strig a int
    year = int(year_str)
    # Comenzamos la validacion
    if 2000 <= year <= 2022:
        return True
    else:
        return False


def principal():
    # Mostrar menu
    mostrar_menu()
    opcion = int(input('Ingrese su opcion: '))

    # Variables
    id_proyecto = 1
    lenguajes = ('Python', 'Java', 'C++', 'Javascript', 'Shell', 'HTML', 'Ruby', 'Swift', 'C#', 'VB', 'Go')
    registros_vec = []
    print('Su opcion es:', opcion)

    while opcion != 8:
        if opcion == 1:
            print('*' * 25, 'Cargar Proyectos', '*' * 25)
            leng_elegido = random.choice(lenguajes)
            titulo_proyecto = input('-> Ingrese el titulo del Proyecto a Registrar:')
            if titulo_proyecto == "":
                titulo_proyecto = input('-> Ingrese el titulo CORRECTAMENTE del Proyecto a Registrar: ')

            fecha_proyecto = input('-> Ingrese la fecha de actualización del Proyecto(dd-mm-yyyy): ')
            while validar_fecha(fecha_proyecto) == False:
                fecha_proyecto = input(
                    '-> Ingrese la fecha de actualización del Proyecto(dd-mm-yyyy), entre los años 2000 y 2022: ')

            cant_lineas = int(input('-> Ingrese la cantidad de lineas de codigo del Proyecto a Registrar:'))
            if cant_lineas <= 0:
                cant_lineas = int(
                    input('-> Ingrese un Valor CORRECTO en la cantidad de lineas de codigo del Proyecto a Registrar:'))

            # Generamos la instancia de la clase Registro
            registro = Registro(id_proyecto, titulo_proyecto, fecha_proyecto, leng_elegido, cant_lineas)

            #Incrementamos el contador de id_proyecto
            id_proyecto += 1

            #Lo agregamos al vector de registros
            registros_vec.append(registro)

        opcion = int(input('Ingrese su opcion: '))


principal()
