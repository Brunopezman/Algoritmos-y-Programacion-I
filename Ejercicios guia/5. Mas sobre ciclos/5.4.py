# Utilizando la función randrange del módulo random, escribir un programa que obtenga un número aleatorio secreto, y luego permita al usuario ingresar números y le indique si son menores o mayores que el número a adivinar, hasta que el usuario ingrese el número correcto.

import random

def adivinar_numero(n):
    numero_random = random.randrange(1,10)

    while numero_random != n:
        if numero_random > n:
            print('El numero secreto es mayor que numero que eligio')
        elif numero_random < n:
            print('El numero secreto es menor que numero que eligio')

        n = int(input('Adivine el numero secreto entre 1 y 10: '))
    
    return print(f'Felicidades! El numero secreto era {n}')


def main():
    n = int(input('Adivine el numero secreto entre 1 y 10: '))
    adivinar_numero(n)

main()