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

def cargar_proyectos(vec, n):
    num_id = 1
    titulos = ('Mario', 'BloodBorne', 'AlphaNum', 'Valorant', 'Doom', 'Metro', 'Calculadora', 'Administrador De Archivos', 'IDE', 'RDR2', 'RE2', 'Bioshock', 'Redes Neuronales')

    #Recorro el range n y voy agregando los datos generados al vector
    for i in range(n):
        #Genero los datos



def principal():
    #Variables
    vec_proyectos = []

    #Mostramos el menu
    mostrar_menu()
    op = int(input('Ingrese su opcion: '))

    #Consultamos op
    while op != 8:
        if op == 1:
            #Le solicitamos al usuario la cantidad de proyectos a registrar
            n = int(input('Ingrese la cantidad de proyectos a registrar: '))
        elif op == 2:
            pass
        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 5:
            pass
        elif op == 6:
            pass
        elif op == 7:
            pass
        elif op == 8:
            pass


#Control De Ejecuccion
if __name__ == '__main__':
    principal()