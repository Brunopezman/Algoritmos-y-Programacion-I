# Escribir una función que reciba dos números y devuelva su producto.

def producto(n1,n2):
    """
        PRE: Recibe dos números 
        POST: Devuelve el producto de ambos
    """
    return n1 * n2

# Utilizando la función del ejercicio anterior, escribir un programa (un archivo .py) que pida al usuario dos números, y luego muestre el producto.

def funcion_producto():
    n1 = int(input('Escriba un número: '))
    n2 = int(input('Escriba otro número: '))

    producto_final = producto(n1,n2)

    return producto_final

