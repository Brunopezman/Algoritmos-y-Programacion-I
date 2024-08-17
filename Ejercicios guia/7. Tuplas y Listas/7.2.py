# Escribir una función que:
# - Indique si dos fichas de dominó encajan o no. Las fichas son recibidas en dos tuplas, por ejemplo: (3,4) y (5,4)
# - Indique si dos fichas de dominó encajan o no. Las fichas son recibidas en una cadena, por ejemplo: 3-4 2-5. Nota: utilizar la función split de las cadenas.

def encajan_tuple(ficha1:tuple, ficha2:tuple) -> bool:
    return ficha1[1] == ficha2[0] or ficha2[1] == ficha1[0]

def encajan_str(fichas:str) -> bool:
    fichas_separadas = fichas.split(sep=' ')
    ficha1 = fichas_separadas[0].split(sep='-')
    ficha2 = fichas_separadas[1].split(sep='-')
    
    return ficha1[1] == ficha2[0] or ficha2[1] == ficha1[0]

