from Registro import *
import random


# Defino una semilla para pruebas
# random.seed(21)


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


def cargar_proyectos(vec, n):
    # Verificar que no se repitan los numeros de proyectos
    long = len(vec)
    if long != 0:
        num_id = long + 1
    else:
        num_id = 1
    titulos = (
        'Mario', 'BloodBorne', 'AlphaNum', 'Valorant', 'Doom', 'Metro', 'Calculadora', 'Administrador De Archivos',
        'IDE',
        'RDR2', 'RE2', 'Bioshock', 'Redes Neuronales')
    lenguajes = ('Python', 'Java', 'C++', 'Javascript', 'Shell', 'HTML', 'Ruby', 'Swift', 'C#', 'VB', 'Go')
    # Recorro el range n y voy agregando los datos generados al vector
    for i in range(n):
        # Genero los datos
        titulo = random.choice(titulos)
        dia = random.randint(1, 30)
        # Veo si es un numero entre el 1-9 el dia
        if 1 <= dia <= 9:
            dia = '0' + str(dia)
        mes = random.randint(1, 12)
        # Veo si es un numero entre el 1-9 el mes
        if 1 <= mes <= 9:
            mes = '0' + str(mes)
        # Para generar la fecha lo que hacemos es generar en tres partes, la tupla correspondiente a dia-mes-año. Y al generar el año en random.randint, nos evitamos la validacion
        year = random.randint(2000, 2022)
        # Fecha
        fecha = str(dia) + '-' + str(mes) + '-' + str(year)
        # Lineas de codigo
        cant_lineas = random.randint(100, 10000)
        # Lenguaje

        lenguaje = random.choice(lenguajes)
        # lenguaje = random.randint(1,10)

        # Generamos la instancia del registro
        proyecto = Registro(num_id, titulo, fecha, lenguaje, cant_lineas)
        # Incrementamos el contador del numero de proyecto para que este no se repita cada vez que cargamos un proyecto
        num_id += 1
        # Agregamos la instancia del registro al vector
        vec.append(proyecto)


def sort_proyectos(vec):
    n = len(vec)
    for i in range(n - 1):
        ordenado = True
        for j in range(n - i - 1):
            if vec[j].titulo > vec[j + 1].titulo:
                ordenado = False
                vec[j], vec[j + 1] = vec[j + 1], vec[j]
        if ordenado:
            break
    return vec


def list_proyectos(vec):
    # Recorro el arreglo
    for i in vec:
        print(i)


def validar_fecha():
    # Solicita al usuario y ahi mismo la valida para poder retornarla correctamente
    date = input('Ingrese la fecha a Actualizar del Proyecto en formato dd-mm-yyyy: ')
    # Vamos a validar que el dia ingresado, mes, y año sean correctos
    dia = date[0] + date[1]
    mes = date[3] + date[4]
    year = date[6] + date[7] + date[8] + date[9]
    # Convierto a int
    dia = int(dia)
    mes = int(mes)
    year = int(year)
    # Verifico
    while not ((1 <= dia <= 30) and (1 <= mes <= 12) and (2000 <= year <= 2022)):
        date = input('Ingrese la fecha CORRECTAMENTE!! en formato dd-mm-yyyy: ')
        # Volvemos extraer los datos en cadena
        dia = date[0] + date[1]
        mes = date[3] + date[4]
        year = date[6] + date[7] + date[8] + date[9]
        # Convierto a int
        dia = int(dia)
        mes = int(mes)
        year = int(year)
    return date


def mod_lineas_codigo():
    cant_lineas = int(input('Ingrese la cantidad de lineas de codigo del proyecto: '))
    while cant_lineas <= 0:
        cant_lineas = int(input('Ingrese la cantidad de lineas de codigo del proyecto: '))

    return cant_lineas


def search_proyect(x, vec):
    pos = -1
    existe = False
    # Recorro el arreglo en busca del registro
    for i in range(len(vec)):
        # Consulto si el numero de proyecto del vector i es igual al numero brindado por el usuario
        if vec[i].num_proyect == x:
            # Prendo la bandera
            existe = True
            # Guardo su posicion
            pos = i
            # Se debe modificar su fecha
            fecha = validar_fecha()
            # Modificar cantidad de lineas de codigo
            cant_lineas = mod_lineas_codigo()
            # Accedemos al registro encontrado y lo modificamos
            vec[pos].fecha_actualizacion = fecha
            vec[pos].cant_lineas = cant_lineas
            # Mostramos el registro modificado
            print(vec[i])
    if existe == False:
        print('-' * 10, '> El Registro con el numero de proyecto', x, 'no se ha encontrado')

    # Reinit bandera
    existe = False


def buscar_pos_leng(vec):
    pos = -1
    lenguaje_reg = ""
    lenguajes = ('Python', 'Java', 'C++', 'Javascript', 'Shell', 'HTML', 'Ruby', 'Swift', 'C#', 'VB', 'Go')
    for i in range(len(vec)):
        # Que lenguaje es; guardar posicion del lenguaje del registro
        for j in range(len(lenguajes)):
            lenguaje_reg = vec[i].lenguaje
            # Chequeo
            if lenguaje_reg == lenguajes[j]:
                pos = j

    return j


def summary_lenguaje(vec):
    pos = -1
    leng = ""
    lenguajes = ('Python', 'Java', 'C++', 'Javascript', 'Shell', 'HTML', 'Ruby', 'Swift', 'C#', 'VB', 'Go')
    # Creamos el vector acumulador con 11 casillas, una por cada lenguaje
    vec_ac = [0] * 11
    # Recorremos el vector de registro
    for i in vec:
        # Guardo el lenguaje del registro
        leng = i.lenguaje
        # Busco la posicion del lenguaje en la tupla
        for l in range(len(lenguajes)):
            if leng == lenguajes[l]:
                vec_ac[l] += i.cant_lineas
    return vec_ac


def summary_year(vec):
    vec_cont = [0] * 23
    # Recorremos el arreglo
    for i in vec:
        year = i.fecha_actualizacion
        year = year[6] + year[7] + year[8] + year[9]
        year = int(year)
        # Accedemos a la casilla correspondiente al year menos 2000, para contar el proyecto
        vec_cont[year - 2000] += 1
    return vec_cont


def filtrar_lenguaje(vec, leng):
    vec_ln = []
    for i in range(len(vec)):
        # Veo si el lenguaje dle registro que estamos iterando en este momento, es igual al lenguaje que me brindo el usuario por teclado
        if vec[i].lenguaje == leng:
            vec_ln.append(vec[i])
    # En este punto tenemos todo el vector con el lenguaje especifico, y lo ordenaremos
    n = len(vec_ln)
    for i in range(n - 1):
        ordenado = True
        for j in range(n - i - 1):
            if vec_ln[j].num_proyect > vec_ln[j + 1].num_proyect:
                ordenado = False
                vec_ln[j], vec_ln[j + 1] = vec_ln[j + 1], vec_ln[j]
        if ordenado:
            break
    # Recorro el vector para mostrarlo como quedo filtrado
    for v in vec_ln:
        print(v)


def productividad(vec_cont):
    mayor = 0
    pos = -1
    for i in range(len(vec_cont)):
        if i == 0:
            mayor = vec_cont[i]
        # Busco El mayor
        if vec_cont[i] > mayor:
            mayor = vec_cont[i]
            pos = i
    print('*' * 11, 'Años con Mayor Cantidad De Proyectos actualizados', '*' * 11)
    print('*' * 11, 'Cantidad de proyectos actualizados:', mayor, ' en el año', str(pos + 2000), '*' * 11)
    # Recorro nuevamente en busqueda de si existen otros mayores
    for j in range(len(vec_cont)):
        if vec_cont[j] == mayor and pos != j:
            print('*' * 11, 'Cantidad de proyectos actualizados:', vec_cont[j], ' en el año', str(j + 2000), '*' * 11)


def principal():
    # Variables
    vec_proyectos = []

    # Mostramos el menu
    mostrar_menu()

    print()
    print()

    op = int(input('Ingrese su opcion: '))
    print()

    lenguajes = ('Python', 'Java', 'C++', 'Javascript', 'Shell', 'HTML', 'Ruby', 'Swift', 'C#', 'VB', 'Go')

    # Consultamos op
    while op != 8:
        if op == 1:
            # Le solicitamos al usuario la cantidad de proyectos a registrar
            n = int(input('-------> Ingrese la cantidad de proyectos a registrar: '))
            cargar_proyectos(vec_proyectos, n)

            print('*' * 21, 'Proyectos Generados', '*' * 21)

            # Muestra de Prouectos para testear ->>>> Eliminar en la entrega
            """
            for i in vec_proyectos:
                print(i)
            """

        elif op == 2:
            print()
            print('*' * 21, 'Proyectos Ordenados Por titulos', '*' * 21)
            sort_proyectos(vec_proyectos)
            list_proyectos(vec_proyectos)
        elif op == 3:
            print()
            print('*' * 21, 'Buscar Proyecto Por ID', '*' * 21)
            x = int(input('Ingrese el numero del proyecto a buscar: '))
            search_proyect(x, vec_proyectos)
        elif op == 4:
            print()
            print('*' * 21, 'Cantidad De Lineas Acumuladas Por Lenguaje', '*' * 21)
            vec_ac = summary_lenguaje(vec_proyectos)
            # print(vec_ac)
            for i in range(len(vec_ac)):
                print('La cantidad de lineas escritas en el lenguaje', lenguajes[i], 'es de', vec_ac[i])
        elif op == 5:
            print()
            print('*' * 21, 'Cantidad De Proyectos Actualizados Por Año', '*' * 21)
            vec_cont = summary_year(vec_proyectos)
            # Recorremos el vector de conteo y mostramos el resultado si es distinto de cero
            for i in range(len(vec_cont)):
                if vec_cont[i] > 0:
                    print('La cantidad de proyectos correspondientes al año:', (i + 2000), ' es de:', vec_cont[i])
        elif op == 6:
            print()
            print('*' * 21, 'Proyectos Filtrados Por lenguaje, y ordenados por ID', '*' * 21)
            print('-' * 15, 'Lenguajes', '-' * 15)
            print(lenguajes)
            leng = input('Ingrese el lenguaje elegido para filtrar:')
            filtrar_lenguaje(vec_proyectos, leng)
        elif op == 7:
            print()
            productividad(vec_cont)
        elif op == 8:
            print('Adios...')

        print()
        print()
        # Solictamos una nueva opcion al usuario
        mostrar_menu()
        op = int(input('Ingrese su opcion: '))


# Control De Ejecuccion
if __name__ == '__main__':
    principal()
