# Dada una lista de números enteros y un entero k, escribir una función que:
# - Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a k
# - Devuelva una lista con aquellos que son múltiplos de k.

def mayores_menores_iguales_k(lista:list[int], k:int):
    mayores = []
    menores = []
    iguales = []

    for numero in lista:
        if numero > k:
            mayores.append(numero)
        elif numero < k:
            menores.append(numero)
        else:
            iguales.append(numero)
    
    return menores, mayores, iguales

def multiplos_de_k(lista:list[int], k:int):
    multiplos = []

    for numero in lista:
        if numero % k == 0 or k % numero == 0:
            multiplos.append(numero)

    return multiplos




