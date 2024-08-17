# Inversión de listas
# - Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea igual a la original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá devolver ['papa', 'a', 'día', 'buen', 'Di'].

def nueva_lista_inversa(l:list):
    l_invertida = []
    for i in l[::-1]:
        l_invertida.append(i)
    return l_invertida

def listar_inversamente(l:list): return l[::-1]

