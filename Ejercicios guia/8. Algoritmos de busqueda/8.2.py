# Escribir una función que reciba una lista de números no ordenada, que:
# - Devuelva el valor máximo
# - Devuelva una tupla que incluya el valor máximo y su posición.

def devolver_valor_max(lista_numeros):
    valor_max = 0

    for n in lista_numeros:
        if n > valor_max:
            valor_max = n
    
    return valor_max

def devolver_valor_max_y_pos(lista_numeros):
    valor_max = 0
    posicion = 0
    for i in range(len(lista_numeros)):
        if lista_numeros[i] > valor_max:
            valor_max = lista_numeros[i]
            posicion = i

    return valor_max, posicion

