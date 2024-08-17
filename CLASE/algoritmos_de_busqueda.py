def buscar(secuencia, elemento):
    '''Devuelve el indice del elemento en la secuencia o -1 si no esta'''

    for i, x in enumerate(secuencia):
        if x == elemento: 
            return i
    return -1

print(buscar(['carlos', 'juan', '11212'], 'carlos'))

# El algoritmo anterior le pregunta a CADA elemento si es el que estoy buscando para devolver el indice. Para una secuencia muy larga, la computadora va a tardar mucho en devolver el resultado. La cantidad de comparaciones es proporcional al tamanio de la lista. Lo que se conoce como busqueda lineal.


# Busqueda binaria
def busqueda_binaria(lista, x):
    izq = 0
    der = len(lista) - 1

    while izq <= der:
        medio = (izq + der)//2
        if len(medio) == x:
            return medio
        elif len(medio) > x:
            der = medio -1
        else:
            izq = medio + 1
    return -1


