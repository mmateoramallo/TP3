from Registro import *
import random


def mostrar_menu():
    print('-' * 25, '> Gestión de Proyectos de Software')
    print('1. Cargar Proyectos')
    print('2. Listar Proyectos')
    print('3. Actualizar Proyectos')
    print('4. Resumen por Lenguaje')
    print('5. Resumen por Año')
    print('6. Filtrar Lenguaje')
    print('7. Productividad')
    print('8. Salir')


def buscar_proyecto(x, vec):
    # Recorremos el array
    for i in range(len(vec)):
        # Corroboramos si el elemento se encuentra en la posicion sub[i] del array
        if vec[i].num_proyect == x:
            return True, vec[i]
        return False


def validar(n):
    x = int(input('Ingrese el numero del proyecto a buscar: '))
    while x < n:
        x = int(input('Ingrese el numero del proyecto a buscar: '))
    return x


def update_proyecto(vec, x):
    # Buscamos ese numero en nuestro array de registros
    se_encontro, registro_encontrado = buscar_proyecto(x, vec)
    # Corroboramos si se encontro o no
    if se_encontro:
        cad = registro_encontrado
        print(cad)


# Accedemos al


def convert_tuple_str(tuple):
    tuple_str = ''
    for i in tuple:
        tuple_str = tuple_str + i
    return tuple_str


def ordenar_titulo(vec):
    # vec_alf = []
    n = len(vec)
    # Acceder al casillero de los titulos en el vector de registros
    """
    for i in range(len(vec)):
        # Almacenar todos los titulos de los proyectos en el vector
        vec_alf.append(vec[i].titulo)
    """
    # Una vez que ya almacenamos todos los titulos en el vector lo ordenamos al vector de los titulos
    for i in range(n - 1):
        ordenado = True
        for j in range(n - i - 1):
            if vec[j].titulo > vec[j + 1].titulo:
                ordenado = False
                vec[j], vec[j + 1] = vec[j + 1], vec[j]
        if ordenado:
            break
    return vec


def mostrar_proyectos_ordenados(vec_ordenado):
    pass


def cargar_proyectos(id, lenguaje, clase=Registro):
    # Le solicitamos al usuario el titulo del proyecto
    titulo_proyecto = input('-> Ingrese el titulo del Proyecto a Registrar:')
    if titulo_proyecto == "":
        titulo_proyecto = input('-> Ingrese el titulo CORRECTAMENTE del Proyecto a Registrar: ')

    # Solicitamos fecha
    fecha_proyecto = input('-> Ingrese la fecha de actualización del Proyecto(dd-mm-yyyy): ')
    while validar_fecha(fecha_proyecto) == False:
        fecha_proyecto = input(
            '-> Ingrese la fecha de actualización del Proyecto(dd-mm-yyyy), entre los años 2000 y 2022: ')
    # Solicitamos Cantidad de lineas de codigo
    cant_lineas = int(input('-> Ingrese la cantidad de lineas de codigo del Proyecto a Registrar:'))
    if cant_lineas <= 0:
        cant_lineas = int(
            input('-> Ingrese un Valor CORRECTO en la cantidad de lineas de codigo del Proyecto a Registrar:'))

    reg = Registro(id, titulo_proyecto, fecha_proyecto, lenguaje, cant_lineas)
    return reg


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
    # print('Su opcion es:', opcion)

    while opcion != 8:
        if opcion == 1:
            print('*' * 25, 'Cargar Proyectos', '*' * 25)
            # Generamos el lenguaje aleatoriamente
            id_lenguaje = random.randint(0, 10)
            # Incrementamos el contador de id_proyecto
            id_proyecto += 1
            # LLamamos a la funcion crear registro para poder generar una instancia de nuestra clase Registro
            registro = cargar_proyectos(id_proyecto, lenguajes[id_lenguaje])
            # Lo agregamos al vector de registros
            registros_vec.append(registro)
        elif opcion == 2:
            # Ordenamos el vector de registros segun sus titulos
            registros_vec_or = ordenar_titulo(registros_vec)
            # Vemos si estan ordenados
            for i in range(len(registros_vec_or)):
                print(registros_vec_or[i])

        elif opcion == 3:
            # Le solicitamos al usuario el valor a buscar del numero del proyecto
            x = validar(0)
            update_proyecto(registros_vec, x)

        # Mostramos nuevamente el menu
        mostrar_menu()
        opcion = int(input('Ingrese su opcion: '))


principal()
