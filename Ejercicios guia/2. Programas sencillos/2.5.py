# Escribir una función que dado un número entero devuelva 1 si el mismo es impar y 0 si fuera par.

def funcion(n:int):
    if n % 2 == 0:
        return 0
    else:
        return 1

# Escribir una función que dado un número entero devuelva el dígito de las unidades. Por ejemplo, para 153 debe devolver 3

def ultimo_digito(n:int):
    digitos = str(n)
    return digitos[-1::]

# Escribir una función que dado un número devuelva el primer número múltiplo de 10 inferior a él. Por ejemplo, para 153 debe devolver 150.

def primer_multiplo_de_10_inferior(n):
    multiplo_de_10 = (n // 10) * 10
    
    return multiplo_de_10

