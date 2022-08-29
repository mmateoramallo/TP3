from Registro import *
import random
def cargar_proyectos():
    print('-'*25, 'Cargar Proyectos', '-'*25)

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

def crear_sentencias(regs):
    persona1 = regs(10, 'Calculadora', '25/09', 'Java', 770)
    return persona1

def principal():

    p1 = crear_sentencias(Registro)
    print(p1)

    #Mostrar menu
    mostrar_menu()
    opcion = int(input('Ingrese su opcion: '))
    print(opcion)




principal()