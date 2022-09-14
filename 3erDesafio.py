import Soporte as soporte
import collections


def create_array():
    # Creamos el array
    v = soporte.vector_unknown_range(300000)
    return v


def main():
    # Crear Arreglos
    num = []
    cont = []
    # Vamos a obtener el arreglo creado con la funcion vector_unkown_range
    v = create_array()
    # Recorreria todo el vector v
    for i in range(len(v)):
        pass
    # Usamos la libreria collections, tenemos un diccionario con los numeros que se repiten y la cantidad de veces que se repiten
    v_dict = collections.Counter(v)
    # En este punto obtenemos las llaves del diccionario de la linea pasada para contar la cantidad que son
    v_dict_d = v_dict.keys()  # LLaves del diccionario de la funcion anterior, (num)
    # En estas lineas contamos la cantidad distintas de llaves que hay, es decir la cantidad de numeros que se repiten
    cont_frec = 0
    for i in range(len(v_dict_d)):
        cont_frec += 1

    # print(len(v_dict_d))
    print('Cantidad de números diferentes en el arreglo v:', cont_frec)
    print()

    # Buscamos el valor modal del array v_dict, dado que este es un diccionario que tiene de valor en la clave a la cantidad de veces que se repite la key de number, de vuelta tengo que acceder al diccionario de numeros repetidos y cantidad de veces que se repitio
    """
    # Buscar valor modal (que numero del dict, tiene la llave mas grande)
    lst_values = []  # Lista para guardar los valores(cont)
    lst_values.extend(v_dict.values())
    print('Lista, cont:', lst_values)
    # Obnteer las llaves
    keys_dict = v_dict.keys()
    print('Lista de nums:', keys_dict)

    # Busco el valor modal
    valor_modal = 0

    # Busco el valor modal
    valor_modal = 0
    for i in range(len(lst_values)):
        if i == 0:
            valor_modal = lst_values[i]
        if lst_values[i] > valor_modal:
            valor_modal = lst_values[i]

    print('El valor modal es', valor_modal)

    # Recorremos nuevamente para verificar si se repite
    for i in range(len(lst_values)):
        if lst_values[i] == valor_modal:
            valor_modal = 0

    print('El valor modal es', valor_modal)
    """

    list_values = []
    list_values.extend(v_dict.values())
    mayor = 0
    pos_mayor = 0
    coincide_may = False

    for j in range(len(list_values)):
        # print('J es:',j)
        if j == 0:
            mayor = list_values[j]
        # Chequeo cual es el mayor
        if list_values[j] > mayor:
            mayor = list_values[j]
            # Recupero la posicion para poder acceder a la llave del diccionario
            pos_mayor = j

    # Deberia volver a recorrer el array para corroborar si hay otro numero igual al mayor
    for i in range(len(list_values)):
        if (list_values[i] == mayor) and i != pos_mayor:
            coincide_may = True

    rst_dos = []
    # Acceder al elemento
    for k, v in v_dict.items():
        if v == 9798:
            rst_dos.append(k)

    print('El mayor es(Cantidad de veces que se repitio el numero):', mayor, 'cuya posicon es:', pos_mayor)
    # print(list_values[0])
    print('Llave en la que se encuentra el elemento que se repitio mas veces',rst_dos)
    #print(v_dict[547])
    if coincide_may:
        print('Hay dos numeros que se repiten la misma cant de veces')
    else:
        print('No hay dos numeros que se repiten la misma cant de veces')

    print('-'*25)
    vec_sub_dos = soporte.vector_known_range(300000)
    c = [0] * 300000
    conta = 0

    #Conteo
    for s in range(len(vec_sub_dos)):
        c[vec_sub_dos[s]] += 1

    #Mostrar cantidad de casilleras diferentes de cero
    for m in range(len(c)):
        if c[m] != 0:
            #print(c)
            conta += 1

    print('Cantidad de casilleros diferentes de cero:', conta)



if __name__ == "__main__":
    main()
