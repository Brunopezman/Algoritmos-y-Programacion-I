# Matrices
# - Escribir una función que reciba dos matrices y devuelva la suma.
# - Escribir una función que reciba dos matrices y devuelva el producto.
# - Escribir una función que opere sobre una matriz y mediante eliminación gaussiana devuelva una matriz triangular superior.
# - Escribir una función que indique si un grupo de vectores, recibidos mediante una lista, son linealmente independientes o no.

def sumar_matrices(m1:list[list], m2:list[list]):

    """Suma dos matrices m1 y m2, y las retorna como lista de filas"""

    matriz_suma = []

    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return "Las matrices deben tener las mismas dimensiones para sumarse." 
         
    for f in range(len(m1)):
        fila = []
        for c in range(len(m1[f])):
            fila.append(m1[f][c] + m2[f][c])
        matriz_suma.append(fila)
    return matriz_suma

def producto_matricial(m1:list[list], m2:list[list]):

    """multiplica dos matrices m1 y m2, y las retorna como lista de filas"""

    matriz_producto = []
    filas_matriz_producto = 0
    if len(m1[0]) != len(m2):
        return "El numero de columnas de m1 debe ser igual al numero de filas de m2" 
         
    for f in range(len(m1)):
        for c in range(len(m2[0])):    
            for k in range(len(m2)):
                filas_matriz_producto +=  m1[f][k] * m2[k][c] 
            matriz_producto.append(filas_matriz_producto)
            filas_matriz_producto = 0
            
    return matriz_producto
