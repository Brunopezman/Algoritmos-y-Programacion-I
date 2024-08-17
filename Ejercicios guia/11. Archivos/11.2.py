# Escribir una función, llamada cp, que copie todo el contenido de un archivo (sea de texto o binario) a otro, de modo que quede exactamente igual.

def cp_texto(origen, destino):
    with open(origen) as origen_f, open(destino, 'w') as destino_f:
        for linea in origen_f:
            destino_f.write(linea)

    return destino_f

def cp_binario(origen, destino, bytes):
    with open(origen, 'rb') as origen_f:
        contenido = origen.read(bytes)
        with open(destino, 'wb') as destino_f:
                destino_f.write(contenido)

    return destino_f