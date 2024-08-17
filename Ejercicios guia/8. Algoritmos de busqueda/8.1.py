# Escribir una función que reciba una lista desordenada y un elemento, que:
# - Busque todos los elementos que coincidan con el pasado por parámetro y devuelva la cantidad de coincidencias encontradas
# - Busque la primera coincidencia del elemento en la lista y devuelva su posición.
# - Utilizando la función anterior, busque todos los elementos que coincidan con el pasado por parámetro y devuelva una lista con las posiciones.

def coincidencias(desordenada:list, e):
    cantidad = 0
    for elemento in range(len(desordenada)):
        if e == desordenada[elemento]:
            cantidad +=1
    return cantidad

def devolver_posicion(desordenada:list, e):
    for elemento in range(len(desordenada)):
        if e == desordenada[elemento]:
            return elemento

def devolver_lista_de_posiciones(desordenada:list, e):
    lista = []
    for elemento in range(len(desordenada)):
        lista.append(elemento)
    return lista



