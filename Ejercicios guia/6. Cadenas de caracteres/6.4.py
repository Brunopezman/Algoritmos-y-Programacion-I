# Escribir una función que reciba una cadena que contiene un largo número entero y devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe '1234567890', debe devolver '1.234.567.890'.

def separar_de_a_miles(n_str):
    
    n = int(n_str)
    numero_formateado = f'{n:,}'

    return numero_formateado

print(separar_de_a_miles('1234567890'))
