# Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena.
# Escribir una función que cuente la cantidad de apariciones de cada caracter en una cadena de texto, y los devuelva en un diccionario
# Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos dados.

from random import randint  

def contar_apariciones_palabra(s):
    diccionario = {}
    for palabra in s.split():
        diccionario[palabra] = diccionario.get(palabra, 0) + 1

    return diccionario

def contar_apariciones_caracter(s):
    diccionario = {}
    for caracter in s:
        diccionario[caracter] = diccionario.get(caracter, 0) + 1
        
    return diccionario

def contar_valor_observado(iteraciones:int):

    resultados = {}

    for _ in range(iteraciones):
        
        dado1 = randint(1, 6)
        dado2 = randint(1, 6)

        suma = dado1 + dado2

        if suma in resultados:
            resultados[suma] += 1
        else:
            resultados[suma] = 1

    return resultados

print(contar_valor_observado(10))

