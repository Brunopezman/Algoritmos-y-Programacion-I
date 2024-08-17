# Escribir una función es_potencia_de_dos que reciba como parámetro un número natural, y devuelva True si el número es una potencia de 2, y False en caso contrario.

from ast import In


def es_potencia_de_dos(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

# Escribir una función que, dados dos números naturales pasados como parámetros, devuelva la suma de todas las potencias de 2 que hay en el rango formado por esos números (0 si no hay ninguna potencia de 2 entre los dos). 

def suma_de_potencias_de_dos(n1,n2):
    suma = 0
    
    for i in range(n1, n2+1):
        if es_potencia_de_dos(i):
            suma += i   
    return suma
      