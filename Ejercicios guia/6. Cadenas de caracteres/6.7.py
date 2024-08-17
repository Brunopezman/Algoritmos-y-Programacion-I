# Escribir funciones que dadas dos cadenas de caracteres:
# - Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, 'cadena' es una subcadena de 'subcadena'.
# - Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe 'kde' y 'gnome' debe devolver 'gnome'.

def es_subcadena(s1:str, s2:str):
    return s2 in s1

def es_anterior_alfabeticamente(s1,s2):
    return s2 if s1 > s2 else s1




