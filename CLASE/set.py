# Funcion que de dos listas me devuelva una lista con los elementos repetidos

def obtener_repetidos(lista1, lista2):
    s = set(lista1)
    repetidas = set()
    for e in lista2:
        if e in s and e in repetidas:
            repetidas.add(e)

    return list(repetidas)