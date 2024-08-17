# Escribir una función que, dado un número entero 𝑛, permita calcular su factorial.
def factorial(numero):
    resultado = 1
    for numero in range(1, numero+1):
        resultado *= numero
    return resultado

print(factorial(4))