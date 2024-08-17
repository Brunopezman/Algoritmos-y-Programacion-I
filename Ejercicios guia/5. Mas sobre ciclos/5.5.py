# Implementar el algoritmo de Euclides para calcular el máximo común divisor de dos números 𝑛 y 𝑚, dado por los siguientes pasos.
# 1. Teniendo 𝑛 y 𝑚, se obtiene 𝑟, el resto de la división entera de 𝑚/𝑛.
# 2. Si 𝑟 es cero, 𝑛 es el mcd de los valores iniciales.
# 3. Se reemplaza 𝑚 ← 𝑛, 𝑛 ← 𝑟, y se vuelve al primer paso.

def mcd(n,m):
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n

    if r == 0:
        mcd = n 

    return print(mcd)
    
# mcd(15,9) == mcd(9,15) == 3
# mcd(10,8) == 2
# mcd(12,6) == 6

