# Escribir funciones que dada una cadena de caracteres:
# - Imprima los dos primeros caracteres.
# - Imprima los tres últimos caracteres.
# - Imprima dicha cadena cada dos caracteres. Ej.: 'recta' debería imprimir 'rca'
# - Dicha cadena en sentido inverso. Ej.: 'hola mundo!' debe imprimir '!odnum aloh'
# - Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime 'reflejoojelfer'.

def imprime_caracteres(cadena):
    print (cadena[:2])

def tres_ultimos_caracteres(cadena):
    print (cadena[-3:])

def cada_dos_caracteres(cadena):
    print (cadena[::2])

def sentido_inverso(cadena):
    print (cadena[::-1])

def dos_sentidos(cadena):
    print (cadena + cadena[::-1])


