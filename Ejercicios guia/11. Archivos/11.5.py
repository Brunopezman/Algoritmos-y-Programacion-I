# Escribir una función, llamada rot13, que reciba un archivo de texto de origen y uno de destino, de modo que para cada línea del archivo origen, se guarde una línea cifrada en el archivo destino. El algoritmo de cifrado a utilizar será muy sencillo: a cada caracter comprendido entre la a y la z, se le suma 13 y luego se aplica el módulo 26, para obtener un nuevo caracter.

def rot13(origen, destino):
    linea_encriptada = ''
    with open(origen) as origen_f, open(destino, 'w') as destino_f:
        for linea in origen_f:
            for caracter in linea:
                if caracter.isalpha():
                    caracter_encriptado = chr(((ord(caracter) + 13) % 26))
                    linea_encriptada += caracter_encriptado
                linea_encriptada += caracter
            destino_f.write(linea_encriptada)

rot13('11. Archivos/archivo_1.txt','11. Archivos/archivo_copia.txt')