# Escribir una función que devuelva la suma de todos los divisores de un número 𝑛, sin incluirlo.
# Usando la función anterior, escribir una función que imprima los primeros 𝑚 números tales que la suma de sus divisores sea igual a sí mismo (es decir los primeros 𝑚 números perfectos).

def divisores(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0 :   
            suma += i
    return suma

def primeros_m_numeros_perfectos(m):
    cantidad_m_perfectos = 0
    n = 1
    while cantidad_m_perfectos <= m:
        if divisores(n) == n:
            cantidad_m_perfectos += 1
            print(n, end = ", ")
        n += 1

primeros_m_numeros_perfectos(5)

