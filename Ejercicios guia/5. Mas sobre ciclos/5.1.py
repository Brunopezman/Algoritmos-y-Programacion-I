# Escribir un programa que permita al usuario ingresar un conjunto de notas, preguntando a cada paso si desea ingresar más notas, e imprimiendo el promedio correspondiente.

def promedio():

    n = input('Ingrese una nota para hacer el promedio o ingrese "*" para salir: ')
    n = int(n)
    notas = 0 
    cantidad = 0 
    while n != '*':
        notas +=1
        cantidad += notas
        promedio = round(notas/cantidad, 2)
        n = input('Ingrese una nota para hacer el promedio o ingrese "*" para salir: ')

    return print(f'Promedio: {promedio}')
        
promedio()

