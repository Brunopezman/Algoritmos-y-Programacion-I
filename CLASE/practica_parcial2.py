# Escribir una función que reciba un texto (formada únicamente por palabras y espacios), y devuelva un diccionario donde para cada palabra muestre la cantidad de veces que es precedida por otra palabra.

def contar_predecesiones(frase):
    d = {}
    palabras = frase.split()

    for i in range(len(palabras)):
        d[palabras[i]] = d.get(palabras[i],{})
        d[palabras[i]][palabras[i - 1]] = d[palabras[i]].get(palabras[i - 1], 0) + 1

    return d

print(contar_predecesiones('Escribir una función una función'))

# Escribir un programa que abra un archivo separado por comas y le pida al usuario dos numeros. El programa debe escribir en otro archivo el contenido del primero con las columnas del archivo CSV intercambiadas segun los numeros del usuario. Por ejemplo, si una lınea del archivo es “lunes, martes,miercoles,jueves” y los n´umeros del usuario son 1 y 3, el archivo de salida ser´a “miercoles, martes,lunes, jueves” (las columnas 1 y 3 est´an intercambiadas)

import csv

def main():
    
    col1, col2 = int(input('ingrese una columna')), int(input('ingrese una columna'))
    with open('origen.csv') as origen, open('destino.csv', 'w') as destino:
        for campos in csv.origen:
            # campos = linea.rstrip().split(',') # [Lunes, martes, miercoles, jueves]
            csv_writer = csv.writer(destino)
            if col1 > len(campos) or col2 >= len(campos):
                continue
            campos[col1 - 1], campos[col2 - 1] = campos[col2 - 1], campos[col1 - 1]
            csv_writer.writerow(campos)
            # destino.write(",".join(campos) + '\n')

main()

# Escribir una funcion que reciba un nombre de un archivo con datos y un nombre de un archivo para guardar errores (los errores se agregan al final). El archivo con datos tiene el siguiente formato: anio , mes , vendedor , cliente , monto

def calcular_monto_por_vendedores(ruta_datos, ruta_errores):
    vendedores = {}
    with open(ruta_datos) as datos, open(ruta_errores, 'a') as errores:
        for campos in csv.reader(datos): # [2023, Noviembre, Roman, Flu, 7]
            errores = csv.writer(errores)
            # if len(campos) != 5 or not campos[4].isdigit():
            #     errores.writerow
            #     continue
            try:
                vendedores[campos[2]] = vendedores.get(campos[2], 0) + int(campos[4])
            except IndexError:
                errores.writerow
            except ValueError:
                errores.writerow

    return vendedores

# Se desea escribir una nota de rescate recortando letras de una revista. Escribir una funci´on que reciba por par´ametro la nota que se desea escribir y el texto completo de la revista, y devuelva True si la revista contiene todas las letras necesarias para escribir la nota (ignorando may´usculas y min´usculas), False en caso contrario. Ejemplo: Si la revista contiene “Algoritmos y Programaci´on”, podemos escribir la nota “Gracias por la moto”, pero no se puede escribir “Porotos amargos” (falta una s). 

def contar_letras(texto):
    d = {}
    for caracter in texto:
        if caracter == ' ':
            continue
        d[caracter] = d.get(caracter, 0) + 1
    return d

def se_puede_escribir(nota, texto):
    letras_nota = contar_letras(nota)
    for caracter in texto:
        if letras_nota.get(caracter):
            letras_nota[caracter] -=1
    return sum(letras_nota.values()) == 0

def se_puede_escribir_v2(nota, texto):
    letras_texto = contar_letras(texto)
    for caracter in ''.join(nota.split()):
        if not letras_texto.get(caracter):
            return False
        letras_texto -=1
    return True

'''
Proponer una serie de atributos y metodos para la clase Botella (no implementarlos, solo
enunciarlos). Adem´as, **implementar** las funcionalidades necesarias para que al imprimir
una instancia de la misma se muestre el siguiente texto:
"Villamanaos: 300ml/500ml - Destapada"
"Glaciar: 150ml/200ml - Tapada"
'''

class Botella:
	def __init__(self, marca, capacidad):
		self.marca = marca
		self.capacidad = capacidad
		self.cantidad = capacidad
		self.esta_tapada = True

	def __str__(self):
		str_tapada = "Tapada" if self.esta_tapada else "Destapada"
		return f'{self.marca}: {self.cantidad}/{self.capacidad} - {str_tapada}'

	def tomar(self, cantidad):
		if self.esta_tapada or self.cantidad - cantidad < 0:
			raise Exception()
		self.cantidad -= cantidad

	def destapar(self):
		if not self.esta_tapada:
			raise Exception()
		self.esta_tapada = False

class Carta:
	def __init__(self, palo, valor):
		self.valor = valor
		self.palo = palo

	def __str__(self):
		return f'{self.valor} de {self.palo}' #type(self.palo) => Palo, Funciona <=> 
											  #Palo implementa __str__
	def __eq__(self, otra):
		return self.palo == otra.palo and self.valor == otra.valor #Palo, Funciona <=> Palo implementa __eq__

	def __lt__(self, otra):
		if self.palo < otra.palo: # Funciona <=> Palo implementa __lt__
			return True
		if self.palo > otra.palo: # Funciona <=> Palo implementa __gt__ OR __lt__ and __eq__
			return False
		return self.valor < otra.valor

