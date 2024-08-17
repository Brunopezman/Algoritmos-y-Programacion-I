# Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los segundos.
def tuplas_a_dic(lista_tuplas):
    '''Recibe una tupla de dos elementos'''

    diccionario = {}

    for clave, valor in lista_tuplas:

        diccionario[clave] = diccionario.get(clave,[])
        diccionario[clave].append(valor) 

    return diccionario

