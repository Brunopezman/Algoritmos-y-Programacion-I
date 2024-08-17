# Escribir un programa que le pida una palabra al usuario, para luego imprimirla 1000 veces, en una única línea, con espacios intermedios.

def mil_veces():
    palabra = input('Escriba una palabra a imprimir: ')
    for i in range(1000):
        print(palabra, end = " ")

mil_veces()