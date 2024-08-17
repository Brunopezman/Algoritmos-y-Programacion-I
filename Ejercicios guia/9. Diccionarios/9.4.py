# Escribir una función que reciba un texto y para cada caracter presente en el texto devuelva la cadena más larga en la que se encuentra ese caracter.

def devolver_cadena_mas_larga_de_c(s):
    diccionario = {}
    cadena_mas_larga = ''
    for c in s:
        for palabra in s.split():
            if c in palabra:
                if len(palabra) > len(cadena_mas_larga):
                    cadena_mas_larga = palabra
        diccionario[c] = cadena_mas_larga
        cadena_mas_larga = ''
    
    return diccionario

