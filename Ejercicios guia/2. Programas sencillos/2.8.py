# Escribir un programa que tome una cantidad 𝑚 de valores ingresados por el usuario, a cada uno le calcule el factorial (utilizando la función escrita en el ejercicio 1.5) e imprima el resultado junto con el número de orden correspondiente

def factorial(numero):
    resultado = 1
    for numero in range(1, numero+1):
        resultado *= numero
    return resultado

def lista_de_factoriales(n):
    for numero in range(1, n+1):
        factorial(numero)
        print(str(numero)+ " - " + str(factorial(numero)))

def main():
    n = int(input("Ingrese una cantidad de valores para calcularles su factorial: "))
    lista_de_factoriales(n)

main()