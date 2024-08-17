# Escribir una función que reciba una lista ordenada y un elemento. Si el elemento se encuentra en la lista, debe encontrar su posición mediante búsqueda binaria y devolverlo. Si no se encuentra, debe agregarlo a la lista en la posición correcta y devolver esa nueva posición

def busqueda_binaria(lista, elemento):
    izq = 0
    der = len(lista) - 1

    while izq <= der:
        medio = (izq + der)//2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] > elemento:
            der = medio -1
        else:
            izq = medio + 1
    
    lista.insert(medio,elemento)

    return lista.index(elemento)