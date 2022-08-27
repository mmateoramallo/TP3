from Registro import *

def mostrar_menu():
    pass

def crear_sentencias(regs):
    persona1 = regs(10, 'Calculadora', '25/09', 'Java', 770)
    return persona1

def principal():

    p1 = crear_sentencias(Registro)
    print(p1)



principal()