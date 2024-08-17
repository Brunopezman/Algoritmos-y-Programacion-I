# Escribir una función que reciba por parámetro una dimensión 𝑛, e imprima la matriz identidad correspondiente a esa dimensión.

def matriz_identidad(n):
    for columna in range(n):
        for fila in range(n):
            if columna == fila:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()

# Si el índice de fila es igual al índice de columna, imprime "1", indicando la diagonal principal, y si no, imprime "0" para el resto de los elementos. Cada vez que se completa una fila, se imprime una nueva línea para avanzar a la siguiente fila.