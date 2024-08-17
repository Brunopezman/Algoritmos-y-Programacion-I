# csv.reader()
# ''.writer:
# ''.DictReader:
# ''.DictWriter:

import csv

ruta = 'archivo.txt' #Bruno 110263623 7
with open(ruta) as f:
    csv_reader = csv.DictReader(ruta, fieldnames=['Nombre', 'Padron', 'Nota'])

csv_writer = csv.writer(ruta)
csv_writer.writer(ruta)

# Implementar una funcion que dado un archivo, que dado un actor devuelva un diccionario.

def listar_actores(ruta):
    dict = {}

    with open(ruta) as f:
        for linea in f:
            if len(linea.split(';')) != 3:
                continue
            pelicula, anio, actores = linea.rstrip().split(';')
            if not anio.isdigit() or len(actores) == 0 or pelicula == '':
                continue
            actores = actores.split(',')
            for actor in actores:
                lista_anios = dict.get(actor, [])
                lista_anios.append(int(anio))
                dict[actor] = lista_anios

    return dict

# Ahora con CSV

class LineError:
    def __init__(self) -> None:
        return Exception

class FieldError:
    def __init__(self) -> None:
        return Exception

def listar_actores(ruta):
    dict = {}

    with open(ruta, newline='') as f:

        for linea in csv.DictReader(f, delimiter= ';',fieldnames=['Pelicula', 'Anio', 'Actores']):
            if len(linea) != 3:
                raise LineError(f'La longitud de la linea es {len(linea)}, se esperaba 3')
            
            if not linea['Anio'].isdigit() or len('Actores') == 0 or linea['Pelicula'] == '':
                raise FieldError(f'Algun campo de la linea {linea} es invalido.')
            
            for actor in linea['Actores'].split(','):
                lista_anios = dict.get(actor, [])
                lista_anios.append(int(linea['Anio']))
                dict[actor] = lista_anios

    return dict

def main():
    ruta = ''

    # try:
        #listar_actores(ruta)
    # except LineError:
        #handle_line_error()
    # except FieldError:
        #handle_field_error()
    # except:
        #handle_error()
    #finally:
        # return ruta
        
