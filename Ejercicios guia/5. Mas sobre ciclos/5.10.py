# Escribir una función que reciba un número natural e imprima todos los números primos que hay hasta ese número.

def numeros_primos(n):
    
    for i in range(1,n):
        if i % 2 != 0 or i == 1 or i == 2:
            print(i, end = " ")
        else:
            continue

