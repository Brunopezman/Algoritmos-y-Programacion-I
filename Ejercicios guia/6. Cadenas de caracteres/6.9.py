# Implementar la función pedir_entero(mensaje, min, max), que debe imprimir el mensaje y luego esperar a que el usuario ingrese un valor. Si el valor ingresado no es un número entero, o no es un número entre min y max (inclusive), se le debe avisar al usuario y pedir el ingreso de otro valor. Una vez que el usuario ingresa un valor válido, la función lo debe devolver.

def pedir_entero(mensaje, min, max):

    n = input(mensaje)

    while n.isalpha() or int(n) not in range(min, max):
        n = input('Por favor ingresa un un numero entre 0 y 100: ')
    return n

pedir_entero('Cual es tu numero favorito?: ', 0, 100)