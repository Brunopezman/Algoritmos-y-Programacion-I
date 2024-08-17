# Dada una lista de números enteros, escribir una función que:
# - Devuelva una lista con todos los que sean primos
# - Devuelva la sumatoria y el promedio de los valores
# - Devuelva una lista con el factorial de cada uno de esos números.

def filtrar_primos(numeros):
    numeros_primos = []
    for n in numeros:
        for i in range(2,n):
            if n % i == 0:
                break   
        numeros_primos.append(n)
    return numeros_primos

print(filtrar_primos([1,2,21]))

def calcular_sumatoria_y_promedio(numeros):
    sumatoria = 0
    for n in numeros:
        sumatoria += n
    promedio = sumatoria/len(numeros)

    return sumatoria, promedio

def listar_factorial(numeros):
    resultado = 1
    lista_de_factoriales = []
    for numero in numeros:
        for factor in (1,numero):
            resultado *= factor
        lista_de_factoriales.append(resultado)

    return lista_de_factoriales
