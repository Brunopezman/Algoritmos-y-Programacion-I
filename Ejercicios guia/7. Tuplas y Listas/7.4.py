#Vectores - Escribir una función que:
# - Escribir una función que reciba dos vectores y devuelva su producto escalar.
# - Escribir una función que reciba dos vectores y devuelva si son o no ortogonales.
# - Escribir una función que reciba dos vectores y devuelva si son paralelos o no.
# - Escribir una función que reciba un vector y devuelva su norma.

def calcular_producto_escalar(v1:tuple,v2:tuple):

    producto_escalar = 0
    if len(v1) != len(v2):
        return "Los vectores deben tener la misma longitud"
    
    for i in range(len(v1)):
        producto_escalar += v1[i] * v2[i]

    return producto_escalar

def son_ortogonales(v1:tuple,v2:tuple):

    if len(v1) != len(v2):
        return "Los vectores deben tener la misma longitud"
    
    return calcular_producto_escalar(v1,v2) == 0

def calcular_norma(v):
    
    suma_c_al_cuadrado = 0
    for c in v:
        suma_c_al_cuadrado += c ** 2
    
    norma = suma_c_al_cuadrado ** 0.5

    return norma


def son_paralelos(v1,v2):

    if len(v1) != len(v2):
        return "Los vectores deben tener la misma longitud"
    
    return abs(calcular_producto_escalar(v1,v2)) == round(calcular_norma(v1) * calcular_norma(v2),0)
        


