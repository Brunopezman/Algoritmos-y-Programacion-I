# Escribir una función que dada una cadena de caracteres, devuelva:
# - La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe devolver 'USB'.
# - Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe 'república argentina' debe devolver 'República Argentina'.
# - Las palabras que comiencen con la letra ‘A’. Por ejemplo, si recibe 'Antes de ayer' debe devolver 'Antes ayer'

def primer_letra(s):
    letras = ''

    letras += s[0]
    for i in range(len(s)):
        if s[i] == ' ':
            letras += s[i + 1]

    return letras

def primer_letra_mayuscula(s:str):

    palabras = s.split()
    nueva_s = '' 
    for palabra in palabras:
        nueva_s += palabra.capitalize() + ' '
    
    return nueva_s

def retornar_palabras_a(s):
    letras_a = 'aAáÁ'
    palabras = s.split()
    resultado = ''
    for palabra in palabras:
        for i in letras_a:
            if i in palabra[0]:
                resultado += palabra + ' '
            
    return resultado
