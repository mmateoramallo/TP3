from Registro import *

def mostrar_menu():
    vector_menu =[
    print('-'*25, '> Gestión de Proyectos de Software'),
    print('1. Cargar Proyectos'),
    print('2. Listar Proyectos'),
    print('3. Actualizar Proyectos'),
    print('4. Resumen por Lenguaje'),
    print('5. Resumen por Año'),
    print('6. Filtrar Lenguaje'),
    print('7. Productividad')]

def validar_opcion_correcta(op):
    while not(1<=op<=7):
        opcion = int(input('Ingrese su opcion: '))
    return opcion


def crear_sentencias(regs):
    persona1 = regs(10, 'Calculadora', '25/09', 'Java', 770)
    return persona1

def principal():

    p1 = crear_sentencias(Registro)
    print(p1)

    #Mostrar menu
    mostrar_menu()
    opcion = int(input('Ingrese su opcion: '))
    if not(1<=opcion<=7):
        opcion = validar_opcion_correcta(opcion)

    print(opcion)




principal()