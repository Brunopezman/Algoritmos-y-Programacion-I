# Escribir un programa que le pida al usuario que ingrese una sucesión de números naturales  hasta que el usuario ingrese ’-1’ como condición de salida. Al final, el programa debe imprimir cuántos números fueron ingresados, la suma total de los valores y el promedio.

def promedio(n):

    cantidad = 0
    suma = 0
    promedio = 0

    while n != -1:
        cantidad +=1
        suma += n
        promedio = suma / cantidad
        n = int(input('Ingrese un numero o ponga "-1" para salir del programa: '))

    return "Cantidad de numeros ingresados: "+ str(cantidad) + " suma total: " + str(suma) + " Promedio: " + str(promedio)

def main():
    n = int(input('Ingrese un numero o ponga "-1" para salir del programa: '))
    print(promedio(n))

main()
