# Escribir funciones que dada una cadena de caracteres:
# - Devuelva solamente las letras consonantes. Por ejemplo, si recibe 'algoritmos' o 'logaritmos' debe devolver 'lgrtms'.
# - Devuelva solamente las letras vocales. Por ejemplo, si recibe 'sin consonantes' debe devolver 'i ooae'.
# - Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe 'vestuario' debe devolver 'vistaerou'.
# - Indique si se trata de un palíndromo. Por ejemplo, 'anita lava la tina' es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

def devolver_consonantes(s:str):

    consonantes = ''

    for letra in s:
        if (letra.isalpha() and letra.lower() not in 'aeiou') or letra == ' ':
            consonantes += letra
    return consonantes

def devolver_vocales(s:str):

    vocales = ''

    for letra in s:
        if (letra.isalpha() and letra.lower() in 'aeiou') or letra == ' ':
            vocales += letra
    return vocales

def devolver_siguiente_vocal(s:str):

    resultado = ''
    vocales = 'aeiouAEIOU'
    
    for caracter in s:
        
        if caracter in vocales:
            posicion = vocales.index(caracter)
            siguiente_vocal = vocales[(posicion + 1) % len(vocales)]
            resultado += siguiente_vocal
        else:
            resultado += caracter 
    
    return resultado

def es_palindromo(s):

    s1= ''
    for letras in s:
        if letras.isalpha():
            s1 += letras
    s2 = s1[::-1]
  
    return s1 == s2
