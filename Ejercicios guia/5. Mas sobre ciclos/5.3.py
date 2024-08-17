# Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
# Modificar el programa anterior para que solamente permita una cantidad fija de intentos.
# Modificar el programa anterior para que después de cada intento agregue una pausa cada vez mayor, utilizando la función sleep del módulo time.

import time

def log_in():
    p = input('Password: ')
    password = 'condr10ma'
    intentos = 1
    tiempo_espera = 1.0

    while password != p:

        time.sleep(tiempo_espera)
        tiempo_espera += 0.5
        intentos +=1
        p = input('Password denied! Try again: ')

        if intentos == 3:
            return print('You failed all your attempts.')
        
    return print('log in successfully completed')

log_in()
