# Escribir una función que reciba una cantidad de pesos, una tasa de interés y un número de años y devuelva el monto final a obtener. 

def plazo_fijo(monto_inicial, interes, anios):

    monto_final = round(monto_inicial * (1 + interes/100)**anios, 2)

    return monto_final

# Utilizando la función del ejercicio anterior, escribir un programa que le pregunte al usuario la cantidad de pesos inicial, la tasa de interés y el número de años y muestre el monto final a obtener.

def main():

    monto_inicial = float(input('Ingrese la cantidad de pesos a depositar: '))
    interes = float(input('Ingrese una tasa de interes en porcentaje: '))
    anios = int(input('Ingrese la cantidad de años en los cuales su dinero quedará depositado: '))

    print(plazo_fijo(monto_inicial, interes, anios))

main()