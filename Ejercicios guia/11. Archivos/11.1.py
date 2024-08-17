# Escribir una función, llamada head que reciba un archivo y un número N e imprima las primeras N líneas del archivo

def head(archivo, n):
    with open(archivo) as f:
        for i, linea in enumerate(f):
                if not i < n:
                    return
                print(linea.strip())

head('11. Archivos/archivo_1.txt', 5)

def escribir_n_lineas(origen, destino, n):
    contador = 0
    with open(destino, 'w') as dest, open(origen) as orig:
        for linea in orig:
            if contador >= n:
                    return
        dest.write(linea)
        contador += 1

escribir_n_lineas('11. Archivos/archivo_1.txt', '11. Archivos/archivo.copia.txt')