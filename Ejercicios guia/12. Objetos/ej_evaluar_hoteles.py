'''
Nos contratan para diseñar una clase para evaluar la relación calidad-precio de diversos hoteles. Nos dicen que los atributos que se cargarán de los hoteles son: nombre, ubicación, puntaje
obtenido por votación, y precio, y que además de guardar hoteles y mostrarlos, debemos poder compararlos en términos de sus valores de relación calidad-precio, de modo tal que x < y
signifique que el hotel x es peor en cuanto a la relación calidad-precio que el hotel y, y que dos
hoteles son iguales si tienen la misma relación calidad-precio. La relación calidad-precio de un
hotel la definen nuestros clientes como 10 ⋅ puntaje **2/precio.
Además, y como resultado de todo esto, tendremos que ser capaces de ordenar de menor a
mayor una lista de hoteles, usando el orden que nos acaban de definir
'''

class Hotel:

    def __init__(self, nombre, ubicacion, puntaje, precio) -> None:

        self.nombre = validar_cadena_no_vacia(nombre)
        self.ubicacion = validar_cadena_no_vacia(ubicacion)
        self.puntaje = validar_numero_positivo(puntaje)
        self.precio = validar_numero_positivo(precio)

    def __str__(self) -> str:
        return f'{self.nombre} de {self.ubicacion} - Puntaje: {self.puntaje} - Precio: ${self.precio}'
    
    def ratio(self):
        """Calcula la relacion calidad precio del hotel."""
        return ((self.puntaje ** 2) * 10 / self.precio)
    
    def __lt__(self, otro):
        """Compara dos hoteles segun sus ratios."""
        return self.ratio() < otro.ratio()
    
    def __eq__(self, otro):
        """Compara dos hoteles segun sus ratios."""
        return self.ratio() == otro.ratio()

def validar_cadena_no_vacia(cadena):
    if not cadena:
        raise ValueError('El nombre o la ubicacion estan vacios')
    return cadena

def validar_numero_positivo(numero):
    if not numero:
        return 0
    if not isinstance(numero, (int, float)) or float(numero) < 0:
        raise ValueError('El valor dado como numero no es valido')
    return numero

def precio(hotel):
    return hotel.precio 
    
h1 = Hotel("Hotel 1* normal", "MDQ", 1, 10)
h2 = Hotel("Hotel 2* normal", "MDQ", 2, 40)
h3 = Hotel("Hotel 3* carisimo", "MDQ", 3, 130)
h4 = Hotel("Hotel vale la pena" ,"MDQ", 4, 130)

# l = [h1, h2, h3, h4]
# l.sort()
# for hotel in l:
#     print(hotel) #Imprime hoteles en orden ascendente sobre cual conviene comprar por su ratio

# l.sort(key= precio)
# for hotel in l:
#     print(hotel) #Imprime hoteles en orden ascendente sobre cual conviene comprar por su precio
