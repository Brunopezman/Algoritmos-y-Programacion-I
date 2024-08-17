# Escribir dos funciones que resuelvan los siguientes problemas:
# - Dado un número entero 𝑛, indicar si es par o no.
# - Dado un número entero 𝑛, indicar si es primo o no

def es_par(n):
    return n % 2 == 0

def es_primo(n):

    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    