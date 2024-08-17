# Escribir una función que reciba una tupla de elementos e indique si se encuentran ordenados de menor a mayor o no.

def estan_ordenados(t:tuple):

    mayor = ''
    l_ordenada = []

    for e in t:
        e = str(e)
        if e >= mayor:
            mayor = e
            l_ordenada.append(mayor)

    return len(l_ordenada) == len(t)

