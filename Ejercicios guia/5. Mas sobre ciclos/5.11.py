# Escribir una función que reciba un dígito y un número natural, y decida numéricamente si el dígito se encuentra en la notación decimal del segundo.

def esta_el_digito(digito, n):

    digito_str = str(digito)
    n_str = str(n)

    for digito in n_str:
        if digito == digito_str:
            return True
        else:
            return False
        

esta_el_digito(3, 102)            

    