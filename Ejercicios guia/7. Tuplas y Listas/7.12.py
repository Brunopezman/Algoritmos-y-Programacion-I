# Funciones que reciben funciones
# - Escribir una funcion llamada map, que reciba una función y una lista y devuelva la lista que resulta de aplicar la función recibida a cada uno de los elementos de la lista recibida.
# - Escribir una función llamada filter, que reciba una función y una lista y devuelva una lista con los elementos de la lista recibida para los cuales la función recibida devuelve un valor verdadero.

def exclamar(s):
    return s + '!' 

def par(n):
    return n % 2 == 0

def mapear(exclamar,l:list):
    lista_nueva = []
    for e in l:
        lista_nueva.append(exclamar(e))
    return lista_nueva

def filtrar(par,l):
    lista_nueva = []
    for e in l:
        if par(e) == True:
            lista_nueva.append(e)

    return lista_nueva

# Optimizacion - map y filter

lista_nueva = list(map(exclamar,['hola', 'como va', 'que talco']))
lista_nueva2 = list(filter(par, [1,2,3,4]))

