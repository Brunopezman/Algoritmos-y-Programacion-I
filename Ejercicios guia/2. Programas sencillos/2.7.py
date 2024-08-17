# Escribir un programa que le pregunte al usuario un número 𝑛 e imprima los primeros 𝑛 números triangulares, junto con su índice. Los números triangulares se obtienen mediante la suma de los números naturales desde 1 hasta 𝑛.

def n_triangulares(n):
    suma_triangular = 0
    for i in range(1,n+1):
        suma_triangular +=i
        print(str(i) + " - " + str(suma_triangular))

def main():
    n = int(input("Escriba un número: "))
    n_triangulares(n)

main()
