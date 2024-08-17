# Campaña electoral - Escribir una función que:
# - Reciba una tupla con nombres, y para cada nombre imprima el mensaje Estimado <nombre>, vote por mí
# - Reciba una tupla con nombres, una posición de origen p y una cantidad n, e imprima el mensaje anterior para los n nombres que se encuentran a partir de la posición p
# - Modificar las funciones anteriores para que tengan en cuenta el género del destinatario, para ello, deberán recibir una tupla de tuplas, conteniendo el nombre y el género.

def pedir_voto(t:tuple):
    for persona in t:
        if persona[1] == 'm':
            print(f'Estimado {persona[0]}, vote por mi')
        print(f'Estimada {persona[0]}, vote por mi')
        
def pedir_voto_con_condicion(t:tuple, p:int, n:int):

   # Obtener los nombres a partir de la posición p y hasta n
    nombres = t[p:n + 1]

    for persona in nombres:
        if persona[1] == 'm':
            print(f'Estimado {persona[0]}, vote por mi')
        else:
            print(f'Estimada {persona[0]}, vote por mi')

pedir_voto_con_condicion((('Carlos','m'), ('juan','f'), ('pedro', 'm'), ('martina', 'f'), ('lucia', 'f')), 2, 4)

