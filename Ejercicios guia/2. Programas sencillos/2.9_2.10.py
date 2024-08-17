# Escribir un programa que imprima por pantalla todas las fichas de dominó, de una por línea y sin repetir.

def domino():

    for i in range(0,7):
        for j in range(0,7):
            print(str([i]) + str([j]))

# Modificar el programa anterior para que pueda generar fichas de un juego que puede tener números de 0 a 𝑛.

def domino(n):

    for i in range(0,n+1):
        for j in range(0,n+1):
            print(str([i]) + str([j]))

def main():
    n = int(input("¿Cuantos numeros desea tener en el juego para poder generar las fichas?: "))
    domino(n)

main()