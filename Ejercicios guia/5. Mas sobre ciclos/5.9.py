# Escribir una función que reciba dos números como parámetros, y devuelva cuántos múltiplos del primero hay, que sean menores que el segundo.
# - Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.
# - Implementarla utilizando un ciclo while, que multiplique el primer número hasta que sea mayor que el segundo.

def multiplos_del_primero(n1,n2):

    cantidad = 0

    for i in range(n1, n2+1):
        if i % n1 == 0 and i < n2:
            cantidad +=1
        else:
            continue

    return cantidad

def multiplos_del_primero_op_dos(n1,n2):

    cantidad = 0
    multiplo = n1
    
    while multiplo < n2:
        cantidad += 1
        multiplo += n1
    
    return cantidad 


