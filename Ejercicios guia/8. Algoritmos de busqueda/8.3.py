# Escribir una función que reciba una cadena a buscar y una lista de tuplas (nombre_completo, telefono), y busque dentro de la lista, todas las entradas que contengan en el nombre completo la cadena recibida (puede ser el nombre, el apellido o sólo una parte de cualquiera de ellos). Debe devolver una lista con todas las tuplas encontradas.

def encontrar_tuplas(cadena, lista_de_tuplas:list[tuple]):
    tuplas_encontradas = ()

    for nombre_completo, telefono in lista_de_tuplas:
        if cadena in nombre_completo.lower():
            tuplas_encontradas += nombre_completo, telefono

    return tuplas_encontradas

