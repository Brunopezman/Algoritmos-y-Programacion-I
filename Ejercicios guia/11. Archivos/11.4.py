# Escribir una función, llamada grep, que reciba una cadena y un archivo e imprima las líneas del archivo que contienen la cadena recibida.

def grep(s, archivo):
    with open(archivo) as f:
        for linea in f:
            if s in linea.lower():
                print(linea.strip())

