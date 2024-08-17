# Escribir funciones que resuelvan los siguientes problemas:
# - Dados dos números, imprimir la suma, resta, división y multiplicación de ambos.

def calcular_operaciones_basicas(n1,n2):
    suma = n1 + n2
    resta = n1 - n2
    division = n1 / n2
    multiplicacion = n1 * n2

    return suma, resta, division, multiplicacion

# - Dado un número natural 𝑛, imprimir su tabla de multiplicar.

def tabla_de_multiplicar(n):
    for numero in range(1,11):
        print(n*numero)

tabla_de_multiplicar(3)