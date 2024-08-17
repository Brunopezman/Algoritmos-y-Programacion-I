# Escribir un programa que use un ciclo definido con rango numérico, que averigue a cuántos amigos quieren saludar, les pregunte los nombres de esos amigos/as, y los salude.

def saludo():
    cantidad_amigos = int(input('A cuantos amigos quiere saludar?: '))
    for amigo in range(cantidad_amigos):
        nombre = input('Como se llama su amigo?: ')
        print('Hola ' + nombre)

saludo()

