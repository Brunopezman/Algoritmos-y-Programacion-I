# Escribir una función que reciba un número entero 𝑘 e imprima su descomposición en factores primos.

def descomponer_primos(k):
    
    while k > 1:
        for i in range(2,k + 1):
            if k % i == 0:
                k = k // i
                if k == i:
                    print(i) 
                else:
                    print(i, end = '.')
                break





